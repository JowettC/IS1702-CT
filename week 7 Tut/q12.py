
from TreeLab import *

b = BinaryTree()
b.setRoot(1)
b.root.setLeft(2)
b.root.setRight(3)
b.root.left.setLeft(4)
b.root.left.setRight(5)
b.root.right.setRight(6)
b.root.left.right.setLeft(7)
print(b.display())

c= BinaryTree()
c.setRoot(1)
c.root.setLeft(2)
c.root.setRight(3)
c.root.left.setLeft(4)
c.root.left.setRight(5)
c.root.right.setRight(6)
c.root.left.right.setLeft(7)
c.root.left.right.left.setRight(8)
# c = BinaryTree()
# c.setRoot(1)
# b.root.setLeft(2)
# b.root.setRight(3)
c.display()

def is_balanced(root):
    if root == None:
        return True
    lh = depth(root.left)
    rh = depth(root.right)
    if abs(lh - rh) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    else:
        return False
def depth(root):
  if root == None:
    return 0
  else:
    return max(dept(root.left), depth(root.right)) + 1

print(is_balanced(b))
print(is_balanced(c))