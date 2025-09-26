from list_ import list_
from super_heroes_data import superheroes

# a)Listado ordenado de manera ascendente por nombre de los personajes.
def abc_nombre(personaje):
    return personaje["name"]

heroes_list = list_()
for hero in superheroes:
    heroes_list.append(hero)

heroes_list.add_criterion("name", abc_nombre)
heroes_list.sort_by_criterion("name")
print("Listado ordenado por nombre:")
heroes_list.show()


# b) Determinar en que posicion esta The Thing y Rocket Raccoon.
pos_thething = heroes_list.search("The Thing", "name")
pos_rocket = heroes_list.search("Rocket Raccoon", "name")

print(f"\nThe Thing está en la posición: {pos_thething}")
print(f"Rocket Raccoon está en la posición: {pos_rocket}")

# c) Listar villanos
print("\nVillanos:")
for hero in heroes_list:
    if hero["is_villain"]: 
        print(hero["name"])

# d) Poner villanos en una cola y filtrar por año
from queue_ import Queue

def villanos_antes_de_1980(lista):
    villanos_queue = Queue()
    
    for hero in lista:
        if hero["is_villain"]:
            villanos_queue.arrive(hero)
    
    print("\nVillanos que aparecieron antes de 1980:")
    for _ in range(villanos_queue.size()):
        villano = villanos_queue.attention()
        if int(villano["first_appearance"]) < 1980:
            print(villano["name"])
        villanos_queue.arrive(villano) # se vuelve a poner al final para mantener la cola

villanos_antes_de_1980(heroes_list)

#e) Listar héroes que empiezan con Bl, G, My, W
def listar_heroes_por_letras(lista, letras=("Bl", "G", "My", "W")):
    print(f"\nHéroes que empiezan con {', '.join(letras)}:")
    for hero in lista:
        nombre = hero["name"]
        if nombre.startswith(letras):
            print(nombre)

listar_heroes_por_letras(heroes_list)

#f) Ordenar por nombre real ascendente
def abc_nombre_real(personaje):
    return personaje["real_name"]   

heroes_list.add_criterion("real_name", abc_nombre_real)
heroes_list.sort_by_criterion("real_name")
print("\nListado ordenado por nombre real:")
heroes_list.show()


# g) Ordenar por fecha de aparición 
def orden_fecha_aparicion(personaje):
    return int(personaje["first_appearance"])

heroes_list.add_criterion("first_appearance", orden_fecha_aparicion)
heroes_list.sort_by_criterion("first_appearance")
print("\n Listado ordenado por fecha de aparición:")
heroes_list.show()


#h) Modificar nombre real de Ant-Man a Scott Lang
def modificar_nombre_antman(lista):
    indice = lista.search("Ant-Man", "name")
    if indice is not None:
        lista[indice]["real_name"] = "Scott Lang"
        print("\nNombre real de Ant-Man modificado a Scott Lang.")
    else:
        print("\nAnt-Man no está en la lista.")

modificar_nombre_antman(heroes_list)

#i) Buscar los que tengan "time-traveling" o "suit" en la bio
def mostrar_personajes_con_bio_especifica(lista):
    print("\nPersonajes con 'time-traveling' o 'suit' en la biografía:")
    for hero in lista:
        bio = hero["short_bio"].lower()
        if "time-traveling" in bio or "suit" in bio:
            print(f"{hero['name']}")

mostrar_personajes_con_bio_especifica(heroes_list)

#j) Eliminar Electro y Baron Zemo de la lista

def eliminar_electro_y_zemo(lista):
    electro = lista.delete_value("Electro", "name")
    baron = lista.delete_value("Baron Zemo", "name")

    if electro:
        print("\nElectro eliminado:")
        print(electro)
    else:
        print("\nElectro no estaba en la lista.")

    if baron:
        print("\nBaron Zemo eliminado:")
        print(baron)
    else:
        print("\nBaron Zemo no estaba en la lista.")

eliminar_electro_y_zemo(heroes_list)



 


