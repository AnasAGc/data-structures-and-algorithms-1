from hashmap_left_join import __version__
from hashmap_left_join.hashmap_left_join import left_join
from hashmap_left_join.hashtable import Hashtable

import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_all_cases(left_hash_fixture, right_hash_fixture,empty_hash_fixture ):
    assert left_join(left_hash_fixture, right_hash_fixture) == [['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'], ['delight', 'employed', 'idle'], ['outfit', 'garp', 'NULL'], ['guide', 'usher', 'follow']]
    assert left_join(right_hash_fixture, left_hash_fixture) == [['fond', 'averse', 'enamored'], ['wrath', 'delight', 'anger'], ['delight', 'idle', 'employed'], ['guide', 'follow', 'usher'], ['flow', 'jam', 'NULL']]
    assert left_join(left_hash_fixture, empty_hash_fixture) == [['fond', 'enamored', 'NULL'], ['wrath', 'anger', 'NULL'], ['delight', 'employed', 'NULL'], ['outfit', 'garp', 'NULL'], ['guide', 'usher', 'NULL']]
    assert left_join(right_hash_fixture, empty_hash_fixture) == [['fond', 'averse', 'NULL'], ['wrath', 'delight', 'NULL'], ['delight', 'idle', 'NULL'], ['guide', 'follow', 'NULL'], ['flow', 'jam', 'NULL']]
    assert left_join(empty_hash_fixture, right_hash_fixture) == []
    assert left_join(empty_hash_fixture, left_hash_fixture) == []

@pytest.fixture
def left_hash_fixture():
    left_hash = Hashtable(10)
    left_hash.add('fond', 'enamored')
    left_hash.add('wrath', 'anger')
    left_hash.add('delight', 'employed')
    left_hash.add('outfit', 'garp')
    left_hash.add('guide', 'usher')
    return left_hash

@pytest.fixture
def right_hash_fixture():
    right_hash = Hashtable(10)
    right_hash.add('fond', 'averse')
    right_hash.add('wrath', 'delight')
    right_hash.add('delight', 'idle')
    right_hash.add('guide', 'follow')
    right_hash.add('flow', 'jam')
    return right_hash

@pytest.fixture
def empty_hash_fixture():
    empty_hash = Hashtable(10)
    return empty_hash