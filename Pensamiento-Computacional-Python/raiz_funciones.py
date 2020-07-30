def aproximacion(objetivo):
    epsilon = 0.001
    paso = epsilon ** 2
    respuesta = 0.0

    while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
        
    if abs(respuesta ** 2 - objetivo) >= epsilon:
        print(f"No se encontró la raiz cuadrada de {objetivo}")
    else:
        print(f"La raiz cuadrada de {objetivo} es {respuesta} m")


def busqueda_binaria(objetivo):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta ** 2 - objetivo) >= epsilon:
        if respuesta ** 2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2

    print(f"La raiz cuadrada del {objetivo} es {respuesta}")


def enumeracion(objetivo):
    respuesta = 0

    while respuesta ** 2 < objetivo:
        respuesta += 1

    if respuesta ** 2 == objetivo:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")
    else:
        print(f"{objetivo} no tiene una raiz cuadrada exacta.")


if __name__ == "__main__": 
    objetivo = int(input("¿A qué número le quieres sacar raiz?: "))
    while True:    
        metodo = input("""
        Eliga el método por el cual quiere sacar la raiz:

            [a] Aproximacion. 
            [b] Busqueda Binaria 
            [e] Enumeracion
            [s] Salir
            
            """) 

    
        if metodo == 'a':
            aproximacion(objetivo)
         
        elif metodo == 'b':
            busqueda_binaria(objetivo)
            
        elif metodo == 'e':
            enumeracion(objetivo)
            
        elif metodo == 's':
            break    
        else:
            print("Argumento no válido.")
            
