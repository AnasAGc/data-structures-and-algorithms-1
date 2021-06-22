class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, value):
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        try:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        except:
            return 'this is an empty Stack'
    def peek(self):
        try:
            return self.front.value
        except:
            return 'this is an empty Stack'
    def is_empty(self):
        return self.front == None





# **************************************************************************************************
class AnimalShelter(Queue):
    
    def __init__(self):
        super().__init__()
    def Animal_enqueue(self, animal):
        if (animal == 'dog' or animal == 'cat'):
            self.enqueue(animal)
            return 'Successfully added the animal'
        else:
            return 'your input should only be a cat or a dog'
            
# this algorithm is built with a hint from google, not entirely by myself, which is the idea  of previous (i needed to create a 
# previous by myself, but previous isn't available in Queues, so, the temp.next worked)
    def Animal_dequeue(self , pref):
        if not self.rear:
            return None
        if (pref != 'dog' and pref != 'cat'):
            return None
        temp = self.front
        if temp.value == pref:
            a = self.dequeue().value
            if not self.front:
                self.rear = None
            return a
        else:
            while temp.next != None:
                if temp.next.value == pref:
                    to_return = temp.next.value
                    temp.next = temp.next.next
                    return to_return
                else:
                    temp = temp.next
            return None






if __name__ == "__main__":
    animals = AnimalShelter()
    animals.Animal_enqueue('dog')
    animals.Animal_enqueue('cat')
    animals.Animal_enqueue('dog')
    animals.Animal_enqueue('dog')
    print(animals.Animal_dequeue("cat"))
    print(animals.Animal_dequeue("dog"))
    print(animals.Animal_dequeue("dog"))
    print(animals.Animal_dequeue("dog"))
    print(animals.Animal_dequeue("dog"))
    print(5555555555555555555)
    animals.Animal_enqueue('dog')
    animals.Animal_enqueue('cat')
    print(animals.Animal_dequeue("cat"))
    print(animals.Animal_dequeue("dog"))
    print(animals.Animal_dequeue("cat"))
    print(animals.Animal_dequeue("dog"))