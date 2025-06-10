#Ejercicio 1: Dado una lista simple de python (array) de 15
# superheroes realizar dos funciones recursivas:
# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# funcion recursiva para listar los superheroes de la lista.
from list_ import list_
from typing import List as TypeList

heroes = [
    "Iron Man", "Spider-Man", "Black Widow", "Hulk", "Thor", "Ant-Man",
    "Doctor Strange", "Black Panther", "Captain Marvel", "Hawkeye",
    "Vision", "Scarlet Witch", "Falcon", "Winter Soldier", "Captain America"
]

#1a. Buscar si Capitán América está en la lista 
#ordenar la lista
heroes.sort()

#búsqueda binaria
def busqueda_binaria_rec(lista, buscado, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        return False  # no encontrado

    medio = (inicio + fin) // 2
    if lista[medio].lower() == buscado.lower():
        return True
    elif buscado.lower() < lista[medio].lower():
        return busqueda_binaria_rec(lista, buscado, inicio, medio - 1)
    else:
        return busqueda_binaria_rec(lista, buscado, medio + 1, fin)


#1b. Listar los Superhéroes
def listar_(lista, indice=0):
    if indice < len(lista):
        print(lista[indice])
        listar_(lista, indice + 1)

print("\nListado de todos los Superhéroes")
listar_(heroes)
print("\n¿Está Captain America en la lista?")
encontrado = busqueda_binaria_rec(heroes, "Captain America")
print("Sí" if encontrado else "No")

