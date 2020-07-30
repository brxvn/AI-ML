def div_elements_in_list(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(10))
divisor = 0

print(div_elements_in_list(lista, divisor))