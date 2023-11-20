from typing import List 

def rob(nums: List[int]) -> int:
    rob1, rob2 = 0, 0

    # imagine array is like this [rob1, rob2, n, n+1, ...]
    # [2, 1, 1, 2]
    for n in nums:
        temp = max(rob1 + n, rob2) # temp = 3
        rob1 = rob2 # rob1 = 2
        rob2 = temp # rob2 = 3
    return rob2