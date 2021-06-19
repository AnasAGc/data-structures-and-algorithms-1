from stack_and_queue import __version__
from stack_and_queue.stacks_and_queues import Node, Stack, Queue
import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_push(stack_3_vals):

    assert stack_3_vals.top.value == 'd'

def test_pop(stack_3_vals):

    assert stack_3_vals.pop() == 'd'
    assert stack_3_vals.top.value == -7

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



# def test_enqueue(queue_vals):
#     assert queue_vals.rear.value == 6
#     assert queue_vals.front.value == 8

# def test_dequeue(queue_vals):
#     data = queue_vals.dequeue()
#     assert data == 8
#     assert queue_vals.front.value == 'hi'

# def test_peek(queue_vals):
#     pass

# def test_is_empty(queue_vals):
#     pass


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