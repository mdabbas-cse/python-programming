def linear_search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
n = len(arr)
x = int(input("Enter the element to be searched: "))
result = linear_search(arr, n, x)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
