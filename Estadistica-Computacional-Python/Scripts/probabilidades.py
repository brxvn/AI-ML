import random

def tirar_dado(num_tiros):
    secuencia_tiros = []
    
    for _ in range(num_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        tiro += random.choice([1, 2, 3, 4, 5, 6])
        secuencia_tiros.append(tiro)
    
    return secuencia_tiros

def main(num_tiros, num_intentos):
    tiros = []
    for _ in range(num_intentos):
        secuencia_tiros = tirar_dado(num_tiros)
        tiros.append(secuencia_tiros)
    
    tiros_12 = 0
    for tiro in tiros:
        if 12 in tiro:
            tiros_12 += 1
    
    probabilidad_tiros_12 = tiros_12 / num_intentos
    print(f"La probabilidad de obtener por lo menos un 12 en {num_tiros} tiros = {probabilidad_tiros_12}")

if __name__ == "__main__":
    num_tiros = int(input("Cuantas tiros del dado: "))
    num_intentos = int(input("Cuantas veces corerrá la simulación: "))

    main(num_tiros, num_intentos)