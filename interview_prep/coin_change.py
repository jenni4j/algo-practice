from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    # [1, 3, 4, 5]  | 7
    dp = [amount + 1] * (amount + 1)
    # [7, 7, 7, 7, 7, 7, 7, 7]

    dp[0] = 0

    for a in range(1, amount + 1):
        # a = 7
        for c in coins:
            # c = 4
            if a - c >= 0:
                # dp[7] = min(dp[7], 1 + dp[3])
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != amount + 1 else - 1