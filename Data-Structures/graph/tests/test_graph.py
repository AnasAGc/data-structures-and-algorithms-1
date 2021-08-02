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
    # check for empty graph
    graph2 = Graph()
    assert graph2.get_nodes() == None

def test_breadth_first():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    h = graph.add_node('h')
    i = graph.add_node('i')
    k = graph.add_node('k')
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(a,e)
    graph.add_edge(b, d)
    graph.add_edge(c, f)
    graph.add_edge(c, b)
    graph.add_edge(e,g)
    graph.add_edge(f,h)
    graph.add_edge(g,h)
    graph.add_edge(f,i)
    graph.add_edge(h,k)
    graph.add_edge(i,k)
    assert len(graph.breadth_first(a)) == 10
    breadth = graph.breadth_first(a)
    assert breadth[0].value == 'a'
    assert breadth[1].value == 'b'
    assert breadth[2].value == 'c'
    assert breadth[3].value == 'e'
    assert breadth[4].value == 'd'
    assert breadth[5].value == 'f'
    assert breadth[6].value == 'g'
    assert breadth[7].value == 'h'
    assert breadth[8].value == 'i'
    assert breadth[9].value == 'k'
