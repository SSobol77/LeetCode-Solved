# 704. Binary Search.

# Topic: Array, Binary Search.

"""
Task:
------------------
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
1 <= nums.length <= 10^4
-10$4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.

# Testcase:
---------------
[-1,0,3,5,9,12]
9
[-1,0,3,5,9,12]
2


# Code:
-----------
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
"""
# Solution
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers, left at the start and right at the end of the array
        left, right = 0, len(nums) - 1

        # Loop until the left pointer is less than or equal to the right pointer
        while left <= right:
            # Calculate the middle index of the current subarray
            mid = (left + right) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                # If it is, return the index of the target
                return mid
            # If the target is greater than the middle element, discard the left half
            elif nums[mid] < target:
                left = mid + 1
            # If the target is less than the middle element, discard the right half
            else:
                right = mid - 1

        # If the target is not found in the array, return -1
        return -1

# Test cases
sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9))  # Output: 4, as 9 is found at index 4
print(sol.search([-1,0,3,5,9,12], 2))  # Output: -1, as 2 is not in the array


# Description:
'''
To solve the given task, we need to implement a binary search algorithm. This algorithm is 
efficient for searching in a sorted array, offering O(log n) runtime complexity.

Here's how the binary search algorithm works:

1. Start with two pointers, one at the start of the array (left) and one at the end (right).
2. Find the middle element of the array (or the subarray defined by left and right).
3. Compare the target value with the middle element.
   - If they are equal, we have found the target and return its index.
   - If the target is smaller, it must be in the left half of the array. So, we move the right
     pointer to the middle - 1.
   - If the target is larger, it must be in the right half of the array. So, we move the left 
     pointer to the middle + 1.
4. Repeat the process until the target is found or the pointers overlap, in which case the target 
   is not in the array and we return -1.

This code implements a standard binary search algorithm. It repeatedly divides the search interval 
in half. If the value of the search key is less than the item in the middle of the interval, it 
narrows the interval to the lower half; otherwise, it narrows it to the upper half. The process 
continues until the target value is found or the interval is empty, indicating that the target is not
in the array.   

'''