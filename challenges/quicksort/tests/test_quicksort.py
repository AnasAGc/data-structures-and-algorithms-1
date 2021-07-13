from quicksort import __version__
from quicksort.quicksort import Partition,QuickSort,Swap

def test_version():
    assert __version__ == '0.1.0'

def test_quicksort():
    a = [8,4,23,42,16,15]
    QuickSort(a,0,len(a)-1)
    assert a == [4, 8, 15, 16, 23, 42]
    reversed_array = [20,18,12,8,5,-2]
    QuickSort(reversed_array,0,len(reversed_array)-1)
    assert reversed_array == [-2, 5, 8, 12, 18, 20]
    uniques = [5,12,7,5,5,7]
    QuickSort(uniques,0,len(uniques)-1)
    assert uniques == [5, 5, 5, 7, 7, 12]
    nearly_sorted = [2,3,5,7,13,11]
    QuickSort(nearly_sorted,0,len(nearly_sorted)-1)
    assert nearly_sorted == [2, 3, 5, 7, 11, 13]