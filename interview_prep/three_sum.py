from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
	res = []
	nums.sort()

	for i, a in enumerate(nums):
		if i > 0 and a == nums[i - 1]:
			continue

		left = i + 1
		right = len(nums) - 1

		while left < right:
			three_sum = a + nums[left] + nums[right]
			if three_sum > 0:
				right -= 1
			elif three_sum < 0:
				left += 1
			else:
				res.append([a, nums[left], nums[right]])
				left += 1
				while nums[left] == nums[left - 1] and left < right:
					left += 1

	return res

if __name__ == '__main__':
	res = three_sum([-1, 1, 0, 2, 3])
	print(res)