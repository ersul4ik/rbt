class Node:
    def __init__(self, key):
        self.key = key
        self.red = True
        self.left = None
        self.right = None
        self.parent = None


class RBTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        current_node = self.root
        while current_node is not None and key != current_node.key:
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        print('Parent your key -', current_node.parent.key)

    def insert(self, key):
        node = Node(key)
        # Base Case - Nothing in the tree
        if self.root is None:
            node.red = False
            self.root = node
            print('first')
            return
        last_node = self.root
        while last_node is not None:
            print('not empty', last_node.key)
            potential_parent = last_node
            print('nod key - {} last_node - {}'.format(node.key, last_node.key) )
            if node.key < last_node.key:
                last_node = last_node.left
            else:
                last_node = last_node.right
        # Assign parents and siblings to the new node
        node.parent = potential_parent
        print('node parent', node.parent.key)
        if node.key < node.parent.key:
            node.parent.left = node
            print('node left ____-', node.parent.left.key)
        else:
            node.parent.right = node
            print('node right ____-', node.parent.right.key)
        node.left = None
        node.right = None
        print(node.parent.key)

