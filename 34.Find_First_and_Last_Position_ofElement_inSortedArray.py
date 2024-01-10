# 34. Find First and Last Position of Element in Sorted Array.

# Topic: Array, Binary Search.

'''
# Task:
-----------------
Given an array of integers nums sorted in non-decreasing order, find the starting and 
ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1] 

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9


# Testcase:
-----------------
[5,7,7,8,8,10]
8
[5,7,7,8,8,10]
6
[]
0


# Code:
-----------------
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
           
'''

# Solution:
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Define a binary search function to find the leftmost (first) occurrence of the target
        def binarySearchLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                # If the target is greater than the middle element, discard the left half
                if nums[mid] < target:
                    left = mid + 1
                # Otherwise, discard the right half
                else:
                    right = mid - 1
            # Return the left index where the target would be or the first occurrence
            return left

        # Define a binary search function to find the rightmost (last) occurrence of the target
        def binarySearchRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                # If the target is greater or equal to the middle element, discard the left half
                if nums[mid] <= target:
                    left = mid + 1
                # Otherwise, discard the right half
                else:
                    right = mid - 1
            # Return the right index where the target's last occurrence is
            return right

        # Perform binary searches to find the first and last positions of the target
        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)

        # Check if the target exists in the array
        if left <= right:
            # If it exists, return the range [left, right]
            return [left, right]
        # If the target is not found, return [-1, -1]
        return [-1, -1]

# Test cases
sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))  # Output: [3,4]
print(sol.searchRange([5,7,7,8,8,10], 6))  # Output: [-1,-1]
print(sol.searchRange([], 0))             # Output: [-1,-1]


# Description:
'''
To solve this problem, we can use a modified binary search approach to find the first and last 
positions of the target value in the sorted array. Since the array is sorted, binary search is 
suitable for achieving the required O(log n) runtime complexity.

The solution involves two main steps:

1. Finding the First Position: Perform binary search to find the first occurrence of the target. 
   In this binary search, when the target is found, continue searching in the left half to see if 
   there is an earlier occurrence of the target.

2. Finding the Last Position: Perform a second binary search to find the last occurrence of the target. 
   This time, when the target is found, continue searching in the right half to find the last occurrence.

In this code, binarySearchLeft and binarySearchRight are two binary search functions tailored to find the 
first and last occurrences of the target in the sorted array, respectively. After finding these positions, 
the code checks if the target actually exists in the array. If it does, the indices of the first and last 
occurrences are returned; otherwise, [-1, -1] is returned, indicating that the target is not present in 
the array. The solution thus effectively uses binary search to achieve the required O(log n) runtime 
complexity.
   
'''
