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
			if a + nums[left] + nums[right] == 0:
				res.append([a, nums[left], nums[right]])
				left += 1
				right -= 1
				while nums[left] == nums[left - 1]:
					left += 1
				while nums[right] == nums[right + 1]:
					right -= 1
			elif a + nums[left] + nums[right] < 0:
				left += 1
			else:
				right -= 1

	return res

if __name__ == '__main__':
	res = three_sum([-1, 1, 0, 2, 3])
	print(res)