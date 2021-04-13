import threading
from LinearDSLab import Queue
from time import sleep

class BinaryTree:
    def __init__(self):
        self.root = None
        self.queue = Queue()
    
    def setRoot(self, node):
        if not isinstance(node, Node):
            node = Node(node)
        self.root = node

    def root(self):
        return self.root 
        
    def countHeight(self, node):
        if node == None:
            return 0
        if node.isLeaf():
            return 1
        return 1 + max(self.countHeight(node.left), self.countHeight(node.right))      

    def heightOfTree(self):
        if self.root == None:
            return 0
        return self.countHeight(self.root)

    def countNode(self, node):
        if node == None:
            return 0
        if node.isLeaf():
            return 1
        return 1 + self.countNode(node.left) + self.countNode(node.right)

    def noOfNodes(self):
        if self.root == None:
            return 0
        return self.countNode(self.root)

    def isEmpty(self):
        return self.root == None
    
    def display(self):
        self.root.display()
        
    def __str__(self):
        if self.root == None:
            return None
        return str(self.root)

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def setLeft(self, leftChild):
        """
        Set the left child of this node
        """
        if not isinstance(leftChild, Node):
            leftChild = Node(leftChild)
        self.left = leftChild

    def setRight(self, rightChild):
        """
        Set the right child of this node
        """
        if not isinstance(rightChild, Node):
            rightChild = Node(rightChild)
        self.right = rightChild

    def delLeft(self):
        """
        Remove the left child of this node
        """
        self.left = None

    def delRight(self):
        """
        Remove the right child of this node
        """
        self.right = None

    def isLeaf(self):
        """
        Return True if this node is a leaf node. False otherwise.
        """
        return self.left == None and self.right == None
        
    def __repr__(self):    
        s = "Value: " + str(self.value)
        if self.left != None:
            s += ", left child: " + str(self.left.value)
        else:
            s += ", left child: None"
        if self.right != None:
            s += ", right child: "+ str(self.right.value)
        else:
            s += ", right child: None"
        return s

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class BinarySearchTree(BinaryTree):
    def __init__(self):
        BinaryTree.__init__(self)
    
    def isStable(self):
        """
        Returns True if this tree is stable. False otherwise.
        """
        self.stableChecker = []
        self.__inOrderCheck(self.root)
        for i in range(1, len(self.stableChecker)):
            if self.stableChecker[i] < self.stableChecker[i-1]:
                return False
        return True

    def search(self, key):
        """
        Starts an animation to show how a BinarySearchTree search is implemented
        """
        if not self.isStable():
            raise Error("Warning! Binary Search tree is not sorted correctly.") 
        q = Queue()
        visited = []
        n = _bstsearch(self.root, key, visited, q)
        return (n, visited)
        #print(searchbst(self.root, key))

    def insert(self, key):
        """
        Inserts a a node into this tree
        """
        if not self.isStable():
            print("Warning! Binary Search tree is not sorted correctly.") 
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
            return
        node = insertbst(self.root, key)
        return node
        
    def minValueNode(self, node):
        current = node
    
        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left
    
        return current
 
    # Given a binary search tree and a key, this function
    # delete the key and returns the new root
    def _remove(self, node, key):
        # Base Case
        if node is None:
            return node
    
        # If the key to be deleted is smaller than the node's
        # key then it lies in the left subtree
        if key < node.value:
            node.left = self._remove(node.left, key)
    
        # If the kye to be delete is greater than the node's key
        # then it lies in right subtree
        elif (key > node.value):
            node.right = self._remove(node.right, key)
    
        # If key is same as node's key, then this is the node
        # to be deleted
        else:
            # Node with only one child or no child
            if node.left is None:
                temp = node.right
                node = None
                return temp
    
            elif node.right is None:
                temp = node.left
                node = None
                return temp
    
            # Node with two children: 
            # Get the inorder successor (smallest in the right subtree)
            temp = self.minValueNode(node.right)
    
            # Copy the inorder successor's content to this node
            node.value = temp.value
    
            # Delete the inorder successor
            node.right = self._remove(node.right, temp.value)
        
        return node

    def remove(self, key):
        self._remove(self.root, key)        
        return self.root

    def __inOrderCheck(self, root):
        if root != None:
            self.__inOrderCheck(root.left)
            self.stableChecker.append(root.value)
            self.__inOrderCheck(root.right)
            
def insertbst(root, key):
    """
    Insert a node with value key into a tree with root root
    """
    if root.value == key.value:
        return root
    elif root.value > key.value:
        if root.left != None:
            return insertbst(root.left, key)
        else:
            root.setLeft(key)
            return key
    else:
        if root.right != None:
            return insertbst(root.right, key)
        else:
            root.setRight(key)
            return key
           
def searchbst(root, key):
    if root.value == key:
        return root
    elif root.left != None and root.value > key:
        return searchbst(root.left, key)
    elif root.right != None and root.value < key:
        return searchbst(root.right, key)
    else:
        return None
           
def _preorder_traverse(node, visited, q = None):
    if node != None:
        visit(node, visited, q)
        _preorder_traverse(node.left, visited, q)
        _preorder_traverse(node.right, visited, q)

def preorder_traverse(node):
    """
    Display an animation of preorder traversal of a tree with root node
    """
    q = Queue()
    tree = BinaryTree()
    tree.setRoot(node)
    visited = []
    _preorder_traverse(node, visited, q)
    return visited
        
def _postorder_traverse(node, visited, q = None):
    if node != None:
        _postorder_traverse(node.left, visited, q)
        _postorder_traverse(node.right, visited, q)
        visit(node, visited, q)
        
def postorder_traverse(node):
    """
    Display an animation of postorder traversal of a tree with root node
    """
    q = Queue()
    tree = BinaryTree()
    tree.setRoot(node)
    visited = []
    _postorder_traverse(node, visited, q)
    return visited
        
def _inorder_traverse(node, visited, q = None):
    if node != None:
        _inorder_traverse(node.left, visited, q)
        visit(node, visited, q)
        _inorder_traverse(node.right, visited, q)
        
def inorder_traverse(node):
    """
    Display an animation of inorder traversal of a tree with root node
    """
    q = Queue()
    tree = BinaryTree()
    tree.setRoot(node)
    visited = []
    _inorder_traverse(node, visited, q)
    return visited
        
def _bstsearch(node, val, visited, q):
    if node != None:
        visit(node, visited, q)
        if val == node.value:
            return node
        elif val < node.value:
            return _bstsearch(node.left, val, visited, q)
        else:
            return _bstsearch(node.right, val, visited, q)
        
def visit(node, visited, q):
    visited.append(node.value)
    if q != None:
        q.enqueue(node.value)

    
class TreeUpdater(threading.Thread):
    def __init__(self, tree, q):
        threading.Thread.__init__(self)
        self.daemon = True
        self.tree = tree
        self.q = q
    
    def run(self):
        while True:
            if self.q.empty():
                sleep(1)
                self.q.enqueue(self.tree)
                #print('updated!')
            
