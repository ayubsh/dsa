# Type: Merge sorted
# Description: Merge sort is an efficient, stable, comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the implementation preserves the input order of equal elements in the sorted output.

# Time Complexity: O(n log n)
# Space Complexity: O(n)

#explain why merge sort is O(n log n)
#merge sort is a divide and conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    print(left, right)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        print(result)
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

sorted = merge_sort([3, 2, 1])
print(sorted)
