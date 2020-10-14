import random
import math
from estadisticas import des_estandar, media


def agujas(num_agujas):
    dentro_circulo = 0

    for _ in range(num_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_centro = math.sqrt(x**2 + y**2)

        if distancia_centro <= 1:
            dentro_circulo += 1

    return (4 * dentro_circulo) / num_agujas


def estimacion(num_agujas, num_intentos):
    estimados = []

    for _ in range(num_intentos):
        estimacion_pi = agujas(num_agujas)
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)
    sigma = des_estandar(estimados)

    print(f"Est={round(media_estimados, 5)}, sigma={round(sigma, 5)}, agujas={num_agujas}")

    return (media_estimados, sigma)


def estimar_pi(precision, num_intentos):
    num_agujas = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        media, sigma = estimacion(num_agujas, num_intentos)
        num_agujas *= 2

    return media

if __name__ == "__main__":
    estimar_pi(0.01, 1000)