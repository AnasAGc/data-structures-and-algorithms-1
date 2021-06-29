class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

def breadthFirst (tree):    
    output = []
    temp_nodes = []
    if not tree.root:
        return "this is an empty Tree"
    temp_nodes.append(tree.root)
    output.append(tree.root.value)
    val = tree.root
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

if __name__ == "__main__":
    tree = Tree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    print(breadthFirst(tree))