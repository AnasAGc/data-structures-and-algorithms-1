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
            return temp.value
        except:
            return 'this is an empty Stack'

    def peek(self):
        try:
            return self.top.value
        except:
            return 'this is an empty Stack'

    def is_empty(self): 
        return self.top == None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, value):
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        try:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        except:
            return 'this is an empty Stack'
    def peek(self):
        try:
            return self.front.value
        except:
            return 'this is an empty Stack'
    def is_empty(self):
        return self.front == Nonez

if __name__ == '__main__':
    # stack = Stack()
    # stack.push(3)
    # stack.push(-7)
    # stack.push('d')
    # print(stack.peek())
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    # print(q.rear.value) //3
    # print(q.dequeue())
    