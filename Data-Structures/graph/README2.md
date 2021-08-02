# Challenge Summary

write a method for the Graph class called breadth first, that takes a Node as an argument, and returns the collection of nodes in the order they were visited.

## Whiteboard Process

<!-- Embedded whiteboard image -->

## Approach & Efficiency

for the approach used, i used two arrays, one for storing all the nodes inside it, and one for storing the nodes depth first one by one, with a while loop over the array that is going to contain all the values, and only has the base value in the beginning, we check if the first node inside the 'all' array have edges or not, if it has, after checking that they are not duplicated, we store them inside 'all' array, and store the first value inside 'all' array inside 'breadth' array and pop the element from 'all', when 'all' is empty, return 'breadth' array.

time complexity: it's O(n^3), because of the nested loops inside each other

space complexity: it's O(n), we have an array completely depending on the values inside the graph

## Solution

the solution is just defining two arrays, one for pushing all the values inside it, and one for the exact sort of which the values were stored inside the graph

```
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
```