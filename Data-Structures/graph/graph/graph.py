class Vertex:
    def __init__(self,value):
        self.value = value
class Edge:
    def __init__(self,node,weight):
        self.node = node
        self.weight = weight
class Graph:
    def __init__(self):
        self.adjacency_list = {}
    def add_node(self,value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex
    def add_edge(self,node1, node2, weight=0):
        try:
            if not node1 in self.adjacency_list.keys():
                raise Exception
            self.adjacency_list[node1].append(Edge(node2,weight))
        except:
            return 'either node 1 or node 2 does not exits'
    def get_nodes(self):
        return list(self.adjacency_list.keys())
    def get_neighbors(self,node):
        return self.adjacency_list[node]
    def size(self):
        return len(self.adjacency_list.keys())


if __name__ == '__main__':
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
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
    print()
