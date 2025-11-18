import os
from tree_ import BinaryTree 
from queue_ import Queue_

#Definición de la estructura de datos
pokemon_data = [
    {"nombre": "Bulbasaur", "numero": 1, "tipo": ["Planta", "Veneno"], "debilidad": ["Fuego", "Hielo", "Volador", "Psíquico"], "mega": False, "gigamax": True},
    {"nombre": "Charmander", "numero": 4, "tipo": ["Fuego"], "debilidad": ["Agua", "Tierra", "Roca"], "mega": False, "gigamax": True},
    {"nombre": "Charizard", "numero": 6, "tipo": ["Fuego", "Volador"], "debilidad": ["Agua", "Eléctrico", "Roca"], "mega": True, "gigamax": True},
    {"nombre": "Squirtle", "numero": 7, "tipo": ["Agua"], "debilidad": ["Planta", "Eléctrico"], "mega": False, "gigamax": True},
    {"nombre": "Pikachu", "numero": 25, "tipo": ["Eléctrico"], "debilidad": ["Tierra"], "mega": False, "gigamax": True},
    {"nombre": "Jolteon", "numero": 135, "tipo": ["Eléctrico"], "debilidad": ["Tierra"], "mega": False, "gigamax": False},
    {"nombre": "Gengar", "numero": 94, "tipo": ["Fantasma", "Veneno"], "debilidad": ["Fantasma", "Siniestro", "Tierra", "Psíquico"], "mega": True, "gigamax": True},
    {"nombre": "Scyther", "numero": 123, "tipo": ["Bicho", "Volador"], "debilidad": ["Fuego", "Volador", "Eléctrico", "Hielo", "Roca"], "mega": False, "gigamax": False},
    {"nombre": "Magikarp", "numero": 129, "tipo": ["Agua"], "debilidad": ["Planta", "Eléctrico"], "mega": False, "gigamax": False},
    {"nombre": "Gyarados", "numero": 130, "tipo": ["Agua", "Volador"], "debilidad": ["Eléctrico", "Roca"], "mega": True, "gigamax": False},
    {"nombre": "Steelix", "numero": 208, "tipo": ["Acero", "Tierra"], "debilidad": ["Fuego", "Agua", "Lucha", "Tierra"], "mega": True, "gigamax": False},
    {"nombre": "Lycanroc", "numero": 745, "tipo": ["Roca"], "debilidad": ["Agua", "Planta", "Lucha", "Tierra", "Acero"], "mega": False, "gigamax": False},
    {"nombre": "Mimikyu", "numero": 778, "tipo": ["Fantasma", "Hada"], "debilidad": ["Fantasma", "Acero"], "mega": False, "gigamax": False},
    {"nombre": "Tyrantrum", "numero": 697, "tipo": ["Roca", "Dragón"], "debilidad": ["Hielo", "Lucha", "Tierra", "Dragón", "Acero", "Hada"], "mega": False, "gigamax": False},
    {"nombre": "Corviknight", "numero": 823, "tipo": ["Volador", "Acero"], "debilidad": ["Fuego", "Eléctrico"], "mega": False, "gigamax": True},
]

#Creación de los tres árboles
tree_nombre = BinaryTree()
tree_numero = BinaryTree()
tree_tipo = BinaryTree()

#Llenado de los árboles
print("Cargando datos en los árboles...")
for pokemon in pokemon_data:
    tree_nombre.insert(pokemon["nombre"], pokemon)
    tree_numero.insert(pokemon["numero"], pokemon)
    for tipo in pokemon["tipo"]:
        tree_tipo.insert(tipo, pokemon)

print("¡Ároboles cargados con éxito!")
os.system('pause') 
print("\n" + "="*40 + "\n")


#Mostrar datos por número y nombre (Búsquedas)
print("--- Búsqueda por Número (Exacta) ---")
numero_buscado = 25
print(f"Buscando Pokémon número {numero_buscado}...")
node = tree_numero.search(numero_buscado) # Usa el .search() genérico
if node:
    print(f"Encontrado: {node.other_values}")
else:
    print(f"Pokémon número {numero_buscado} no encontrado.")

print("\nBúsqueda por Nombre (Proximidad)")
nombre_buscado = "Char"
print(f"Buscando Pokémon que contengan '{nombre_buscado}'...")
# ¡Usa el método proximity_search modificado!
tree_nombre.proximity_search(nombre_buscado)

os.system('pause')
print("\n" + "="*40 + "\n")


# Mostrar Pokémon por tipo
print("Listado por Tipo")
tipos_a_buscar = ["Fantasma", "Fuego", "Acero", "Eléctrico"]
# ¡Usa el NUEVO método!
tree_tipo.in_order_pokemon_by_tipo(tipos_a_buscar)

os.system('pause')
print("\n" + "="*40 + "\n")


# Listados (Recorridos)
print("Listado en orden ascendente por NÚMERO")
# Usa el 'in_order'
tree_numero.in_order()

print("\nListado en orden ascendente por NOMBRE")
# Usa el 'in_order'
tree_nombre.in_order()

print("\nListado por NIVEL por NOMBRE")
# Usa el 'by_level'
tree_nombre.by_level()

os.system('pause')
print("\n" + "="*40 + "\n")


#Pokémon débiles frente a..
print("Pokémon débiles frente a..")

print("\nDébiles a Eléctrico (Jolteon)")

tree_nombre.in_order_weakness("Eléctrico")

print("\nDébiles a Roca (Lycanroc/Tyrantrum)")

tree_nombre.in_order_weakness("Roca")

print("\nDébiles a Dragón (Tyrantrum)")

tree_nombre.in_order_weakness("Dragón")

os.system('pause')
print("\n" + "="*40 + "\n")


# Conteo de tipos
print("Conteo de todos los tipos")
tipos_dict = {} # Usamos un diccionario externo

tree_nombre.count_types(tipos_dict)
print(tipos_dict)

os.system('pause')
print("\n" + "="*40 + "\n")


#Conteo de Megaevoluciones
print("Conteo de Megaevoluciones")
total_mega = tree_nombre.count_megas()
print(f"Total de Pokémon con megaevolución: {total_mega}")


print("\n" + "="*40 + "\n")


# Conteo de Gigamax
print("Conteo de Gigamax")
total_gigamax = tree_nombre.count_gigamax()
print(f"Total de Pokémon con forma gigamax: {total_gigamax}")
