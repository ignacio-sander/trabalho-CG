import pygame
import numpy as np
import math
import random
import colorsys
import matplotlib.colors as mcolors
import sys

# =====================================================================
# ======================== DADOS DO CACHORRO ==========================
# =====================================================================

Torso = [[(-1, 0, 0.5), (0, -0.5, 0.5), (1, -0.5, 0.5), (1.5, 0, 0.5), (1.0, 1.5, 0.5), (-1, 1.5, 0.5), (-1, 0, 0.5)],
    [(-1, 0, -0.5), (0, -0.5, -0.5), (1, -0.5, -0.5), (1.5, 0, -0.5), (1.0, 1.5, -0.5), (-1, 1.5, -0.5), (-1, 0, -0.5)],
    [(-1, 0, 0.5), (-1, 0, -0.5), (0, -0.5, -0.5), (0, -0.5, 0.5)],
    [(0, -0.5, 0.5), (1, -0.5, 0.5), (1, -0.5, -0.5), (0, -0.5, -0.5)],
    [(1, -0.5, 0.5), (1.5, 0, 0.5), (1.5, 0, -0.5), (1, -0.5, -0.5)],
    [(1.5, 0, 0.5), (1.0, 1.5, 0.5), (1.0, 1.5, -0.5), (1.5, 0, -0.5)],
    [(1.0, 1.5, 0.5), (-1, 1.5, 0.5), (-1, 1.5, -0.5), (1.0, 1.5, -0.5)],
    [(-1, 1.5, 0.5), (-1, 0, 0.5), (-1, 0, -0.5), (-1, 1.5, -0.5)]]
shtorso = [1, 1, 1, 1, 1, 0.5, 1, 1]

Quadril = [[(-1, 0, 0.5), (-1, 1.5, 0.5), (-2.5, 1.5, 0.5), (-2.5, 0, 0.5), (-1, 0, 0.5)],
    [(-1, 0, -0.5), (-1, 1.5, -0.5), (-2.5, 1.5, -0.5), (-2.5, 0, -0.5), (-1, 0, -0.5)],
    [(-1, 0, 0.5), (-1, 1.5, 0.5), (-1, 1.5, -0.5), (-1, 0, -0.5)],
    [(-1, 1.5, 0.5), (-2.5, 1.5, 0.5), (-2.5, 1.5, -0.5), (-1, 1.5, -0.5)],
    [(-2.5, 1.5, 0.5), (-2.5, 0, 0.5),  (-2.5, 0, -0.5), (-2.5, 1.5, -0.5)],
    [(-2.5, 0, 0.5), (-1, 0, 0.5),  (-1, 0, -0.5), (-2.5, 0, -0.5)]]
shquadril = [1, 1, 1, 0.5, 1, 1]

Cauda = [    
    [(-2.5, 1.5, 0.1), (-2.5, 2.25, 0.1), (-2.3, 3, 0.1), (-2.15, 2.9, 0.1), (-2.3, 2.25, 0.1), (-2.3, 1.5, 0.1), (-2.5, 1.5, 0.1)],
    [(-2.5, 1.5, 0.1), (-2.5, 2.25, 0.1), (-2.5, 2.25, -0.1), (-2.5, 1.5, -0.1)],
    [(-2.5, 2.25, 0.1), (-2.3, 3, 0.1), (-2.3, 3, -0.1), (-2.5, 2.25, -0.1)],
    [(-2.3, 3, 0.1), (-2.15, 2.9, 0.1), (-2.15, 2.9, -0.1), (-2.3, 3, -0.1)],
    [(-2.15, 2.9, 0.1), (-2.3, 2.25, 0.1), (-2.3, 2.25, -0.1), (-2.15, 2.9, -0.1)],
    [(-2.3, 2.25, 0.1), (-2.3, 1.5, 0.1), (-2.3, 1.5, -0.1), (-2.3, 2.25, -0.1)],
    [(-2.3, 1.5, 0.1), (-2.5, 1.5, 0.1), (-2.5, 1.5, -0.1), (-2.3, 1.5, -0.1)],
    [(-2.3, 1.5, 0.1), (-2.5, 1.5, 0.1), (-2.5, 1.5, -0.1), (-2.3, 1.5, -0.1)]]
