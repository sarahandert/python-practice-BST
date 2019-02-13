"""Name: Sarah Andert
    Course: CMPS 1500
    Date: 11/29/2018
    A program that writes a recursive function that takes as input a root node of a binary search tree and returns its height

"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




def getheight(T):
    if T != None:
        count = 0
        if T.right != None or T.left != None:
            count += 1
            getheight(T.right)
            getheight(T.left)
        return count
        
T = TreeNode(4)
T.left = TreeNode(2)
T.right = TreeNode(5)
T.left.left = TreeNode(1)
T.right.right = TreeNode(3)

print(getheight(T))
