
def max_sum_finder(arr: list[int], n: int, k: int) -> int:
    max_sum = 0
    for i in range(n - k + 1):
        curr_sum = 0
        for j in range(k):
            curr_sum += arr[i + j]
        max_sum = max(curr_sum, max_sum)


    return max_sum


if __name__ == '__main__':
    res = max_sum_finder([1, 4, 2, 10, 2, 3, 1, 0, 20], 9, 4)
    print(res)
