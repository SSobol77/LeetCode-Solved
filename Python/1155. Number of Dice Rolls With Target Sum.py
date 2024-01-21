# 1155. Number of Dice Rolls With Target Sum

# Topic

'''
# Task:
-------
You have n dice, and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) 
to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, 
return it modulo 10^9 + 7.

Example 1:
Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.

Example 2:
Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:
Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 10^9 + 7.

Constraints:
1 <= n, k <= 30
1 <= target <= 1000

'''
# Solution:

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7  # Module to prevent integer overflow

        # Initialize the dynamic programming table
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # Base case: 0 ways to reach sum 0 with 0 dice

        for dice in range(1, n + 1):
            for sum_ in range(1, target + 1):
                # The current cell is updated based on the sum of two values:
                # 1. The number of ways to reach the previous sum with the current number of dice
                # 2. The number of ways to reach the sum - 1 with one less dice
                dp[dice][sum_] = dp[dice][sum_ - 1] + dp[dice - 1][sum_ - 1]

                # If the sum exceeds the number of faces on the dice,
                # subtract the number of ways to achieve an unreachable sum
                if sum_ > k:
                    dp[dice][sum_] -= dp[dice - 1][sum_ - k - 1]

                # Apply modulo operation to keep values within the MOD limit
                dp[dice][sum_] %= MOD

        return dp[n][target]

# Test cases
solution = Solution()
print(solution.numRollsToTarget(1, 6, 3))  # Output: 1
print(solution.numRollsToTarget(2, 6, 7))  # Output: 6
print(solution.numRollsToTarget(30, 30, 500))  # Output: 222616187



# Description:
'''
In this solution, we use dynamic programming to build a dp table, where dp[dice][sum_] stores
the number of ways to achieve the sum_ sum using dice dice. The main improvement is that we take 
into account the previous values to update the current values, which significantly reduces the 
number of calculations needed. This makes the algorithm more efficient for large values of n, k,
and target.

'''
