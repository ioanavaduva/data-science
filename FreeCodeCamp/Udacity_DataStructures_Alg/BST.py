class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.insert_aux(self.root, new_val)

    def search(self, find_val):
        return self.preorder_search(self.root, find_val)
        
    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start == None:
            return False
        if start.value == find_val:
            return True
        else:
            if start.value > find_val:
                return self.preorder_search(start.left, find_val)
            else:
                return self.preorder_search(start.right, find_val)
                
    def insert_aux(self, start, new_val):
        if start == None:
            return Node(new_val)
        if start.value > new_val:
            start.left = self.insert_aux(start.left, new_val)
        else:
            start.right = self.insert_aux(start.right, new_val)
        return start
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))