"""
EJERCICIO 03: Día del año.

1. Haga una función que dado un mes (en número), retorne la cantidad de días que tiene el mes (considere febrero con 28 días)
2. Haga otra función que dado un mes y el día actual del mes (ambos en número), calcule la cantidad de días que van del año
3. Pídale al usuario que ingrese el mes actual (en número). Debe validar el dato ingresado.
4. Pídale al usuario que ingrese el día actual (en número). Debe validar el dato ingresado y debe tener coherencia con el mes
   indicado en el paso anterior. Por ejemplo, abril no puede tener 31 días.
5. Calcule el día presente del año según los datos ingresados por el usuario, utilizando las funciones que acaba de implementar
6. Muestre en pantalla el resultado

"""
def dias_en_mes(mes):
    if (1, 3, 5, 7, 8, 10, 12).__contains__(mes):
        return 31
    elif mes == 2:
        return 28
    else:
        return 30
    raise ValueError("Mes inválido. Debe estar entre 1 y 12.")

def dia_del_ano(mes, dia):
    total = dia
    for m in range(1, mes):
         total += dias_en_mes(m)
    return total

def pedir_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Por favor, ingrese un número entre {minimo} y {maximo}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def main():
    mes = pedir_entero("Ingrese el mes actual (1-12): ", 1, 12)
    dia = pedir_entero(f"Ingrese el día actual del mes {mes} (1-{dias_en_mes(mes)}): ", 1, dias_en_mes(mes))
    
    dia_ano = dia_del_ano(mes, dia)
    print(f"Hoy es el día {dia_ano} del año.")

if __name__ == "__main__":
    assert dia_del_ano(1, 1) == 1
    assert dia_del_ano(3, 15) == 74    # 31 + 28 + 15
    assert dia_del_ano(12, 31) == 365

    main()
    
    