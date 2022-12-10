# insertion sorting
# 1. Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
# 2. The array is virtually split into a sorted and an unsorted part.
def insertionSort(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index
        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = current_value
    return alist


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(insertionSort(alist))
