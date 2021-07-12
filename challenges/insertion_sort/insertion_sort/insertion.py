def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i-1
        temp = arr[i]

        while j>=0 and temp < arr[j]:
            j=j-1
        arr.pop(i)
        arr.insert(j+1,temp)

    return arr