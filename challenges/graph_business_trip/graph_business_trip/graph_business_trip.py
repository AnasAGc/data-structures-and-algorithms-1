from graph_business_trip.graph import Vertex,Edge,Graph
# from graph import Vertex,Edge,Graph


def business_trip(graph, array):
  counter = 0
  bool = True
  all_nodes = graph.get_nodes()
  # first, we check if the array have more than one value
  if len(array)<2:
    return 'False, $0'
  # then , we check if the given values are inside the graph nodes
  new_array = []
  for item in array:
    for node in all_nodes:
      if item == node.value:
        new_array.append(node)
        continue
  if len(array) != len(new_array):
    return None

  # now, we check the value step by step
  def route (value, next_value):
    nonlocal counter,bool, new_array
    if not bool:
      return

    edges = graph.get_neighbors(value)
    if not len(edges):
      bool = False
      return
    for edge in edges:
      if next_value == edge.node:
        counter += edge.weight
        break
    else:
      bool = False
      return
    new_array.pop(0)
    if len(new_array)<2:
      return
    route(new_array[0], new_array[1])

  route(new_array[0], new_array[1])
  if bool:
    return f'{bool}, ${counter}'

  return f'{bool}, $0'
    

if __name__ == '__main__':
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    graph.add_edge(a,b,150)
    graph.add_edge(b,a,150)
    graph.add_edge(b,c,200)
    graph.add_edge(c,b,200)
    
    print(business_trip(graph,['a','b']))