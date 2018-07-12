from termcolor import colored


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
        print('Parent {} is {}'.format(current_node.key, current_node.parent.key))

    def insert(self, key):
        node = Node(key)
        # Base Case - Nothing in the tree
        if self.root is None:
            node.red = False
            self.root = node
            print('ROOT IS - {}'.format(self.root.key))
            return
        last_node = self.root
        while last_node is not None:
            potential_parent = last_node
            if node.key < last_node.key:
                last_node = last_node.left
            else:
                last_node = last_node.right
        # Assign parents and siblings to the new node
        node.parent = potential_parent
        print('NODE KEY- {} NODE PARENT - {} '.format(node.key, node.parent.key))
        if node.key < node.parent.key:
            node.parent.left = node
            print('GO LEFT < NODE PARENT PARENT LEFT KEY - ', node.parent.key)
        else:
            node.parent.right = node
            print('GO RIGHT > NODE PARENT PARENT RIGHT KEY - ', node.parent.key)
        node.left = None
        node.right = None
        self.fix_tree(node)

    def fix_tree(self, node):
        print('NODE PARENT RED - {}'.format(node.parent.red))
        try:
            while node.parent.red is True and node is not self.root:
                print('FIX>> NODE KEY - {} NODE PARENT KEY - {} '.format(node.key, node.parent.key))
                if node.parent == node.parent.parent.left:
                    uncle = node.parent.parent.right
                    print('[LEFT] UNCLE RED - {} UNCLE KEY - {}'.format(uncle.red, uncle.key))
                    if uncle.red:
                        '''  
                        This is Case #1. Insert new node, where parent and uncle is red -> is wrong
                        We make recolor parent, uncle to black 
                        '''
                        node.parent.red = False
                        uncle.red = False
                        node.parent.parent.red = True
                        print('NODE RED - {} UNCLE RED - {} PARENT RED - {}'
                              .format(colored(node.red, 'red', attrs=['reverse', 'blink']),
                                      colored(uncle.red, 'yellow', attrs=['reverse', 'blink']),
                                      colored(node.red, 'yellow', attrs=['reverse', 'blink'])))
                        break
                else:
                    try:
                        uncle = node.parent.parent.left
                        print('[RIGHT] UNCLE RED - {} UNCLE KEY - {}'.format(uncle.red, uncle.key))
                        if uncle.red:
                            #  Case 1
                            node.parent.red = False
                            uncle.red = False
                            node.parent.parent.red = True
                            print('NODE RED - {} UNCLE RED - {} PARENT RED - {}'
                                  .format(colored(node.red, 'red', attrs=['reverse', 'blink']),
                                          colored(uncle.red, 'yellow', attrs=['reverse', 'blink']),
                                          colored(node.parent.red, 'yellow', attrs=['reverse', 'blink'])))

                    except AttributeError:
                        print("DOES NOT GAVE UNCLE")
                        break

        except AttributeError:
            print("\n\nTree BUILT")
