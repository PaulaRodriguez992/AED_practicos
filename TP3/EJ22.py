from collections import deque

#Cola con personajes
cola_personajes = deque([
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
    {"personaje": "Shuri", "superheroe": "Shuri", "genero": "F"},
])

# a) Determinar el nombre del personaje de la superhéroe Capitana Marvel
def obtener_personaje_por_superheroe(cola, nombre_superheroe):
    for item in cola:
        if item["superheroe"] == nombre_superheroe:
            return item["personaje"]
    return "No encontrado"

# b) Mostrar los nombres de los superhéroes femeninos
def mostrar_superheroes_femeninos(cola):
    for item in cola:
        if item["genero"] == "F":
            print(item["superheroe"])

# c) Mostrar los nombres de los personajes masculinos
def mostrar_personajes_masculinos(cola):
    for item in cola:
        if item["genero"] == "M":
            print(item["personaje"])

# d) Determinar el nombre del superhéroe del personaje Scott Lang
def obtener_superheroe_por_personaje(cola, nombre_personaje):
    for item in cola:
        if item["personaje"] == nombre_personaje:
            return item["superheroe"]
    return "No encontrado"

# e) Mostrar todos los datos de superhéroes o personajes que empiezan con S
def mostrar_datos_con_S(cola):
    for item in cola:
        if item["personaje"].startswith("S") or item["superheroe"].startswith("S"):
            print(item)

# f) Determinar si Carol Danvers está en la cola e indicar su superhéroe
def verificar_carol_danvers(cola):
    for item in cola:
        if item["personaje"] == "Carol Danvers":
            return (f"Sí, su superhéroe es {item['superheroe']}.")
    return "No, Carol Danvers no está en la cola."

print("a. Personaje de Capitana Marvel:")
print(obtener_personaje_por_superheroe(cola_personajes, "Capitana Marvel"))

print("\nb. Superhéroes femeninos:")
mostrar_superheroes_femeninos(cola_personajes)

print("\nc. Personajes masculinos:")
mostrar_personajes_masculinos(cola_personajes)

print("\nd. Superhéroe de Scott Lang:")
print(obtener_superheroe_por_personaje(cola_personajes, "Scott Lang"))

print("\ne. Datos de personajes o superhéroes que comienzan con 'S':")
mostrar_datos_con_S(cola_personajes)

print("\nf. ¿Está Carol Danvers?")
print(verificar_carol_danvers(cola_personajes))
