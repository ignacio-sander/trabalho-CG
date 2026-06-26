import numpy as np


def _profundidade_face(face_3d, proj):

    z_total = 0.0
    for ponto in face_3d:
        c = np.matmul(ponto, proj)
        z_total += c[2]
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

    todas.sort(key=lambda t: t[0], reverse=False)

    return [(pontos_2d, parte_idx, face_idx) for (_, parte_idx, face_idx, pontos_2d) in todas]