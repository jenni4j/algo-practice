from typing import List

def max_product(nums: List[int]) -> int: 
    res = max(nums)
    currMin, currMax = 1, 1

    for n in nums:
        currMin, currMax = min(n * currMax, n * currMin, n), max(n * currMax, n * currMin, n)
        res = max(res, currMax)

    return res


if __name__ == '__main__':
    res = max_product([-3,-1,-1])
    print(res)