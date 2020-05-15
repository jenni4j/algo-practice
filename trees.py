#Binary Tree Implementation

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if self.preorder_search(self.root, find_val):
            return True
        else: 
            return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        ret = self.preorder_print(self.root, [])
        strBuilder = ""
        for idx, val in enumerate(ret):
            if idx == len(ret)-1: 
                strBuilder = strBuilder + str(val)
            else: 
                strBuilder = strBuilder + str(val) + "-"
                
        
        return strBuilder
        

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start == None:
            return False
        elif start.value == find_val:
            return True
        else:
            return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        
        if start == None:
            return traversal
        else:
            traversal.append(start.value)
            self.preorder_print(start.left, traversal)
            self.preorder_print(start.right, traversal)
            return traversal
        
        
        # if start == None:
        #     return traversal
        # else: 
        #     traversal = traversal + str(start.value) + "-"
        #     traversal = self.preorder_print(start.left, traversal)
        #     traversal = self.preorder_print(start.right, traversal)
        #     return traversal

# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()



#BST Implementation

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_node(self.root, new_val)
    
    def insert_node(self, root, new_val):
        if root is None:
            root = Node(new_val)
        elif new_val > root.value:
            root.right = self.insert_node(root.right, new_val)
        elif new_val < root.value:
           root.left = self.insert_node(root.left, new_val)
        return root

    def search(self, find_val):
        return self.bst(self.root, find_val)
    
    def bst(self, node, val):
        if node is None:
            return False
        if node.value == val:
            return True
        if val > node.value:
            return self.bst(node.right, val)
        else:
            return self.bst(node.left, val)
        
    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        ret = self.preorder_print(self.root, [])
        strBuilder = ""
        for idx, val in enumerate(ret):
            if idx == len(ret)-1: 
                strBuilder = strBuilder + str(val)
            else: 
                strBuilder = strBuilder + str(val) + "-"
                
        
        return strBuilder
        
    def preorder_print(self, start, traversal):        
        if start == None:
            return traversal
        else:
            traversal.append(start.value)
            self.preorder_print(start.left, traversal)
            self.preorder_print(start.right, traversal)
            return traversal
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print tree.print_tree()

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)