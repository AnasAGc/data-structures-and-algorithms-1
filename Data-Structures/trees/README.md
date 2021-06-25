# Trees

Trees are non-linear data structures that represent nodes connected by edges. Each tree consists of a root node as the Parent node, and the left node and right node as Child nodes.
![d](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/images/BinaryTree1.PNG)

## Binary tree

A tree whose elements have at most two children is called a binary tree. Each element in a binary tree can have only two children. A node’s left child must have a value less than its parent’s value, and the node’s right child must have a value greater than its parent value.

![d](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/images/BST2.PNG)

## Challenge

* Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

* Create a Binary Tree class that has three methods, pre order, in order, and post order

* Create a Binary Search Tree class that has two methods, add and Contains

## Approach & Efficiency

for today's approach, i used only one method to complete today's code challenge, which is using regression inside the methods in order to loop over the entire tree, it's impossible to use a while or for loop in a multi-directional problem, that's why i used regression.

we have three classes, Tree, Node and Binary_Search_Tree.

## API

for today, we have 3 classes with multiple functionalities:

* Node class: Node class is responsible for creating new nodes that has a value, a right and a lift defined as None

* the Tree class has three methods, pre_order, in_order and post_order:
    
    * pre_order method: Pre-order means that the root has to be looked at first. In our case, looking at the root just means that we output its value. When we call preOrder for the first time, the root will be added to the call stack

    * in_order:  Pre-order means that the left has to be looked at first. In our case, we start from the farthest node to the left, and work our way to the root, to reach the right nodes

    * post_order:  Pre-order means that the left has to be looked at first. In our case, we start from the farthest node to the left, and work our way to the right, finally, we reach the root