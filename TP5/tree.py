from typing import Any, Optional
from queue_ import Queue

class BinaryTree:

    class __nodeTree:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.other_values = other_values
            self.left = None
            self.right = None
            self.hight = 0

    def __init__(self):
        self.root = None

    def insert(self, value: Any, other_values: Optional[Any] = None):
        def __insert(root, value, other_values):
            if root is None:
                return BinaryTree.__nodeTree(value, other_values)
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
            else:
                root.right = __insert(root.right, value, other_values)

            root = self.auto_balance(root)
            self.update_hight(root)

            return root

        self.root = __insert(self.root, value, other_values)

    def pre_order(self):
        def __pre_order(root):
            if root is not None:
                print(root.value, root.other_values, root.hight)
                __pre_order(root.left)
                __pre_order(root.right)

        if self.root is not None:
            __pre_order(self.root)

    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value, root.other_values)
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)

    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(root.value)
                __post_order(root.left)

        if self.root is not None:
            __post_order(self.root)

    def search(self, value: Any) -> __nodeTree:
        def __search(root, value):
            if root is not None:
                if root.value == value:
                    return root
                elif root.value > value:
                    return __search(root.left, value)
                else:
                    return __search(root.right, value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux

    def proximity_search(self, value: Any) -> __nodeTree:
        def __search(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value)
                # elif root.value > value:
                __search(root.left, value)
                # else:
                __search(root.right, value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux

    def delete(self, value: Any):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            delete_value = None
            deleter_other_values = None
            if root is not None:
                if value < root.value:
                    root.left, delete_value, deleter_other_values = __delete(root.left, value)
                elif value > root.value:
                    root.right, delete_value, deleter_other_values = __delete(root.right, value)
                else:
                    delete_value = root.value
                    deleter_other_values = root.other_values
                    if root.left is None:
                        root = root.right
                    elif root.right is None:
                        root.right = root.left
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_values = replace_node.other_values

                root = self.auto_balance(root)
                self.update_hight(root)
            return root, delete_value, deleter_other_values

        delete_value =  None
        deleter_other_values = None
        if self.root is not None:
            self.root, delete_value, deleter_other_values = __delete(self.root, value)
        
        return delete_value, deleter_other_values
    
    def by_level(self):
        tree_queue = Queue()
        if self.root is not None:
            tree_queue.arrive(self.root)

            while tree_queue.size() > 0:
                node = tree_queue.attention()
                print(node.value)
                if node.left is not None:
                    tree_queue.arrive(node.left)
                if node.right is not None:
                    tree_queue.arrive(node.right)

    def hight(self, root):
        if root is None:
            return -1
        else:
            return root.hight

    def update_hight(self, root):
        if root is not None:
            alt_left = self.hight(root.left)
            alt_right = self.hight(root.right)
            root.hight = max(alt_left, alt_right) + 1

    def simple_rotation(self, root, control):
        if control: # RS Right
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # RS Left
            aux = root.right
            root.right = aux.left
            aux.left = root

        self.update_hight(root)
        self.update_hight(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control: # RD Right
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        
        return root

    def auto_balance(self, root):
        if root is not None:
            if self.hight(root.left) - self.hight(root.right) == 2:
                if self.hight(root.left.left) >= self.hight(root.left.right):
                    # print("RS RIGHT")
                    root = self.simple_rotation(root, True)
                else:
                    # print("RD RIGHT")
                    root = self.double_rotation(root, True)
            if self.hight(root.right) - self.hight(root.left) == 2:
                if self.hight(root.right.right) >= self.hight(root.right.left):
                    # print("RS LEFT")
                    root = self.simple_rotation(root, False)
                else:
                    # print("RD LEFT")
                    root = self.double_rotation(root, False)
        return root

    def villain_in_order(self):
        def __villain_in_order(root):
            if root is not None:
                __villain_in_order(root.left)
                if root.other_values["is_villain"] is True:
                    print(root.value)
                __villain_in_order(root.right)

        if self.root is not None:
            __villain_in_order(self.root)
            
    def in_order_starts_with_c(self): #agregado para ej5 c
        """Muestra los superhéroes que empiezan con C."""
        def __in_order_starts_with_c(root):
            if root is not None:
                __in_order_starts_with_c(root.left)
                # Verificamos si es héroe y si su nombre empieza con 'C'
                if not root.other_values["is_villain"] and root.value.startswith('C'):
                    print(root.value)
                __in_order_starts_with_c(root.right)

        if self.root is not None:
            __in_order_starts_with_c(self.root)

    def in_order_desc(self): #agregado para ej5 f
        """Lista los superhéroes en orden descendente."""
        def __in_order_desc(root):
            if root is not None:
                # Recorremos primero el subárbol derecho para el orden inverso
                __in_order_desc(root.right)
                if not root.other_values["is_villain"]:
                    print(root.value)
                # Luego recorremos el subárbol izquierdo
                __in_order_desc(root.left)

        if self.root is not None:
            __in_order_desc(self.root)

    def count_nodes(self): #agregado para ej5 g.
        """Cuenta el número total de nodos en el árbol."""
        def __count_nodes(root):
            if root is None:
                return 0
            else:
                # Un nodo es 1 + la cuenta de sus subárboles izquierdo y derecho
                return 1 + __count_nodes(root.left) + __count_nodes(root.right)
        
        return __count_nodes(self.root)

    def count_heroes(self):
        def __count_heroes(root):
            count = 0
            if root is not None:
                if root.other_values["is_villain"] is False:
                    count += 1
                count += __count_heroes(root.left)
                count += __count_heroes(root.right)

            return count

        total = 0
        if self.root is not None:
            total = __count_heroes(self.root)
        
        return total
    
    # MÉTODOS NUEVOS para ej23
    def in_order_defeats(self): #punto a
        """Realiza un barrido in-order mostrando la criatura y por quién fue derrotada."""
        def __in_order_defeats(root):
            if root is not None:
                __in_order_defeats(root.left)
                defeated_by = root.other_values.get("derrotado_por") or "Nadie"
                print(f"- {root.value} (Derrotado por: {defeated_by})")
                __in_order_defeats(root.right)
        
        if self.root is not None:
            __in_order_defeats(self.root)

    def in_order_defeated_by(self, hero_name): #punto e
        """Lista las criaturas derrotadas por un héroe o dios específico."""
        def __in_order_defeated_by(root, hero_name):
            if root is not None:
                __in_order_defeated_by(root.left, hero_name)
                if root.other_values.get("derrotado_por") == hero_name:
                    print(f"- {root.value}")
                __in_order_defeated_by(root.right, hero_name)
        
        if self.root is not None:
            __in_order_defeated_by(self.root, hero_name)

    def in_order_not_defeated(self): #punto 
        """Lista las criaturas que no han sido derrotadas."""
        def __in_order_not_defeated(root):
            if root is not None:
                __in_order_not_defeated(root.left)
                # Usamos .get() para evitar errores si la clave no existiera
                if not root.other_values.get("derrotado_por"):
                    print(f"- {root.value}")
                __in_order_not_defeated(root.right)

        if self.root is not None:
            __in_order_not_defeated(self.root)

    def generate_ranking_defeats(self):
        """Genera un ranking de los héroes que más criaturas derrotaron."""
        ranking = {}
        def __generate_ranking(root, ranking):
            if root is not None:
                __generate_ranking(root.left, ranking)
                hero = root.other_values.get("derrotado_por")
                if hero: # Si el valor no es None o una cadena vacía
                    ranking[hero] = ranking.get(hero, 0) + 1
                __generate_ranking(root.right, ranking)
        
        __generate_ranking(self.root, ranking)
        return ranking

    def in_order_captured_by(self, hero_name):
        """Muestra las criaturas capturadas por un héroe o dios específico."""
        def __in_order_captured_by(root, hero_name):
            if root is not None:
                __in_order_captured_by(root.left, hero_name)
                if root.other_values.get("capturada") == hero_name:
                    print(f"- {root.value}")
                __in_order_captured_by(root.right, hero_name)
        
        if self.root is not None:
            __in_order_captured_by(self.root, hero_name)  
            
            # MÉTODOS PARA EJ23
    
    def divide_tree(self, arbol_h, arbol_v):
        def __divide_tree(root, arbol_h, arbol_v):
            if root is not None:
                if root.other_values["is_villain"] is False:
                    arbol_h.insert(root.value, root.other_values)
                else:
                    arbol_v.insert(root.value, root.other_values)
                __divide_tree(root.left, arbol_h, arbol_v)
                __divide_tree(root.right, arbol_h, arbol_v)


        __divide_tree(self.root, arbol_h, arbol_v)
    
    def in_order_height(self):
        def __in_order_height(root):
            if root is not None:
                __in_order_height(root.left)
                if root.other_values['height'] > 100:
                    print(root.value, root.other_values['height'])
                __in_order_height(root.right)

        if self.root is not None:
            __in_order_height(self.root)
    
    def in_order_weight(self):
        def __in_order_weight(root):
            if root is not None:
                __in_order_weight(root.left)
                if root.other_values['weight'] < 75:
                    print(root.value, root.other_values['weight'])
                __in_order_weight(root.right)

        if self.root is not None:
            __in_order_weight(self.root)

    def ranking(self, ranking_result):
        def __ranking(root, ranking_result):
            if root is not None:
                __ranking(root.left, ranking_result)
                hero = root.other_values['derrotado_por']
                if hero is not None:
                    if hero not in ranking_result:
                        ranking_result[hero] = 1
                    else:
                        ranking_result[hero] += 1
                __ranking(root.right, ranking_result)

        if self.root is not None:
            __ranking(self.root, ranking_result)

arbol = BinaryTree()
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()


