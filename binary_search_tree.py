

class Node:
    """
    basic element of a BST
    """
    def __init__(self, key):
        """
        initializes a Node
        :param key: data in the node
        """
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None