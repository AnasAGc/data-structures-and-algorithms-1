class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        try:
            output = ''
            if not self.root:
                return output
            def _traverse(node):
                nonlocal output
                output = output + str(node.value)
                if node.left:
                    _traverse(node.left)
                if node.right:
                    _traverse(node.right)
                return output
            _traverse(self.root)
            return output
        except:
            return 'an error occurred during pre-order method'

    def in_order(self):
        try:
            output = ''
            if not self.root:
                return output
            def _traverse(node):
                nonlocal output
                if node.left:
                    _traverse(node.left)
                output = output + str(node.value)
                if node.right:
                    _traverse(node.right)
                return output
            _traverse(self.root)
            return output
        except:
            return 'an error occurred during in-order method'

    def post_order(self):
        try:
            output = ''
            if not self.root:
                return output
            def _traverse(node):
                nonlocal output
                if node.left:
                    _traverse(node.left)
                if node.right:
                    _traverse(node.right)
                output = output + str(node.value)
                return output
            _traverse(self.root)
            return output
        except:
            return 'an error occurred during post-order method'

class Binary_Search_Tree(Tree):
    
    def __init__(self):
        super().__init__()

    def add(self,value):
        try: 
            if not self.root:
                self.root = Node(value)
                return
            def assigns(node):
                if value >= node.value:
                    if not node.right:
                        node.right = Node(value)
                        return    
                    assigns(node.right)
                else:
                    if not node.left:
                        node.left = Node(value)
                        return
                    assigns(node.left)
            assigns(self.root)
        except:
            return 'an error occurred using adding method, please enter a valid non-duplicated input the next time'
    def Contains(self,value):
        try:
            bool = False
            if not self.root:
                return False
            def check(node):
                nonlocal bool
                if node.value == value:
                    bool = True
                    return
                elif value > node.value:
                    if not node.right:
                        return
                    check(node.right)
                else:
                    if not node.left:
                        return
                    check(node.left)

            check(self.root)
            return bool
        except:
            return 'an error occurred using Contains, please enter a valid input the next time'

if __name__ == "__main__":
    tree = Binary_Search_Tree()
    tree.add(5)
    tree.add(15)
    tree.add(7)
    print(tree.Contains(7))

# done