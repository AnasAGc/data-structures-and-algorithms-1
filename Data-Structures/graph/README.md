# Graphs

A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges

## Challenge

Implement a Graph. The graph should be represented as an adjacency list, and should include the following methods:

* add node

* add edge

* get nodes

* get neighbors

* size

## Approach & Efficiency

the approach used is creating three classes, one is for the vertexes, one is for Edges and one for creating a new Graph. the vertex class is for creating new vertexes with values, the Edge class is for creating edges between graph's vertexes, and the graph is for creating a new graph

Time complexity => O(n), for the creation of all the nodes

Space complexity => O(n), to create the nodes and store them inside vertexes



## API

we used multiple methods for the Graph class:

* add node: takes a node as an input, and implement it inside the graph as a vertex, then returns the vertex of the value

* add edge => it adds edges to the vertexes, and it takes two nodes and a weight as an input

* get nodes => gets all the nodes inside the graph

* get neighbors => get the nodes that are attached to a certain node

* size => returns the size of the graph, by calculating the number of nodes implemented inside the graph