shcauda = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.98, 0.4]

CoxaR = [[(-1.34, 0.55, 0.5), (-2.16, 1.13, 0.5), (-2.8, -0.4, 0.5), (-2.45, -0.81, 0.5), (-1.34, 0.55, 0.5)],
    [(-1.34, 0.55, 0.7), (-2.16, 1.13, 0.7), (-2.8, -0.4, 0.7), (-2.45, -0.81, 0.7), (-1.34, 0.55, 0.7)],
    [(-1.34, 0.55, 0.5), (-2.16, 1.13, 0.5), (-2.16, 1.13, 0.7), (-1.34, 0.55, 0.7)],
    [(-2.16, 1.13, 0.5), (-2.8, -0.4, 0.5),  (-2.8, -0.4, 0.7), (-2.16, 1.13, 0.7)],
    [(-2.8, -0.4, 0.5), (-2.45, -0.81, 0.5), (-2.45, -0.81, 0.7), (-2.8, -0.4, 0.7)],
    [(-2.45, -0.81, 0.5), (-1.34, 0.55, 0.5), (-1.34, 0.55, 0.7), (-2.45, -0.81, 0.7)]]
shcoxar = [1, 1, 1, 0.5, 0.9, 0.36]

CoxaL = [[(-1.34, 0.55, -0.5), (-2.16, 1.13, -0.5), (-2.8, -0.4, -0.5), (-2.45, -0.81, -0.5), (-1.34, 0.55, -0.5)],
    [(-1.34, 0.55, -0.7), (-2.16, 1.13, -0.7), (-2.8, -0.4, -0.7), (-2.45, -0.81, -0.7), (-1.34, 0.55, -0.7)],
    [(-1.34, 0.55, -0.5), (-2.16, 1.13, -0.5), (-2.16, 1.13, -0.7), (-1.34, 0.55, -0.7)],
    [(-2.16, 1.13, -0.5), (-2.8, -0.4, -0.5),  (-2.8, -0.4, -0.7), (-2.16, 1.13, -0.7)],
    [(-2.8, -0.4, -0.5), (-2.45, -0.81, -0.5), (-2.45, -0.81, -0.7), (-2.8, -0.4, -0.7)],
    [(-2.45, -0.81, -0.5), (-1.34, 0.55, -0.5), (-1.34, 0.55, -0.7), (-2.45, -0.81, -0.7)]]
shcoxal = [1, 1, 1, 1, 1, 1]

PataTraseiraR = [[(-3.03, -0.47, 0.7), (-2.79, -2.10, 0.7), (-2.35, -2.10, 0.7), (-2.32, -1.79, 0.7), (-2.53, -1.72, 0.7), (-2.45, -0.81, 0.7), (-2.8, -0.4, 0.7), (-3.03, -0.47, 0.7)],
    [(-3.03, -0.47, 0.5), (-2.79, -2.10, 0.5), (-2.79, -2.10, 0.7), (-3.03, -0.47, 0.7)],
    [(-2.79, -2.10, 0.5), (-2.35, -2.10, 0.5), (-2.35, -2.10, 0.7), (-2.79, -2.10, 0.7)],
    [(-2.53, -1.72, 0.5), (-2.45, -0.81, 0.5), (-2.45, -0.81, 0.7), (-2.53, -1.72, 0.7)],
    [(-2.45, -0.81, 0.5), (-2.8, -0.4, 0.5), (-2.8, -0.4, 0.7), (-2.45, -0.81, 0.7)],
    [(-2.8, -0.4, 0.5), (-3.03, -0.47, 0.5), (-3.03, -0.47, 0.7), (-2.8, -0.4, 0.7)],
    [(-2.32, -1.79, 0.5), (-2.53, -1.72, 0.5), (-2.53, -1.72, 0.7), (-2.32, -1.79, 0.7)],
    [(-2.35, -2.10, 0.5), (-2.32, -1.79, 0.5), (-2.32, -1.79, 0.7), (-2.35, -2.10, 0.7)]]
