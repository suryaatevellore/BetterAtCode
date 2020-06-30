from typing import List

class Solution:
    def __init__(self):
        self.number_of_ways = 0

    def change(self, amount: int, coins: List[int]) -> int:
       dp = [0] * (amount+1)

       dp[0] = 1
       for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]

