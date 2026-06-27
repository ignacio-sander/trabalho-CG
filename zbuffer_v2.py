import numpy as np

def _profundidade_face(face_3d, proj):
    # A 3ª coluna da matriz de projeção representa o eixo Z (profundidade/vetor da câmera)
    # Extraímos essa direção para simular o ponto de vista real no espaço 3D,
    # garantindo que a distância se atualize corretamente quando você rotaciona a cena.
    cam_dir = np.array([proj[0][2], proj[1][2], proj[2][2]])
    camera_pos = cam_dir * 1000.0  # Joga a câmera "para o infinito"

    z_total = 0.0
    for ponto in face_3d:
        p = np.array(ponto)
        # Calcula a distância euclidiana real do ponto até a câmera virtual
        distancia = np.linalg.norm(p - camera_pos)
        z_total += distancia
        
    return z_total / len(face_3d)

def ordenar_faces(dog, proj, res, interval):
    todas = [] 

    for parte_idx, parte in enumerate(dog):
        for face_idx, face in enumerate(parte):
            if len(face) < 2:
                continue

            prof = _profundidade_face(face, proj)

            pontos_2d = []
            for ponto in face:
                c = np.matmul(ponto, proj)
                px = res[0] * c[0] / (2 * interval[0]) + res[0] / 2
                py = res[1] * -c[1] / (2 * interval[1]) + res[1] / 2
                pontos_2d.append((px, py))

            todas.append((prof, parte_idx, face_idx, pontos_2d))

    # reverse=True garante que as maiores distâncias (fundo) sejam desenhadas primeiro
    todas.sort(key=lambda t: t[0], reverse=True)

    return [(pontos_2d, parte_idx, face_idx) for (_, parte_idx, face_idx, pontos_2d) in todas]