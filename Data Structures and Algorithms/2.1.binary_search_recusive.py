# Binary search is a search algorithm that works on sorted arrays.

# TODO 1: Write a function that takes an array and a number as input and returns the index of the number in the array.
#   @def binarySearch(arr, arrLen, search_value):
#   @param arr: list of numbers
#   @param arrLen: length of the list
#   @param search_value: number to be searched
def binarySearch(arr, start, end, search_value):
    if start <= end:
        mid = (start + end) // 2
        if search_value == arr[mid]:
            return mid
        elif search_value < arr[mid]:
            return binarySearch(arr, start, mid - 1, search_value)
        else:
            return binarySearch(arr, mid + 1, end, search_value)
    return -1


arr = [2, 3, 4, 10, 40]
end = len(arr)
searchValue = int(input("Enter the element to be searched: "))
result = binarySearch(arr, 0, end - 1, searchValue)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