shpatatr = [1, 0.92, 0.46, 0.92, 0.92, 0.5, 0.44, 0.49]

PataTraseiraL = [[(-3.03, -0.47, -0.5), (-2.79, -2.10, -0.5), (-2.35, -2.10, -0.5), (-2.32, -1.79, -0.5), (-2.53, -1.72, -0.5), (-2.45, -0.81, -0.5), (-2.8, -0.4, -0.5), (-3.03, -0.47, -0.5)],
    [(-3.03, -0.47, -0.5), (-2.79, -2.10, -0.5), (-2.79, -2.10, -0.7), (-3.03, -0.47, -0.7)],
    [(-2.79, -2.10, -0.5), (-2.35, -2.10, -0.5), (-2.35, -2.10, -0.7), (-2.79, -2.10, -0.7)],
    [(-2.35, -2.10, -0.5), (-2.32, -1.79, -0.5), (-2.32, -1.79, -0.7), (-2.35, -2.10, -0.7)],
    [(-2.32, -1.79, -0.5), (-2.53, -1.72, -0.5), (-2.53, -1.72, -0.7), (-2.32, -1.79, -0.7)],
    [(-2.53, -1.72, -0.5), (-2.45, -0.81, -0.5), (-2.45, -0.81, -0.7), (-2.53, -1.72, -0.7)],
    [(-2.45, -0.81, -0.5), (-2.8, -0.4, -0.5), (-2.8, -0.4, -0.7), (-2.45, -0.81, -0.7)],
    [(-2.8, -0.4, -0.5), (-3.03, -0.47, -0.5), (-3.03, -0.47, -0.7), (-2.8, -0.4, -0.7)]]
shpatatrl = [1, 0.46, 0.92, 1, 1, 0.5, 0.44, 0.5]

BraçoR = [[(1.24, -0.62, 0.5), (0.77, -0.55, 0.5), (0.84, 0.53, 0.5), (1.5, 0.53, 0.5), (1.24, -0.62, 0.5)],
    [(1.24, -0.62, 0.7), (0.77, -0.55, 0.7), (0.84, 0.53, 0.7), (1.5, 0.53, 0.7), (1.24, -0.62, 0.7)],
    [(1.24, -0.62, 0.5), (0.77, -0.55, 0.5), (0.77, -0.55, 0.7), (1.24, -0.62, 0.7)],
    [(0.77, -0.55, 0.5), (0.84, 0.53, 0.5), (0.84, 0.53, 0.7), (0.77, -0.55, 0.7)],
    [(0.84, 0.53, 0.5), (1.5, 0.53, 0.5), (1.5, 0.53, 0.7), (0.84, 0.53, 0.7)],
    [(1.5, 0.53, 0.5), (1.24, -0.62, 0.5), (1.24, -0.62, 0.7), (1.5, 0.53, 0.7)]]
shbracor = [1, 1, 1, 0.5, 1, 0.46]

BraçoL = [[(1.24, -0.62, -0.5), (0.77, -0.55, -0.5), (0.84, 0.53, -0.5), (1.5, 0.53, -0.5), (1.24, -0.62, -0.5)],
    [(1.24, -0.62, -0.7), (0.77, -0.55, -0.7), (0.84, 0.53, -0.7), (1.5, 0.53, -0.7), (1.24, -0.62, -0.7)],
    [(1.24, -0.62, -0.5), (0.77, -0.55, -0.5), (0.77, -0.55, -0.7), (1.24, -0.62, -0.7)],
    [(0.77, -0.55, -0.5), (0.84, 0.53, -0.5), (0.84, 0.53, -0.7), (0.77, -0.55, -0.7)],
    [(0.84, 0.53, -0.5), (1.5, 0.53, -0.5), (1.5, 0.53, -0.7), (0.84, 0.53, -0.7)],
    [(1.5, 0.53, -0.5), (1.24, -0.62, -0.5), (1.24, -0.62, -0.7), (1.5, 0.53, -0.7)]]
