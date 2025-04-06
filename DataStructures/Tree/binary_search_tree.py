from DataStructures.Tree import bst_node as bst_node
from DataStructures.List import single_linked_list as sll
from DataStructures.List.single_linked_list import new_list, add_last

def new_map():
    """Crea un nuevo árbol de búsqueda"""
    
    return {'root': None, 'size': 0}

def put(my_bst, key, value):
    """Agrega un nuevo nodo llave-valor a un árbol binario de búsqueda (BST). 
    Si la llave ya existe, se actualiza el value del nodo."""
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    my_bst["size"] = size_tree(my_bst["root"])
    return my_bst


def insert_node(root, key, value):
    """Inserta un nuevo nodo llave-valor en el árbol binario de búsqueda (BST) de manera recursiva.
    Esta función es llamada por la función put"""
    if root is None:
        return {
            "key": key,
            "value": value,
            "size": 1,
            "left": None,
            "right": None
        }
    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
    root["size"] = size_tree(root)
    return root

def get(my_bst, key):
    """Busca un nodo en el árbol binario de búsqueda (BST) y devuelve su valor.
    Esta función llama a la función get_node para buscar el nodo en el árbol de manera recursiva."""
    return get_node(my_bst["root"], key)

def get_node(root, key):
    if root is None:
        return None
    if key < root["key"]:
        return get_node(root["left"], key)
    elif key > root["key"]:
        return get_node(root["right"], key)
    else:
        return root["value"]

def remove(my_bst, key):
    "elimina el nodo con la clave ``key`` del árbol"
    
    my_bst["root"] = remove_node(my_bst["root"], key)
    my_bst["size"] = size_tree(my_bst["root"])
    return my_bst

def remove_node(root, key):
    "Elimina la pareja llave-valor que coincida con``key`` es usada por la función remove"
    if root is None:
        return None
    if key < root["key"]:
        root["left"] = remove_node(root["left"], key)
    elif key > root["key"]:
        root["right"] = remove_node(root["right"], key)
    else:
        if root["left"] is None:
            return root["right"]
        if root["right"] is None:
            return root["left"]
        temp = get_min_node(root["right"])
        root["key"], root["value"] = temp["key"], temp["value"]
        root["right"] = remove_node(root["right"], temp["key"])
    root["size"] = size_tree(root)
    return root

def contains(my_bst, key):
    """Devuelve True si el árbol de búsqueda contiene la llave ``key``, False en caso contrario."""
    return get(my_bst, key) is not None

def size(my_bst):
    """Retorna el número de entradas en la tabla de simbolos
    usa la función size_tree() para contar el número de elementos."""
    return size_tree(my_bst["root"])

def size_tree(root):
    """Retornar el número de entradas en la a partir del nodo root
    Es usada en la función size()"""
    if root is None:
        return 0
    return root["size"]

def is_empty(my_bst):
    """Informa si la tabla de simbolos se encuentra vacia"""
    return my_bst["root"] is None

def key_set(my_bst):
    """Retorna una lista con todas las llaves de la tabla.
    Usa la función key_set_tree() para construir la lista de llaves"""
    lista = new_list()
    def inorder_keys(node):
        if node is not None:
            inorder_keys(node["left"])
            add_last(lista, node["key"])
            inorder_keys(node["right"])
    
    inorder_keys(my_bst["root"])
    return lista

def value_set(my_bst):
    """
    Retorna una lista con todos los valores del árbol de búsqueda.

    Parameters:
    my_bst (dict): El árbol binario de búsqueda.

    Returns:
    linked_list: Lista enlazada con todos los valores del árbol.
    """
    lista = new_list()
    def inorder_values(node):
        if node is not None:
            inorder_values(node["left"])
            add_last(lista, node["value"])
            inorder_values(node["right"])
    
    inorder_values(my_bst["root"])
    return lista

def get_min(my_bst):
    """"Retorna la llave mas pequeña de la tabla de simbolos
    Usa la función get_min_node() para encontrar la llave más a la izquierda"""
    if my_bst is None or my_bst['root'] is None:
        return None
    return get_min_node(my_bst['root'])

