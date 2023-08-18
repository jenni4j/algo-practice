from typing import List

def two_sum_ii(numbers: List[int], target: int) -> List[int]:
    # remainder is key, i is value
	index_map = {}
	for i in range(len(numbers)):
		remainder = target - numbers[i]
		if index_map.get(remainder) is None:
			index_map[numbers[i]] = i
		else:
			return [index_map[remainder] + 1, i + 1]
		
def two_sum_pointer(numbers: List[int], target: int) -> List[int]:
	left = 0
	right = len(numbers) - 1
	while left <= right:
		if numbers[left] + numbers[right] == target:
			return [left, right]
		elif numbers[left] + numbers[right] < target:
			left += 1
		else:
			right -= 1

	return None




if __name__ == '__main__':
	res = two_sum_pointer([2, 3, 4], 6)
	print(res)