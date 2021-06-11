class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Adds a node of a value to the head of LL
        """
        node = Node(value)
        if not self.head:
            self.head = node
        else:

            """
            try fix
            ---------sol1-----------
            # a = self.head 1
            # self.head.value = node.value
            # self.head.next = a
            ---------sol2-----------
            # self.head.next= self.head
            # self.head.value = node.value
            """
            node.next= self.head
            self.head = node


    def append(self, value):
        """
        Adds a node of a value to the end of LL
        """
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node


    def include(self, value):
        """
        Return T/F if value is in the linked list or not
        """
        inc = False
        current = self.head
        if not current:
            return inc
        else:
            while(current.next != None):
                if current.value == value:
                    inc = True
                    break
                current = current.next
            else:
                if(current.value == value): # in case of one value only inside the 
                    return True
            return inc

    
    def __str__(self):
        out = ''
        # "{ a } -> { b } -> { c } -> NULL"
        # Loop over all nodes
        # print all values in one line
        current = self.head
        if not current: # first 
            return 'None'
        else:
            while current.next != None:
                out = out + '{ ' + str(current.value) + ' } -> '
                current = current.next
            else:
                out += '{ ' + str(current.value) + ' } -> None'
            return out

    


if __name__ == "__main__":
    # Instances of Node
    # n1 = Node(34)
    # n2 = Node('Suhaib')
    # n3 = Node(True)
    # print(n2.value)


    ll = LinkedList()
    # Value of first node on head
    # ll.append(4)
    # ll.insert(5)
    # ll.append(-1)
    # ll.append(7)
    # print(ll.head.value)
    print(ll.include(7))
    # print(ll.head.value)
    # print(str(ll))
    # print(ll.head.value)
    # print(ll.head.next)
    # print(str(ll))

    # next of head (next of Node(4)) is Null
    # I have ll: head - Node(4) -> Node(-1) -> Node('s') -> None
    # print(ll.head.next.value)
    # print(ll.head.next.next.value)