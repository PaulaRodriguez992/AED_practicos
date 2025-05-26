
from typing import Any, Optional 


class Stack:   #crea un  objeto de la clase stack

    def __init__(self):  #constructor de la clase stack
        self.__elements = [] #crea una lista vacia para almacenar los elementos de la pila


    def push(self, value: Any) -> None:  #agrega un elemento a la pila y no devuelve nada solo agrega
        self.__elements.append(value) #agrega el elemento al final de la lista

    def pop(self) -> Optional[Any]: #saca un elemento de la pila y lo devuelve
        # Si la pila está vacía, devuelve None
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )

    def size(self) -> int: #devuelve la cantidad de elementos en la pila
        return len(self.__elements)

    def on_top(self) -> Optional[Any]: #devuelve el elemento que está en la parte superior de la pila sin sacarlo
        # Si la pila está vacía, devuelve None
        return (
            self.__elements[-1] 
            if self.__elements
            else None
        )

    def show(self): #muestra los elementos de la pila
        # Si la pila está vacía, devuelve None
        if self.size() == 0:
            print("La pila está vacía")
            return None
        aux_stack = Stack() #crea una pila auxiliar para almacenar los elementos de la pila original
        # Muestra los elementos de la pila original y los almacena en la pila auxiliar  
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value) #saca el elemento de la pila original y lo agrega a la pila auxiliar
        
        while aux_stack.size() > 0: #vuelve a agregar los elementos a la pila original
            self.push(aux_stack.pop()) 