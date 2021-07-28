## Code Link

[Code](hashmap_left_join/hashmap_left_join.py)

# Hashmap LEFT JOIN

The Hashmap LEFT JOIN returns an array that contains all the keys and the values from the left has table, with the values for the right hash tables if they have the same key

## Challenge

Write a function called left join, that takes two hash maps as an input, and returns an array that has the keys and values for the left hashmap, and the values from the right hashmap if they have the same key

## Whiteboard

![image](resources/cc33.png)

## Approach & Efficiency

for tha approach taken, i used a new hash table and an array, for the new hash table, i stored the keys as the keys from the left hash table, and the values as an array with two elements, the first one is the value for the key in the left hash table, and the second one is either a NULL if the key does not exist inside the second hash table, or the value if it exists. then, i used a for loop for the keys inside the new hash table, in order to get all the keys and the values, store them inside the array and return the array.

time complexity: the time complexity is O(n), we have a for loop inside the function.

space complexity: the space complexity for the function is also O(n), we have an array depending on the output of a for loop.

## Solution

for the solution, i decided to create a new hash table, and a new array of which the values are going to be returned to it, the following block of code is the solution

```
def left_join(left_hash,right_hash):
    new = Hashtable(20)
    array = []
    for key in left_hash.keys:
        if right_hash.contains(key):
            new.add(key,[left_hash.get(key),right_hash.get(key)])
        else:
            new.add(key,[left_hash.get(key),'NULL'])
    for key in new.keys:
        subarray = [key, new.get(key)[0],new.get(key)[1]]
        array.append(subarray)
    return array
```