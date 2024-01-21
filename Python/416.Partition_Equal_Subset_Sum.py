"""
# 416. Partition Equal Subset Sum.

# Topic: Array, Dynamic Programming.

# Task:
-----------
Given an integer array nums, return true if you can partition the array into two subsets such 
that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100


# Testcase:
------------
[1,5,11,5]
[1,2,3,5]


# Code:
------------
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
      
"""
# Solution:
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd, it's not possible to split the array into two equal-sum subsets
        if total_sum % 2 != 0:
            return False

        # Calculate the sum of one subset (half of the total sum)
        subset_sum = total_sum // 2

        # Initialize a dynamic programming (DP) array
        # dp[i] indicates whether a subset with sum i can be formed from the elements in nums
        dp = [False] * (subset_sum + 1)
        dp[0] = True  # Base case: A subset with sum 0 is always possible (an empty subset)

        # Iterate through each number in nums
        for num in nums:
            # Iterate backwards through the DP array
            # This avoids using the same item multiple times and overwriting the DP array prematurely
            for i in range(subset_sum, num - 1, -1):
                # Update the DP array:
                # dp[i] is true if it was already true or if dp[i - num] was true
                # (which means a subset with sum (i - num) existed, and now including num forms a subset with sum i)
                dp[i] = dp[i] or dp[i - num]

        # The final answer is whether a subset with sum equal to subset_sum (half of the total sum) exists
        return dp[subset_sum]


# Description:
'''
To solve the "Partition Equal Subset Sum" problem, we can use Dynamic Programming. The task is essentially to determine 
if we can find a subset of nums whose sum is exactly half of the total sum of nums. If the total sum is odd, it's not 
possible to partition the array into two subsets with equal sum, so we return false in that case. If the sum is even, 
we check if there's a subset that sums up to half of the total sum.

Here's a detailed approach using Dynamic Programming:
--------------------------------------------------------
1. Calculate Total Sum: Compute the total sum of all elements in nums. If this sum is odd, return false immediately.

2. Check Subset Sum Problem: This problem can be reduced to a subset sum problem: Can we find a subset of 
   nums that sums up to total_sum / 2?

3. Dynamic Programming Approach:
    - Create a boolean DP table of size (total_sum / 2) + 1, where dp[i] will be true if there is a subset with sum i.
    - Initialize dp[0] as true because a sum of 0 is always possible (with an empty subset).
    - For each number in nums, update the DP table. For each element num, we iterate backwards from total_sum / 2 to 
      num, setting dp[j] to true if dp[j - num] is true.

4. Return Result: The answer will be the value in dp[total_sum / 2], indicating whether there's a subset with the desired sum.

In this code:
-------------------

- We first sum up all the elements in nums to get total_sum. If this sum is odd, we immediately return False, as it's 
  impossible to divide the array into two equal-sum subsets.
- We then determine the target subset sum, subset_sum, which is half of total_sum.
- A DP array dp is initialized with False values. Its size is subset_sum + 1 to include all possible sums from 0 to 
  subset_sum.
- The dp array is updated for each number in nums. The backward iteration is crucial as it ensures that each number 
  in nums is considered only once for each subset sum.
- For each num in nums, we check if a subset with a sum of i - num was possible (i.e., dp[i - num] is true). If it was, 
  then by adding num to this subset, we can now achieve a subset with a sum of i.
- Finally, dp[subset_sum] tells us whether it's possible to achieve a subset sum equal to subset_sum, thus determining 
  if the array can be partitioned into two subsets with equal sums.

'''
