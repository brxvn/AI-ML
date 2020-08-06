import random

def busqueda_binaria(lista, start, end, objetivo):
    print(f"Buscando: {objetivo} entre {lista[start]} y {lista[end - 1]}")
    if start > end:
        return False
    
    medio = (start + end) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, end, objetivo)
    else:
        return busqueda_binaria(lista, start, medio - 1, objetivo)


if __name__ == "__main__":
    tamano_lista = int(input("De que tamaño será la lista?: "))
    objetivo = int(input("Qué número quieres encontrar?: "))
    
    lista = sorted([random.randint(0,100) for i in range(tamano_lista)])
    
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f"El elemento {objetivo} {'está' if encontrado else 'no está'} en la lista")