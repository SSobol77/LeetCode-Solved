# 918. Maximum Sum Circular Subarray

# Topic: Array, Divide and Conquer, Dynamic Programming, Queue, Monotonic Queue.

'''
# Task:
-------
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element 
of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a 
subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 
Constraints:
n == nums.length
1 <= n <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4


Hint 1
For those of you who are familiar with the Kadane's algorithm, think in terms of that. For the newbies, Kadane's algorithm 
is used to finding the maximum sum subarray from a given array. This problem is a twist on that idea and it is advisable 
to read up on that algorithm first before starting this problem. Unless you already have a great algorithm brewing up in 
your mind in which case, go right ahead!

Hint 2
What is an alternate way of representing a circular array so that it appears to be a straight array? Essentially, there are
two cases of this problem that we need to take care of. Let's look at the figure below to understand those two cases.

Hint 3
The first case can be handled by the good old Kadane's algorithm. However, is there a smarter way of going about handling 
the second case as well?


# Testcase:
-----------
[1,-2,3,-2]
[5,-3,5]
[-3,-2,-3]


# Code:
-------
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
'''
# Solution:
from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(gen):
            # Kadane's algorithm to find the maximum subarray sum
            cur = total = next(gen)
            for x in gen:
                # Update the current sum, either adding the current element or starting new from the current element
                cur = x + max(cur, 0)
                # Update the total if the current sum is greater than the total
                total = max(total, cur)
            return total

        # Case 1: Maximum subarray is in the middle of the array (non-circular)
        max_normal = kadane(iter(nums))

        # Case 2: Maximum subarray is circular, wrapping around the array
        # Calculate the total sum of the array and the minimum subarray sum
        # The circular max subarray sum is the total sum minus the minimum subarray sum
        max_wrap = sum(nums) + kadane(-x for x in nums)

        # Special case: If all numbers are negative, return the maximum subarray sum found in Case 1
        if max_wrap == 0:
            return max_normal

        # Return the maximum of the two cases
        return max(max_normal, max_wrap)

# Testing the solution
sol = Solution()
print(sol.maxSubarraySumCircular([1,-2,3,-2]))  # Expected output: 3
print(sol.maxSubarraySumCircular([5,-3,5]))  # Expected output: 10
print(sol.maxSubarraySumCircular([-3,-2,-3]))  # Expected output: -2



# Description:
'''
To solve the "Maximum Sum Circular Subarray" problem, we can use a modification of the Kadane algorithm. 
In a circular array, the maximum submassive can be either in the middle of the array (as in a regular array), 
or divided into two parts at the beginning and end of the array. We can solve this problem by finding the 
maximum submassive using the Kadan algorithm and the minimum submassive, also using the Kadan algorithm, and 
then subtracting the minimum submassive from the sum of the entire array. The maximum result of these two will 
be the answer, except in the case when all the numbers are negative.

This code uses two passes of the Kadan algorithm: one to find the maximum sum of the subarray in the middle 
of the array and one to find the minimum sum of the subarray (which is equivalent to the maximum sum of the 
subarray spanning the beginning and end of the array). We select the maximum value from these two cases to 
find the maximum sum of the circular submarray.

'''
