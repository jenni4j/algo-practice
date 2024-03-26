from typing import List

def solution(firstArray: List[int], secondArray: List[int], target: int) -> int:
    if len(firstArray) > len(secondArray):
        smallest_array = secondArray
        other_array = firstArray
    else:
        smallest_array = firstArray
        other_array = secondArray

    result = 0
    remainders = {}
    
    for i in range(len(smallest_array)):
        cum_sum = smallest_array[i]
        if cum_sum >= target:
            continue
        j = i + 1
        while cum_sum < target and j < len(smallest_array):
            remainder = target - cum_sum
            count = remainders.get(remainder, 0)
            remainders[remainder] = count + 1
            cum_sum += smallest_array[j]
            j += 1
        
    for n in range(len(other_array)):
        cum_sum = other_array[i]
        remainder = target - cum_sum
        for k in remainders.keys():
            if k == remainder:
                result += remainders[k]
    return result