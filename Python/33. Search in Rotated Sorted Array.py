# 33. Search in Rotated Sorted Array.

# Topic: Array, Binary Search.

'''
# Task:
-------
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such
that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in 
nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
 
Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4


# Testcase:
------------
[4,5,6,7,0,1,2]
0
[4,5,6,7,0,1,2]
3
[1]
0

'''
# Solution:
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initializing the left and right pointers for the binary search
        left, right = 0, len(nums) - 1

        # The while loop continues as long as 'left' is less than or equal to 'right'
        while left <= right:
            # Calculate the middle index of the current segment
            mid = (left + right) // 2

            # If the middle element is the target, return its index
            if nums[mid] == target:
                return mid

            # Lambda functions to simplify conditions
            # Check if the left side of the array is sorted
            is_left_sorted = lambda: nums[left] <= nums[mid]
            # Check if the target is in the left sorted part of the array
            is_target_in_left = lambda: nums[left] <= target < nums[mid]
            # Check if the target is in the right part of the array
            is_target_in_right = lambda: nums[mid] < target <= nums[right]

            # Determine which half of the array to search next
            if is_left_sorted():
                # If the left side is sorted and the target is in the left side, 
                # adjust the 'right' pointer
                if is_target_in_left(): right = mid - 1
                # Otherwise, adjust the 'left' pointer
                else: left = mid + 1
            else:
                # If the right side is where the target should be, 
                # adjust the 'left' pointer
                if is_target_in_right(): left = mid + 1
                # Otherwise, adjust the 'right' pointer
                else: right = mid - 1
        
        # Return -1 if the target is not found
        return -1

# Test cases
solution = Solution()
print(solution.search([4,5,6,7,0,1,2], 0))  # Output: 4
print(solution.search([4,5,6,7,0,1,2], 3))  # Output: -1
print(solution.search([1], 0))  # Output: -1


# Description:
'''
In this code:
- A binary search algorithm is used to find the target element in a rotated sorted array.
- The array is divided into segments, and it's determined which segment is sorted (left or right from the middle).
- Based on whether the segment is sorted and if the target is within that segment, the search space is narrowed by 
  adjusting the left and right pointers.
- Lambda functions are used for clarity, making it easier to understand the conditions being checked.
- The loop continues until the target is found or the search space is exhausted. If the target is not found, -1 is returned.

'''
