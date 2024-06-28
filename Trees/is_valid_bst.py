class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_valid_bst(root):
    if root is None:
        return True

    if root.left is not None and root.left.value >= root.value:
        return False

    if root.right is not None and root.right.value <= root.value:
        return False

    return is_valid_bst(root.left) and is_valid_bst(root.right)


# Example usage:

root = Node(5)
root.left = Node(3)
root.left.left = Node(4)
root.right = Node(7)

print(is_valid_bst(root))