shbracol = [1, 1, 1, 0.5, 1, 0.46]

PataDianteiraR = [[(0.77, -0.55, 0.7), (0.71, -1.53, 0.7), (0.84, -2.10, 0.7), (1.19, -2.10, 0.7), (1.21, -1.81, 0.7), (1.03, -1.74, 0.7), (1.24, -0.62, 0.7), (0.77, -0.55, 0.7)],
    [(0.77, -0.55, 0.5), (0.71, -1.53, 0.5), (0.71, -1.53, 0.7), (0.77, -0.55, 0.7)],
    [(0.71, -1.53, 0.5), (0.84, -2.10, 0.5), (0.84, -2.10, 0.7), (0.71, -1.53, 0.7)],
    [(0.84, -2.10, 0.5), (1.19, -2.10, 0.5), (1.19, -2.10, 0.7), (0.84, -2.10, 0.7)],
    [(1.21, -1.81, 0.5), (1.03, -1.74, 0.5), (1.03, -1.74, 0.7), (1.21, -1.81, 0.7)],
    [(1.03, -1.74, 0.5), (1.24, -0.62, 0.5), (1.24, -0.62, 0.7), (1.03, -1.74, 0.7)],
    [(1.24, -0.62, 0.5), (0.77, -0.55, 0.5), (0.77, -0.55, 0.7), (1.24, -0.62, 0.7)],
    [(1.19, -2.10, 0.5), (1.21, -1.81, 0.5), (1.21, -1.81, 0.7), (1.19, -2.10, 0.7)]]
shpatadr = [0.96, 0.96, 0.96, 0.49, 0.96, 0.5, 0.46, 0.5]

PataDianteiraL = [[(0.77, -0.55, -0.5), (0.71, -1.53, -0.5), (0.84, -2.10, -0.5), (1.19, -2.10, -0.5), (1.21, -1.81, -0.5), (1.03, -1.74, -0.5), (1.24, -0.62, -0.5), (0.77, -0.55, -0.5)],
    [(0.77, -0.55, -0.5), (0.71, -1.53, -0.5), (0.71, -1.53, -0.7), (0.77, -0.55, -0.7)],
    [(0.71, -1.53, -0.5), (0.84, -2.10, -0.5), (0.84, -2.10, -0.7), (0.71, -1.53, -0.7)],
    [(0.84, -2.10, -0.5), (1.19, -2.10, -0.5), (1.19, -2.10, -0.7), (0.84, -2.10, -0.7)],
    [(1.19, -2.10, -0.5), (1.21, -1.81, -0.5), (1.21, -1.81, -0.7), (1.19, -2.10, -0.7)],
    [(1.21, -1.81, -0.5), (1.03, -1.74, -0.5), (1.03, -1.74, -0.7), (1.21, -1.81, -0.7)],
    [(1.03, -1.74, -0.5), (1.24, -0.62, -0.5), (1.24, -0.62, -0.7), (1.03, -1.74, -0.7)],
    [(1.24, -0.62, -0.5), (0.77, -0.55, -0.5), (0.77, -0.55, -0.7), (1.24, -0.62, -0.7)]]
shpatadl = [1, 1, 0.49, 0.96, 0.5, 0.5, 0.46, 0.5]

