# naive solution for checking if tree is balanced
# For each node of the tree, get the height (depth) of left subtree and right subtree and check the difference , if it is greater than 1, return False.
# complexity of depth() is O(n) where n is the no. of nodes in the tree passed in
# worst case will be when tree is complete
# overall complexity is O(n log n). 

def is_balanced(root):
  if root == None:  # base case
    return True

  lh = depth(root.left)    # left height
  rh = depth(root.right)   # right height

  if abs(lh - rh) <= 1 and 
     is_balanced(root.left) and
     is_balanced(root.right):
    return True
  else:
    return False

# O(n), once for each node in this subtree
def depth(root):
  if root == None:
    return 0
  else:
    return max(dept(root.left), depth(root.right)) + 1

# see https://www.afternerd.com/blog/python-check-tree-balanced/
