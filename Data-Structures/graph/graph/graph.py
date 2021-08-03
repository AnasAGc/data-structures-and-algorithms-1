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
        if len(self.adjacency_list.keys()):
            return list(self.adjacency_list.keys())
        return None
    def get_neighbors(self,node):
        return self.adjacency_list[node]
    def size(self):
        return len(self.adjacency_list.keys())
    def breadth_first(self,node):
        try:
            if not node in self.adjacency_list.keys():
                raise Exception
            all = []
            breadth = []
            all.append(node)
            breadth.append(node)
            while(len(all)):
                edges = self.get_neighbors(node)
                if len(edges):
                    for edge in edges:
                        if not (edge.node in all) and not (edge.node in breadth):
                            all.append(edge.node)
                breadth.append(all.pop(0))
                if len(all):
                    node = all[0]
            breadth.pop(0)
            return breadth
        except:
            return "this node is not one of this graph's vertexes"
    
    def depth_first(self,node):
        try:
            output = []
            visited = set()
            def looping(node):
                nonlocal output
                output.append(node)
                visited.add(node)
                if self.adjacency_list[node]:
                    for element in self.adjacency_list[node]:
                        if not (element.node in visited):
                            looping(element.node)
            looping(node)
            return output
        except:
            return 'an error occurred during depth_first method'
    







if __name__ == '__main__':
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
    # graph.add_edge(c, b)
    graph.add_edge(d,e)
    graph.add_edge(e,g)
    graph.add_edge(f,h)
    graph.add_edge(g,h)
    graph.add_edge(f,i)
    graph.add_edge(h,k)
    graph.add_edge(i,k)
    # print(graph.breadth_first(a)[0].value)
    # print(graph.breadth_first(a)[1].value)
    # print(graph.breadth_first(a)[2].value)
    # print(graph.breadth_first(a)[3].value)
    print(len(graph.breadth_first(e)))
    graph2 = Graph()
    A = graph2.add_node('A')
    B = graph2.add_node('B')
    C = graph2.add_node('C')
    D = graph2.add_node('D')
    E = graph2.add_node('E')
    F = graph2.add_node('F')
    G = graph2.add_node('G')
    H = graph2.add_node('H')
    graph2.add_edge(A,B)
    graph2.add_edge(A,D)
    graph2.add_edge(D,E)
    graph2.add_edge(D,H)
    graph2.add_edge(D,F)
    graph2.add_edge(B,C)
    graph2.add_edge(C,G)

    out = graph2.depth_first(A)
    for item in out:
        print(item.value)




