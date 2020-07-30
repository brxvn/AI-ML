objetivo = int(input("Escoge un numero: "))
epsilon = 0.0001
paso = epsilon ** 2
respuesta = 0.0
iteraciones = 0
while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
    iteraciones += 1

if abs(respuesta ** 2 - objetivo) >= epsilon:
    print(f"No se encontró la raiz cuadrada de {objetivo}")
else:
    print(f"La raiz cuadrada de {objetivo} es {respuesta} y se calculo con {iteraciones} iteraciones.")