Cabeça = [[(1, 1.5, 0.5), (1.23, 1.72, 0.5), (1.63, 2.54, 0.5), (2.28, 2.43, 0.5), (2.49, 1.83, 0.5), (2.15, 1.13, 0.5), (1.5, 0, 0.5), (1, 1.5, 0.5)],
    [(1, 1.5, -0.5), (1.23, 1.72, -0.5), (1.63, 2.54, -0.5), (2.28, 2.43, -0.5), (2.49, 1.83, -0.5), (2.15, 1.13, -0.5), (1.5, 0, -0.5), (1, 1.5, -0.5)],
    [(1, 1.5, 0.5), (1.23, 1.72, 0.5),  (1.23, 1.72, -0.5), (1, 1.5, -0.5)],
    [(1.23, 1.72, 0.5), (1.63, 2.54, 0.5), (1.63, 2.54, -0.5), (1.23, 1.72, -0.5)],
    [(1.63, 2.54, 0.5), (2.28, 2.43, 0.5), (2.28, 2.43, -0.5), (1.63, 2.54, -0.5)],
    [(2.28, 2.43, 0.5), (2.49, 1.83, 0.5), (2.49, 1.83, -0.5), (2.28, 2.43, -0.5)],
    [(2.15, 1.13, 0.5), (1.5, 0, 0.5), (1.5, 0, -0.5), (2.15, 1.13, -0.5)],
    [(1.5, 0, 0.5), (1, 1.5, 0.5), (1, 1.5, 0.5), (1.5, 0, 0.5)],
    [(2.49, 1.83, 0.5), (3.06, 1.68, 0.25), (2.8, 1.18, 0.25), (2.15, 1.13, 0.5)],
    [(2.49, 1.83, -0.5), (3.06, 1.68, -0.25), (2.8, 1.18, -0.25), (2.15, 1.13, -0.5)],
    [(2.49, 1.83, 0.5), (3.06, 1.68, 0.25), (3.06, 1.68, -0.25), (2.49, 1.83, -0.5)],
    [(3.06, 1.68, 0.25), (2.8, 1.18, 0.25), (2.8, 1.18, -0.25), (3.06, 1.68, -0.25)],
    [(2.8, 1.18, 0.25), (2.15, 1.13, 0.5), (2.15, 1.13, -0.5), (2.8, 1.18, -0.25)]]
shcab = [1, 0.72, 0.38, 1, 1, 1, 0.5, 0.96, 0.8, 0.8, 0.5, 0.9, 0.42]

OrelhaR = [[(1.63, 2.54, 0.3), (1.97, 2.5, 0.5), (1.97, 2.5, 0.1)],
           [(1.63, 2.54, 0.3), (2.01, 3.04, 0.3), (1.97, 2.5, 0.1)],
           [(1.63, 2.54, 0.3), (2.01, 3.04, 0.3), (1.97, 2.5, 0.5)],
           [(2.01, 3.04, 0.3), (1.97, 2.5, 0.5), (1.97, 2.5, 0.1)]]
shorelhar = [1, 0.5, 0.75, 0.5]

OrelhaL = [[(1.63, 2.54, -0.3), (1.97, 2.5, -0.5), (1.97, 2.5, -0.1)],
           [(1.63, 2.54, -0.3), (2.01, 3.04, -0.3), (1.97, 2.5, -0.5)],
           [(2.01, 3.04, -0.3), (1.97, 2.5, -0.5), (1.97, 2.5, -0.1)],
           [(1.63, 2.54, -0.3), (2.01, 3.04, -0.3), (1.97, 2.5, -0.1)]]
shorelhal = [1, 0.5, 0.5, 0.75]

dog = [PataTraseiraL, CoxaL, PataDianteiraL, BraçoL, Quadril, Cauda, Torso, Cabeça, OrelhaR, OrelhaL, PataTraseiraR, CoxaR, PataDianteiraR, BraçoR]
shades = [shpatatrl, shcoxal, shpatadl, shbracol, shquadril, shcauda, shtorso, shcab, shorelhar, shorelhal, shpatatr, shcoxar, shpatadr, shbracor]
hues = [0.08, 0.42, 0.86, 0.11, 0.66, 0.02, 0.33, 0.76, 0.15, 0.5, 0.59, 0, 0.2, 0.7]

