def nodeDepths(root):
    final = [0]
	helper(root,0,final)
	return final[0]

def helper(node, d, final):
	if not node:
		return
	print(final[0])
	final[0]+=d
	print('here',final[0])
	helper(node.left,d+1,final)
	helper(node.right,d+1, final)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
