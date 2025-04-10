from DataStructures.List import single_linked_list as sl

def new_map(cmpfunction=None):
    """Crea un nuevo árbol de búsqueda"""
    return {'root': None, 'size': 0, 'cmpfunction': cmpfunction}

def new_node(key, value=None):
    """Crea un nuevo nodo para el BST"""
    return {
        "key": key,
        "value": value,
        "left": None,
        "right": None,
        "size": 1
    }

def _update_size(node):
    """Actualiza el tamaño de un nodo"""
    if node is None:
        return
    left_size = node["left"]["size"] if node["left"] else 0
    right_size = node["right"]["size"] if node["right"] else 0
    node["size"] = 1 + left_size + right_size

def put(bst, key, value):
    """Agrega un nuevo nodo llave-valor al BST"""
    bst['root'] = _put(bst['root'], key, value, bst.get('cmpfunction'))
    bst['size'] = size(bst)
    return bst

def _put(node, key, value, cmpfunction):
    """Función auxiliar para put"""
    if node is None:
        return new_node(key, value)
    
    if cmpfunction:
        cmp = cmpfunction(key, node)
    else:
        cmp = -1 if key < node["key"] else 1 if key > node["key"] else 0
    
    if cmp < 0:
        node["left"] = _put(node["left"], key, value, cmpfunction)
    elif cmp > 0:
        node["right"] = _put(node["right"], key, value, cmpfunction)
    else:
        node["value"] = value
    
    _update_size(node)
    return node

def get(bst, key):
    """Obtiene el valor asociado a una llave"""
    node = _get(bst['root'], key, bst.get('cmpfunction'))
    return node["value"] if node else None

def _get(node, key, cmpfunction):
    """Función auxiliar para get"""
    if node is None:
        return None
    
    if cmpfunction:
        cmp = cmpfunction(key, node)
    else:
        cmp = -1 if key < node["key"] else 1 if key > node["key"] else 0
    
    if cmp < 0:
        return _get(node["left"], key, cmpfunction)
    elif cmp > 0:
        return _get(node["right"], key, cmpfunction)
    else:
        return node

def remove(bst, key):
    """Elimina un nodo del BST"""
    if bst['root'] is not None:
        bst['root'] = _remove(bst['root'], key, bst.get('cmpfunction'))
        bst['size'] = size(bst)
    return bst

def _remove(node, key, cmpfunction):
    """Función auxiliar para remove"""
    if node is None:
        return None
    
    if cmpfunction:
        cmp = cmpfunction(key, node)
    else:
        cmp = -1 if key < node["key"] else 1 if key > node["key"] else 0
    
    if cmp < 0:
        node["left"] = _remove(node["left"], key, cmpfunction)
    elif cmp > 0:
        node["right"] = _remove(node["right"], key, cmpfunction)
    else:
        if node["left"] is None:
            return node["right"]
        if node["right"] is None:
            return node["left"]
        
        temp = _get_min_node(node["right"])
        node["key"], node["value"] = temp["key"], temp["value"]
        node["right"] = _delete_min(node["right"])
    
    _update_size(node)
    return node

def contains(bst, key):
    """Verifica si una llave existe en el BST"""
    return _get(bst['root'], key, bst.get('cmpfunction')) is not None

def size(bst):
    """Retorna el número de elementos en el BST"""
    return bst['size']

def is_empty(bst):
    """Verifica si el BST está vacío"""
    return bst['root'] is None

def key_set(bst):
    """Retorna todas las llaves en orden"""
    keys = sl.newList('SINGLE_LINKED')
    _in_order(bst['root'], keys, 'key')
    return keys

def value_set(bst):
    """Retorna todos los valores en orden"""
    values = sl.newList('SINGLE_LINKED')  # Usar la lista enlazada
    _in_order(bst['root'], values, 'value')
    return values

def _in_order(node, result_list, attr):
    """Recorrido in-order"""
    if node is not None:
        _in_order(node["left"], result_list, attr)
        sl.addLast(result_list, node[attr])
        _in_order(node["right"], result_list, attr)

def get_min(bst):
    """Obtiene la llave mínima"""
    if is_empty(bst):
        return None
    return _get_min_node(bst['root'])["key"]

def _get_min_node(node):
    """Función auxiliar para get_min"""
    while node["left"] is not None:
        node = node["left"]
    return node

def get_max(bst):
    """Obtiene la llave máxima"""
    if is_empty(bst):
        return None
    return _get_max_node(bst['root'])["key"]

def _get_max_node(node):
    """Función auxiliar para get_max"""
    while node["right"] is not None:
        node = node["right"]
    return node

def delete_min(bst):
    """Elimina el nodo con la llave mínima"""
    if bst['root'] is not None:
        bst['root'] = _delete_min(bst['root'])
        bst['size'] = size(bst)
    return bst

def _delete_min(node):
    """Función auxiliar para delete_min"""
    if node["left"] is None:
        return node["right"]
    node["left"] = _delete_min(node["left"])
    _update_size(node)
    return node

