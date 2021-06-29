import copy
class Node:
    def __init__(self,value):
        self.value = value
        self.children = []

class k_ary_tree:
    def __init__(self):
        self.root = None

def fizz_buzz_tree(k_array):
    if not k_array.root:
        return None
    new_tree = copy.deepcopy(k_array)
    all_nodes = []
    all_nodes.append(new_tree.root)
    val = all_nodes[0]
    while True:
        if val.children:
            all_nodes += val.children
        if val.value % 3 == 0 and val.value % 5 == 0:
            val.value = 'FizzBuzz'
        elif val.value % 3 == 0:
            val.value = 'Fizz'
        elif val.value % 5 == 0:
            val.value = 'Buzz'
        else:
            val.value = str(val.value)
        all_nodes.pop(0)
        if not all_nodes:
            break
        val = all_nodes[0]
    return new_tree



if __name__ == "__main__":
    tree = k_ary_tree()
    tree.root = Node(3)
    tree.root.children.append(Node(2))
    tree.root.children.append(Node(5))
    tree.root.children.append(Node(15))
    tree.root.children[0].children.append(Node(4))
    tree.root.children[0].children.append(Node(6))
    tree.root.children[0].children.append(Node(7))
    tree.root.children[1].children.append(Node(9))
    tree.root.children[1].children.append(Node(18))
    tree.root.children[2].children.append(Node(45))
    new_tree =  fizz_buzz_tree(tree)
    print(new_tree.root.value)
    print(tree.root.value)
    # print(dir([]))
    # a = new_tree.__init__()
    # print(a)


#               Input (k_arr_tree)
#                      3 
#                ______|______
#               /      |      \
#              /       |       \
#             2        5        15
#           / | \     / \        \
#          4  6  7   9   18       45 
#                   Output 
#                      F
#                ______|______
#               /      |      \
#              /       |       \
#             2        B        FB
#           / | \     / \        \
#          4  F  7   F   F       FB 

#     FB =>  FizzBuzz F => Fizz , B => Buzz

