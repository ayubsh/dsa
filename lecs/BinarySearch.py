import math

def bs_list(haystack: [int], needle: int) -> bool:
    lo, hi = 0, len(haystack)

    while lo < hi:
        mid = math.floor(lo + (hi - lo) / 2)
        print(haystack[mid])
        if needle == haystack[mid]:
            print("yay", haystack[mid])
            return True
        elif needle > haystack[mid]:
            lo = mid + 1
        else:
            hi = mid

    return False

print(bs_list([1,2,3,4,5,6,7,8], 6))
print(bs_list([1,2,3,4,5,6,7,8], 8))
