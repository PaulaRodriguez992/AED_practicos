from typing import Any

class HeapMax:
   
    def __init__(self):
        self.elements = []
    
    def size(self) -> int:
        return len(self.elements)

    def add(self, value: Any) -> None:
        self.elements.append(value)
        self.float(self.size()-1)
    
    def remove(self) -> Any:
        if self.size() == 0:
            return None # Evita errores si la cola está vacía
        last = self.size() - 1
        self.interchange(0, last)
        value = self.elements.pop()
        if self.size() > 0:
            self.sink(0)
        return value

    def float(self, index: int) -> None:
        father = (index - 1) // 2
        # Comparamos el primer elemento del par [prioridad, valor]
        while index > 0 and self.elements[index][0] > self.elements[father][0]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index: int) -> None:
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1
            mayor = left_son
            if right_son < self.size():
                # Comparamos la prioridad
                if self.elements[right_son][0] > self.elements[mayor][0]:
                    mayor = right_son
            
            # Comparamos la prioridad
            if self.elements[index][0] < self.elements[mayor][0]:
                self.interchange(index, mayor)
                index = mayor
                left_son = (2 * index) + 1
            else:
                control = False

    def interchange(self, index_1: int, index_2: int) -> None:
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    # --- Métodos para Cola de Prioridad ---
    def arrive(self, value: Any, priority: int) -> None:
        self.add([priority, value])
    
    def attention(self) -> Any:
        return self.remove()