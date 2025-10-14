#Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe
#(MCU), desarrollar un algoritmo que contemple lo siguiente:
#a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
#que indica si es un héroe o un villano, True y False respectivamente;
#b. listar los villanos ordenados alfabéticamente;
#c. mostrar todos los superhéroes que empiezan con C;
#d. determinar cuántos superhéroes hay el árbol;
#e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#encontrarlo en el árbol y modificar su nombre;
#f. listar los superhéroes ordenados de manera descendente;
#g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
#los villanos, luego resolver las siguiente tareas:
#I. determinar cuántos nodos tiene cada árbol;
#II. realizar un barrido ordenado alfabéticamente de cada árbol.

from tree import BinaryTree
from super_heroes_data import superheroes
# Creación y carga del árbol principal
superheroes_tree = BinaryTree()

# Iteramos sobre la lista de personajes y los insertamos en el árbol.
# 'name' se usa como clave de ordenación (value).
# El diccionario completo se guarda como 'other_values'.
for character in superheroes:
    superheroes_tree.insert(character['name'], character)

print("Árbol de superhéroes cargado con éxito.")
print("-" * 40) 
# a. Además del nombre del superhéroe, en cada nodo del árbol se almacena un campo booleano y otros datos mas que ya vienen en el diccionario

# b. Listar los villanos ordenados alfabéticamente.
print("b. Villanos ordenados alfabéticamente:")
# Usamos el método 'villain_in_order' 
# in-order en un Árbol Binario de Búsqueda SIEMPRE devuelve los elementos ordenados.
superheroes_tree.villain_in_order()
print("-" * 40)


# c. Mostrar todos los superhéroes que empiezan con C.
print("c. Superhéroes cuyo nombre empieza con 'C':")
# metodo agregado, este hace un recorrido in-order y aplica un filtro.
superheroes_tree.in_order_starts_with_c()
print("-" * 40)


# d. Determinar cuántos superhéroes hay en el árbol.
# Usamos el método 'count_heroes' 
count = superheroes_tree.count_heroes()
print(f"d. Número total de superhéroes en el árbol: {count}")
print("-" * 40)


# e. Corregir el nombre de Doctor Strange.
print("e. Corrigiendo el nombre de 'Doctor Strange'...")
# buscamos y eliminamos el nodo con el nombre incorrecto.
value, other_values = superheroes_tree.delete('Doctor Strange')

# si se encontró y eliminó correctamente, corregimos y reinsertamos.
if value is not None:
    # modificamos el nombre en los datos recuperados.
    new_name = 'Dr. Strange'
    other_values['name'] = new_name
    # reinsertamos el personaje con el nombre corregido.
    superheroes_tree.insert(new_name, other_values)
    print(f"   '{value}' ha sido actualizado a '{new_name}'.")
else:
    print("   'Doctor Strange' no se encontró en el árbol.")

# Verificamos que ahora aparece con el nuevo nombre.
print("   Búsqueda por proximidad de 'Dr.':")
superheroes_tree.proximity_search('Dr.')
print("-" * 40)


# f. Listar los superhéroes ordenados de manera descendente.
print("f. Superhéroes en orden descendente:")
# Llamamos al nuevo método que creamos. Este realiza un recorrido in-order inverso
# (derecha -> raíz -> izquierda) para obtener el orden descendente.
superheroes_tree.in_order_desc()
print("-" * 40)


# g. Generar un bosque (dos árboles: uno de héroes y otro de villanos).
heroes_tree = BinaryTree()
villains_tree = BinaryTree()

# Usamos el método 'divide_tree' que creamos
# Recorre el árbol original y va insertando cada nodo en el árbol correspondiente.
superheroes_tree.divide_tree(heroes_tree, villains_tree)
print("   ¡Bosque generado!")
print()

# I. Determinar cuántos nodos tiene cada árbol.
print("Conteo de nodos en cada árbol del bosque:")
# Usamos el método genérico 'count_nodes'
print(f"Nodos en el árbol de héroes: {heroes_tree.count_nodes()}")
print(f"Nodos en el árbol de villanos: {villains_tree.count_nodes()}")
print()

# II. Realizar un barrido ordenado alfabéticamente de cada árbol.
print("Listado alfabético de cada árbol:")

print("   --- HÉROES ---")
# El barrido ordenado es un recorrido in-order.
heroes_tree.in_order()
print()

print("   --- VILLANOS ---")
villains_tree.in_order()
print("-" * 40)