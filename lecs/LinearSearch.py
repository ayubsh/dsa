def linear_search(haystack: [int], needle: int) -> bool:
    for i in range(len(haystack)):
        if needle == haystack[i]:
            return True

    return False


print(linear_search([1,2,3,4,5], 410))
