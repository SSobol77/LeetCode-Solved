# 53. Maximum Subarray.

# Topic: Array,Divide and Conquer, Dynamic Programming

'''
# Task:
-------
Given an integer array nums, find the subarray  with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
 
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer 
approach, which is more subtle.

# Testcase:
-----------
[-2,1,-3,4,-1,2,1,-5,4]
[1]
[5,4,-1,7,8]


# Code:
-------
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
'''
# Solution:
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize max_sum and current_sum with the first element of nums
        max_sum = current_sum = nums[0]

        # Iterate over the array starting from the second element
        for num in nums[1:]:
            # Update current_sum:
            # If current_sum is negative, it's better to start a new subarray from the current element
            # Otherwise, add the current element to the existing subarray
            current_sum = max(num, current_sum + num)

            # Update max_sum if the current_sum is greater than the max_sum found so far
            max_sum = max(max_sum, current_sum)

        # Return the maximum subarray sum found
        return max_sum

# Testing the solution
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Expected output: 6
print(sol.maxSubArray([1]))  # Expected output: 1
print(sol.maxSubArray([5,4,-1,7,8]))  # Expected output: 23




# Description:
'''
The main algorithm for this task remains the Kadan method, which is the fastest and most efficient way to find 
the maximum sum of a subarray. This method has a time complexity of O(n) and does not require additional memory, 
which makes it ideal for this task. 
This code sequentially traverses the nums array, updating the current_sum for each element. If current_sum becomes 
negative, it means that the current subarray will not increase the maximum amount, and current_sum is reset. The 
maximum amount of the max_sum subarray is updated at each step if current_sum exceeds it.
In this code, the maxSubArray function uses Kadane's algorithm to find the maximum sum of a contiguous subarray within
a one-dimensional array of numbers. The algorithm iterates through the array, at each step calculating the maximum 
subarray sum ending at that position. This is done by comparing the sum of the current subarray with the current 
element and updating the maximum sum found so far. The algorithm is efficient, with a time complexity of O(n), and 
does not require additional space.

'''
