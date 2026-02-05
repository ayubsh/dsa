# Type: Insertion sorted
# Description: Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j - 1
    return arr

sorted = insertion_sort([3, 2, 1])
print(sorted)
