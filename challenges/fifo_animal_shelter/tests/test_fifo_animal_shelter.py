from fifo_animal_shelter import __version__
from fifo_animal_shelter.fifo_animal_shelter import *

def test_version():
    assert __version__ == '0.1.0'


# testing Animal_enqueue method against "cat" or "dog" inputs, also, testing against random inputs

def test_Animal_enqueue():

    animals = AnimalShelter()
    assert animals.Animal_enqueue('sugar','cat') == 'Successfully added the animal'
    assert animals.front.name == 'sugar'
    assert animals.rear.name == 'sugar'
    assert animals.Animal_enqueue('shawerma','dog') == 'Successfully added the animal'
    assert animals.front.name == 'sugar'
    assert animals.rear.name == 'shawerma'
    assert animals.Animal_enqueue('abd','human') == 'your input should only be a cat or a dog'
    assert animals.front.name == 'sugar'
    assert animals.rear.name == 'shawerma'

# testing Animal_dequeue method against empty instance, values that aren't 'cat' or 'dog', or when there is no
# more "dog" and "cat", after the shelter is empty, i tested the enqueue and dequeue again, just to make sure
# everything is working properly

def test_Animal_dequeue():
    animals = AnimalShelter()
    assert animals.Animal_dequeue('human') == None
    assert animals.Animal_dequeue('cat') == None
    animals.Animal_enqueue('sugar','cat')
    animals.Animal_enqueue('shawerma','dog')
    animals.Animal_enqueue('caramel','cat')
    animals.Animal_enqueue('banana','dog')
    assert animals.Animal_dequeue('cat') == 'sugar'
    assert animals.Animal_dequeue('cat') == 'caramel'
    assert animals.Animal_dequeue('cat') == None
    assert animals.Animal_dequeue('dog') == 'shawerma'
    assert animals.Animal_dequeue('dog') == 'banana'
    assert animals.Animal_dequeue('dog') == None
    animals.Animal_enqueue('argon','dog')
    animals.Animal_enqueue('biter','cat')
    assert animals.Animal_dequeue('cat') == 'biter'
    assert animals.Animal_dequeue('cat') == None
    assert animals.Animal_dequeue('dog') == 'argon'