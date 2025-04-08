from DataStructures.List import single_linked_list as sl

def new_map():
    """Crea un nuevo árbol de búsqueda"""
    
    return {'root': None, 'size': 0}

def new_node(key, value=None):
    """Crea un nuevo nodo para el BST con la estructura solicitada:
    - key: llave del nodo.
    - value: valor asociado (opcional).
    - size: tamaño del subárbol (inicialmente 1).
    - left: hijo izquierdo (inicialmente None).
    - right: hijo derecho (inicialmente None).
    """
    return {
        "key": key,
        "value": value,
        "left": None,
        "right": None,
        "size": 1  
    }

def _update_size(node):
    """Actualiza el campo 'size' de un nodo basado en sus hijos."""
    if node is None:
        return
    left_size = node["left"]["size"] if node["left"] else 0
    right_size = node["right"]["size"] if node["right"] else 0
    node["size"] = 1 + left_size + right_size

def put(node, key, value):
    """Agrega un nuevo nodo llave-valor a un árbol binario de búsqueda (BST). 
    Si la llave ya existe, se actualiza el value del nodo."""
    my_bst['root'] = insert_node(my_bst['root'], key, value, my_bst['cmpfunction'])
    return my_bst


def insert_node(root, key, value):
    """Inserta un nuevo nodo llave-valor en el árbol binario de búsqueda (BST) de manera recursiva.
    Esta función es llamada por la función put"""
    if root is None:
        return {
            'key': key,
            'value': value,
            'left': None,
            'right': None,
            'size': 1
        }

    comparison = cmpfunction(key, root['key'])

    if comparison < 0:
        root['left'] = insert_node(root['left'], key, value, cmpfunction)
    elif comparison > 0:
        root['right'] = insert_node(root['right'], key, value, cmpfunction)
    else:
        root['value'] = value 

    root['size'] = 1 + size_tree(root['left']) + size_tree(root['right'])
    return root

def get(root, key):
    """Busca un nodo en el árbol binario de búsqueda (BST) y devuelve su valor.
    Esta función llama a la función get_node para buscar el nodo en el árbol de manera recursiva."""
    node = get_node(root, key)
    return node["value"] if node else None

def get_node(root, key):
    """Busca un nodo en el árbol binario de búsqueda (BST) y devuelve su valor.
    Esta función llama a la función get_node para buscar el nodo en el árbol de manera recursiva."""
    if root is None or "key" not in root:
        return None
    if key == root["key"]:
        return root["value"]
    elif key < root["key"]:
        return get_node(root["left"], key)
    else:
        return get_node(root["right"], key)

def remove(root, key):
    "elimina el nodo con la clave ``key`` del árbol"
    
    return remove_node(root, key)

def remove_node(root, key):
    "Elimina la pareja llave-valor que coincida con``key`` es usada por la función remove"
    if root is None:
        return None
    if key < root["key"]:
        root["left"] = remove_node(root["left"], key)
    elif key > root["key"]:
        root["righ"] = remove_node(root["right"], key)
    else:
        if root["left"] is None:
            return root["right"]
        if root["right"] is None:
            return root["left"]
        successor = get_min_node(root["right"])
        root["key"], root["value"] = successor["key"], successor["value"]
        root["right"] = delete_min_tree(root["right"])
    _update_size(root)
    return root

def contains(my_bst, key):
    """Devuelve True si el árbol de búsqueda contiene la llave ``key``, False en caso contrario."""
    return get(my_bst, key) is not None

def size(my_bst):
    """Retorna el número de entradas en la tabla de simbolos
    usa la función size_tree() para contar el número de elementos."""
    return my_bst["size"] if my_bst else 0

def size_tree(root):
    """Retornar el número de entradas en la a partir del nodo root
    Es usada en la función size()"""
    if root is None:
        return 0
    return 1 + size_tree(root['left']) + size_tree(root['right'])

def is_empty(my_bst):
    """Informa si la tabla de simbolos se encuentra vacia"""
    return my_bst['root'] is None

def key_set(my_bst):
    """Retorna una lista con todas las llaves de la tabla.
    Usa la función key_set_tree() para construir la lista de llaves"""
    keys = lt.newList('SINGLE_LINKED')  
    key_set_tree(my_bst['root'], keys)
    return keys

def value_set(my_bst):
    """
    Retorna una lista con todos los valores del árbol de búsqueda.

    Parameters:
    my_bst (dict): El árbol binario de búsqueda.

    Returns:
    linked_list: Lista enlazada con todos los valores del árbol.
    """
    values = lt.newList('SINGLE_LINKED')
    value_set_tree(my_bst['root'], values)
    return values

def keys_set_tree(root, keys):
    if root:
        keys_set_tree(root["left"], keys)
        keys.append(root["key"])
        keys_set_tree(root["right"], keys)

def get_min(my_bst):
    """"Retorna la llave mas pequeña de la tabla de simbolos
    Usa la función get_min_node() para encontrar la llave más a la izquierda"""
    if is_empty(my_bst):
        return None
    return get_min_node(my_bst)["key"]

def get_min_node(root):
    """Retorna la llave mas pequeña de la tabla de simbolos
    Es usada en la función get_min()"""
    min_node = get_min_node(my_bst['root'])
    if min_node is not None:
        return min_node['key']
    return None

