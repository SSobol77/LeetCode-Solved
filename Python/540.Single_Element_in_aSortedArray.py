"""
# 540. Single Element in a Sorted Array.

# Topic:Array, Binary Search.


# Task:
---------------
You are given a sorted array consisting of only integers where every element appears exactly 
twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5


# Testcase:
--------------------
[1,1,2,3,3,4,4,8,8]
[3,3,7,7,10,11,11]


# Code:
--------------------
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
"""
# Solution:
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Initialize the low and high pointers for binary search
        low, high = 0, len(nums) - 1

        # Binary search loop
        while low < high:
            # Find the middle index
            # Adjust mid to be even if it's odd, as pairs are supposed to start at even indices
            mid = low + (high - low) // 2
            if mid % 2 == 1:
                mid -= 1

            # Compare the element at mid with the next element
            # If they are the same, the single element must be in the right half
            # Hence, we move the low pointer to mid + 2
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                # If they are not the same, the single element is in the left half
                # Hence, we move the high pointer to mid
                high = mid

        # The single element is found at the position 'low' after the loop ends
        return nums[low]

# Description:
'''
To solve the problem "Single Element in a Sorted Array" using binary search, we must find 
the element that appears exactly once in a sorted array where every other element appears 
exactly twice. The key to the solution is to leverage the sorted property of the array.

The main idea is to use binary search to split the array into halves.
At each step, we check whether the single element is in the left or right half. 
This check is based on the fact that pairs of identical elements should be adjacent, 
and the first instance of each pair should occur at an even index in a 0-indexed array.

Here's the step-by-step approach:
------------------------------------------
    Initialize Search Space: Set low (low) to 0 and high (high) to the length of the nums array minus one.

    Binary Search:
        While low is less than high, do the following:
            Find the middle index (mid). Ensure mid is even; if it's odd, decrement it by 1.
            Check if the element at mid is equal to the element at mid + 1.
            If they are equal, the single element must be in the right half; hence, set low to mid + 2.
            If they are not equal, the single element must be in the left half; hence, set high to mid.

    Return Result: The single element is at index low after the loop finishes.

Testing the Solution:
-------------------------
    Test Case 1: nums = [1,1,2,3,3,4,4,8,8]
        The single element is 2.

    Test Case 2: nums = [3,3,7,7,10,11,11]
        The single element is 10.

This solution employs binary search to effectively find the single non-duplicate element in logarithmic time, adhering to the given constraints of time and space complexity.

'''
