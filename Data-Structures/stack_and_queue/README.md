## Code Link

[code Link](stack_and_queue/stacks_and_queues.py)

# Stacks and Queues
## Stacks

A stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle. In the pushdown stacks only two operations are allowed: push the item into the stack, and pop the item out of the stack. A stack is a limited access data structure - elements can be added and removed from the stack only at the top. push adds an item to the top of the stack, pop removes the item from the top. A helpful analogy is to think of a stack of books; you can remove only the top book, also you can add a new book on the top.

## Queues


A queue is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle. An excellent example of a queue is a line of students in the food court of the UC. New additions to a line made to the back of the queue, while removal (or serving) happens in the front. In the queue only two operations are allowed enqueue and dequeue. Enqueue means to insert an item into the back of the queue, dequeue means removing the front item. The picture demonstrates the FIFO access.
The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.



## Challenge

Create a class called Stack, a class called Queue, and a class called Node

* Node class has properties for the value stored in the Node, and a pointer to the next node.

* Stack class has a top property. It creates an empty Stack when instantiated.

* Queue class has a front property. It creates an empty Queue when instantiated.

## Approach & Efficiency

First, i created a class called Node, that takes in a value, and define a value and a next property for every instance created, then i defined the Stack class, that has four methods for now, push is for appending a new node to the stack, pop is for removing a node form the stack, peek is to see whats the last value added to the stack, and isEmpty is to check if the stack is empty or not, exceptions were created in case of an empty stack.

then, i created a class called Queue, that has four methods, enqueue, that takes a value as an argument, then add the new node to the Queue, dequeue is to remove the first node out of the Queue, peek is to check the first node inside the Queue, and the isEmpty is to check if the queue is empty or not, exceptions were created in case of empty stack.


## API

there are several methods that are appended to Stack and Queue classes, that are:

for the **Stack** class:

a. push: takes any value as an argument and adds a new node with that value to the top of the stack

b. pop: does not take any argument, removes the node from the top of the stack, and returns the node’s value.

c. peek : does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.

d. isEmpty : takes no argument, and returns a boolean indicating whether or not the stack is empty.

***for the **Queue** class:***

a. enqueue : takes any value as an argument and adds a new node with that value to the back of the queue

b. dequeue : does not take any argument, removes the node from the front of the queue, and returns the node’s value.

c. peek : does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.

d. isEmpty : takes no argument, and returns a boolean indicating whether or not the queue is empty.