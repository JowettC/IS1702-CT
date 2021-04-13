# O(n) solution for checking if tree is balanced
# the subtree is checked for balance when height is determined

# post order traversal. travel al lthe way down to leaf nodes and then go up.
# while going up, calcualte the left & right subtree height.
# if difference between them is >1, return -1
# else return max(left height, right height) + 1

# you won't actually calculate the height of the subtrees by calling the function. Instead
# you are storing the height at each level and when you go up one level, you add one to items

# see https://algorithms.tutorialhorizon.com/find-whether-if-a-given-binary-tree-is-balanced/

def is_balanced(root):
  if depth(root) == -1:
    return False
  else:
    return True

# returns either height or -1 (if unbalanced)
def depth(root):
  if root == None:  # base case
    return 0  # height is 0

  # check if left subtree is balanced
  lh = depth(root.left)
  if lh == -1:  # not balanced
    return -1  

  # check if right subtree is balanced
  rh = depth(root.right)
  if rh == -1:  # not balanced
    return -1  

  # check if current node is balanced
  if abs(lh - rh) > 1:
    return -1   # not balanced
  else:
    return max(lh, rh) + 1
    
    
    