# Importamos nuestra clase BinaryTree desde el archivo tree.py
from tree import BinaryTree

# Carga del Árbol
from criaturas_data import criaturas_data as creatures_data

# Creamos la instancia del árbol
creature_tree = BinaryTree()

# Cargamos los datos en el árbol
for creature in creatures_data:
    # Agregamos los campos 'descripcion' y 'capturada' a cada registro antes de insertarlo.
    creature_info = {
        "derrotado_por": creature["derrotado_por"],
        "descripcion": None,  # Campo listo para ser llenado (punto b)
        "capturada": None     # Campo listo para ser llenado (punto g)
    }
    creature_tree.insert(creature["nombre"], creature_info)

print("Árbol de criaturas mitológicas cargado.")
print("-" * 90)


#a. Listado inorden de las criaturas y quienes la derrotaron
print("a. Listado inorden de criaturas y quienes la derrotaron:")
creature_tree.in_order_defeats()#metodo creado en tree.py
print("-" * 50)


#b. Cargar una breve descripción de cada criatura
print("b. Agregando descripción a la Hidra de Lerna...")
# El patrón para modificar es: buscar/eliminar, cambiar los datos y reinsertar.
value, other_values = creature_tree.delete("Hidra de Lerna")
if value:
    other_values["descripcion"] = "Una serpiente acuática con múltiples cabezas que se regeneraban."
    creature_tree.insert(value, other_values)
    print("   Descripción agregada con éxito.")
print("-" * 50)


#c. Mostrar toda la información de la criatura Talos
print("c. Información completa de Talos:")
# Usamos el método de búsqueda para encontrar el nodo.
talos_node = creature_tree.search("Talos")
if talos_node:
    print(f"   Nombre: {talos_node.value}")
    print(f"   Datos adicionales: {talos_node.other_values}")
else:
    print("   Talos no encontrado.")
print("-" * 50)


#d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
print("d. Los 3 héroes/dioses más victoriosos son:")
ranking = creature_tree.generate_ranking_defeats()
# ordenamos el ranking por el número de victorias (el valor del diccionario) en orden descendente.
sorted_ranking = sorted(ranking.items(), key=lambda item: item[1], reverse=True)
#mostramos los 3 primeros.
for i in range(min(3, len(sorted_ranking))):
    hero, count = sorted_ranking[i]
    print(f"   {i+1}. {hero} - {count} criaturas derrotadas")
print("-" * 50)


#e. Listar las criaturas derrotadas por Heracles
print("e. Criaturas derrotadas por Heracles:")
creature_tree.in_order_defeated_by("Heracles") #metodo creado en tree.py
print("-" * 50)


#f. Listar las criaturas que no han sido derrotadas
print("f. Criaturas que no fueron derrotadas:")
creature_tree.in_order_not_defeated() #metodo creado en tree.py
print("-" * 50)


#g. El campo "capturada" ya fue agregado al cargar los datos.


#h. Modificar nodos para indicar capturas de Heracles
print("h. Marcando criaturas como capturadas por Heracles...")
creatures_to_capture = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
for creature_name in creatures_to_capture:
    # Reutilizamos el patrón de eliminar-modificar-reinsertar.
    value, other_values = creature_tree.delete(creature_name)
    if value:
        other_values["capturada"] = "Heracles"
        creature_tree.insert(value, other_values)
        print(f"   - {value} ha sido marcada como capturada.")
print("-" * 50)


#i. Permitir búsquedas por coincidencia
print("i. Búsqueda por coincidencia de criaturas que empiezan con 'C':")
# búsqueda por proximidad.
creature_tree.proximity_search("C")
print("-" * 50)


#j. Eliminar al Basilisco y a las Sirenas
print("j. Eliminando a Basilisco y Sirenas...")
creature_tree.delete("Basilisco")
print("   - Basilisco eliminado.")
creature_tree.delete("Sirenas")
print("   - Sirenas eliminadas.")
#print("-" * 50)


#k. Modificar Aves del Estínfalo
print("k. Modificando a las Aves del Estínfalo...")
value, other_values = creature_tree.delete("Aves del Estínfalo")
if value:
    other_values["derrotado_por"] = "Heracles"
    other_values["descripcion"] = "Aves con plumas de bronce que lanzaban como proyectiles."
    creature_tree.insert(value, other_values)
    print("   Nodo de Aves del Estínfalo actualizado.")
print("-" * 50)


# l. Modificar el nombre de la criatura Ladón por Dragón Ladón
print("l. Renombrando a Ladón...")
# como el nombre es la clave del árbol, es obligatorio eliminar y reinsertar.
value, other_values = creature_tree.delete("Ladón")
if value:
    new_name = "Dragón Ladón"
    creature_tree.insert(new_name, other_values)
    print(f"   '{value}' ha sido renombrado a '{new_name}'.")
print("-" * 50)


#m. Realizar un listado por nivel del árbol
print("m. Listado del árbol por nivel:")
# usa una cola para funcionar.
creature_tree.by_level()
print("-" * 50)


#n. Muestre las criaturas capturadas por Heracles
print("n. Criaturas capturadas por Heracles:")
creature_tree.in_order_captured_by("Heracles")
print("-" * 50)