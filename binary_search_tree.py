

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

    def remove(self, key):
        """
        removes a node with a given key (if it is in the BST)
        :param key: key of Node to be removed
        :return: None
        """
        parent = None
        current_node = self.root

        # search for the node
        while current_node is not None:

            # check if current_node has a matching key
            if current_node.key == key:
                # case 1
                if current_node.left is None and current_node.right is None:
                    if parent is None: # Node is root
                        self.root = None
                    elif parent.left is current_node:
                        parent.left = None
                    else:
                        parent.right = None
                    return # Node found and removed
                # case 2a
                elif current_node.left is not None and current_node.right is None:
                    if parent is None: # Node is root
                        self.root = current_node.left
                    elif parent.left is current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return # Node found and removed
                # case 2b
                elif current_node.left is none and current_node.right is not None:
                    if parent is None: # Node is root
                        self.root = current_node.right
                    elif parent.left is current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    return # Node found and removed
                # case 3
                else:
                    # find successor (leftmost child of right subtree)
                    successor = current_node.right
                    while successor.left is not None:
                        successor = successor.left
                    # copy successor to current node
                    current_node.key = successor.key
                    parent = current_node
                    # remove successor from right subtree
                    current_node = current_node.right
                    # loop continues with new key
                    key = parent.key
            elif current_node.key < key: # search right
                parent = current_node
                current_node = current_node.right
            else: # search left
                parent = current_node
                current_node = current_node.left

        # the node to be removed was not found
        return

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

    # test remove method
    tree.remove(3)
    found_node = tree.search(3)
    if found_node is not None:
        print(f'Found node with key = {found_node.key}.')
    else:
        print('Key 3 not found.')