# 153. Find Minimum in Rotated Sorted Array.

# Topic: Array, Binary Search.

'''
# Task:
-------
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, 
the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in 
the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 
Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

Hint 1
Array was originally in ascending order. Now that the array is rotated, there would be a point in the array
where there is a small deflection from the increasing sequence. eg. The array would be something like [4, 5, 6, 7, 0, 1, 2].

Hint 2
You can divide the search space into two and see which direction to go. Can you think of an algorithm which 
has O(logN) search complexity?

Hint 3
All the elements to the left of inflection point > first element of the array.
All the elements to the right of inflection point < first element of the array.


# Testcase:
-----------
[3,4,5,1,2]
[4,5,6,7,0,1,2]
[11,13,15,17]

'''
# Solution:
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            
            # If the mid element is greater than the rightmost element,
            # the smallest value must be to the right of mid.
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # If the mid element is less than or equal to the rightmost element,
                # the smallest value is either at mid or to the left of mid.
                right = mid

        # When left equals right, we've found the smallest element
        return nums[left]

# Test cases
solution = Solution()
print(solution.findMin([3,4,5,1,2]))  # Output: 1
print(solution.findMin([4,5,6,7,0,1,2]))  # Output: 0
print(solution.findMin([11,13,15,17]))  # Output: 11


# Description:
'''
The code provided for finding the minimum in a rotated sorted array is already quite efficient, using a binary 
search with a time complexity of O(log n), which is optimal for this problem.

The condition left < right is used in the while loop to prevent unnecessary iteration when the minimum is found.
The calculation of mid is optimized to prevent potential integer overflow.
The logic to determine whether to move left or right is based on the comparison of nums[mid] with nums[right], 
which ensures that the search space is reduced by half with each iteration.
The final return is simplified to nums[left] as left and right converge to the index of the minimum element.
This refined approach should maintain the optimal time complexity while ensuring robust performance across various
test cases.






'''