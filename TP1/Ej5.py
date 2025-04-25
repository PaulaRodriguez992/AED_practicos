
# #def romano_a_decimal(romano):
#     valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
#                'C': 100, 'D': 500, 'M': 1000}

#     # Caso base: si hay un solo carácter
#     if len(romano) == 1:
#         return valores[romano]

#     # Tomamos los dos primeros caracteres
#     actual = valores[romano[0]]
#     siguiente = valores[romano[1]]

#     # Si el actual es menor que el siguiente, se resta
#     if actual < siguiente:
#         return siguiente - actual + romano_a_decimal(romano[2:])
#     else:
#         # return actual + romano_a_decimal(romano[1:])


def romano_a_decimal(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    if romano == "":
        return 0

    if len(romano) == 1:
        return valores[romano]

    if valores[romano[0]] < valores[romano[1]]:
        return valores[romano[1]] - valores[romano[0]] + romano_a_decimal(romano[2:])
    else:
        return valores[romano[0]] + romano_a_decimal(romano[1:])

# Interfaz de usuario minimalista pero con estilo
def main():
    print("🟡 Conversor de Números Romanos a Decimales")
    romano = input("👉 Ingresá un número romano (en mayúsculas): ").strip().upper()
    
    try:
        resultado = romano_a_decimal(romano)
        print(f"✅ El número decimal equivalente es: {resultado}")
    except KeyError:
        print("❌ Error: Ingresaste un carácter que no es un número romano válido.")
    except Exception as e:
        print(f"⚠️ Ocurrió un error inesperado: {e}")

# Punto de entrada del script
if __name__ == "__main__":
    main()

