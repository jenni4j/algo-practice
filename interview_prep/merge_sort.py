# insert and sort method

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]: 
	for i in range(n):
		nums1[m + i] = nums2[i]
	
	nums1.sort()

	return nums1


# two pointers method

def merge_pointers(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:

	i = 0
	j = 0
	k = 0
	res = [None] * (m + n)

	while i < m and j < n:
		if nums1[i] < nums2[j]:
			res[k] = nums1[i]
			i += 1
			k += 1

		else:
			res[k] = nums2[j]
			j += 1
			k += 1
	
	if i < m:
		res[k:] = nums1[i:]

	if j < n:
		res[k:] = nums2[j:]

	return res
	

if __name__ == '__main__':
	res = merge_pointers([1,2,3,8], 4, [2,5,6], 3)
	print(res)