# Pré-processamento do Cachorro (Ordenação e Cores)
def kdist(p):
    bd = 0
    for i in p:
        if math.dist(i, (-27.9, -21.0, -5)) > bd:
            bd = math.dist(i, (-27.9, -21.0, -5))
    return bd

for parte in dog:
    parte.sort(key=kdist)

cols = []
random.seed()
for i, hue in enumerate(hues):
    facecolors = []
    for sh in shades[i]:
        facecolors.append(colorsys.hsv_to_rgb(hue, 1, sh))
    cols.append(facecolors)

cols255 = []
for part in cols:
    part255 = []
    for face in part:
        face255 = [k * 255 for k in face]
        part255.append(face255)
    cols255.append(part255)


# =====================================================================
# =========================== DADOS DO GATO ===========================
# =====================================================================

def gerar_curva_bezier_cubica(p0, p1, p2, p3, numero_de_pontos=15):
    t_valores = np.linspace(0, 1, numero_de_pontos)
    curva_pontos = []
    for t in t_valores:
        b0 = (1-t)**3
        b1 = 3 * t * (1-t)**2
        b2 = 3 * (t**2) * (1-t)
        b3 = t**3
        x = b0*p0[0] + b1*p1[0] + b2*p2[0] + b3*p3[0]
        y = b0*p0[1] + b1*p1[1] + b2*p2[1] + b3*p3[1]
        curva_pontos.append((x, y))
    return curva_pontos

profundidades = {
    "corpo": (-1.0, 1.0), "cabeca": (-1.0, 1.0), "rabo": (-0.4, 0.4),             
    "pata_frente_dir": (-1.0, -0.2), "pata_frente_esq": (0.2, 1.0),   
    "pata_tras_dir": (-1.0, -0.2), "pata_tras_esq": (0.2, 1.0)
}

camadas_renderizacao = {
    "pata_frente_esq": 1, "pata_tras_esq": 1, 
    "pata_tras_dir": 2, "pata_frente_dir": 2, 
    "corpo": 3, "rabo": 4, "cabeca": 5 
}

dados_pata_frente = {
    "pontos_guias": [(4.8, 3), (4.5, 1.5), (5, 0), (4, 0), (3.5, 2), (4.2, 2.9)],
    "segmentos_curvos": [(0, 0, 1, 1), (1, 1, 2, 2), (2, 2, 3, 3), (3, 4, 4, 5), (5, 5, 0, 0)]
}

dados_pata_tras = {
    "pontos_guias": [(0.8, 2.8), (0.5, 1.5), (1, 0), (0, 0), (-0.5, 2), (0.2, 3)],
    "segmentos_curvos": [(0, 0, 1, 1), (1, 1, 2, 2), (2, 2, 3, 3), (3, 4, 4, 5), (5, 5, 0, 0)]
}

gato_vetorial_curvo = {
    "corpo": {
        "pontos_guias": [(0, 3), (0, 5), (2, 5.5), (4.5, 5.3), (5, 5), (5, 3), (2, 2.5)],
        "segmentos_curvos": [(0, 0, 1, 1), (1, 2, 2, 3), (3, 3, 4, 4), (4, 4, 5, 5), (5, 6, 6, 0)]
    },
    "cabeca": {
        "pontos_guias": [(5, 5), (7.5, 6), (7, 7), (6.5, 8.5), (5.5, 7.5), (4, 8), (4.5, 5.3), (5, 5)],
        "segmentos_curvos": [(0, 1, 1, 2), (2, 3, 3, 4), (4, 5, 5, 6), (6, 6, 7, 7)]
    },
    "rabo": {
        "pontos_guias": [(0, 4.5), (-2.5, 5.0), (-4.5, 5.5), (-2.5, 7.5), (-2, 5.5), (0, 4.8), (0, 4.5)],
        "segmentos_curvos": [(0, 0, 1, 1), (1, 2, 3, 4), (4, 4, 5, 5), (5, 5, 6, 6)]
    },
    "pata_frente_dir": dados_pata_frente, "pata_frente_esq": dados_pata_frente,
    "pata_tras_dir": dados_pata_tras, "pata_tras_esq": dados_pata_tras
}

