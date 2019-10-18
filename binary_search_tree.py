

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

    def search(self, desired_key):
        """
        searches for the desired_key in the BST
        :param desired_key: item to be found
        :return: the item if found, else None
        """
        current_node = self.root

        while current_node is not None:
            # return the node if the key matches
            if current_node.key == desired_key:
                return current_node

            # navigate to the left if the search key is
            # less than the node's key
            elif desired_key < current_node.key:
                current_node = current_node.left

            # navigate to the right if the search key is
            # greater than the node's key
            else:
                current_node = current_node.right

        # the key was not found in the tree
        return None

if __name__ == '__main__':
