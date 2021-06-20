class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        try:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp
        except:
            return 'this is an empty Stack'

    def peek(self):
        try:
            return self.top.value
        except:
            return 'this is an empty Stack'

    def is_empty(self): 
        return self.top == None


class PseudoQueue:

    def __init__(self):
        self.front = Stack()
        self.rear = Stack()
    def enqueue(self, value):
        node = Node(value)
        if not self.rear.top:
            self.front.top = node
            self.rear.top = node
        else:
            """ SOL1
            self.rear.top.next = node
            self.rear.top = node
            """
            # sol2 
            temp = self.rear.top
            self.rear.push(value)
            self.rear.top.next = None
            temp.next =  self.rear.top

    def dequeue(self):
        try:
            """ SOL1
            temp = self.front.top
            self.front.top = self.front.top.next
            temp.next = None
            return temp
            """
            # Sol2
            temp = self.front.pop()
            return temp
        except:
            return 'this is an empty Stack'




if __name__ == '__main__':
    a = PseudoQueue()
    a.enqueue(5)
    a.enqueue(6)
    a.enqueue(7)
    print(a.dequeue().value)
    print(a.dequeue().value)
    print(a.dequeue().value)
    print(a.dequeue())