def get_max(my_bst):
    """Retorna la llave mas grande de la tabla de simbolos
    usa la función get_max_node() para encontrar la llave más grande de del arbol"""
    if is_empty(my_bst):
        return None
    return get_max_node(my_bst)["key"]
def get_max_node(root):
    """"Retorna la llave mas grande de la tabla de simbolos
    Es usada en la función get_max() Usa la función get_max_node() para encontrar la llave más grande"""
    if root is None:
        return None
    while root['right'] is not None:
        root = root['right']
    return root

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
    node = floor_key(my_bst['root'], key)
    return node['key'] if node else None


def floor_key(root, key):
    """Retorna la llave que precede a la llave key en la tabla de simbolos.
    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave predecedente más cercana como si la llave key existiera en la tabla.
    Es usada en la función floor() Usa la función floor_key() para encontrar la llave predecesora a key"""
    if root is None:
        return None

    if key == root['key']:
        return root['key']
    elif key < root['key']:
        return floor_key(root['left'], key)
    else:
        temp = floor_key(root['right'], key)
        if temp is not None:
            return temp
        else:
            return root['key']


def ceiling(my_bst, key):
    """Retorna la llave que sucede a la llave key en la tabla de simbolos.
    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave sucesora más cercana como si la llave key existiera en la tabla. Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 7.
    Usa la función ceiling_key() para encontrar la llave sucesora a key"""
    return ceiling_key(my_bst["root"], key)

def ceiling_key(root, key):
    """Función auxiliar para ceiling"""
    if root is None:
        return None
    if key == root["key"]:
        return root["key"]
    if key > root["key"]:
        return ceiling_key(root["right"], key)
    temp = ceiling_key(root["left"], key)
    return temp if temp is not None else root["key"]

def select(my_bst, pos):
    """Retorna la siguiente llave a la k-esima llave de izquierda a derecha de la tabla de simbolos.
    Usa la función select_key() para encontrar la llave en la posición pos"""
    if pos < 1 or pos > size(my_bst):
        return None
    return select_key(my_bst, pos)["key"]

def select_key(root, pos):
    """Retorna la siguiente llave a la k-esima llave de izquierda a derecha de la tabla de simbolos.
    Es usada en la función select() Usa la función select_key() para encontrar la llave en la posición pos"""   
    left_size = size(root["left"])
    if pos < left_size:
        return select_key(root["left"], pos)
    elif pos > left_size:
        return select_key(root["right"], pos - left_size - 1)
    return root

def rank(my_bst, key):
    """Retorna el número de llaves en la tabla que son estrictamente predecesoras a key Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 3.
    Usa la función rank_keys() para encontrar el número de llaves predecesoras a keyo""" 
    return rank_keys(my_bst, key)

def rank_keys(root, key):
    """Retorna el número de llaves en la tabla que son estrictamente predecesoras a key Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 3.
    Es usada en la función rank() Usa la función rank_keys() para encontrar el número de llaves predecesoras a key""" 
    if root is None:
        return 0
    if key < root["key"]:
        return rank_keys(root["left"], key)
    elif key > root["key"]:
        return 1 + size(root["left"]) + rank_keys(root["right"], key)  
    return size(root["left"])

def height(root):
    "devuelve la altura del arbol usa la función heigth_tree"
    return heigth_tree(root)

def heigth_tree(root):
    """Retorna la altura del arbol de busqueda
    Es usada en la "función height()" Usa la función height_tree() para encontrar la altura del arbol"""
    if root is None:
        return -1
    return 1 + max(heigth_tree(root["left"]), heigth_tree(root["right"]))

def keys(my_bst, key_initial, key_final):
    """Retorna todas las llaves del arbol que se encuentren entre [key_initial, key_final].
    Usa la función keys_range() para encontrar las llaves en el rango especificado"""   
    list_key = []
    keys_range(my_bst, key_initial, key_final, list_key)
    return list_key

def keys_range(root, key_initial, key_final, list_key):   
    """Retorna todas las llaves del arbol que se encuentren entre [key_initial, key_final].
    Es usada en la función keys() Usa la función keys_range() para encontrar las llaves en el rango especificado"""
    if root is None:
        return  
    if key_initial < root["key"]:
        keys_range(root["left"], key_initial, key_final, list_key)
    if key_initial <= root["key"] <= key_final:
        sl.add_last(list_key, root["key"])
    if root["key"] < key_final:
        keys_range(root["right"], key_initial, key_final, list_key)

def keys(my_bst, key_initial, key_final):
    result_list = sl.new_list() 
    keys_range(my_bst["root"], key_initial, key_final, result_list)
    return result_list
def values(root):
    """Retorna todas los valores del arbol que se encuentren entre [key_initial, key_final]
    Usa la función values_range() para encontrar los valores en el rango especificado"""
    vals = []
    values_range(root, vals)
    return vals
def values_range(root, vals):
    """Función de comparación por defecto. Compara una llave con la llave de un elemento llave-valor."""
    if root:
        values_range(root["left"], vals)
        vals.append(root["value"])
        values_range(root["right"], vals)



