import auth
import operaciones


def mostrar_menu():
    print("\n1. Consultar saldo")
    print("\n2. Depositar dinero")
    print("\n3. Retirar dinero")
    print("\n4. Salir")


def pedir_monto(mensaje):
    """Pide un monto. Si no es un número, retorna 0.0,
    que las operaciones rechazan como 'Monto inválido'."""
    try:
        return float(input(mensaje))
    except ValueError:
        return 0.0


def main():
    saldo = 1000.0
    pin_correcto = "1234"

    print("CAJERO AUTOMÁTICO")

    if not auth.verificar_pin(pin_correcto):
        print("Tarjeta bloqueada por seguridad.")
        return

    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                operaciones.consultar_saldo(saldo)
            case "2":
                monto = pedir_monto("Ingrese monto a depositar: ")
                saldo = operaciones.depositar(saldo, monto)
            case "3":
                monto = pedir_monto("Ingrese monto a retirar: ")
                saldo = operaciones.retirar(saldo, monto)
            case "4":
                print("Gracias por usar el cajero.")
                break
            case _:
                print("Opción inválida.")


if __name__ == "__main__":
    main()