"""
# 611. Valid Triangle Number

# Topic: Array, Two Pointers, Binary Search, Greedy, Sorting.

# Task:
------------------
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:
Input: nums = [4,2,3,4]
Output: 4

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 1000

# Testcase:
------------
[2,2,3,4]
[4,2,3,4]


# Code:
-----------
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        

"""
# Solution:
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array
        count = 0

        # Iterate from the third element to the end
        for i in range(2, len(nums)):
            left, right = 0, i - 1

            # Two pointers approach
            while left < right:
                # If it forms a triangle, move the left pointer and increase the count
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    # If it doesn't form a triangle, move the left pointer
                    left += 1

        return count

# Description:
'''
To solve the "Valid Triangle Number" problem, we need to count the number of triplets in the array nums 
that can form a triangle. The triangle inequality theorem states that the sum of the lengths of any two 
sides of a triangle must be greater than the length of the third side.

A two-pointer approach can be utilized after sorting the array. Here's how we can approach it:
----------------------------------------------------------------------------------------------

    Sort the Array: Sort nums in non-decreasing order.

    Iterate and Apply Two-Pointers:
        Iterate through the array from the third element to the end (as a potential longest side of a triangle).
        For each element, use two pointers to find pairs that satisfy the triangle inequality with this element.
        The two pointers start at the beginning of the array and just before the current element in the outer loop.

    Count Valid Combinations:
        If the sum of the two pointed elements is greater than the current element (from the outer loop), it forms a valid triangle. Increase the count of valid triangles.
        Move the left pointer right or the right pointer left based on the sum comparison.

    Return the Count.

Testing the Solution:
----------------------
    Test Case 1: nums = [2,2,3,4]
        The valid combinations are [2,2,3], [2,3,4] (first 2), and [2,3,4] (second 2). 
        So, the output is 3.

    Test Case 2: nums = [4,2,3,4]
        The valid combinations are [2,3,4] (first 4), [2,3,4] (second 4), [2,4,4], and [3,4,4]. 
        So, the output is 4.

This solution efficiently finds all the valid triangle combinations using a sorted array and a 
two-pointer approach, ensuring optimal performance.

'''