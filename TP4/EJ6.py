#6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
#casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias
#para poder realizar las siguientes actividades:


from list_ import List_
from Superheroes_data2 import superheroes

# Inicialización de la lista de superhéroes
heroes_list = List_()
for heroe in superheroes:
    heroes_list.append(heroe)

# Criterio que usaremos en varias operaciones
def get_nombre(personaje):
    return personaje["nombre"]

heroes_list.add_criterion("nombre", get_nombre)

#a. eliminar el nodo que contiene la información de Linterna Verde;
eliminado = heroes_list.delete_value("Linterna Verde", "nombre")
if eliminado:
    print(f"Se eliminó a {eliminado['nombre']} de la lista.")
else:
    print("Linterna Verde no se encontraba en la lista.")

#b. mostrar el año de aparición de Wolverine;
indice_wolverine = heroes_list.search("Wolverine", "nombre")
if indice_wolverine is not None:
    año = heroes_list[indice_wolverine]["año_aparicion"]
    print(f"Wolverine apareció por primera vez en el año: {año}")
else:
    print("Wolverine no está en la lista.")

#c. cambiar la casa de Dr. Strange a Marvel;
indice_strange = heroes_list.search("Dr. Strange", "nombre")
if indice_strange is not None:
    heroes_list[indice_strange]["casa_comic"] = "Marvel"
    print(f"La casa de Dr. Strange ha sido actualizada a: {heroes_list[indice_strange]['casa_comic']}")
else:
    print("Dr. Strange no está en la lista.")
    
#d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
#“traje” o “armadura”;
for heroe in heroes_list:
    biografia = heroe["biografia"].lower()
    if "traje" in biografia or "armadura" in biografia:
        print(heroe["nombre"])

#e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
#sea anterior a 1963;
for heroe in heroes_list:
    if heroe["año_aparicion"] < 1963:
        print(f"{heroe['nombre']} - Casa: {heroe['casa_comic']}")

#f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
for nombre_heroe in ["Capitana Marvel", "Mujer Maravilla"]:
    indice = heroes_list.search(nombre_heroe, "nombre")
    if indice is not None:
        casa = heroes_list[indice]["casa_comic"]
        print(f"{nombre_heroe} pertenece a la casa: {casa}")
    else:
        print(f"{nombre_heroe} no se encuentra en la lista.")

#punto g. mostrar toda la información de Flash y Star-Lord
for nombre_heroe in ["Flash", "Star-Lord"]:
    indice = heroes_list.search(nombre_heroe, "nombre")
    if indice is not None:
        print(f"Información de {nombre_heroe}:")
        info_completa = heroes_list[indice]
        for clave, valor in info_completa.items():
            print(f"  - {clave.capitalize().replace('_', ' ')}: {valor}")
    else:
        print(f"{nombre_heroe} no se encuentra en la lista.")

#h. listar los superhéroes que comienzan con la letra B, M y S
for heroe in heroes_list:
    if heroe["nombre"].startswith(("B", "M", "S")):
        print(heroe["nombre"])

# i. determinar cuántos superhéroes hay de cada casa de comic.
conteo_casas = {}
for heroe in heroes_list:
    casa = heroe["casa_comic"]
    conteo_casas[casa] = conteo_casas.get(casa, 0) + 1

for casa, cantidad in conteo_casas.items():
    print(f"Casa {casa}: {cantidad} superhéroe(s)")