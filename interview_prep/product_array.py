from typing import List

def product_array(nums: List[int]) -> List[int]:
    
	answer = [None] * len(nums)
	prefix = 1
	postfix = 1

	for i in range(len(nums)):
		answer[i] = prefix
		prefix *= nums[i]

	for i in range(len(nums)):
		j = len(nums) - i - 1
		answer[j] *= postfix
		postfix *= nums[j]

	return answer


if __name__ == '__main__':
	res = product_array([1,2,3,4])
	print(res)
		

