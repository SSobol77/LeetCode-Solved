# 75. Sort Colors.

# Topic:Array, Two Pointers, Sorting.
'''
# Task:
--------
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same
color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

Hint 1:
A rather straight forward solution is a two-pass algorithm using counting sort.
Hint 2:
Iterate the array counting number of 0's, 1's, and 2's.
Hint 3:
Overwrite array with the total number of 0's, then 1's and followed by 2's.


# Testcase:
-----------
[2,0,2,1,1,0]
[2,0,1]

# Code:
-------------
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
'''
# Solution:
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize two pointers: 'low' at the start and 'high' at the end of the array.
        low, high = 0, len(nums) - 1
        # 'i' is used for traversing the array.
        i = 0

        # Iterate through the array.
        while i <= high:
            # If the current element is 0.
            if nums[i] == 0:
                # Swap only if 'i' and 'low' are pointing to different elements.
                if i != low:
                    nums[i], nums[low] = nums[low], nums[i]
                # Move the 'low' pointer up and 'i' to the next element.
                low += 1
                i += 1
            # If the current element is 2.
            elif nums[i] == 2:
                # Swap the current element with the element at the 'high' pointer.
                nums[i], nums[high] = nums[high], nums[i]
                # Move the 'high' pointer down.
                high -= 1
            # If the current element is 1, just move to the next element.
            else:
                i += 1

# Testcases
sol = Solution()
nums1 = [2, 0, 2, 1, 1, 0]
sol.sortColors(nums1)
print(nums1)  # Output: [0, 0, 1, 1, 2, 2]

nums2 = [2, 0, 1]
sol.sortColors(nums2)
print(nums2)  # Output: [0, 1, 2]


# Description:
'''
To sort the colors in-place, we can use the Dutch National Flag algorithm by Edsger W. Dijkstra. 
This algorithm segregates an array of 0s, 1s, and 2s. The idea is to use three pointers: one for 
traversing the array (i), one for tracking the next position of 0 (low), and one for tracking the
next position of 2 (high). The algorithm makes one pass through the array and swaps elements to 
move 0s to the beginning and 2s to the end, leaving 1s in the middle.

In this code:

- We have three pointers: low, high, and i. low starts from the beginning of the array, high starts from the end, 
  and i is used to iterate through the array.
- The array is sorted in such a way that all 0s are moved to the beginning and all 2s to the end. The 1s automatically
  end up in the middle.
- We iterate through the array using the i pointer. If we encounter a 0, we swap it with the element at the low pointer
  and increment both low and i. This moves the 0s to the beginning of the array.
- If we encounter a 2, we swap it with the element at the high pointer and decrement high. This moves the 2s to the end
  of the array. We don't increment i here because the swapped element might be a 0, and we need to process it in the next iteration.
- If the element is 1, we just move to the next element by incrementing i.
- The process continues until i surpasses high. At this point, the array is sorted in the required order.

'''
