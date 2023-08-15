from typing import List

def rotated_search(nums: List[int], target: int) -> int:
	left, right = 0, len(nums) - 1
    
	while left <= right:
		mid = (left + right) // 2
		if target == nums[mid]:
			return mid

		elif nums[mid] >= nums[left]:
			if nums[left] <= target <= nums[mid]:
				right = mid - 1
			else:
				left = mid + 1

		else:
			if nums[mid] <= target <= nums[right]:
				left = mid + 1
			else:
				right = mid - 1			
	return -1

if __name__ == '__main__':
	res = rotated_search([4,5,6,7,0,1,2], 6)
	print(res)
		
		



		