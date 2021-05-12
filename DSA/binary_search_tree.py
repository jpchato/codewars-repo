'''
We don't want any duplicate values in a BST
'''
class Node:
    def __init__(self, data= None):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
    
    def inset(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
               self._insert(data, cur_node.left) 
        elif data > cur_node:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print('Value is already present in tree')
        