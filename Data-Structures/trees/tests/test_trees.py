from typing import NewType
from trees import __version__
from trees.trees import *

import pytest

def test_version():
    assert __version__ == '0.1.0'


# testing for empty tree
def test_pre_order_empty_tree():
    tree = Tree()
    assert tree.pre_order() == ''
    assert tree.in_order() == ''
    assert tree.post_order() == ''

# testing the pre-order to check if it works properly
def test_pre_order(prepared_tree):
    assert prepared_tree.pre_order() == 'ABDECF'


# testing the in-order to check if it works properly
def test_in_order(prepared_tree):
    assert prepared_tree.in_order() == 'DBEAFC'

#testing the post-order to check if it works properly
def test_post_order(prepared_tree):
    assert prepared_tree.post_order() == 'DEBFCA'



# testing the Binary_Search_Tree
def test_Binary_Search_Tree(binery):
    assert binery.pre_order() == '10728131247'
    assert binery.in_order() == '27810121347'
    assert binery.post_order() == '28712471310'
    assert binery.Contains(7) is True
    assert binery.Contains(13) is True
    assert binery.Contains(5) is False


# testing max, for an empty Tree, a tree with one value and a tree with multiple values
def test_max(max):
    new_tree = Tree()
    assert new_tree.max() is None
    assert max.max() is 47
    new_tree.root =  Node(5)
    assert new_tree.max() is 5


def test_breadthFirst(prepared_tree):
    new_tree = Tree()
    assert new_tree.breadthFirst() == "this is an empty Tree"
    assert prepared_tree.breadthFirst() == ['A','B','C','D','E','F']


# all the provided tests cover the required ones inside 

@pytest.fixture
def prepared_tree():
    tree = Tree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    return tree

@pytest.fixture
def binery():
    newTree = Binary_Search_Tree()
    newTree.add(10)
    newTree.add(7)
    newTree.add(13)
    newTree.add(12)
    newTree.add(47)
    newTree.add(2)
    newTree.add(8)
    return newTree

@pytest.fixture
def max():
    tree = Tree()
    tree.root = Node(10)
    tree.root.left = Node(7)
    tree.root.right = Node(13)
    tree.root.left.left = Node(12)
    tree.root.left.right = Node(47)
    tree.root.right.left = Node(8)
    return tree

#                10
#               /  \
#              7    13
#             / \   / \
#            2   8 12  47
