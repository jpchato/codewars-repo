class Node:
    def __init__(self, val):
        self.val = val
        self.next = None # the pointer initially points to nothing

node1 = Node(12)
node2 = Node(99)
node3 = Node(37)

node1.next = node2 # 12 -> 99
node2.next = node3 # 99 -> 37

# The entire linked list now looks like: 12 -> 99 -> 37

print(node1)