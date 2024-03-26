from typing import List

def single_array_pairs(arr: List[int], k: int) -> int:

    # Find the number of subarrays with sum exactly equal to k in a given array arr
    # Solution is O(n)

    prev_sum = {}

    curr_sum = 0

    res = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum == k:
            res += 1

        # why are we checking if curr_sum - k is in prev_sum? If the diff is in the map, we can remove the
        # elements that made up that difference from the array and get another valid subarray with the k target value
        if (curr_sum - k) in prev_sum.keys():
            res += prev_sum[curr_sum - k]
        
        prev_sum[curr_sum] = prev_sum.get(curr_sum, 0) + 1

    return res

if __name__ == '__main__':
    res = single_array_pairs([10, 2, -2, -20, 10], -10)
    print(res)
