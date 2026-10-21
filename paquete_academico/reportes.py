from . import operaciones


def generar_resumen(lista_notas):
    promedio = operaciones.calcular_promedio(lista_notas)
    maximo = operaciones.encontrar_maximo(lista_notas)

    print("=== Reporte de notas ===")
    print(f"Promedio: {promedio:.2f}")
    print(f"Nota máxima: {maximo}")