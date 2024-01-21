# 322. Coin Change

# Topic: Array, Dynamic Programming, Breadth-First Search.


'''
# Task:
--------
You are given an integer array coins representing coins of different denominations and an integer 
amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4


# Testcase:
------------
[1,2,5]
11
[2]
3
[1]
0


# Code:
-------
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
     

'''
# Solution:
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the DP array with a value greater than the possible maximum
        # This value is chosen as amount + 1, since it's not possible to have more coins than the amount itself
        dp = [amount + 1] * (amount + 1)

        # Base case: No coins needed to make amount 0
        dp[0] = 0

        # Iterate over each amount from 1 to the target amount
        for a in range(1, amount + 1):
            # Check each coin in the coins list
            for coin in coins:
                # If it's possible to pick this coin (amount is greater or equal to coin value)
                if a - coin >= 0:
                    # Update the DP array for this amount
                    # The new value is the minimum between the current value and
                    # 1 (for picking this coin) plus the best known way to make up the remaining amount
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        # If dp[amount] is still amount + 1, it means it's impossible to make up this amount with the given coins
        return dp[amount] if dp[amount] != amount + 1 else -1

# Test cases
solution = Solution()
print(solution.coinChange([1, 2, 5], 11))  # Expected output: 3
print(solution.coinChange([2], 3))         # Expected output: -1
print(solution.coinChange([1], 0))         # Expected output: 0


'''
Description:
To solve the Coin Change problem, we can use dynamic programming. The approach involves creating a DP array 
where each element dp[i] represents the fewest number of coins needed to make up the amount i. The idea is 
to build up the solution for the total amount from the solutions of smaller amounts.

'''
