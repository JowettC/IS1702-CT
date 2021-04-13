from TreeLab import *

b = BinaryTree()
b.setRoot(1)
b.root.setLeft(2)
b.root.setRight(3)
b.root.left.setLeft(4)
b.root.left.setRight(5)

print(b.display())

def mirrorTree(root):
    if root != None:
        temp = root.left
        root.setLeft(root.right)
        root.setRight(temp)
        mirrorTree(root.left)
        mirrorTree(root.right)
    else:
        return
print(b.root.left.left.left)
# mirrorTree(b.root)
# print(b.display())
