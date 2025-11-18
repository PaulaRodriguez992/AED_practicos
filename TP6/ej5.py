import math
from graph import Graph
from typing import Dict, Any

# ====================================================================
# FUNCIONES AUXILIARES (¡MUY ÚTILES!)
# ====================================================================

def get_all_shortest_paths(graph: Graph, origin: str) -> Dict[str, Any]:
    """
    Ejecuta Dijkstra desde un origen y devuelve un diccionario simple
    con {destino: costo_total} para todos los nodos alcanzables.
    """
    distances = {}
    path_stack = graph.dijkstra(origin)
    
    # El stack tiene [vertex_name, total_cost, previous_vertex]
    while path_stack.size() > 0:
        value = path_stack.pop()
        distances[value[0]] = value[1] # Guardamos {nombre: costo}
    return distances

def print_shortest_path(graph: Graph, origin: str, destination: str):
    """
    Ejecuta Dijkstra y formatea la salida para un camino
    específico, igual que hicimos en el ej14.py.
    """
    print(f"--- Calculando camino: {origin} -> {destination} ---")
    
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
        print(f"  Costo total: {peso_total_camino}")
    else:
        print(f"  No se encontró un camino de {origin} a {destination}.")


# ====================================================================
# INICIO DEL EJERCICIO 5
# ====================================================================

# 5.h. Debe utilizar un grafo no dirigido
# (Recordemos que en tu clase, is_directed=True lo hace no dirigido)
g = Graph(is_directed=True)


# 5.a. Cargar nodos con nombre y tipo
print("--- 5.a. Cargando Nodos (Vértices) ---")

# Lista de tuplas: (nombre_del_nodo, tipo_de_nodo)
vertices_data = [
    ("Manjaro", "PC"),
    ("Parrot", "PC"),
    ("Fedora", "PC"),
    ("Ubuntu", "PC"),
    ("Mint", "PC"),
    ("Red Hat", "Notebook"),
    ("Debian", "Notebook"),
    ("Arch", "Notebook"),
    ("Impresora", "Impresora"),
    ("Guaraní", "Servidor"),
    ("MongoDB", "Servidor"),
    ("Switch 1", "Switch"),
    ("Switch 2", "Switch"),
    ("Router 1", "Router"),
    ("Router 2", "Router"),
    ("Router 3", "Router")
]

for nombre, tipo in vertices_data:
    # Usamos el 'insert_vertex' modificado
    g.insert_vertex(nombre, {"tipo": tipo})
    print(f"Insertado: {nombre} (Tipo: {tipo})")


print("\n--- Cargando Conexiones (Aristas) ---")

# Lista de tuplas: (origen, destino, peso)
aristas_data = [
    ("Red Hat", "Router 2", 25),
    ("Debian", "Switch 1", 17),
    ("Ubuntu", "Switch 1", 18),
    ("Impresora", "Switch 1", 22),
    ("Mint", "Switch 1", 80),
    ("Switch 1", "Router 1", 29),
    ("Guaraní", "Router 2", 9),
    ("Router 2", "Router 3", 50),
    ("Router 2", "Router 1", 37),
    ("Router 1", "Router 3", 43),
    ("Manjaro", "Switch 2", 40),
    ("Parrot", "Switch 2", 12),
    ("Fedora", "Switch 2", 3),
    ("MongoDB", "Switch 2", 5),
    ("Arch", "Switch 2", 56),
    ("Router 3", "Switch 2", 61)
]

for origen, destino, peso in aristas_data:
    g.insert_edge(origen, destino, peso)
    print(f"Insertada arista: {origen} <-> {destino} (Peso: {peso})")


# 5.b. Barrido en profundidad (DFS) y amplitud (BFS)
print("\n--- 5.b. Barridos DFS y BFS desde Notebooks ---")
notebooks = ["Red Hat", "Debian", "Arch"]

for nb in notebooks:
    print(f"\n>>>>> Barrido en Profundidad (DFS) desde: {nb} <<<<<")
    g.deep_sweep(nb)
    print(f"\n>>>>> Barrido en Amplitud (BFS) desde: {nb} <<<<<")
    g.amplitude_sweep(nb)


# 5.c. Camino más corto a la impresora
print("\n--- 5.c. Camino más corto a la Impresora ---")
pcs_imprimir = ["Manjaro", "Red Hat", "Fedora"]
destino_impresora = "Impresora"

for pc in pcs_imprimir:
    print_shortest_path(g, pc, destino_impresora)


