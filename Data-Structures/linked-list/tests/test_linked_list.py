from linked_list import __version__
import linked_list
from linked_list.linked_list import LinkedList, Node

def test_version():
    assert __version__ == '0.1.0'

# testing Node

def test_Node():
    a = Node(5)
    assert a.value is 5
    assert a.next is None

# testing append by itself

def test_append_1():
    ll = LinkedList()
    ll.append(1)
    assert ll.head.value is 1
    ll.append(2)
    assert ll.head.next.value is 2
    assert ll.head.next.next is None

# mixing between insert and append, to make sure everything works properly, testing for one value at first
# then for mixing between append and insert

def test_insert():
    ll = LinkedList()
    ll.insert(5)
    assert ll.head.value is 5
    assert ll.head.next is None
    ll.insert('s')
    assert ll.head.value is 's'
    assert ll.head.next.value is 5
    ll.append('i')
    assert ll.head.value is 's'
    assert ll.head.next.value is 5
    ll.insert(17)
    assert ll.head.value is 17
    assert ll.head.next.value is 's'

# testing the include method, first for an empty linkedlist, then for one that only has one element, at last, for 
# one that has multiple Nodes

def test_include():
    ll = LinkedList()
    assert ll.include(4) is False
    ll.append(5)
    assert ll.include(1) is False
    assert ll.include(5) is True
    ll.append(4)
    ll.insert(3)
    assert ll.include(1) is False
    assert ll.include(5) is True
    assert ll.include(4) is True
    assert ll.include(3) is True
    ll.insert(2)
    ll.append(1)
    assert ll.include(5) is True
    assert ll.include(1) is True
    assert ll.include(6) is False

# testing the __str__, which should return a string of the values in the Linkedlist, edge case is for an
# empty Linkedlist
def test_str():
    ll=LinkedList()
    assert str(ll) is 'None'
    ll.append(5)
    assert str(ll) == '{ 5 } -> None'
    ll.append(5)
    assert str(ll) == '{ 5 } -> { 5 } -> None'
    ll.append(4)
    ll.insert(3)
    ll.append(2)
    assert str(ll) == '{ 3 } -> { 5 } -> { 5 } -> { 4 } -> { 2 } -> None'

# testing the insertAfter method, to check how the method react for empty Linked lists, ones that are normal,
# and ones that don't have the value

def test_insertAfter():
    ll = LinkedList()
    assert ll.insertAfter(5,1) == "the value 5 does not exist in this instance"
    ll.append(5)
    ll.insertAfter(5,1)
    assert ll.head.next.value == 1
    assert ll.head.next.next == None
    ll.insertBefore(1,4)
    assert ll.head.next.value == 4
    assert ll.head.next.next.value == 1

# testing the insertBefore, to check how the method react for empty Linked lists, ones that are normal,
# and ones that don't have the value

def test_insertBefore():
    ll = LinkedList()
    assert ll.insertBefore(5,1) == "the value 5 does not exist in this instance"
    ll.append(5)
    ll.insertBefore(5,1)
    assert ll.head.value is 1
    assert ll.head.next.value is 5
    ll.insertBefore(5,2)
    assert ll.head.next.value is 2
    assert ll.head.next.next.value is 5

# testing the insertBefore, to check how the method react for empty Linked lists, ones that are normal,
# and ones that don't have the value

def test_kthFromEnd():
    ll = LinkedList()
    assert ll.kthFromEnd(1) == 'this instance is not long enough'
    ll.append(5)
    assert ll.kthFromEnd(1) == 'this instance is not long enough'
    ll.kthFromEnd(0) == 5
    ll.append(17)
    ll.insert('foo')
    ll.append(61)
    assert ll.kthFromEnd(2) == 5
    assert ll.kthFromEnd(3) == 'foo'
    assert ll.kthFromEnd(6) == 'this instance is not long enough'
    assert ll.kthFromEnd(-1) == 'foo'