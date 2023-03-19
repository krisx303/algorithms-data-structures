from turtle import right


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.parent = None
    
    def __str__(self) -> str:
        return f"{self.val} -> [{self.left}, {self.right}]"

"""Wstawianie obiektu do drzewa BST"""

def insert(root: Node, val: int) -> Node:
    if root is None:
        node = Node(val)
        node.parent = node
        return node
    
    prev = None
    dest = root
    while dest is not None:
        prev = dest
        if val > dest.val:
            dest = dest.right
        elif val < dest.val:
            dest = dest.left
        else:
            return root
    if val > prev.val:
        prev.right = Node(val)
        prev.right.parent = prev
    else:
        prev.left = Node(val)
        prev.left.parent = prev
    return root

"""Wyszukiwanie najmniejszego elementu w drzewie"""

def min(root):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root

"""
Zwraca 'następnika' wskazanego obiektu.
Następnik to chyba najmniejsza liczba większa od wskazanej.
"""

def nastepnik(curr: Node):
    if curr.right is not None:
        return min(curr.right)
    while curr.parent.right == curr:
        curr = curr.parent
    return curr

def findNode(root: Node, val: int) -> Node:
    node = root
    while node is not None:
        if node.val == val:
            return node
        
        if node.val > val:
            node = node.left
        else:
            node = node.right
        
    return node

def delete(root: Node, val: int) -> Node:

    toDelete = findNode(root, val)

    if toDelete is None:
        return root

    children = (toDelete.left is not None) + (toDelete.right is not None)
    if children == 0:
        if toDelete == root:
            return None
        else:
            if toDelete.parent.left == toDelete:
                toDelete.parent.left = None
            else:
                toDelete.parent.right = None
    elif children == 1:
        ch = None
        if node.left is not None:
            ch = node.left
        else:
            ch = node.right
        
        if root == node:
            root = node
        else:
            if node == node.parent.left:
                node.parent.left = ch
            else:
                node.parent.right = ch
    else:
        val = min(node.right).val
        delete(node, val)
        node.val = val
    
    return root
    

    



node = Node(15)

for x in [10, 20, 8, 12, 16]:
    node = insert(node, x)

print(node)

print(delete(node, 10))