class Node(object):
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data
    
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end='')
        if self.right:
            self.right.inorder()
    
    def preorder(self):
        print(self.data, end='')
        if self.left:
            self.left.inorder()
        if self.right:
            self.right.inorder()
    
    def postorder(self):
        if self.left:
            self.left.inorder()
        if self.right:
            self.right.inorder()
        print(self.data, end='')
            
            
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.inorder()
print()
root.preorder()
print()
root.postorder()
    

# Trees can be traversed in different ways. Following are the generally used ways for traversing trees.

# Inorder (left, data, right)
# Preorder (data, left, right)
# Postorder (left, right, data)