cores_gato = {
    "corpo": "gray", "cabeca": "orange", "rabo": "brown",
    "pata_frente_dir": "blue", "pata_frente_esq": "darkblue",
    "pata_tras_dir": "purple", "pata_tras_esq": "indigo"
}

# Funções do Gato (Matemática de Rendering)
L = np.array([0.5, 1.0, -0.8])
L = L / np.linalg.norm(L)

def calcular_normal_parede(p1, p2, p3):
    v1 = np.array(p2) - np.array(p1)
    v2 = np.array(p3) - np.array(p1)
    N = np.cross(v2, v1)
    norma = np.linalg.norm(N)
    if norma == 0: return np.array([0,1,0])
    return N / norma

def calcular_normal_suave(p1, p2, p3, p4):
    v1 = np.array(p3) - np.array(p1)
    v2 = np.array(p4) - np.array(p2)
    N = np.cross(v1, v2)
    return N / np.linalg.norm(N)

def aplicar_shading_hsv_gato(cor_base_hex, normal):
    I_amb = 0.4
    k_d = 0.6
    produto_escalar = max(0, np.dot(normal, L))
    intensidade = I_amb + (k_d * produto_escalar)
    rgb = mcolors.to_rgb(cor_base_hex)
    hsv = list(mcolors.rgb_to_hsv(rgb))
    hsv[2] = min(1.0, hsv[2] * intensidade)
    rgb_final = mcolors.hsv_to_rgb(hsv)
    return tuple(int(c * 255) for c in rgb_final)

def projecao_isometrica_gato(pontos_3d):
    pontos_projetados = []
    cos30 = np.cos(np.pi / 6)
    sin30 = np.sin(np.pi / 6)
    for p in pontos_3d:
        x, y, z = p
        x_tela = (x - z) * cos30
        y_tela = y + (x + z) * sin30
        pontos_projetados.append((x_tela, y_tela))
    return pontos_projetados

def calcular_profundidade_gato(pontos_3d):
    c = np.mean(pontos_3d, axis=0)
    return c[0] * 0.5 - c[1] * 0.866025 + c[2] * 0.5

# Construção Estática do Sólido do Gato
faces_gato = []
for parte, dados in gato_vetorial_curvo.items():
    pontos_2d = []
    pontos_guias = dados["pontos_guias"]
    segmentos = dados["segmentos_curvos"]
    for seg in segmentos:
        curva = gerar_curva_bezier_cubica(pontos_guias[seg[0]], pontos_guias[seg[1]], 
                                          pontos_guias[seg[2]], pontos_guias[seg[3]])
        pontos_2d.extend(curva[:-1])
    
    z_frente, z_fundo = profundidades[parte]
    layer_atual = camadas_renderizacao[parte]
    face_frente_3d = [(p[0], p[1], z_frente) for p in pontos_2d]
    face_fundo_3d = [(p[0], p[1], z_fundo) for p in reversed(pontos_2d)]
    cor_base = cores_gato[parte]
    
    normal_frente = np.array([0.0, 0.0, -1.0])
    faces_gato.append({
        '3d': face_frente_3d, 'cor': aplicar_shading_hsv_gato(cor_base, normal_frente), 
        'z_sort': calcular_profundidade_gato(face_frente_3d), 'layer': layer_atual
    })
    
    normal_fundo = np.array([0.0, 0.0, 1.0])
    faces_gato.append({
        '3d': face_fundo_3d, 'cor': aplicar_shading_hsv_gato(cor_base, normal_fundo), 
        'z_sort': calcular_profundidade_gato(face_fundo_3d), 'layer': layer_atual
    })
    
    for i in range(len(pontos_2d)):
        p1_frente = face_frente_3d[i]
        p2_frente = face_frente_3d[(i + 1) % len(pontos_2d)]
        idx_fundo = len(pontos_2d) - 1 - i
        idx_fundo_prev = len(pontos_2d) - 1 - ((i + 1) % len(pontos_2d))
        parede = [p1_frente, p2_frente, face_fundo_3d[idx_fundo_prev], face_fundo_3d[idx_fundo]]
        
        if parte == "rabo":
            normal_parede = calcular_normal_suave(parede[0], parede[1], parede[2], parede[3])
        else:
            normal_parede = calcular_normal_parede(parede[0], parede[1], parede[2])
            
        faces_gato.append({
            '3d': parede, 'cor': aplicar_shading_hsv_gato(cor_base, normal_parede), 
            'z_sort': calcular_profundidade_gato(parede), 'layer': layer_atual
        })

