from typing import List

def max_profit_threes_first(prices: List[int], profit: List[int]) -> int:

    combined = []
    indices = range(0, len(prices))
    max_profit = 0

    # zip the two lists using zip() function
    data = list(zip(indices, prices))

    data.sort(key=lambda x: x[1]) 

    print(data)
    
    for i in range(len(data) - 2):
        if data[i][0] < data[i + 1][0] and data[i + 1][0] < data[i + 2][0]:
            max_profit = max(max_profit, profit[data[i][0]] + profit[data[i + 1][0]] + profit[data[i + 2][0]])

    return max_profit



def max_profit_threes(prices: List[int], profit: List[int]) -> int:
    left = 0
    right = len(prices) - 1
    max_profit = -1

    
    while left < right:
        for mid in range(left + 1, right):
            if prices[left] < prices[mid] and prices[mid] < prices[right] and prices[left] < prices[right]:
                curr_profit = profit[left] + profit[mid] + profit[right]
                max_profit = max(max_profit, curr_profit)

        left += 1
    
    left = 0
    right = len(prices) - 1

    while right > 0:
        for mid in range(left + 1, right):
            if prices[left] < prices[mid] and prices[mid] < prices[right] and prices[left] < prices[right]:
                curr_profit = profit[left] + profit[mid] + profit[right]
                max_profit = max(max_profit, curr_profit)

        right -= 1
        
    return max_profit

def max_profit_threes_two(prices: List[int], profit: List[int]) -> int:
    n = len(prices)
    max_profit = 0

    for i in range(n):
        max_profit_i = 0
        for j in range(i + 1, n):
            if prices[j] > prices[i]:
                max_profit_i = max(max_profit_i, profit[j])
        for k in range(i + 2, n):
            if prices[k] > prices[i + 1]:
                max_profit = max(max_profit, max_profit_i + profit[k])

    return max_profit


if __name__ == '__main__':
    res1 = max_profit_threes([1,5,3,4,6], [2,3,4,5,6])
    res2 = max_profit_threes([9,8,7,6], [2,3,4,5])
    res3 = max_profit_threes([2,5,3,8,9,10], [12,5,2,8,45,60])
    res4 = max_profit_threes([2,5,3,8,10,1], [12,5,2,8,45,60])
    res5 = max_profit_threes_two([10,1,2,3,4], [1,100,200,5,300])
    print(res1, res2, res3, res4, res5)

    