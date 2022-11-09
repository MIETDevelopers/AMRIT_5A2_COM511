'''Purpose:Write a program to perform searching activity using Linear and binary search.
Author:AMRIT PAL SINGH
'''
def LinearSearch(array, n, k):

    for j in range(0, n):

        if (array[j] == k):

            return j

    return -1

 
array = [1, 3, 5, 7, 9]

k = 7
print("Searching element",k,"using linear search")
n = len(array)

result = LinearSearch(array, n, k)

if(result == -1):

    print("Element not found")

else:

    print("Element found at index:",result)

print()
def binarySearch(arr, k, low, high):
   
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:

            low = mid + 1
        else:

            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9]

k = 3
print("Searching element",k,"using binary search")

result = binarySearch(arr, k, 0, len(arr)-1)

if result != -1:

    print("Element is present at index " + str(result))

else:

    print("Not found")