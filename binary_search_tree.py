

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
    def __init__(self, root=None):
        self.root = root

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

    def insert(self, node):
        """
        inserts a new node into the BST
        :param node: node to be inserted
        :return: None
        """
        # check if the tree is empty
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if node.key < current_node.key:
                    # if there is no left child, add the new node here;
                    # otherwise, repeat from the left child
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    # if there is no right child, add the new node here;
                    # otherwise repeat from the right child
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right

if __name__ == '__main__':
    tree = BinarySearchTree()
    node_a = Node(17)
    node_b = Node(32)
    node_c = Node(10)
    node_d = Node(3)
    node_e = Node(21)

    tree.insert(node_a)
    tree.insert(node_b)
    tree.insert(node_c)
    tree.insert(node_d)
    tree.insert(node_e)

    # search for key 3
    found_node = tree.search(3)
    if found_node is not None:
        print(f'Found node with key = {found_node.key}.')
    else:
        print('Key 3 not found.')

    # search for key 99
    found_node = tree.search(99)
    if found_node is not None:
        print(f'Found node with key = {found_node.key}.')
    else:
        print('Key 99 not found.')