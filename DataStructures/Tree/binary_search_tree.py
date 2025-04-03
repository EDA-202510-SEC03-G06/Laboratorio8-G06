def new_map():
    """Crea un nuevo árbol de búsqueda"""
    
    pass
def put(root, key):
    """Agrega un nuevo nodo llave-valor a un árbol binario de búsqueda (BST). 
    Si la llave ya existe, se actualiza el value del nodo."""
    
    pass

def insert_node(root, key):
    """Inserta un nuevo nodo llave-valor en el árbol binario de búsqueda (BST) de manera recursiva.
    Esta función es llamada por la función put"""
    
    pass

def get(root, key):
    """Busca un nodo en el árbol binario de búsqueda (BST) y devuelve su valor.
    Esta función llama a la función get_node para buscar el nodo en el árbol de manera recursiva."""
    
    pass

def remove(root, key):
    "elimina el nodo con la clave ``key`` del árbol"
    
    pass

def remove_node(root, key):
    "Elimina la pareja llave-valor que coincida con``key`` es usada por la función remove"
    
    pass

def contains(root, key):
    """Devuelve True si el árbol de búsqueda contiene la llave ``key``, False en caso contrario."""
    
    pass

def size(root):
    """Retorna el número de entradas en la tabla de simbolos
    usa la función size_tree() para contar el número de elementos."""
    
    pass    

def size_tree(root):
    """Retornar el número de entradas en la a partir del nodo root
    Es usada en la función size()"""
    
    pass       

def is_empty(my_bst):
    """Informa si la tabla de simbolos se encuentra vacia"""
    
    pass

def key_set(my_bst):
    """Retorna una lista con todas las llaves de la tabla.
    Usa la función key_set_tree() para construir la lista de llaves"""
    
    pass

def get_min(my_bst):
    """"Retorna la llave mas pequeña de la tabla de simbolos
    Usa la función get_min_node() para encontrar la llave más a la izquierda"""
    pass

def get_min_node(root):
    """Retorna la llave mas pequeña de la tabla de simbolos
    Es usada en la función get_min()"""
    
    pass

def get_max(my_bst):
    """Retorna la llave mas grande de la tabla de simbolos
    usa la función get_max_node() para encontrar la llave más grande de del arbol"""
    
    pass
def get_max_node(root):
    """"Retorna la llave mas grande de la tabla de simbolos
    Es usada en la función get_max() Usa la función get_max_node() para encontrar la llave más grande"""
    
    pass

def delete_min(my_bst):
    """Encuentra y remueve la llave mas pequeña de la tabla de simbolos y su valor asociado.
    Usa la función delete_min_tree() para eliminar la llave más pequeña"""
    
    pass

def delete_min_tree(root):
    """Encuentra y remueve la llave mas pequeña de la tabla de simbolos y su valor asociado
    Es usada en la función delete_min() Usa la función delete_min_tree() para eliminar la llave más pequeña"""
    
    pass

def delete_max(my_bst):
    """Encuentra y remueve la llave mas grande de la tabla de simbolos y su valor asociado.
    Usa la función delete_max_tree() para eliminar la llave más grande"""
    
    pass

def delete_max_tree(root):
    """Encuentra y remueve la llave mas grande de la tabla de simbolos y su valor asociado
    Es usada en la función delete_max() Usa la función delete_max_tree() para eliminar la llave más grande"""   
    
    pass


def key_set_tree(root):
    """Devuelve una lista con todas las llaves de la tabla de simbolos.
    Es usada en la función key_set()"""
    
    pass
def values(root):
    """Retorna todas los valores del arbol que se encuentren entre [key_initial, key_final]
    Usa la función values_range() para encontrar los valores en el rango especificado"""

    pass

def values_range(root, key_initial, key_final):
    """Función de comparación por defecto. Compara una llave con la llave de un elemento llave-valor."""
    
    pass

def height(root):
    "devuelve la altura del arbol usa la función heigth_tree"
    
    pass

def heigth_tree(root):
    """Retorna la altura del arbol de busqueda
    Es usada en la "función height()" Usa la función height_tree() para encontrar la altura del arbol"""
    
    pass


