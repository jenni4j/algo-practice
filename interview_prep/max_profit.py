from typing import List

def getMaximumProfit(price: List[int], profit: List[int]) -> int:
    n = len(price)
    if n < 3:
        return -1

    max_profit = [-1] * n
    
    for i in range(n):
        max_profit[i] = profit[i]

        for j in range(i):
            if price[i] > price[j]:
                max_profit[i] = max(max_profit[i], max_profit[j] + profit[i])
    
    result = max(max_profit)

    if result < 0:
        return -1
    else:
        return result

if __name__ == '__main__':
    res = getMaximumProfit([1,5,3,4,6], [2,3,4,5,6])
    print(res)