faces_gato.sort(key=lambda f: (f['layer'], -f['z_sort']))


# =====================================================================
# ======================= FUUUSION DO MOTOR PYGAME ======================
# =====================================================================

pygame.init()
LARGURA = 1280
ALTURA = 720
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cena 3d do gato e cachorro")

clock = pygame.time.Clock()
running = True


# Cachorro na Esquerda
OFFSET_X_CACHORRO = LARGURA * 0.25 
OFFSET_Y_CACHORRO = ALTURA * 0.5   
interval = (3.6 * 16/9, 3.6) 

# Gato na Direita
OFFSET_X_GATO = LARGURA * 0.70
OFFSET_Y_GATO = ALTURA * 0.5 + 200
ESCALA_GATO = 45 


wf = False
po = False
yang = -math.pi/4
xang = math.pi/4

while running:
    window.fill((230, 230, 230))
    

    
    # ---------------------------------------------------------
    # 1. RENDERIZAÇÃO DO CACHORRO
    # ---------------------------------------------------------
    proj_cachorro = (
        (math.cos(yang), math.sin(yang) * math.sin(xang), -math.sin(yang) * math.cos(xang)),
        (0, math.cos(xang), math.sin(xang)),
        (math.sin(yang), -math.sin(xang) * math.cos(yang), math.cos(xang) * math.cos(yang))
    )
    
    pontos_cachorro = []
    for q in dog:
        partes = []
        for face in q:
            p = []
            for i in face:
                c = np.matmul(i, proj_cachorro)
                x_tela = LARGURA * c[0]/(2*interval[0]) + OFFSET_X_CACHORRO
                y_tela = ALTURA * -c[1]/(2*interval[1]) + OFFSET_Y_CACHORRO
                p.append((x_tela, y_tela))
            partes.append(p)
        pontos_cachorro.append(partes)

    for c, part in enumerate(pontos_cachorro):
        for m, face in enumerate(part):
            pygame.draw.polygon(window, cols255[c][m], face)
            if wf:
                pygame.draw.polygon(window, 'black', face, 1)

    if po:
        for j in pontos_cachorro:
            for i in j:
                for k in i:
                    pygame.draw.circle(window, 'red', k, 2)


    # ---------------------------------------------------------
    # RENDERIZAÇÃO DO GATO
    # ---------------------------------------------------------
    for face in faces_gato:
        pontos_2d_proj = projecao_isometrica_gato(face['3d'])
        
        pontos_tela = []
        for p in pontos_2d_proj:
            x_tela = p[0] * ESCALA_GATO + OFFSET_X_GATO
            y_tela = -p[1] * ESCALA_GATO + OFFSET_Y_GATO
            pontos_tela.append((x_tela, y_tela))
            
        pygame.draw.polygon(window, face['cor'], pontos_tela)
        pygame.draw.polygon(window, face['cor'], pontos_tela, 1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()
    
    # Mantém os 60 FPS
    clock.tick(60)
    
pygame.quit()
sys.exit()