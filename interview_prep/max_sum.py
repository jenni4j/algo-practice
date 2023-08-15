
def max_sum_finder(arr: list[int], n: int, k: int) -> int:
	max_sum = 0

	for i in range(n - k + 1):
		curr_sum = 0
		for j in range(k):
			curr_sum += arr[i + j]
		max_sum = max(curr_sum, max_sum)
		

def max_sum_window(arr: list[int], n: int, k: int) -> int:
	if n < k:
		return None
	
	window_sum = sum(arr[:k])
	
	max_sum = sum(arr[:k])
	
	for i in range(n - k):
		window_sum = window_sum - arr[i] + arr[i + k]
		max_sum = max(window_sum, max_sum)

	return max_sum
		

if __name__ == '__main__':
	res = max_sum_window([1, 4, 2, 10, 2, 3, 1, 0, 20], 9, 4)
	res_again = max_sum_window([5, 2, -1, 0, 3], 5, 3)
	print(res)