# 5.d. Árbol de expansión mínima
print("\n--- 5.d. Árbol de Expansión Mínima (Kruskal) ---")

# 'Router 1' es solo un punto de partida, Kruskal funciona igual
arbol_expansion_str = g.kruskal('Router 1')

if arbol_expansion_str:
    metros_totales_cable = 0
    aristas_del_arbol = arbol_expansion_str.split(';')

    for arista_str in aristas_del_arbol:
        partes = arista_str.split('-')
        if len(partes) == 3:
            origen, destino, peso_str = partes
            metros_totales_cable += int(peso_str)
            
    print(f"El costo total del árbol de expansión mínima es: {metros_totales_cable}")
else:
    print("No se pudo generar el árbol de expansión.")


# 5.e. PC (no notebook) con camino más corto a "Guaraní"
print("\n--- 5.e. PC con camino más corto a 'Guaraní' ---")

# 1. Obtenemos todas las distancias desde "Guaraní"
distancias_desde_guarani = get_all_shortest_paths(g, "Guaraní")

# 2. Filtramos solo las que son de tipo "PC"
caminos_pc_guarani = {}
for i in range(len(g)): # Iteramos sobre el grafo
    nodo = g[i]
    if nodo.other_values["tipo"] == "PC":
        costo = distancias_desde_guarani.get(nodo.value)
        if costo is not None and costo != math.inf:
            caminos_pc_guarani[nodo.value] = costo

# 3. Encontramos la PC con el costo mínimo
if caminos_pc_guarani:
    # Esta es una forma elegante en Python de encontrar la llave con el valor mínimo
    min_pc = min(caminos_pc_guarani, key=caminos_pc_guarani.get)
    print(f"Resultados de PCs a 'Guaraní': {caminos_pc_guarani}")
    print(f"El PC (no notebook) con el camino más corto a 'Guaraní' es: {min_pc} (Costo: {caminos_pc_guarani[min_pc]})")
else:
    print("No se encontraron caminos desde PCs a 'Guaraní'.")


# 5.f. Computadora de Switch 1 con camino más corto a "MongoDB"
print("\n--- 5.f. Dispositivo de Switch 1 con camino más corto a 'MongoDB' ---")

# 1. Identificamos dispositivos conectados a "Switch 1" (excluyendo routers)
# Mirando la data, son: Debian, Ubuntu, Impresora, Mint
dispositivos_s1 = ["Debian", "Ubuntu", "Impresora", "Mint"]

# 2. Obtenemos todas las distancias desde "MongoDB"
distancias_desde_mongo = get_all_shortest_paths(g, "MongoDB")

# 3. Filtramos solo para nuestros dispositivos
caminos_s1_mongo = {}
for disp in dispositivos_s1:
    costo = distancias_desde_mongo.get(disp)
    if costo is not None and costo != math.inf:
        caminos_s1_mongo[disp] = costo

# 4. Encontramos el mínimo
if caminos_s1_mongo:
    min_disp = min(caminos_s1_mongo, key=caminos_s1_mongo.get)
    print(f"Resultados de dispositivos S1 a 'MongoDB': {caminos_s1_mongo}")
    print(f"El dispositivo en Switch 1 con camino más corto a 'MongoDB' es: {min_disp} (Costo: {caminos_s1_mongo[min_disp]})")
else:
    print("No se encontraron caminos desde dispositivos de Switch 1 a 'MongoDB'.")


# 5.g. Cambiar conexión de Impresora y repetir punto 5.b
print("\n--- 5.g. Modificando el grafo y repitiendo 5.b ---")

# 1. Borramos la conexión vieja
g.delete_edge("Impresora", "Switch 1")
print("Arista 'Impresora <-> Switch 1' eliminada.")

# 2. Añadimos la nueva conexión. El peso no se especifica, usaré 30 como ejemplo.
nuevo_peso = 30
g.insert_edge("Impresora", "Router 2", nuevo_peso)
print(f"Arista 'Impresora <-> Router 2' (Peso: {nuevo_peso}) creada.")

# 3. Repetimos el código del punto 5.b
print("\n--- Repitiendo 5.b en el grafo modificado ---")
for nb in notebooks:
    print(f"\n>>>>> Barrido en Profundidad (DFS) desde: {nb} (Modificado) <<<<<")
    g.deep_sweep(nb)
    print(f"\n>>>>> Barrido en Amplitud (BFS) desde: {nb} (Modificado) <<<<<")
    g.amplitude_sweep(nb)

print("\n--- Fin del Ejercicio 5 ---")