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
class Animal:
    def __init__(self,name,kind):
        self.name = name
        self.kind = kind
        self.next = None



class AnimalShelter():
    
    def __init__(self):
        self.front = None
        self.rear = None

    def Animal_enqueue(self, name,kind):
        animal = Animal(name,kind)

        if (animal.kind == 'dog' or animal.kind == 'cat'):
            if not self.rear:
                self.rear = animal
                self.front = animal
            else:
                self.rear.next = animal
                self.rear = animal

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
        else:
            temp = self.front
            if self.front.kind == pref:
                self.front = self.front.next
                temp.next = None
                if not self.front:
                    self.rear = None
                return temp.name
            else:
                while temp.next:
                    if temp.next.kind == pref:
                        to_return = temp.next.name
                        temp.next =  temp.next.next
                        return to_return
                    else:
                        temp = temp.next
                return None






if __name__ == "__main__":
    animals = AnimalShelter()
    animals.Animal_enqueue('sugar','cat')
    animals.Animal_enqueue('shawerma','dog')
    animals.Animal_enqueue('caramel','cat')
    animals.Animal_enqueue('banana','dog')
    print(animals.Animal_dequeue("cat"))
    print(animals.Animal_dequeue("dog"))
    print(animals.Animal_dequeue("dog"))
    print(animals.Animal_dequeue("cat"))
    print(animals.front)
    print(animals.rear)
    print(animals.Animal_dequeue("dog"))
    print(5555555555555555555)
    animals.Animal_enqueue('argon','dog')
    animals.Animal_enqueue('biter','cat')
    print(animals.Animal_dequeue("cat"))
    print(animals.Animal_dequeue("dog"))
    print(animals.Animal_dequeue("cat"))
    print(animals.Animal_dequeue("dog"))