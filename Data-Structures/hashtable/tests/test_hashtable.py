from hashtable import __version__
import hashtable
from hashtable.hashtable import Hashtable
from hashtable.linked_list import LinkedList
def test_version():
    assert __version__ == '0.1.0'

def test_hash_table_generic():
    hashtable = Hashtable(1024)

    # testing for single input
    hashtable.add('ahmad', 25)
    hashtable.add('silent', True)

    assert hashtable.contains('ahmad') is True
    assert hashtable.contains('ahmadd') is False

    # testing for multiple inputs for a single bucket

    hashtable.add('hamad', 29)
    hashtable.add('listen', 'Hey man')

    assert hashtable.contains('ahmad') is True
    assert hashtable.contains('hamad') is True
    assert hashtable.contains('listen') is True
    assert hashtable.contains('silent') is True
    
    # check for duplicate input
    assert hashtable.add('ahmad',35) == 'key already exists'


    # testing the values

    assert hashtable.get('ahmad') == 25
    assert hashtable.get('hamad') == 29
    assert hashtable.get('dada') == None

