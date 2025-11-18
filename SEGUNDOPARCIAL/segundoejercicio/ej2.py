import math
from graph import Graph
from typing import Dict, Any

def print_shortest_path(graph: Graph, origin: str, destination: str):
   
    print(f"\n Calculando camino más corto: {origin} -> {destination}")
    
    
    path_stack = graph.dijkstra(origin)
    
    camino_completo = []
    peso_total_camino = None
    destino_actual = destination 

    while path_stack.size() > 0:
        # [vértice, costo_total, vértice_anterior]
        value = path_stack.pop()
        
        if value[0] == destino_actual:
            if peso_total_camino is None:
                peso_total_camino = value[1]
            
            camino_completo.append(value[0])
            destino_actual = value[2] # El vértice anterior

    camino_completo.reverse()

    if peso_total_camino is not None:
        print(f"  Camino: {' -> '.join(camino_completo)}")
        print(f"  Costo total (suma de episodios en el camino): {peso_total_camino}")
    else:
        print(f"  No se encontró un camino de {origin} a {destination}.")


#Cargar el grafo no dirigido con los personajes
print("Cargando Nodos (Vértices)")

g = Graph(is_directed=True)

# Lista de tuplas: (nombre_personaje, aparecio_en_9_episodios)
personajes_data = [
    ("Luke Skywalker", False),
    ("Darth Vader", False),
    ("Yoda", False),
    ("Boba Fett", False),
    ("C-3PO", True),  
    ("Leia", False),
    ("Rey", False),
    ("Kylo Ren", False),
    ("Chewbacca", False),
    ("Han Solo", False),
    ("R2-D2", True),   
    ("BB-8", False)
]

for nombre, en_nueve_episodios in personajes_data:
    # Usamos el 'insert_vertex'
    g.insert_vertex(nombre, {"en_nueve": en_nueve_episodios})
    print(f"Insertado: {nombre}")

print("\n--- Cargando Conexiones (Aristas) ---")
# ¡Estos datos están basados en el canon de las películas I-IX!
# El peso es la cantidad de películas en las que AMBOS personajes aparecen.
aristas_data = [
    # Pares de Luke
    ("Luke Skywalker", "Darth Vader", 4),  
    ("Luke Skywalker", "Leia", 6),         
    ("Luke Skywalker", "Han Solo", 4),     
    ("Luke Skywalker", "Chewbacca", 6),    
    ("Luke Skywalker", "C-3PO", 6),        
    ("Luke Skywalker", "R2-D2", 6),        
    ("Luke Skywalker", "Yoda", 4),         
    # Pares de Vader
    ("Darth Vader", "Boba Fett", 2),       
    ("Darth Vader", "C-3PO", 4),           
    ("Darth Vader", "Yoda", 3),            
    
    # Pares de Han Solo
    ("Han Solo", "Chewbacca", 5),          
    ("Han Solo", "Leia", 5),               
    ("Han Solo", "C-3PO", 5),              
    
    # Pares de Leia
    ("Leia", "C-3PO", 7),                 
    ("Leia", "R2-D2", 7),                 
    
    # Pares de C-3PO
    ("C-3PO", "R2-D2", 9),               
    ("C-3PO", "BB-8", 3),                  

    # Pares de Rey
    ("Rey", "Kylo Ren", 3),                
    ("Rey", "BB-8", 3),                    
    ("Rey", "Han Solo", 2),                
    ("Rey", "Chewbacca", 3),               

    # Pares de Boba Fett
    ("Boba Fett", "Han Solo", 2)           
]

for origen, destino, peso in aristas_data:
    g.insert_edge(origen, destino, peso)
    print(f"Insertada arista: {origen} <-> {destino} (Episodios: {peso})")


# Hallar el árbol de expansión mínimo
print("\n Árbol de Expansión Mínima (Kruskal)")

mst_str = g.kruskal('C-3PO')

if mst_str:
    costo_total = 0
    aristas_del_arbol = mst_str.split(';')
    print("Conexiones del Árbol de Expansión Mínima:")
    
    for arista_str in aristas_del_arbol:
        partes = arista_str.split('-')
        if len(partes) == 3:
            origen, destino, peso_str = partes
            costo = int(peso_str)
            costo_total += costo
            print(f"  * {origen} <-> {destino} (Costo: {costo})")
            
    print(f"\n  Costo total del MST (suma de episodios): {costo_total}")
else:
    print("No se pudo generar el árbol de expansión.")


# Número máximo de episodios que comparten dos personajes
print("\n Pares de personajes con máximo de episodios")

max_episodios = -1
pares_maximos = []

# Usamos un 'set' para no guardar duplicados (A-B y B-A)
pares_visitados = set()

for vertice in g:
    for arista in vertice.edges:
        # Creamos una clave única para el par
        par_clave = tuple(sorted((vertice.value, arista.value)))
        
        if par_clave not in pares_visitados:
            if arista.weight > max_episodios:
                # Encontramos un nuevo máximo
                max_episodios = arista.weight
                pares_maximos = [par_clave] # Reiniciamos la lista
            elif arista.weight == max_episodios:
                # Añadimos este par al máximo actual
                pares_maximos.append(par_clave)
            
            pares_visitados.add(par_clave)

if max_episodios != -1:
    print(f"El número máximo de episodios compartidos es: {max_episodios}")
    print("Los pares que comparten este número son:")
    for par in pares_maximos:
        print(f"  * {par[0]} y {par[1]}")
else:
    print("No se encontraron aristas en el grafo.")


#Calcule el camino más corto
# (La función print_shortest_path se definió al inicio)
print_shortest_path(g, 'C-3PO', 'R2-D2')
print_shortest_path(g, 'Yoda', 'Darth Vader')


# Indicar qué personajes aparecieron en los nueve episodios
print("\n Personajes que aparecieron en los 9 episodios")

encontrados = False
for vertice in g:
    # Aquí usamos la información que guardamos gracias
    # a la modificación de 'insert_vertex'
    if vertice.other_values and vertice.other_values.get("en_nueve") is True:
        print(f"  * {vertice.value}")
        encontrados = True

if not encontrados:
    print("No se encontraron personajes que cumplan el criterio.")
