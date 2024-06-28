class Node(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.val == data:
            return False
        
        elif data < self.val:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True
    
    def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')
    
class BST(object):
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    
    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()
    
    