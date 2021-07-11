from insertion_sort import __version__
from insertion_sort.insertion import insertionSort

def test_version():
    assert __version__ == '0.1.0'

def test_insertionSort():
    assert insertionSort([8,4,23,42,16,15]) == [4, 8, 15, 16, 23, 42]
    assert insertionSort([20,18,12,8,5,-2]) == [-2, 5, 8, 12, 18, 20]
    assert insertionSort([5,12,7,5,5,7]) ==[5, 5, 5, 7, 7, 12]
    assert insertionSort ([2,3,5,7,13,11]) == [2,3,5,7,11,13]