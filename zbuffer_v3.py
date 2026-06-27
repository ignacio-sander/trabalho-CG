import numpy as np
import math

def renderizar_cena(dog, proj, res, interval, shademap, wf, toon):
    # Inicializa o buffer de pixels (preto) e o buffer de profundidade (Z-Buffer)
    # No Pygame surfarray, a estrutura da matriz é (largura, altura, 3)
    largura, altura = res[0], res[1]
    pixel_array = np.zeros((largura, altura, 3), dtype=np.uint8)
    depth_array = np.full((largura, altura), -np.inf, dtype=np.float32)

    # Lista para armazenar todas as arestas/linhas de contorno que precisam ser desenhadas depois
    linhas_contorno = []

    for parte_idx, parte in enumerate(dog):
        for face_idx, face in enumerate(parte):
            if len(face) < 3:
                continue

            # 1. Projeta os pontos da face para coordenadas de tela 2D e mantém o Z
            pontos_projetados = []
            for ponto in face:
                c = np.matmul(ponto, proj)
                px = largura * c[0] / (2 * interval[0]) + largura / 2
                py = altura * -c[1] / (2 * interval[1]) + altura / 2
                pz = c[2] # Profundidade (Z)
                pontos_projetados.append((px, py, pz))

            # 2. Triangulação da face (para garantir suporte a qualquer polígono convexo)
            triangulos = []
            for i in range(1, len(pontos_projetados) - 1):
                triangulos.append([pontos_projetados[0], pontos_projetados[i], pontos_projetados[i+1]])

            # Determina a cor da face baseada no shademap
            import colorsys
            shade = shademap[parte_idx][face_idx]
            cor_rgb = [int(item * 255) for item in colorsys.hsv_to_rgb(0, 1, shade)]

            # Se não estiver em modo wireframe puro, renderiza os triângulos sólidos
            if not wf:
                for tri in triangulos:
                    # Ordena os vértices por Y de forma crescente (y0 <= y1 <= y2)
                    tri_sorted = sorted(tri, key=lambda p: p[1])
                    p0, p1, p2 = tri_sorted[0], tri_sorted[1], tri_sorted[2]
                    
                    x0, y0, z0 = p0[0], p0[1], p0[2]
                    x1, y1, z1 = p1[0], p1[1], p1[2]
                    x2, y2, z2 = p2[0], p2[1], p2[2]

                    if int(math.floor(y2)) == int(math.floor(y0)):
                        continue

                    # Scanline do triângulo
                    y_start = max(0, int(math.floor(y0)))
                    y_end = min(altura, int(math.ceil(y2)))

                    for y in range(y_start, y_end):
                        # Interpolação na aresta longa (p0 -> p2)
                        t_long = (y - y0) / (y2 - y0) if y2 != y0 else 0
                        x_long = x0 + t_long * (x2 - x0)
                        z_long = z0 + t_long * (z2 - z0)

                        # Interpolação na aresta curta (p0 -> p1 ou p1 -> p2)
                        if y < y1:
                            t_short = (y - y0) / (y1 - y0) if y1 != y0 else 0
                            x_short = x0 + t_short * (x1 - x0)
                            z_short = z0 + t_short * (z1 - z0)
                        else:
                            t_short = (y - y1) / (y2 - y1) if y2 != y1 else 0
                            x_short = x1 + t_short * (x2 - x1)
                            z_short = z1 + t_short * (z2 - z1)

                        # Determina os limites horizontais da linha atual (X)
                        x_start, x_end = x_long, x_short
                        z_start, z_end = z_long, z_short
                        if x_start > x_end:
                            x_start, x_end = x_end, x_start
                            z_start, z_end = z_end, z_start

                        x_start_int = max(0, int(math.floor(x_start)))
                        x_end_int = min(largura, int(math.ceil(x_end)))

                        if x_start_int < x_end_int:
                            xs = np.arange(x_start_int, x_end_int)
                            if x_end != x_start:
                                zs = z_start + (xs - x_start) * (z_end - z_start) / (x_end - x_start)
                            else:
                                zs = np.full_like(xs, z_start)

                            # Teste de profundidade per-pixel usando NumPy vetorizado
                            mask = zs > depth_array[xs, y]
                            depth_array[xs[mask], y] = zs[mask]
                            pixel_array[xs[mask], y] = cor_rgb

            # Guarda as arestas para desenhar os contornos (toon ou wireframe)
            if wf or toon:
                cor_linha = [0, 255, 255] if wf else [0, 0, 0] # Ciano para WF, Preto para Toon
                n_pontos = len(pontos_projetados)
                for i in range(n_pontos):
                    p_atual = pontos_projetados[i]
                    p_proximo = pontos_projetados[(i + 1) % n_pontos]
                    linhas_contorno.append((p_atual, p_proximo, cor_linha))

    # 3. Renderização das linhas de contorno respeitando o Z-Buffer gerado
    for p0, p1, cor_linha in linhas_contorno:
        x0, y0, z0 = p0[0], p0[1], p0[2]
        x1, y1, z1 = p1[0], p1[1], p1[2]

        num_steps = max(int(abs(x1 - x0)), int(abs(y1 - y0))) + 1
        if num_steps > 1:
            xs = np.linspace(x0, x1, num_steps).astype(np.int32)
            ys = np.linspace(y0, y1, num_steps).astype(np.int32)
            zs = np.linspace(z0, z1, num_steps)

            # Filtra coordenadas que estão dentro dos limites da tela
            valid = (xs >= 0) & (xs < largura) & (ys >= 0) & (ys < altura)
            xs, ys, zs = xs[valid], ys[valid], zs[valid]

            # Teste de profundidade para a linha (com um pequeno bias para evitar Z-fighting com a própria face)
            mask = zs >= depth_array[xs, ys] - 0.01
            pixel_array[xs[mask], ys[mask]] = cor_linha

    return pixel_array