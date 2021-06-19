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
                self.insert(newVal)
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

    def kthFromEnd (self,value):
        try:
            current = self.head
            allValues = []
            while(current.next != None):
                allValues.append(current.value)
                current = current.next
            else:
                allValues.append(current.value)
            allValues.reverse()
            return allValues[value]
        except:
            return 'this instance is not long enough'


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

# def zipLists (ll1,ll2):
#     current1 = ll1.head
#     current2 = ll2.head
#     status1 = True
#     status2 = True
#     if(not current1):
#         status1 = False
#     if(not current2):
#         status2 = False
#     if(status1 and status2):
#         new = LinkedList()
#         while(current1.next != None or current2.next != None or status1 or status2):
#             if current1.next != None:
#                 new.append(current1.value)
#                 current1 = current1.next
#             elif (current1.value and status1):
#                 new.append(current1.value)
#                 status1 = False

#             if current2.next != None:
#                 new.append(current2.value)
#                 current2 = current2.next
#             elif (current2.value and status2):
#                 new.append(current2.value)
#                 status2 = False
#         return new.head

#     elif status1:
#         return ll1

#     elif status2:
#         return ll2
    
#     else:
#         return LinkedList()

def zipLists (ll1,ll2):
    current1 = ll1.head
    current2 = ll2.head
    new = LinkedList()
    current3 = new.head
    status1 = True
    status2 = True
    if(not current1):
        status1 = False
    if(not current2):
        status2 = False
    if(status1 and status2):
        new.head = current1
        current3 = new.head
        print(current3.value)
        if (not current1.next):
            status1 = False
        else:
            current1 = current1.next
        while(status1 or status2):
            if(status2):
                print(current2.value)
                if current2.next:
                    b = current2.next
                    current3.next = current2
                    current3 = current3.next
                    current2 = b
                elif (current2.value and status2):
                    current3.next = current2
                    current3 = current3.next
                    status2 = False
            if(status1):
                if current1.next:
                    a = current1.next
                    current3.next = current1
                    current3 = current3.next
                    current1 = a
                elif (current1.value and status1):
                    current3.next = current1
                    current3 = current3.next
                    status1 = False
        return new

    elif status1:
        return ll1

    elif status2:
        return ll2
    
    else:
        return LinkedList()


if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    # print(palindrome(ll1))
    # 's' 4 -1 7
    ll2 = LinkedList()
    ll2.append(2)
    # ll2.append(4)
    # ll2.append(6)
    # current1 = ll1.head
    # current2 = ll2.head
    # a = current1.next
    # b = current2.next
    # current1.next = current2
    # current2.next = a
    # current1 = current1.next.next
    new = zipLists(ll1,ll2)
    print('aaa')
    print(str(new))
    # print(ll1.head.value)
    
    # current2 = ll2.head.next
    # print(current1.next.next.value)
    # print(curr)
    # print(str(ll1))
    
    
    # ll2.append(4)
    # ll2.insert('w')
    # 'w' 17 -2 'q'
    # new,h = zipLists(ll1,ll2)
    # print(h)