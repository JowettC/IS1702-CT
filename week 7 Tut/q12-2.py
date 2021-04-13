def depth(root):
  if root == None:
    return 0
  else:
    return max(dept(root.left), depth(root.right)) + 1