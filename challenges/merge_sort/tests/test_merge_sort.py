from merge_sort import __version__
from merge_sort.merge_sort import Merge, Mergesort

def test_version():
    assert __version__ == '0.1.0'
def test_merge_sort():
    a = [8,4,23,42,16,15]
    Mergesort(a)
    assert a == [4, 8, 15, 16, 23, 42]
    reversed_array = [20,18,12,8,5,-2]
    Mergesort(reversed_array)
    assert reversed_array == [-2, 5, 8, 12, 18, 20]
    uniques = [5,12,7,5,5,7]
    Mergesort(uniques)
    assert uniques == [5, 5, 5, 7, 7, 12]
    nearly_sorted = [2,3,5,7,13,11]
    Mergesort(nearly_sorted)
    assert nearly_sorted == [2, 3, 5, 7, 11, 13]