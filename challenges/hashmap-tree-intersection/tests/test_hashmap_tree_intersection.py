from hashmap_tree_intersection import __version__
from hashmap_tree_intersection.hashmap_tree_intersection import hashmap_tree_intersections
from hashmap_tree_intersection.tree import Tree, Node
import pytest
def test_version():
    assert __version__ == '0.1.0'

def test_one_tree_is_empty(tree2fixture,tree1fixture, empty_tree):
    assert hashmap_tree_intersections(tree1fixture, empty_tree) == []
    assert hashmap_tree_intersections(tree2fixture, empty_tree) == []


def test_regular_complicated_trees(tree2fixture, tree1fixture):
    assert hashmap_tree_intersections(tree2fixture, tree1fixture) == [100,160,125,175,200,350,500]
    assert hashmap_tree_intersections(tree1fixture, tree2fixture) == [100,160,125,175,200,350,500]

@pytest.fixture
def tree1fixture():
    tree1 = Tree()
    tree1.root = Node(150)
    tree1.root.left = Node(100)
    tree1.root.right = Node(250)
    tree1.root.left.left = Node(75)
    tree1.root.left.right = Node(160)
    tree1.root.left.right.left = Node(125)
    tree1.root.left.right.right = Node(175)
    tree1.root.right.left = Node(200)
    tree1.root.right.right = Node(350)
    tree1.root.right.right.right = Node(500)
    tree1.root.right.right.left = Node(300)
    return tree1

@pytest.fixture
def tree2fixture():
    tree2 = Tree()
    tree2.root = Node(42)
    tree2.root.left = Node(100)
    tree2.root.right = Node(600)
    tree2.root.left.left = Node(15)
    tree2.root.left.right = Node(160)
    tree2.root.left.right.left = Node(125)
    tree2.root.left.right.right = Node(175)
    tree2.root.right.left = Node(200)
    tree2.root.right.right = Node(350)
    tree2.root.right.right.right = Node(500)
    tree2.root.right.right.left = Node(4)
    return tree2

@pytest.fixture
def empty_tree():
    tree = Tree()
    return tree