# 300. Longest Increasing Subsequence.

# Topic: Array, Binary Search, Dynamic Programming.

"""
# Task:
-----------------
Given an integer array nums, return the length of the longest strictly increasing
subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?


# Testcase:
[10,9,2,5,3,7,101,18]
[0,1,0,3,2,3]
[7,7,7,7,7,7,7]

# Code:
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
"""
# Solution:

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0  # If the input array is empty, return 0

        # Create an array 'lis' of the same length as 'nums', initialized with 1s.
        # lis[i] will hold the length of the longest increasing subsequence
        # ending with nums[i]
        lis = [1] * len(nums)

        # Iterate through the array 'nums'
        for i in range(1, len(nums)):
            # For each element nums[i], check all previous elements nums[j]
            for j in range(i):
                # If nums[i] is greater than nums[j], it can be appended to the 
                # increasing subsequence ending at nums[j]
                if nums[i] > nums[j]:
                    # Update lis[i] to be the maximum of its current value
                    # and the length of the increasing subsequence ending at nums[j] plus 1
                    lis[i] = max(lis[i], lis[j] + 1)

        # Return the maximum value in lis, which represents the length
        # of the longest increasing subsequence in 'nums'
        return max(lis)

# Test cases
sol = Solution()
test_cases = [
    [10,9,2,5,3,7,101,18],
    [0,1,0,3,2,3],
    [7,7,7,7,7,7,7]
]

# Calculate the length of the longest increasing subsequence for each test case
outputs = [sol.lengthOfLIS(tc) for tc in test_cases]
outputs



# Description:
'''
The implemented Python code successfully solves the Longest Increasing Subsequence problem for the given test cases. The outputs are as follows:

    For the input [10,9,2,5,3,7,101,18], the length of the longest strictly increasing subsequence is 4. The subsequence is [2,3,7,101].
    For the input [0,1,0,3,2,3], the length of the longest strictly increasing subsequence is also 4. A possible subsequence is [0,1,2,3].
    For the input [7,7,7,7,7,7,7], the length of the longest strictly increasing subsequence is 1, since all elements are the same.

The solution follows a dynamic programming approach and works efficiently for the given input constraints
'''