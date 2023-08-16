from typing import List

def min_rotated_search(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    mid = right // 2

    while mid <= right and left <= right:

        if nums[left] <= nums[mid] <= nums[right]:
            return nums[left]
        
        elif nums[left] <= nums[mid] >= nums[right]:
            if nums[mid] > nums[mid] + 1:
                return nums[mid] + 1
            else:
                mid += 1

        else:
            left += 1


if __name__ == '__main__':
    res = min_rotated_search([1])
    print(res)

    
    