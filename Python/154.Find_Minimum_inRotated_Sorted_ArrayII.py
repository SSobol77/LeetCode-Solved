"""
# 154. Find Minimum in Rotated Sorted Array II

# Topic: Array, Binary Search.



# Task:
----------------------
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,4,4,5,6,7] might become:

    [4,5,6,7,0,1,4] if it was rotated 4 times.
    [0,1,4,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in 
the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [1,3,5]
Output: 1

Example 2:
Input: nums = [2,2,2,0,1]
Output: 0

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.

Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

# Testcase:
-----------------
[1,3,5]
[2,2,2,0,1]


# Code:
-----------------
class Solution:
    def findMin(self, nums: List[int]) -> int:
        

"""

# Solution:
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize left and right pointers to the start and end of the array.
        left, right = 0, len(nums) - 1

        # Perform a modified binary search.
        while left < right:
            # Calculate the middle index of the current range.
            mid = left + (right - left) // 2

            # Compare the middle element with the rightmost element.
            if nums[mid] > nums[right]:
                # If the middle element is greater than the rightmost element,
                # the minimum must be in the right half of the array.
                left = mid + 1
            elif nums[mid] < nums[right]:
                # If the middle element is less than the rightmost element,
                # the minimum is in the left half including mid.
                right = mid
            else:  # nums[mid] == nums[right]
                # When the middle element is equal to the rightmost element,
                # it's uncertain where the minimum is, so we reduce the search
                # space from the right by one step.
                right -= 1

        # The left index will point to the minimum element of the array.
        return nums[left]

# Description:
'''
To solve the problem of finding the minimum element in a rotated sorted array that may contain duplicates, 
we can still use a modified binary search approach. The presence of duplicates requires us to handle a 
few additional cases compared to a standard binary search.

Approach:

1. Initialize: Start with two pointers, left and right, pointing to the beginning and the end of the array, 
   respectively.

2. Binary Search:
   - While left < right, calculate the mid-point mid.
   - If nums[mid] > nums[right], the minimum value must be to the right of mid, so set left = mid + 1.
   - If nums[mid] < nums[right], the minimum value is to the left of mid or at mid, so set right = mid.
   - If nums[mid] == nums[right], we cannot determine the side of the minimum, so we reduce the search 
     space by doing right -= 1.

3. Result: The minimum value is at index left after the loop ends.

Explanation:

* In the case of nums[mid] > nums[right], the minimum must be to the right of mid.
* In the case of nums[mid] < nums[right], the minimum is either at mid or to the left of mid.
* In the case of nums[mid] == nums[right], we cannot determine which side the minimum is on, so we reduce 
  the search space by one from the right.

Complexity Analysis:

- Time Complexity: O(log n) in the average case, but in the worst case (when all elements are the same), 
  it can become O(n).
- Space Complexity: O(1), as we are using a constant amount of extra space.

The follow-up question addresses the impact of duplicates on the runtime complexity. The presence of 
duplicates can degrade the average case time complexity to O(n) in the worst case, as we might need to 
linearly scan the array when nums[mid] == nums[right].

'''