def get_min_node(root):
    """Retorna la llave mas pequeña de la tabla de simbolos
    Es usada en la función get_min()"""
    current = root
    while current['left'] is not None:
        current = current['left']
    return current['key']

def get_max(my_bst):
    """Retorna la llave mas grande de la tabla de simbolos
    usa la función get_max_node() para encontrar la llave más grande de del arbol"""
    if my_bst is None or my_bst['root'] is None:
        return None
    return get_max_node(my_bst['root'])

def get_max_node(root):
    """"Retorna la llave mas grande de la tabla de simbolos
    Es usada en la función get_max() Usa la función get_max_node() para encontrar la llave más grande"""
    current = root
    while current['right'] is not None:
        current = current['right']
    return current['key']

def delete_min_tree(root):
    """Encuentra y remueve la llave mas pequeña de la tabla de simbolos y su valor asociado
    Es usada en la función delete_min() Usa la función delete_min_tree() para eliminar la llave más pequeña"""
    if root is None:
        return None

    if root['left'] is None:
        return root['right'] 

    root['left'] = delete_min_tree(root['left'])

    left_size = root['left']['size'] if root['left'] else 0
    right_size = root['right']['size'] if root['right'] else 0
    root['size'] = 1 + left_size + right_size

    return root

def delete_min(my_bst):
    """Encuentra y remueve la llave mas pequeña de la tabla de simbolos y su valor asociado.
    Usa la función delete_min_tree() para eliminar la llave más pequeña"""
    my_bst['root'] = delete_min_tree(my_bst['root'])
    return my_bst

def delete_max(my_bst):
    """Encuentra y remueve la llave mas grande de la tabla de simbolos y su valor asociado.
    Usa la función delete_max_tree() para eliminar la llave más grande"""
    my_bst['root'] = delete_max_tree(my_bst['root'])
    return my_bst


def delete_max_tree(root):
    """Encuentra y remueve la llave mas grande de la tabla de simbolos y su valor asociado
    Es usada en la función delete_max() Usa la función delete_max_tree() para eliminar la llave más grande"""   
    if root is None:
        return None

    if root['right'] is None:
        return root['left']  

    root['right'] = delete_max_tree(root['right'])

    left_size = root['left']['size'] if root['left'] else 0
    right_size = root['right']['size'] if root['right'] else 0
    root['size'] = 1 + left_size + right_size

    return root

def floor(my_bst, key):
    """Retorna la llave que precede a la llave key en la tabla de simbolos.
    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave predecedente más cercana como si la llave key existiera en la tabla. Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 5.
    Usa la función floor_key() para encontrar la llave predecesora a key"""
    return floor_key(my_bst['root'], key)


def floor_key(root, key):
    """Retorna la llave que precede a la llave key en la tabla de simbolos.
    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave predecedente más cercana como si la llave key existiera en la tabla.
    Es usada en la función floor() Usa la función floor_key() para encontrar la llave predecesora a key"""
    if root is None:
        return None

    root_key = root['key']

    if key == root_key:
        return root_key
    elif key < root_key:
        return floor_key(root['left'], key)
    else:
        right_floor = floor_key(root['right'], key)
        return right_floor if right_floor is not None else root_key


def ceiling(my_bst, key):
    """Retorna la llave que sucede a la llave key en la tabla de simbolos.
    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave sucesora más cercana como si la llave key existiera en la tabla. Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 7.
    Usa la función ceiling_key() para encontrar la llave sucesora a key"""
    return ceiling_key(my_bst['root'], key)

def ceiling_key(root, key):
    """Función auxiliar para ceiling"""
    if root is None:
        return None

    root_key = bst_node.get_key(root)

    if key == root_key:
        return root_key

    if key > root_key:
        return ceiling_key(bst_node.get_right(root), key)

    left_ceiling = ceiling_key(bst_node.get_left(root), key)
    return left_ceiling if left_ceiling is not None else root_key

def select(my_bst, pos):
    """Retorna la siguiente llave a la k-esima llave de izquierda a derecha de la tabla de simbolos.
    Usa la función select_key() para encontrar la llave en la posición pos"""
    node = select_key(my_bst["root"], pos)
    if node:
        return bst_node.get_key(node)
    return None

