import random

def usar_la_fuerza(mochila, objetos_sacados=0):
   
    if not mochila:
        print("\n No se encontró ningún sable de luz en la mochila...")
        return False, objetos_sacados

    # Preguntamos si quiere sacar un objeto
    decision = input("\n¿Querés usar la Fuerza para sacar el siguiente objeto? (s/n): ").lower()
    if decision != 's':
        print("\n Decidió no sacar más objetos")
        return False, objetos_sacados

    objeto = mochila[0]
    objetos_sacados += 1
    print(f"Sacaste un '{objeto}'.")

    if objeto == "sable de luz":
        print("\n¡Se encontró el sable de luz!")
        return True, objetos_sacados

    return usar_la_fuerza(mochila[1:], objetos_sacados)


def main():
    
    objetos_posibles = ["comida", "mate", "lupa", "manto", "sable de luz"]
    mochila = random.choices(objetos_posibles, k=10) 

    print("Tu mochila contiene varios objetos misteriosos...")
    print("Usá la Fuerza sabiamente para encontrar el sable de luz.\n")

    encontrado, objetos_sacados = usar_la_fuerza(mochila)

    print(f"\n Objetos sacados: {objetos_sacados}")
    if encontrado:
        print("Misión cumplida: sable de luz en mano.")
    else:
        print("Misión fallida: no encontramos el sable.")

if __name__ == "__main__":
    main()