def delete_max(bst):
    """Elimina el nodo con la llave máxima"""
    if bst['root'] is not None:
        bst['root'] = _delete_max(bst['root'])
        bst['size'] = size(bst)
    return bst

def _delete_max(node):
    """Función auxiliar para delete_max"""
    if node["right"] is None:
        return node["left"]
    node["right"] = _delete_max(node["right"])
    _update_size(node)
    return node

def floor(bst, key):
    """Encuentra el floor de una llave"""
    node = _floor(bst['root'], key, bst.get('cmpfunction'))
    return node["key"] if node else None

def _floor(node, key, cmpfunction):
    """Función auxiliar para floor"""
    if node is None:
        return None
    
    if cmpfunction:
        cmp = cmpfunction(key, node)
    else:
        cmp = -1 if key < node["key"] else 1 if key > node["key"] else 0
    
    if cmp == 0:
        return node
    if cmp < 0:
        return _floor(node["left"], key, cmpfunction)
    
    temp = _floor(node["right"], key, cmpfunction)
    return temp if temp is not None else node

def ceiling(bst, key):
    """Encuentra el ceiling de una llave"""
    node = _ceiling(bst['root'], key, bst.get('cmpfunction'))
    return node["key"] if node else None

def _ceiling(node, key, cmpfunction):
    """Función auxiliar para ceiling"""
    if node is None:
        return None
    
    if cmpfunction:
        cmp = cmpfunction(key, node)
    else:
        cmp = -1 if key < node["key"] else 1 if key > node["key"] else 0
    
    if cmp == 0:
        return node
    if cmp > 0:
        return _ceiling(node["right"], key, cmpfunction)
    
    temp = _ceiling(node["left"], key, cmpfunction)
    return temp if temp is not None else node

def select(bst, k):
    """Selecciona la llave en la posición k (0-indexed)"""
    if k < 0 or k >= size(bst):
        return None
    return _select(bst['root'], k)["key"]

def _select(node, k):
    """Función auxiliar para select"""
    if node is None:
        return None
    
    left_size = node["left"]["size"] if node["left"] else 0
    if k < left_size:
        return _select(node["left"], k)
    elif k > left_size:
        return _select(node["right"], k - left_size - 1)
    else:
        return node

def rank(bst, key):
    """Calcula el rank de una llave"""
    return _rank(bst['root'], key, bst.get('cmpfunction'))

def _rank(node, key, cmpfunction):
    """Función auxiliar para rank"""
    if node is None:
        return 0
    
    if cmpfunction:
        cmp = cmpfunction(key, node)
    else:
        cmp = -1 if key < node["key"] else 1 if key > node["key"] else 0
    
    if cmp < 0:
        return _rank(node["left"], key, cmpfunction)
    elif cmp > 0:
        return 1 + (node["left"]["size"] if node["left"] else 0) + _rank(node["right"], key, cmpfunction)
    else:
        return node["left"]["size"] if node["left"] else 0

def height(bst):
    """Calcula la altura del BST"""
    return _height(bst['root'])

def _height(node):
    """Función auxiliar para height"""
    if node is None:
        return 0  # Cambiado de -1 a 0
    return 1 + max(_height(node["left"]), _height(node["right"]))

def keys(bst, lo, hi):
    """Obtiene llaves en un rango"""
    result = sl.newList('SINGLE_LINKED')
    _keys(bst['root'], result, lo, hi, bst.get('cmpfunction'))
    return result

def _keys(node, result_list, lo, hi, cmpfunction):
    """Función auxiliar para keys"""
    if node is None:
        return
    
    if cmpfunction:
        cmp_lo = cmpfunction(lo, node)
        cmp_hi = cmpfunction(hi, node)
    else:
        cmp_lo = -1 if lo < node["key"] else 1 if lo > node["key"] else 0
        cmp_hi = -1 if hi < node["key"] else 1 if hi > node["key"] else 0
    
    if cmp_lo < 0:
        _keys(node["left"], result_list, lo, hi, cmpfunction)
    if cmp_lo <= 0 <= cmp_hi:
        sl.addLast(result_list, node["key"])
    if cmp_hi > 0:
        _keys(node["right"], result_list, lo, hi, cmpfunction)

def values(bst, lo=None, hi=None):
    """Obtiene valores en un rango"""
    result = sl.newList('SINGLE_LINKED')
    if lo is None and hi is None:
        _in_order(bst['root'], result, 'value')
    else:
        _keys(bst['root'], result, lo, hi, bst.get('cmpfunction'), attr='value')
    return result


def default_compare(key, node):
    """Función de comparación por defecto"""
    if key < node["key"]:
        return -1
    elif key > node["key"]:
        return 1
    return 0

def _in_order_list(node, result_list, attr):
    if node is not None:
        _in_order_list(node["left"], result_list, attr)
        result_list.append(node[attr])
        _in_order_list(node["right"], result_list, attr)