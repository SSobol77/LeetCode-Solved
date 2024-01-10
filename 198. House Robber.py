# 198. House Robber.

# Topic: Array, Dynamic Programming.

'''
# Task:
-------
You are a professional robber planning to rob houses along a street. Each house has a certain 
amount of money stashed, the only constraint stopping you from robbing each of them is that 
adjacent houses have security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum 
amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400


# Testcase:
------------
[1,2,3,1]
[2,7,9,3,1]


# Code:
-------
class Solution:
    def rob(self, nums: List[int]) -> int:
        
    
'''
# Solution:

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Get the number of houses
        n = len(nums)
        
        # Handle base cases
        if n == 0: 
            return 0  # No houses to rob
        if n == 1: 
            return nums[0]  # Only one house to rob

        # Initialize the dynamic programming (DP) array
        # dp[i] will store the maximum amount that can be robbed up to the i-th house
        dp = [0] * n
        dp[0] = nums[0]  # The maximum amount from the first house is its own value
        dp[1] = max(nums[0], nums[1])  # The maximum from the first two houses

        # Fill the DP array for each subsequent house
        for i in range(2, n):
            # For each house, you have two choices:
            # 1. Rob this house, and add its value to the max amount from two houses back
            # 2. Skip this house, and take the max amount from the previous house
            # Choose the option that gives the maximum amount
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # The last element in the DP array contains the maximum amount that can be robbed
        return dp[-1]

# Test cases
solution = Solution()
print(solution.rob([1, 2, 3, 1]))  # Expected output: 4
print(solution.rob([2, 7, 9, 3, 1]))  # Expected output: 12


'''
Description:
To solve the House Robber problem, we can use dynamic programming to find the maximum amount 
of money that can be robbed without triggering the security systems. The idea is to create a 
dynamic array where each element represents the maximum amount that can be robbed up to that 
house.

The dynamic programming relation can be defined as follows: For each house i, the robber has 
two options: either rob this house or skip it. If the robber robs house i, they cannot rob 
house i-1 but can take the money from house i plus the maximum amount from house i-2. If the 
robber skips house i, the maximum amount is the same as the maximum amount from house i-1.

'''
