#ejercicio 13 de pila

# pila (modelo, película, estado)
pila_trajes = [
    {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Dañado"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Impecable"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Destruido"},
    {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Dañado"},
    {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Impecable"},
    {"modelo": "Mark XLVI", "pelicula": "Captain America: Civil War", "estado": "Dañado"},
    {"modelo": "Mark L", "pelicula": "Avengers: Endgame", "estado": "Dañado"},
]

# a. ¿Se usó el modelo Hulkbuster (Mark XLIV)? ¿En qué películas?
def buscar_hulkbuster(pila):
    aux = []
    encontrado = False
    peliculas = []

    while pila:
        traje = pila.pop()
        aux.append(traje)
        if traje["modelo"] == "Mark XLIV":
            encontrado = True
            peliculas.append(traje["pelicula"])

    while aux:
        pila.append(aux.pop())

    if encontrado:
        print("\n[a] El modelo Hulkbuster (Mark XLIV) fue usado en:")
        for p in peliculas:
            print("-", p)
    else:
        print("\n[a] El modelo Hulkbuster (Mark XLIV) no fue usado en ninguna película.")

# b. Mostrar los modelos dañados sin perder la pila
def mostrar_danados(pila):
    aux = []
    print("\n[b] Modelos dañados:")
    while pila:
        traje = pila.pop()
        aux.append(traje)
        if traje["estado"] == "Dañado":
            print("-", traje["modelo"], "en", traje["pelicula"])
    while aux:
        pila.append(aux.pop())

# c. Eliminar los modelos destruidos y mostrar sus nombres
def eliminar_destruidos(pila):
    aux = []
    print("\n[c] Modelos destruidos eliminados:")
    while pila:
        traje = pila.pop()
        if traje["estado"] == "Destruido":
            print("-", traje["modelo"], "en", traje["pelicula"])
        else:
            aux.append(traje)
    while aux:
        pila.append(aux.pop())

# e. Agregar un nuevo traje, sin repetir modelo en misma película
def agregar_modelo(pila, nuevo_traje):
    aux = []
    repetido = False

    while pila:
        traje = pila.pop()
        aux.append(traje)
        if traje["modelo"] == nuevo_traje["modelo"] and traje["pelicula"] == nuevo_traje["pelicula"]:
            repetido = True

    if not repetido:
        aux.append(nuevo_traje)
        print("\n[e] Modelo agregado:", nuevo_traje)
    else:
        print("\n[e] Ya existe ese modelo para esa película.")

    while aux:
        pila.append(aux.pop())

# f. Mostrar trajes usados en películas específicas
def mostrar_trajes_peliculas(pila, peliculas_objetivo):
    aux = []
    print("\n[f] Trajes usados en películas seleccionadas:")
    while pila:
        traje = pila.pop()
        aux.append(traje)
        if traje["pelicula"] in peliculas_objetivo:
            print("-", traje["modelo"], "en", traje["pelicula"])
    while aux:
        pila.append(aux.pop())



buscar_hulkbuster(pila_trajes)
mostrar_danados(pila_trajes)
eliminar_destruidos(pila_trajes)
nuevo_traje = {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Impecable"}
agregar_modelo(pila_trajes, nuevo_traje)
pelis = ["Spider-Man: Homecoming", "Captain America: Civil War"]
mostrar_trajes_peliculas(pila_trajes, pelis)

    
    
    
        
        