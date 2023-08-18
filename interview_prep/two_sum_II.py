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


if __name__ == '__main__':
	res = two_sum_ii([2, 3, 4], 6)
	print(res)