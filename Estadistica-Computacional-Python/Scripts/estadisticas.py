import random

def media(X):
    return sum(X) / len(X)


def varianza(X):
    mu = media(X)

    acumulador = 0

    for x in X:
        acumulador += (x- mu) ** 2

    return acumulador/len(X)

    
def des_estandar(X):
    return varianza(X) ** 0.5

if __name__ == "__main__":
    X = [random.randint(9,12) for i in range(20)]
    mu = media(X)
    Var = varianza(X)
    sigma = des_estandar(X)

    print(f"El arreglo es: {X}")
    print(f"La medias es: {mu}")
    print(f"La varianza es: {Var}")
    print(f"La desviacion estandar es: {sigma}")