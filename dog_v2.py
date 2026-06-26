import pygame
import numpy as np
import math
import random
import colorsys
import cat
import dogpoints
import capy
import zbuffer

dog = []

for f in capy.capy:
    dog.append(f)

for f in dogpoints.dog:
    dog.append(f)

for f in cat.cat:
    dog.append(f)

hues = [0.08, 0.42, 0.86, 0.11, 0.66, 0.02, 0.33, 0.76, 0.15, 0.5, 0.59, 0, 0.2, 0.7]

yang = -math.pi/4
xang = math.pi/4

proj = (
    (math.cos(yang), math.sin(yang) * math.sin(xang), -math.sin(yang) * math.cos(xang)),
    (0, math.cos(xang), math.sin(xang)),
    (math.sin(yang), -math.sin(xang) * math.cos(yang), math.cos(xang) * math.cos(yang))
)

wf = True  # Wireframe ligado (Modo contornos cianos)  tecla w
po = False  # Pontos vermelhos nos vértices  tecla q
toon = True # Linhas pretas (Fora do modo wireframe)  tecla t
rotating_d = False     # seta direita
rotating_e = False     # seta esquerda

pygame.init()
res = (1280, 720)
interval = (3.6 * 16/9, 3.6)
window = pygame.display.set_mode(res)

running = True
clock = pygame.time.Clock()

# Z-BUFFER
faces_ordenadas = zbuffer.ordenar_faces(dog, proj, res, interval)

def calcular_pontos(dog, proj, res, interval):
    pontos = []
    for q in dog:
        partes = []
        for face in q:
            p = []
            for i in face:
                c = np.matmul(i, proj)
                p.append((res[0] * c[0]/(2*interval[0]) + res[0]/2, res[1] * -c[1]/(2*interval[1]) + res[1]/2))
            partes.append(p)
        pontos.append(partes)
    return pontos

pontos = calcular_pontos(dog, proj, res, interval)

while running:
    window.fill('black')
    pygame.draw.line(window, (32, 32, 32), (0, res[1]/2), (res[0], res[1]/2))
    pygame.draw.line(window, (32, 32, 32), (res[0]/2, 0), (res[0]/2, res[1]))

    # Z-BUFFER
    for face_2d, parte_idx, face_idx in faces_ordenadas:
        if not wf:
            pygame.draw.polygon(window, 'cyan', face_2d)
            if toon:
                pygame.draw.polygon(window, 'black', face_2d, 1)
        if wf:
            pygame.draw.polygon(window, 'cyan', face_2d, 1)

    if po:
        for j in pontos:
            for i in j:
                for k in i:
                    pygame.draw.circle(window, 'red', k, 2)

    # HANDLING DE EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rotating_d = True

            if event.key == pygame.K_LEFT:
                rotating_e = True

            if event.key == pygame.K_t:
                toon = not toon
            if event.key == pygame.K_w:
                wf = not wf
            if event.key == pygame.K_q:
                po = not po
            if event.key == pygame.K_c:
                cols = []
                random.seed()
                for i in range(len(dog)):
                    cols.append(colorsys.hsv_to_rgb(random.random(), 1, 1))

                cols255 = []
                for i in cols:
                    b = []
                    for j in i:
                        b.append(j * 255)
                    cols255.append(b)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rotating_d = False

            if event.key == pygame.K_LEFT:
                rotating_e = False

    pygame.display.flip()
    dt = clock.tick(144)/1000

    if rotating_d:
        yang += dt
    if rotating_e:
        yang -= dt
    if yang >= math.pi * 2 or yang <= -math.pi * 2:
        yang = 0

    proj = (
        (math.cos(yang), math.sin(yang) * math.sin(xang), -math.sin(yang) * math.cos(xang)),
        (0, math.cos(xang), math.sin(xang)),
        (math.sin(yang), -math.sin(xang) * math.cos(yang), math.cos(xang) * math.cos(yang))
    )
    # Z-BUFFER
    faces_ordenadas = zbuffer.ordenar_faces(dog, proj, res, interval)


    if po:
        pontos = calcular_pontos(dog, proj, res, interval)