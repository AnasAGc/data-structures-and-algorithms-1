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
    
    def max(self):
        try:
            output = float('-inf')
            if not self.root:
                return None
            def _traverse(node):
                nonlocal output
                if node.value > output:
                    output = node.value
                if node.left:
                    _traverse(node.left)
                if node.right:
                    _traverse(node.right)
                return output
            _traverse(self.root)
            return output
        except:
            return 'an error occurred during finding the maximum value'

    # instead of creating a Queue (i don't like it), used the images to come up with this idea, Queue acts like 
    # a temporary storage and that's it, i can do this with just an array, it will check the left then the right
    # for all the nodes, then go to the next level

    def breadthFirst (self):    
        output = []
        temp_nodes = []
        if not self.root:
            return "this is an empty Tree"
        temp_nodes.append(self.root)
        output.append(self.root.value)
        val = self.root
        while val:
            if val.left:
                output.append(val.left.value)
                temp_nodes.append(val.left)
            if val.right:
                output.append(val.right.value)
                temp_nodes.append(val.right)
            temp_nodes.pop(0)
            if not len(temp_nodes):
                break
            val = temp_nodes[0]
        return (output)





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
    # tree.add(5)
    # tree.add(15)
    # tree.add(4)
    # tree.add(37)
    # tree.add(1)
    # tree.add(2)
    # print(tree.Contains(7))
    print(tree.breadthFirst())

# done