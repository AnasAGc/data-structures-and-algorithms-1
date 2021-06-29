from breadthfirst import __version__
from breadthfirst.breadth_first import *

def test_version():
    assert __version__ == '0.1.0'

import pytest

def test_breadthFirst(prepared_tree):
    new_tree = Tree()
    assert breadthFirst(new_tree) == "this is an empty Tree"
    assert breadthFirst(prepared_tree) == ['A','B','C','D','E','F']



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