def select_key(root, key):
    """Retorna la siguiente llave a la k-esima llave de izquierda a derecha de la tabla de simbolos.
    Es usada en la función select() Usa la función select_key() para encontrar la llave en la posición pos"""   
    if root is None:
        return None

    left = bst_node.get_left(root)
    left_size = size_tree(left) if left else 0

    if key < left_size:
        return select_key(left, key)
    elif key > left_size:
        return select_key(bst_node.get_right(root), key - left_size - 1)
    else:
        return root

def rank(my_bst, key):
    """Retorna el número de llaves en la tabla que son estrictamente predecesoras a key Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 3.
    Usa la función rank_keys() para encontrar el número de llaves predecesoras a keyo""" 
    return rank_keys(my_bst["root"], key)

def rank_keys(root, key):
    """Retorna el número de llaves en la tabla que son estrictamente predecesoras a key Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 3.
    Es usada en la función rank() Usa la función rank_keys() para encontrar el número de llaves predecesoras a key""" 
    if root is None:
        return 0

    current_key = bst_node.get_key(root)

    if key <= current_key:
        return rank_keys(bst_node.get_left(root), key)
    else:
        left_size = size_tree(bst_node.get_left(root))
        return 1 + left_size + rank_keys(bst_node.get_right(root), key)

def height(my_bst):
    "devuelve la altura del arbol usa la función heigth_tree"
    return height_tree(my_bst['root'])

def height_tree(node):
    """
    Calcula la altura de un árbol binario de búsqueda desde un nodo dado.

    Parámetros:
    - node: nodo raíz del árbol o subárbol

    Retorna:
    - int: altura del árbol (0 si está vacío)
    """
    if node is None:
        return 0
    left_height = height_tree(get_left(node))
    right_height = height_tree(get_right(node))
    return max(left_height, right_height) + 1

def get_left(node):
    """
    Retorna el hijo izquierdo del nodo dado.
    """
    if node is None:
        return None
    return node.get("left")


def get_right(node):
    """
    Retorna el hijo derecho del nodo dado.
    """
    if node is None:
        return None
    return node.get("right")

def keys(my_bst, key_initial, key_final):
    """Retorna todas las llaves del arbol que se encuentren entre [key_initial, key_final].
    Usa la función keys_range() para encontrar las llaves en el rango especificado"""   
    list_keys = sll.new_single_linked_list()
    keys_range(my_bst["root"], key_initial, key_final, list_keys)
    return list_keys

def keys_range(root, key_initial, key_final, list_key):   
    """Retorna todas las llaves del arbol que se encuentren entre [key_initial, key_final].
    Es usada en la función keys() Usa la función keys_range() para encontrar las llaves en el rango especificado"""
    if root is None:
        return

    key = bst_node.get_key(root)

    if key > key_initial:
        keys_range(bst_node.get_left(root), key_initial, key_final, list_key)

    if key_initial <= key <= key_final:
        sll.add_last(list_key, key)

    if key < key_final:
        keys_range(bst_node.get_right(root), key_initial, key_final, list_key)
        
def values(my_bst, key_initial, key_final):
    """Retorna todas los valores del arbol que se encuentren entre [key_initial, key_final]
    Usa la función values_range() para encontrar los valores en el rango especificado"""
    list_values = sll.new_single_linked_list()
    values_range(my_bst["root"], key_initial, key_final, list_values)
    return list_values

def values_range(root, key_initial, key_final, list_value):
    """Función de comparación por defecto. Compara una llave con la llave de un elemento llave-valor."""
    if root is None:
        return

    key = bst_node.get_key(root)

    if key_initial < key:
        values_range(bst_node.left(root), key_initial, key_final, list_value)

    if key_initial <= key <= key_final:
        sll.add_last(list_value, bst_node.get_value(root))

    if key < key_final:
        values_range(bst_node.right(root), key_initial, key_final, list_value)

    return list_value

def default_compare(key, element):
    """Función de comparación por defecto. Compara una llave con la llave de un elemento llave-valor."""
    if key == bst_node.get_key(element):
        return 0
    elif key > bst_node.get_key(element):
        return 1
    return -1


