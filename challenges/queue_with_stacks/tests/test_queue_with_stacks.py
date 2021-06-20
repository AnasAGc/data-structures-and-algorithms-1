from queue_with_stacks import __version__
from queue_with_stacks.queue_with_stacks import *
import pytest

def test_version():
    assert __version__ == '0.1.0'



# testing enqueue for a single, or multiple inputs
def test_enqueue(queue_vals):

    # no nodes
    q = PseudoQueue()
    assert q.front.top == None
    assert q.rear.top == None

    # only one node
    q.enqueue(5)
    assert q.front.top.value == 5
    assert q.rear.top.value == 5

    # two nodes
    q.enqueue(7)
    assert q.front.top.value == 5
    assert q.rear.top.value == 7

    assert queue_vals.rear.top.value == 6
    assert queue_vals.front.top.value == 8


# testing dequeue for a single, or a multiple inputs

def test_dequeue(queue_vals):
    data = queue_vals.dequeue()
    assert data.value == 8
    assert queue_vals.front.top.value == 'hi'
    queue_vals.dequeue()
    queue_vals.dequeue()
    assert queue_vals.front.top.value == 6
    queue_vals.dequeue()
    # empty Queue
    empty = queue_vals.dequeue()
    assert empty == 'this is an empty Stack'

@pytest.fixture
def queue_vals():
    queue = PseudoQueue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    return queue