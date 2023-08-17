from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    index_map = {}
    for i in range(len(nums)):
        remainder = target - nums[i]
        if  index_map.get(remainder) is not None:
            return [i, index_map[remainder]]
        else:
            index_map[nums[i]] = i 


if __name__ == '__main__':
    res = two_sum([2,7,11,15], 9)
    print(res)