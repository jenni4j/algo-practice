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


def min_rotated_search_ii(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    res = nums[0]

    while left < right:
        if nums[left] < nums[right]:
            res = min(res, nums[left])
            break
        
        mid = right // 2
        res = min(res, nums[mid])

        if nums[mid] > nums[left]:
            left = mid + 1
        else:
            right = mid - 1



    
    return res


if __name__ == '__main__':
    res = min_rotated_search([3, 4, 5, 1, 2])
    print(res)

    
    