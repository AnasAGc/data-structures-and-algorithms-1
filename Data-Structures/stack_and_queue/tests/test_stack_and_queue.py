from stack_and_queue import __version__
from stack_and_queue.stacks_and_queues import  Stack, Queue
import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_push(stack_3_vals):

    assert stack_3_vals.top.value == 'd'

def test_pop(stack_3_vals):

    assert stack_3_vals.pop() == 'd'
    assert stack_3_vals.top.value == -7
    assert stack_3_vals.pop() == -7
    assert stack_3_vals.pop() == 3
    # now we reach the empty stack
    assert stack_3_vals.pop() == 'this is an empty Stack'

    # for Empty stack, we expect an exception
    
    empty = Stack()
    assert empty.pop() == 'this is an empty Stack'

def test_peek(stack_3_vals):

    assert stack_3_vals.peek() == 'd'
    assert stack_3_vals.top.value == 'd'

    # for Empty stack, we expect an exception
    
    empty = Stack()
    assert empty.peek() == 'this is an empty Stack'

def test_is_empty(stack_3_vals):

    assert stack_3_vals.is_empty() == False



def test_enqueue(queue_vals):

    # no nodes
    q = Queue()
    assert q.front == None
    assert q.rear == None

    # only one node
    q.enqueue(5)
    assert q.front.value == 5
    assert q.rear.value == 5

    # two nodes
    q.enqueue(7)
    assert q.front.value == 5
    assert q.rear.value == 7

    assert queue_vals.rear.value == 6
    assert queue_vals.front.value == 8

def test_dequeue(queue_vals):
    data = queue_vals.dequeue()
    assert data.value == 8
    assert data.next == None
    assert queue_vals.front.value == 'hi'
    queue_vals.dequeue()
    queue_vals.dequeue()
    assert queue_vals.front.value == 6
    queue_vals.dequeue()
    # empty Queue
    empty = queue_vals.dequeue()
    assert empty == 'this is an empty Stack'
    

    
def test_peek(queue_vals):
    q = Queue()
    assert q.peek() == 'this is an empty Stack'
    assert queue_vals.peek() == 8

def test_is_empty(queue_vals):
    q = Queue()
    assert q.is_empty() == True
    assert queue_vals.is_empty() == False


# Decorator
@pytest.fixture
def stack_3_vals():
    stack = Stack()
    stack.push(3)
    stack.push(-7)
    stack.push('d')
    return stack

@pytest.fixture
def queue_vals():
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    return queue