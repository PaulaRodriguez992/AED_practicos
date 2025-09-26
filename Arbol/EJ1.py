# A continuación se plantean una serie de problemas, que se deberán resolver utilizar el TDA árbol
# binario de búsqueda AVL, salvo que el ejercicio pida utilizar otro tipo particular de árbol.

# 1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea-
# toria– que resuelva las siguientes actividades:

# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;

from typing import Any, Optional
from tree  import BinaryTree


# Crear un árbol binario
tree = BinaryTree()

# Insertar 10 números enteros aleatorios
import random
for _ in range(10):
        num = random.randint(1, 10)  # Números entre 1 y 10
        tree.insert(num)

print("=== Recorridos ===")
print("Pre-orden:")
tree.pre_order()

print("\nIn-orden:")
tree.in_order()

print("\nPost-orden:")
tree.post_order()

print("\nPor niveles:")
tree.by_level()

# b. determinar si un número está cargado en el árbol o no;
print("\n=== Búsquedas ===")
nodo = tree.search(500)  # Cambia 500 por el número que quieras buscar
if nodo:
    print(f"Encontrado: {nodo.value}")
else:
    print("No se encontró el 500")

# c. eliminar tres valores del árbol;
values_to_delete = [200, 400, 600]  # Cambia estos valores por los que quieras eliminar
for value in values_to_delete:
    tree.delete(value)
    print(f"Eliminado: {value}")

# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
if tree.root:
    left_height = tree.get_height(tree.root.left)
    right_height = tree.get_height(tree.root.right)
    print(f"\nAltura del subárbol izquierdo: {left_height}")
    print(f"Altura del subárbol derecho: {right_height}")