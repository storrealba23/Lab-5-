def calcular_promedio(lista_notas):
    if not lista_notas:
        raise ValueError("La lista de notas no puede estar vacía")
    return sum(lista_notas) / len(lista_notas)


def encontrar_maximo(lista_notas):
    if not lista_notas:
        raise ValueError("La lista de notas no puede estar vacía")
    return max(lista_notas)