# Binary search is a search algorithm that works on sorted arrays.

# TODO 1: Write a function that takes an array and a number as input and returns the index of the number in the array.
#   @def binarySearch(arr, arrLen, search_value):
#   @param arr: list of numbers
#   @param arrLen: length of the list
#   @param search_value: number to be searched
def binarySearch(arr, arrLen, search_value):
    start = 0
    end = arrLen - 1

    while start <= end:
        mid = (start + end) // 2
        if search_value == arr[mid]:
            return mid
        elif search_value < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


arr = [2, 3, 4, 10, 40]
n = len(arr)
searchValue = int(input("Enter the element to be searched: "))
result = binarySearch(arr, n, searchValue)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
