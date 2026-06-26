def prism(poly, start, width):
    priz = []
    base = []
    for i, point in enumerate(poly):
        base.append([point[0], point[1], start])
    priz.append(base)
    base = []
    for i, point in enumerate(poly):
        base.append([point[0], point[1], start + width])
    priz.append(base)

    for i, p in enumerate(priz[0]):
        if i + 1 < len(priz[0]):
            face = [priz[0][i], priz[0][i+1], priz[1][i + 1], priz[1][i]]
            priz.append(face)
        else:
            face = [priz[0][i], priz[0][-1], priz[1][-1], priz[1][i]]
            priz.append(face)


    return priz    

ocabeca = [(5, 5), (7.5, 6), (7, 7), (6.5, 8.5), (5.5, 7.5), (4, 8), (4.5, 5.3), (5, 5)]
orabo = [(0, 4.5), (-2.5, 5.0), (-4.5, 5.5), (-2.5, 7.5), (-2, 5.5), (0, 4.8), (0, 4.5)]
ocorpo = [(0, 3), (0, 5), (2, 5.5), (4.5, 5.3), (5, 5), (5, 3), (2, 2.5)]
opatad = [(4.8, 3), (4.5, 1.5), (5, 0), (4, 0), (3.5, 2), (4.2, 2.9)]
opatat = [(0.8, 2.8), (0.5, 1.5), (1, 0), (0, 0), (-0.5, 2), (0.2, 3)]

SCALE = 0.4
XSHIFT = -2 * SCALE
YSHIFT = -5 * SCALE
ZSHIFT = 5
ogato = [ocabeca, orabo, ocorpo, opatad, opatat]

gato = []

for oparte in ogato:
    parte = []
    for i in oparte:
        parte.append([SCALE * i[0] + XSHIFT, SCALE * i[1] + YSHIFT])
    gato.append(parte)






corpo3d = prism(gato[2], (0 + ZSHIFT) * SCALE, 1.5 * SCALE)
cabeca3d = prism(gato[0], (0 + ZSHIFT) * SCALE, 1.5 * SCALE)
rabo3d = prism(gato[1], (1.5/4 + ZSHIFT) * SCALE, 0.75 * SCALE)

patate = prism(gato[4], (0 + ZSHIFT) * SCALE, 0.6 * SCALE)
patatd = prism(gato[4], (0.9 + ZSHIFT) * SCALE, 0.6 * SCALE)

patade = prism(gato[3], (0 + ZSHIFT) * SCALE, 0.6 * SCALE)
patadd = prism(gato[3], (0.9 + ZSHIFT) * SCALE, 0.6 * SCALE)

print(patade)

cat = [corpo3d, cabeca3d, rabo3d, patate, patatd, patade, patadd]


