# Quicksort

QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 

1. Always pick first element as pivot.

2. Always pick last element as pivot (implemented below)

3. Pick a random element as pivot.

4. Pick median as pivot.

The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

## Tracing

![1](resources/1.png)
![1](resources/2.png)
![1](resources/3.png)


## Efficiency

> Time: O(n^2)

due to the recursive call, we are looping over every element inside the array n times, and we have n elements inside the array, so it's O(n^2)

> Space: O(n)

we have arrays depending on for loop to fill