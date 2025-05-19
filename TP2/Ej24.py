from typing import List

pila_temperaturas: List[float] = [
    21.5, 22.0, 20.8, 19.4, 23.1, 24.0, 22.5, 25.2,
    20.3, 19.0, 21.9, 23.0, 20.0, 21.1, 22.3, 24.5,
    23.7, 25.0, 22.8, 21.0, 20.6, 19.8, 22.7, 23.3,
    24.8, 25.5, 23.9, 22.6, 21.4, 20.2
]

def calcular_rango(pila: List[float]) -> None:
    aux: List[float] = []
    temp_min: float = float('inf')
    temp_max: float = float('-inf')

    while pila:
        temp = pila.pop()
        aux.append(temp)
        temp_min = min(temp_min, temp)
        temp_max = max(temp_max, temp)

    while aux:
        pila.append(aux.pop())

    print(f"\n[a] Temperatura mínima: {temp_min}°C")
    print(f"[a] Temperatura máxima: {temp_max}°C")
    print(f"[a] Rango: {temp_max - temp_min:.2f}°C")

def calcular_promedio(pila: List[float]) -> float:
    aux: List[float] = []
    suma: float = 0
    cantidad: int = 0

    while pila:
        temp = pila.pop()
        aux.append(temp)
        suma += temp
        cantidad += 1

    while aux:
        pila.append(aux.pop())

    promedio: float = suma / cantidad if cantidad > 0 else 0
    print(f"\n[b] Promedio del mes: {promedio:.2f}°C")
    return promedio

def comparar_con_promedio(pila: List[float], promedio: float) -> None:
    aux: List[float] = []
    arriba: int = 0
    abajo: int = 0

    while pila:
        temp = pila.pop()
        aux.append(temp)
        if temp > promedio:
            arriba += 1
        elif temp < promedio:
            abajo += 1

    while aux:
        pila.append(aux.pop())

    print(f"\n[c] Valores por encima del promedio: {arriba}")
    print(f"[c] Valores por debajo del promedio: {abajo}")

calcular_rango(pila_temperaturas)
media = calcular_promedio(pila_temperaturas)
comparar_con_promedio(pila_temperaturas, media)
