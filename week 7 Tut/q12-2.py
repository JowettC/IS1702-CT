# def is_balanced(root):
#     if 

def depth(root):
  if root == None:
    return 0
  else:
    return max(depth(root.left), depth(root.right)) + 1