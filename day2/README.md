# Reverse an Array
Write a function called insertShiftArray which takes an array and a variable as inputs. Without utilizing any of the built-in methods available to your language, return an array with the element inserted at the array's center

## Whiteboard Process
1. Problem Domain:

> define a function that takes two arguments, one is an array and one is a value, then, insert that value at the middle index without using any built-in methods

*****************************
2. In/Out

**In** => Array of n elements and a Value

**Out** => Array of n+1 elements, the extra element is the input value, that is located at the array's center
*****************************
3. Edge cases:

* first input is not an array
* empty array
*****************************
4. Visulization

**In** => ```[2,4,6,-8], 5```

**Out** => ```[2,4,5,6,-8]```

**In** => ```[42,8,15,23,42], 16```

**Out** => ```[42,8,15,16,23,42]```

**In** => ```[], 16```

**Out** => ```[16]```

**In** => ```5, 16```

**Out** => ```the first input is not an array```

*****************************

5. Big-O

time Complexity => O(1)

space Complexity => O(1)

*****************************

6. Algortihm:

    1. check if the first input is an array or not
    2. locate the array's center
    3. insert the second input in the middle index of the array, then return it

*****************************

7. Pseudo Code
    * if input1 type not array, return error
    * define middle = len(input1)/2 if input1 length is even, or middle = len(input1)/2 + 1 if input1 length is odd
    * insert input2 at the middle index

*****************************

8. Code
```python
def insertShiftArray (input1, input2):
  if(type(input1) != list):
    return 'the first input is not an array'
  if(len(input1)%2 == 0):
    a = len(input1)//2
  else:
    a = len(input1)//2 + 1
  b = input1[:a] + [input2] + input1[a:]
  return(b)
```

*****************************

9. Verification: 

In: input1 = [7, 'a', 6, -4],'z'
expected Out: [-4, 6,'z','a', 7]

def insertShiftArray (input1, input2):     
  // input1 = [7, 'a', 6, -4], input2 = 'z'     
  if(type(input1) != list): # False     
    return 'the first input is not an array'     
  if(len(input1)%2 == 0): # True     
    a = len(input1)//2 # a = 2     
  else:     
    a = len(input1)//2 + 1     
  b = input1[:a] + [input2] + input1[a:]      
  // b = [7,'a'] + ['z'] + [6,-4] = [7,'a','z',6,-4]     
  return(b)     

  ## Approach & Efficiency
  
  for the approach, i created a function that takes two inputs, one is an array, and the other is any value, then returned a new array with the value inserted at the array's middle index

Big O:

* time => from the shifting procedure it should loop over half of the array length, it gives an O(N)

* space => the stored values are inside an array, and this array is O(1) because the array's length increased be a known amount, that is 1, and does not depend on any looping