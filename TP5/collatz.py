def collatz_info(numero):
    """
    Calcula la secuencia de Collatz para un número dado y devuelve
    la cantidad de iteraciones y la lista de números intermedios.
    
    Parámetros:
        numero (int): Número entero positivo.

    Retorna:
        tuple: (iteraciones, secuencia)
    """
    # --- Validación del número ---
    if not isinstance(numero, int):
        raise TypeError("El número debe ser un entero.")
    if numero <= 0:
        raise ValueError("El número debe ser mayor que cero.")
    
    # --- Aplicación del algoritmo de Collatz ---
    secuencia = [numero]
    while numero != 1:
        if numero % 2 == 0:
            numero //= 2
        else:
            numero = 3 * numero + 1
        secuencia.append(numero)
    
    # --- Resultado ---
    iteraciones = len(secuencia) - 1
    return iteraciones, secuencia


# Ejemplo de uso:
if __name__ == "__main__":
    try:
        n = int(input("Ingresá un número entero positivo: "))
        iteraciones, secuencia = collatz_info(n)
        print(f"\n🔹 Secuencia generada: {secuencia}")
        print(f"🔹 Cantidad de iteraciones: {iteraciones}")
    except (ValueError, TypeError) as e:
        print(f"⚠️ Error: {e}")
