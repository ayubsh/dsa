from typing import List

def bubble(l: List[int]) -> List[int]:
    for i in range(len(l)):
        for j in range(len(l)):
            if(l[i] < l[j]):
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
    return l

print(bubble([1,4,2,5,7,2]))

