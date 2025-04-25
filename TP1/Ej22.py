def usar_la_fuerza(mochila, objetos_sacados=0):
    # Caso base 1: mochila vacía
    if not mochila:
        print("No se encontró ningún sable de luz.")
        return False, objetos_sacados

    # Sacamos el primer objeto
    objeto = mochila[0]
    objetos_sacados += 1

    # Caso base 2: encontramos el sable
    if objeto == "sable de luz":
        print("¡Se encontró el sable de luz!")
        return True, objetos_sacados

    # Llamada recursiva con el resto de la mochila
    return usar_la_fuerza(mochila[1:], objetos_sacados)
