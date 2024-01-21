# 81. Search in Rotated Sorted Array II.

# Topic:Array, Binary Search

'''
# Task:
----------
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is 
not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4

Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. 
Would this affect the runtime complexity? How and why?


# Testcase:
-------------
[2,5,6,0,0,1,2]
0
[2,5,6,0,0,1,2]
3


# Code:
-------------
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
    
'''
# Solution:

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            
            # If duplicates are found, reduce search space
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                # Left part is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right part is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

# Testcases
sol = Solution()
print(sol.search([2,5,6,0,0,1,2], 0))  # Output: True
print(sol.search([2,5,6,0,0,1,2], 3))  # Output: False


# Description:
'''
To solve the problem of searching in a rotated sorted array where the array may contain duplicates,
we can still use a modified version of the binary search algorithm. The presence of duplicates affects 
the runtime complexity because, in the worst case, we might need to perform a linear search. However, 
we can try to optimize the binary search as much as possible to handle most cases efficiently.

The modified binary search needs to handle the scenario where the middle element is equal to the end 
elements. In such cases, we can't decide which part of the array is sorted, so we reduce our search 
space by one and continue.

In this code:

- We perform a binary search, but with an additional check to handle duplicates.
- If nums[mid] equals the target, we return True.
- If nums[left], nums[mid], and nums[right] are all equal, we can't decide the sorted part, so we simply 
  reduce the search space by incrementing left and decrementing right.
- If the left part of the array is sorted (i.e., nums[left] <= nums[mid]), we check if the target lies in
  this sorted part. If it does, we search in the left part; otherwise, in the right part.
- Similarly, if the right part of the array is sorted and the target lies in this part, we search in the 
  right part; otherwise, in the left part.
- If the target is not found, we return False.

'''