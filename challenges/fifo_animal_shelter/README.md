## code link

[code Link](fifo_animal_shelter/fifo_animal_shelter.py)

# Challenge Summary
Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach. implement these methods:

* enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.

* dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.

## Whiteboard Process
![d](resources/cc12.png)

## Approach & Efficiency

i created the AnimalShelter class, made it inherit from the Queue class, to utilize the front and the rear method, with thinking about all the edge cases possible, i created a suitable code for enqueue and dequeue methods

## Solution

for the enqueue method, i used this simple code that checks if the input is 'cat' or 'dog' or anything else, then add it to the Queue instance
```
        if (animal == 'dog' or animal == 'cat'):
            self.enqueue(animal)
            return 'Successfully added the animal'
        else:
            return 'your input should only be a cat or a dog'
```

then i used a code for the dequeue method, first i checked if the Queue is empty or not, then checked if the prep is 'dog' or 'cat' or something else, then i dequeue the value if exists

```
        if not self.rear or not self.front:
            return None
        if (pref != 'dog' and pref != 'cat'):
            return None
        temp = self.front
        if temp.value == pref:
            a = self.dequeue().value
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
```
