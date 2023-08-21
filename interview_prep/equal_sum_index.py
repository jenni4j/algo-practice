
# [1, 3, 2, 3, 1]
# [1, 3, 2, 1, 3]
# [1, 3, 2, 4]
# [4, 2, 3, 1]
# []

from typing import List

def index_finder(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    left_sum = nums[left]
    right_sum = nums[right]

    while left < right:
        diff = abs(right - left) 
        if left_sum == right_sum and diff == 2:
            return left + 1
        elif left_sum == right_sum and diff != 2:
            left += 1
            right -= 1
            left_sum += nums[left]
            right_sum += nums[right]
        elif left_sum < right_sum:
            left += 1
            left_sum += nums[left]
        else:
            right -= 1
            right_sum += nums[right]

if __name__ == '__main__':
    res = index_finder([5, 3, 5])
    print(res)