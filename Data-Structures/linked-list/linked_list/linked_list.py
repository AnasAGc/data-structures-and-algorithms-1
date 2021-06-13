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

    def insertBefore(self,value, newVal):
        try:
            node = Node(newVal)
            current = self.head
            if(current.value == value):
                LinkedList.insert(self,newVal)
                return
            while(current.next.value != value):
                current = current.next
            a = current.next
            current.next=node
            node.next = a
        except TypeError:
            return f'please enter a proper type'
        except:
            return f"the value {value} does not exist in this instance"
    
    def insertAfter(self,value, newVal):
        try:
            node = Node(newVal)
            current = self.head
            while(True):
                if(current.value == value):
                    a = current.next
                    current.next = node
                    node.next = a
                    break
                current = current.next
        except:
            return f"the value {value} does not exist in this instance"


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
    # n3 = Node(True)
    # print(n2.value)


    ll = LinkedList()
    # Value of first node on head
    # ll.append(4)
    # ll.insert('s')
    # ll.append(-1)
    # ll.append(7)
    # print(ll.head.value)
    # ll.insertBefore(1,1)
    # ll.insertAfter(-1,1)
    # ll.insertAfter(17,5)
    # print(ll.head.value)
    # print(str(ll))
    # print(ll.head.value)
    # print(ll.head.next)
    # print(str(ll))