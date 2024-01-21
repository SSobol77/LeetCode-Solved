"""
# 446. Arithmetic Slices II - Subsequence.


# Topic: Array, Dynamic Programming.


# Task:
---------
Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference 
between any two consecutive elements is the same.

    For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
    For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.

A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of 
the array.

    For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].

The test cases are generated so that the answer fits in 32-bit integer.

 

Example 1:

Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

Example 2:

Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.

Constraints:

1  <= nums.length <= 1000
-2^31 <= nums[i] <= 2^31 - 1


# Testcase:
-------------------
[2,4,6,8,10]
[7,7,7,7,7]


# Code:
------------------
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
   

"""
# Solution:

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0  # If the array has less than 3 elements, there can't be any arithmetic subsequences
        
        dp = [defaultdict(int) for _ in range(n)]  # Create a 2D dynamic programming array
        total_count = 0  # Initialize a variable to keep track of the total count of arithmetic subsequences
        
        for i in range(n):  # Iterate through the array
            for j in range(i):  # For each element, iterate through the previous elements
                diff = nums[i] - nums[j]  # Calculate the difference between elements at indices i and j
                dp[i][diff] += 1  # Increment the count of subsequences ending at index i with difference diff
                
                if diff in dp[j]:  # If the difference is already present in the previous index's dp
                    dp[i][diff] += dp[j][diff]  # Add the count from the previous index to the current index
                    total_count += dp[j][diff]  # Add the count to the total count
        
        return total_count  # Return the total count of arithmetic subsequences

# Description
'''
This code uses a 2D dp array, where dp[i][diff] represents the number of arithmetic subsequences ending at 
index i with a common difference of diff. We iterate through the array, calculate the difference between 
pairs of elements, and update the dp array accordingly. Finally, we sum up all the counts in the dp array 
to get the total number of arithmetic subsequences.

You can use this Solution class to call the numberOfArithmeticSlices method and pass in your nums array as 
an argument to get the desired result.

'''
