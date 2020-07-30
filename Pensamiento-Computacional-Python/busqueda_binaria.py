objetivo = int(input("Escoge un numero: "))
epsilon = 0.0000000001
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

while abs(respuesta ** 2 - objetivo) >= epsilon:
    print(f"bajo: {bajo}, alto: {alto}, respuetsa: {respuesta}")
    if respuesta ** 2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    
    respuesta = (alto + bajo) / 2

print(f"La raiz cuadrada del {objetivo} es {respuesta}")
