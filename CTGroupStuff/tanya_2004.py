# algo to check binary search tree
def bittree(root):
    if root == None:
        return True
    if root.left > root:
        return False
    if root.right < root:
        return False
    # if bittree(root.left) and bittree(root.right):
    #     return True
    # else:
    #     return False
    return (bittree(root.left) and bittree(root.right))
# print(False * True)

print((False and True))