from fifo_animal_shelter import __version__
from fifo_animal_shelter.fifo_animal_shelter import *

def test_version():
    assert __version__ == '0.1.0'


# testing Animal_enqueue method against "cat" or "dog" inputs, also, testing against random inputs

def test_Animal_enqueue():

    animals = AnimalShelter()
    assert animals.Animal_enqueue('cat') == 'Successfully added the animal'
    assert animals.front.value == 'cat'
    assert animals.rear.value == 'cat'
    assert animals.Animal_enqueue('dog') == 'Successfully added the animal'
    assert animals.front.value == 'cat'
    assert animals.rear.value == 'dog'
    assert animals.Animal_enqueue('humans') == 'your input should only be a cat or a dog'
    assert animals.front.value == 'cat'
    assert animals.rear.value == 'dog'

# testing Animal_dequeue method against empty instance, values that aren't 'cat' or 'dog', or when there is no
# more "dog" and "cat", after the shelter is empty, i tested the enqueue and dequeue again, just to make sure
# everything is working properly

def test_Animal_enqueue():
    animals = AnimalShelter()
    assert animals.Animal_dequeue('human') == None
    assert animals.Animal_dequeue('cat') == None
    animals.Animal_enqueue('cat')
    animals.Animal_enqueue('dog')
    animals.Animal_enqueue('cat')
    animals.Animal_enqueue('dog')
    assert animals.Animal_dequeue('cat') == 'cat'
    assert animals.Animal_dequeue('cat') == 'cat'
    assert animals.Animal_dequeue('cat') == None
    assert animals.Animal_dequeue('dog') == 'dog'
    assert animals.Animal_dequeue('dog') == 'dog'
    assert animals.Animal_dequeue('dog') == None
    animals.Animal_enqueue('cat')
    animals.Animal_enqueue('dog')
    assert animals.Animal_dequeue('cat') == 'cat'
    assert animals.Animal_dequeue('cat') == None
    assert animals.Animal_dequeue('dog') == 'dog'