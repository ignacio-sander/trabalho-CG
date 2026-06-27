import pygame
import numpy as np
import math
import random
import colorsys
import cat
import dog
import capy
import zbuffer

animals = []

for f in capy.capy:
    animals.append(f)

for f in dog.dog:
    animals.append(f)

for f in cat.cat:
    animals.append(f)

hues = [0.08, 0.42, 0.86, 0.11, 0.66, 0.02, 0.33, 0.76, 0.15, 0.5, 0.59, 0, 0.2, 0.7]

yang = -math.pi/4
xang = math.pi/4

proj = (
    (math.cos(yang), math.sin(yang) * math.sin(xang), -math.sin(yang) * math.cos(xang)),
    (0, math.cos(xang), math.sin(xang)),
    (math.sin(yang), -math.sin(xang) * math.cos(yang), math.cos(xang) * math.cos(yang))
)

wf = False  # Wireframe ligado (Modo contornos cianos)  tecla w
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
faces_ordenadas = zbuffer.ordenar_faces(animals, proj, res, interval)

def calcular_pontos(animals, proj, res, interval):
    pontos = []
    for q in animals:
        partes = []
        for face in q:
            p = []
            for i in face:
                c = np.matmul(i, proj)
                p.append((res[0] * c[0]/(2*interval[0]) + res[0]/2, res[1] * -c[1]/(2*interval[1]) + res[1]/2))
            partes.append(p)
        pontos.append(partes)
    return pontos

pontos = calcular_pontos(animals, proj, res, interval)

normalmap = []
for parte in animals:
    partes = []
    for face in parte:
        v0 = [face[1][0] - face[0][0], face[1][1] - face[0][1], face[1][2] - face[0][2]]
        v1 = [face[1][0] - face[2][0], face[1][1] - face[2][1], face[1][2] - face[2][2]]
        n = np.cross(v0, v1)
        partes.append(n)
    normalmap.append(partes)

shademap = []
for parte in normalmap:
    partes = []
    for face in parte:
        
        N = np.linalg.norm(face)
        if N != 0:

            shade = ((np.dot(face, (0, 1, 0))/(np.linalg.norm(face))) + 1)/2

        else:
            shade = 0
        partes.append(shade)
    shademap.append(partes)


hues = []
for parte in animals:
    hues.append(random.random())

while running:
    window.fill('black')
    pygame.draw.line(window, (32, 32, 32), (0, res[1]/2), (res[0], res[1]/2))
    pygame.draw.line(window, (32, 32, 32), (res[0]/2, 0), (res[0]/2, res[1]))

    # Z-BUFFER
    for face_2d, parte_idx, face_idx in faces_ordenadas:
        if not wf:
            pygame.draw.polygon(window, [item * 255 for item in colorsys.hsv_to_rgb(hues[parte_idx], 1, shademap[parte_idx][face_idx])], face_2d)
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
                hues = []
                for parte in animals:
                    hues.append(random.random())

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
    faces_ordenadas = zbuffer.ordenar_faces(animals, proj, res, interval)


    if po:
        pontos = calcular_pontos(animals, proj, res, interval)