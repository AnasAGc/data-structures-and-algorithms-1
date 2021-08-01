from graph import __version__
import graph
from graph.graph import Vertex, Edge, Graph

def test_version():
    assert __version__ == '0.1.0'

def test_graph():
    # check for successful input
    graph = Graph()
    a = graph.add_node('a')
    assert a.value == 'a'
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    # check the get_nodes function
    assert graph.get_nodes()[0].value == 'a'
    assert graph.get_nodes()[1].value == 'b'
    assert graph.get_nodes()[5].value == 'f'
    # check if the add_edges and get_neighbors are working properly
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(b, f)
    graph.add_edge(c, a)
    graph.add_edge(c, b)
    graph.add_edge(c, e)
    graph.add_edge(d, a)
    graph.add_edge(d, e)
    graph.add_edge(e, c)
    graph.add_edge(e, d)
    graph.add_edge(e, f)
    graph.add_edge(f, b)
    graph.add_edge(f, e)
    assert graph.get_neighbors(a)[0].node.value == 'c'
    assert graph.get_neighbors(a)[1].node.value == 'd'
    # testing the size method
    assert graph.size()==6