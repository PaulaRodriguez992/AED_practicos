# main.py

from list_ import List_
from jedis_data import jedis

# Inicialización de la lista de Jedi
jedi_list = List_()
for jedi in jedis:
    jedi_list.append(jedi)

# Definición de Criterios
def get_nombre(jedi):
    return jedi["nombre"]

def get_especie(jedi):
    return jedi["especie"]

jedi_list.add_criterion("nombre", get_nombre)
jedi_list.add_criterion("especie", get_especie)

# punto a listado ordenado por nombre y especie

print("Ordenado por nombre:")
jedi_list.sort_by_criterion("nombre")
jedi_list.show()

print("\nOrdenado por especie:")
jedi_list.sort_by_criterion("especie")
jedi_list.show()

# punto b. Informacion de Ahsoka Tano y Kit Fisto

def mostrar_info_completa(nombre_jedi):
    indice = jedi_list.search(nombre_jedi, "nombre")
    if indice is not None:
        print(f"Información completa de {nombre_jedi}:")
        info = jedi_list[indice]
        for clave, valor in info.items():
            # Unimos los elementos de las listas para una mejor visualización
            if isinstance(valor, list):
                valor_str = ", ".join(valor) if valor else "Ninguno"
                print(f"  - {clave.capitalize().replace('_', ' ')}: {valor_str}")
            else:
                print(f"  - {clave.capitalize().replace('_', ' ')}: {valor}")
    else:
        print(f"{nombre_jedi} no se encuentra en la lista.")

mostrar_info_completa("Ahsoka Tano")
print() # Salto de línea
mostrar_info_completa("Kit Fisto")

#Punto c. Padawans de Yoda y Luke Skywalker

def mostrar_padawans_de(maestro):
    padawans = []
    for jedi in jedi_list:
        if maestro in jedi["maestros"]:
            padawans.append(jedi["nombre"])
    
    print(f"Padawans de {maestro}:")
    if padawans:
        for padawan in padawans:
            print(f"  - {padawan}")
    else:
        print(f"  - No se encontraron padawans de {maestro} en la lista.")

mostrar_padawans_de("Yoda")
mostrar_padawans_de("Luke Skywalker")

# Punto d. Jedi de especie Humana y Twi'lek 
for jedi in jedi_list:
    if jedi["especie"] in ["Humana", "Twi'lek"]:
        print(f"- {jedi['nombre']} (Especie: {jedi['especie']})")

# Punto e. Jedi que comienzan con la letra A
for jedi in jedi_list:
    if jedi["nombre"].startswith("A"):
        print(f"- {jedi['nombre']}")

#Punto f. Jedi que usaron más de un color de sable de luz
for jedi in jedi_list:
    if len(jedi["colores_sable"]) > 1:
        colores = ", ".join(jedi["colores_sable"])
        print(f"- {jedi['nombre']} (Colores: {colores})")

#punto g. Jedi que utilizaron sable de luz amarillo o violeta 
for jedi in jedi_list:
    # Usamos un conjunto para una verificación eficiente y elegante
    if set(jedi["colores_sable"]) & {"amarillo", "violeta"}:
        print(f"- {jedi['nombre']}")
        
#punto h. Padawans de Qui-Gon Jinn y Mace Windu
# Reutilizamos la función que creamos en el punto c
mostrar_padawans_de("Qui-Gon Jinn")
mostrar_padawans_de("Mace Windu")