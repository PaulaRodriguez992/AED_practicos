from graph import Graph

# 1. Crear el grafo no dirigido
# (Según tu código, is_directed=True añade la arista en ambas direcciones)
g = Graph(is_directed=True)

# 14.a. Cargar vértices (ambientes de la casa)
ambientes = [
    "cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
    "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"
]

for ambiente in ambientes:
    g.insert_vertex(ambiente)

print("--- Vértices cargados ---")


# 14.b. Cargar aristas (distancias en metros)
# (origen, destino, distancia)
conexiones = [
    # Cocina (5 aristas)
    ("cocina", "comedor", 4),
    ("cocina", "patio", 5),
    ("cocina", "baño 1", 3),
    ("cocina", "habitación 2", 7),
    ("cocina", "sala de estar", 6),

    # Comedor (5 aristas)
    ("comedor", "sala de estar", 5),
    ("comedor", "terraza", 6),
    ("comedor", "habitación 1", 8),
    ("comedor", "baño 1", 4),

    # Cochera (3 aristas)
    ("cochera", "patio", 6),
    ("cochera", "quincho", 7),
    ("cochera", "comedor", 9), 

    # Quincho (3 aristas)
    ("quincho", "patio", 3),
    ("quincho", "baño 2", 2),

    # Baño 1 (3 aristas)
    ("baño 1", "habitación 1", 2),

    # Baño 2 (3 aristas)
    ("baño 2", "habitación 2", 2),
    ("baño 2", "terraza", 5),

    # Habitación 1 (3 aristas)
    ("habitación 1", "sala de estar", 3),

    # Habitación 2 (3 aristas)
    ("habitación 2", "terraza", 4),
    
    # Sala de estar (4 aristas - cumple >= 3)
    ("sala de estar", "terraza", 3), 
]

for origen, destino, peso in conexiones:
    g.insert_edge(origen, destino, peso)

print("--- Aristas cargadas ---")


# 14.c. Obtener el árbol de expansión mínima (MST) con Kruskal
print("\n--- 14.c. Árbol de Expansión Mínima (Kruskal) ---")

arbol_expansion_str = g.kruskal('cocina') # 'cocina' es solo un punto de partida

if arbol_expansion_str:
    print(f"Las conexiones del árbol de expansión mínima son:")
    
    metros_totales_cable = 0
    aristas_del_arbol = arbol_expansion_str.split(';') # Separa cada arista

    for arista_str in aristas_del_arbol:
        partes = arista_str.split('-')
        if len(partes) == 3:
            origen, destino, peso_str = partes
            peso = int(peso_str)
            
            print(f"* De {origen} a {destino} - {peso} metros")
            metros_totales_cable += peso
        
    
    print(f"Total de metros de cable necesarios para conectar TODOS los ambientes:")
    print(f"==> {metros_totales_cable} metros")
    
else:
    print("No se pudo generar el árbol de expansión.")


# 14.d. Determinar el camino más corto (Dijkstra)
print("\n--- 14.d. Camino Más Corto (Dijkstra) ---")

origen_dijkstra = 'habitación 1'
destino_dijkstra = 'sala de estar'

# 1. Ejecutamos Dijkstra desde el origen
pila_caminos = g.dijkstra(origen_dijkstra)

# 2. Procesamos la pila para encontrar nuestro destino
camino_completo = []
peso_total_camino = None
destino_actual = destino_dijkstra 

while pila_caminos.size() > 0:
    # La pila contiene [vértice, costo_total_desde_origen, vértice_anterior]
    value = pila_caminos.pop()
    
    if value[0] == destino_actual:
        if peso_total_camino is None:
            peso_total_camino = value[1]
        
        camino_completo.append(value[0])
        destino_actual = value[2] # El vértice anterior

# 3. Mostrar el resultado
camino_completo.reverse() # Invertimos porque lo armamos al revés

if peso_total_camino is not None:
    print(f"El camino más corto desde '{origen_dijkstra}' hasta '{destino_dijkstra}' es:")
    print(f"==> {' -> '.join(camino_completo)}")
    print(f"Total de metros de cable de red necesarios:")
    print(f"==> {peso_total_camino} metros")
else:
    print(f"No se encontró un camino desde '{origen_dijkstra}' hasta '{destino_dijkstra}'.")