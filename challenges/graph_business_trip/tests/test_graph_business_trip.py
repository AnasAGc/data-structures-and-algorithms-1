from graph_business_trip import __version__
from graph_business_trip.graph import Vertex, Edge, Graph
from graph_business_trip.graph_business_trip import business_trip

import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_base_graph(base_graph):
    assert business_trip(base_graph,['a','b']) == 'True, $150'
    assert business_trip(base_graph,['a','b','c']) == 'True, $350'
    assert business_trip(base_graph,['a','c']) == 'False, $0'
    assert business_trip(base_graph,['a','a']) == 'False, $0'
    assert business_trip(base_graph,['a']) == 'False, $0'

def test_cc_graph(cc_graph):
    assert business_trip(cc_graph, ['Metroville', 'Pandora', ]) == 'True, $82'
    assert business_trip(cc_graph, ['Metroville', 'Pandora', 'Metroville']) == 'True, $164'
    assert business_trip(cc_graph, ['Arendelle', 'Monstropolis', 'Naboo']) == 'True, $115' 
    assert business_trip(cc_graph, ['Naboo', 'Pandora']) == 'False, $0'
    assert business_trip(cc_graph, ['Narnia', 'Arendelle', 'Naboo']) == 'False, $0'



@pytest.fixture
def base_graph():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_node('g')
    graph.add_edge(a,b,150)
    graph.add_edge(b,a,150)
    graph.add_edge(b,c,200)
    graph.add_edge(c,b,200)
    return graph

@pytest.fixture
def cc_graph():
    graph = Graph()
    Pandora = graph.add_node('Pandora')
    Arendelle = graph.add_node('Arendelle')
    Metroville = graph.add_node('Metroville')
    Monstropolis = graph.add_node('Monstropolis')
    Narnia = graph.add_node('Narnia')
    Naboo = graph.add_node('Naboo')
    graph.add_edge(Pandora,Arendelle,150)
    graph.add_edge(Pandora, Metroville, 82)
    graph.add_edge(Arendelle,Pandora,150)
    graph.add_edge(Arendelle, Metroville,99)
    graph.add_edge(Arendelle,Monstropolis,42)
    graph.add_edge(Metroville,Pandora,82)
    graph.add_edge(Metroville,Arendelle,99)
    graph.add_edge(Metroville, Monstropolis, 105)
    graph.add_edge(Metroville, Naboo, 26)
    graph.add_edge(Metroville, Narnia, 37)
    graph.add_edge(Monstropolis, Arendelle, 42)
    graph.add_edge(Monstropolis, Metroville, 105)
    graph.add_edge(Monstropolis, Naboo, 73)
    graph.add_edge(Naboo, Monstropolis, 73)
    graph.add_edge(Naboo, Metroville, 26)
    graph.add_edge(Naboo,Narnia,250)
    graph.add_edge(Narnia, Naboo,250)
    graph.add_edge(Narnia, Metroville, 37)
    return graph

