def romano_a_decimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}

    if len(romano) == 1:
        return valores[romano]

    actual = valores[romano[0]]
    siguiente = valores[romano[1]]

    if actual < siguiente:
        return siguiente - actual + romano_a_decimal(romano[2:])
    else:
        return actual + romano_a_decimal(romano[1:])


def main():
    numero_romano = input("Ingresá un número romano (en mayúsculas): ")
    try:
        decimal = romano_a_decimal(numero_romano)
        print(f"El número romano {numero_romano} equivale a {decimal} en decimal.")
    except KeyError:
        print("Error: ingresaste un carácter que no es romano.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()