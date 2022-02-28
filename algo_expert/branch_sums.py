# This is the class of the input root. Do not edit it.
'''
https://stackoverflow.com/questions/60202046/python-calculating-branch-sum-of-binary-tree
'''
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def branchSums(root):
    # Write your code here.
        sums = []
        return branchHelper(root, sums)

    def branchHelper(root, sums = [], branchSum = 0):
        if root is None: 
            return

        if sums is None:
            sums = []
            
        branchSum += root.value

        if root.left is None and root.right is None:
            sums.append(branchSum)
            
        branchHelper(root.left, sums, branchSum)
        branchHelper(root.right, sums, branchSum)
        return sums