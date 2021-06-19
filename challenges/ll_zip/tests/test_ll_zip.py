from ll_zip import __version__
from ll_zip.ll_zip import LinkedList
from ll_zip.ll_zip import zipLists as zip

def test_version():
    assert __version__ == '0.1.0'

# we need to test today's function against one empty LL, two empty LL,
# LL that only have one node, LLs that differ in length, both ways

def test_two_empty_ll():
    ll1 = LinkedList()
    ll2 = LinkedList()
    h=zip(ll1,ll2)
    assert h.head == None

def test_one_empty_ll2():
    ll1 = create_list_append([1,3,2])
    ll2 = LinkedList()
    # h=zip(ll1,ll2)
    # assert h.value is 1
    # assert h.next.value is 3
    assert str(zip(ll1,ll2)) == '{ 1 } -> { 3 } -> { 2 } -> None'


def test_one_empty_ll1():
    ll1 = LinkedList()
    ll2 = create_list_append([5,9,4])
    # h=zip(ll1,ll2)
    # assert h.value is 5
    # assert h.next.value is 9
    assert str(zip(ll1,ll2)) == '{ 5 } -> { 9 } -> { 4 } -> None'


def test_two_ll_with_one_value():
    ll1 = create_list_append([1])
    ll2 = create_list_append([2])
    # h=zip(ll1,ll2)
    # assert h.value is 1
    # assert h.next.value is 2
    assert str(zip(ll1,ll2)) == '{ 1 } -> { 2 } -> None'


def test_two_equal_length_ll():
    ll1 = create_list_append([1,3,2])
    ll2 = create_list_append([5,9,4])
    # h=zip(ll1,ll2)
    # assert h.value is 1
    # assert h.next.value is 5
    assert str(zip(ll1,ll2)) == '{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> None'

def test_ll1_longer_than_ll2():
    ll1 = create_list_append([1,3,2])
    ll2 = create_list_append([5,9])
    # h=zip(ll1,ll2)
    # assert h.value is 1
    # assert h.next.value is 5
    assert str(zip(ll1,ll2)) == '{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> None'

def test_ll2_longer_than_ll1():
    ll1 = create_list_append([1,3])
    ll2 = create_list_append([5,9,4])
    # h=zip(ll1,ll2)
    # assert h.value is 1
    # assert h.next.value is 5
    assert str(zip(ll1,ll2)) == '{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> None'




def create_list_insert(lis):
    """helper function to create list by insert with given values, used in test module"""
    my_l_list = LinkedList()
    for i in lis:
        my_l_list.insert(i)
    return my_l_list
    
def create_list_append(lis):
    """helper function to create list by append with given values, used in test module"""
    my_l_list = LinkedList()
    for i in lis:
        my_l_list.append(i)
    return my_l_list