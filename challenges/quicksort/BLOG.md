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

1. set the pivot to be the value to the far right (15)

2. find the position for the value (15), using multiple steps to assure that every element to the right of 15 is smaller than 15, and every element to the left of 15 is larger than 15

3. now, this is the new position for 15, and it's the sorted position.

4. now we have two portions, left and right of the first pivot (15), lets start with the left one

5. set a new pivot , that is the value to the far right (4)

6. find the position for the value (4), using multiple steps to assure that every element to the right of 4 is smaller than 4, and every element to the left of 4 is larger than 4

7. now, this is the new position for 4, and it's the sorted position.

8. set a new pivot , that is the value to the far right (8)

9. find the position for the value (8), using multiple steps to assure that every element to the right of 8 is smaller than 8, and every element to the left of 8 is larger than 8, we don't have any non-pivot or end values around the 8, so the 8 is currently in it's correct position.

10. now lets go to the left side, and set a new pivot , that is the value to the far right (15)

11. find the position for the value (15), using multiple steps to assure that every element to the right of 15 is smaller than 15, and every element to the left of 15 is larger than 15

12. now, this is the new position for 15, and it's the sorted position.

13. set a new pivot , that is the value to the far right (16)

14. find the position for the value (16), using multiple steps to assure that every element to the right of 16 is smaller than 16, and every element to the left of 16 is larger than 16

15. now, this is the new position for 16, and it's the sorted position.

16. set a new pivot , that is the value to the far right (42)

17. find the position for the value (42), using multiple steps to assure that every element to the right of 42 is smaller than 42, and every element to the left of 42 is larger than 42, we don't have any non-pivot or end values around the 42, so the 42 is currently in it's correct position.

18. since all the values are in their correct position, we can combine then again, and this will give a sorted array.


## Efficiency

> Time: O(n^2)

due to the recursive call, we are looping over every element inside the array n times, and we have n elements inside the array, so it's O(n^2)

> Space: O(n)

we have arrays depending on for loop to fill