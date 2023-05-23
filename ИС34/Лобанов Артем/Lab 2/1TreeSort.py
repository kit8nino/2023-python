# сбалансированное дерево круче чем дерево потому что дерево не может перебрать 100000 чисел сидящих с одной стороны, 
# а сбалансированное может 😎

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None # место для слабаков
        self.right = None # место для крутых
        #так как задача перебрать столько данных, введем крутость узла, на которой надо балансировать
        #крутостью узла будем называть максимальное количество связей слева или справа до самого отдаленного вниз
        self.height = 1

# слияние бесконечно вечного
# фрактальное многообразие вселенской бескрайности
# бесконечно бесподобное и идентичное в тоже время
def insert(node, value, key=lambda x: x):
    if node == None:
        return Node(value)
    if key(value) < key(node.val):
        node.left = insert(node.left, value, key=key)
    else:
        node.right = insert(node.right, value, key=key)
    
    # крутость слева минус крутость справа
    left_height = get_height(node.left) if node.left != None else 0
    right_height = get_height(node.right) if node.right != None else 0
    balance_factor = left_height - right_height

    if balance_factor > 1 and key(value) < key(node.left.val):
        # слева больше - поднять лево
        return rotate_right(node)
    if balance_factor < -1 and key(value) > key(node.right.val):
        # справа больше - поднять право
        return rotate_left(node)

    # Левый правый поворот
    """
                       node
                     /
        node.left_child
                     \
                       new_node
    """
    if balance_factor > 1 and key(value) > key(node.left.val):
        node.left = rotate_left(node.left)
        """              node
                        /
                new_node      
               /                 
        node.left_child """
        return rotate_right(node)
    
    # Правый левый поворот
    """
             node
                 \
                node.right_child
                 /
         new_node
    """
    if balance_factor < -1 and key(value) < key(node.right.val):
        node.right = rotate_right(node.right)
        """ node
                \
                 new_node
                         \
                          node.right_child"""
        return rotate_left(node)
    
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    return node

def get_height(node):
    return node.height if node != None else 0

# Поворот
"""
           A God                        The God
            |                              |
      node(new_root)      Правый     new_root(node)
        /         \     -------->      /      \ 
  new_root(node)   A                  B     node(new_root)
     /   \              <--------               /  \ 
    B     C               (Левый)              C    A
"""
def rotate_right(node):
    if node == None or node.left == None:
        return node
    new_root = node.left
    node.left = new_root.right
    new_root.right = node

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    return new_root

def rotate_left(node):
    if node == None or node.right == None:
        return node
    new_root = node.right
    node.right = new_root.left
    new_root.left = node

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    return new_root

def recursion_traversal(root):
    return recursion_traversal(root.left) + [root.val] + recursion_traversal(root.right) if root!=None else []
def iterative_traversal(root):
    stack = []
    result = []
    current = root
    # Доведем до последней черты, вернемся назад, посмотрим в другую строну
    # Если там будет смерть - примем её как конец
    # Либо возвращаться уже некуда - безысходность - смерть
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result

def tree_sort(arr, key=lambda x: x):
    root = Node(arr[0])
    for i in range(1, len(arr)):
        # вернуть надо бы корень пересбалансированного деревца
        # аргументы это предыдущий корень и значение нового узла 
        root = insert(root, arr[i], key=key)
    # Теперь нужно превратить !сбалансированное! дерево в сортированный список
    # называется это обходом дерева в порядке возрастания
    res = iterative_traversal(root)
    # Также нужно побалываться поприкалываться
    return res if res==recursion_traversal(root) else "тайлер дерден?"


from generation import read_file

# Список целых чисел от 0 до 999999
arr = read_file('integers.txt',int)
sorted_arr = tree_sort(arr)
print(sorted_arr==arr,len(arr))

# Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
arr = read_file('floats.txt',float)
sorted_arr = tree_sort(arr)
print(sorted_arr==sorted(arr),len(arr))

# 42000 разных точки комплексной плоскости, лежащие в пределах окружности радиуса r = birth_day / birth_month
arr = read_file('points.txt',complex)
sorted_arr = tree_sort(arr, key=lambda x: abs(x))
print(sorted_arr==sorted(arr, key=lambda x: abs(x)),len(arr))

# Отрывок из книги не менее 10000 слов, разбитый в список по словам
from words import words
arr=words.split()
sorted_arr = tree_sort(arr)
print(sorted_arr==sorted(arr), len(arr))
