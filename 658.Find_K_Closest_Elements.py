"""
# 658. Find K Closest Elements.


# Topic: Array, Two Pointers, Binary Search, Sliding Window, Sorting, Heap (Priority Queue).


# Task:
--------------
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b


Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:
1 <= k <= arr.length
1 <= arr.length <= 10^4
arr is sorted in ascending order.
-10^4 <= arr[i], x <= 10^4



# Testcase:
-----------------
[1,2,3,4,5]
4
3
[1,2,3,4,5]
4
-1


# Code:
----------------
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        

"""
# Solution:
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary search to find the closest element to x
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            # Move right pointer to the left if the middle element is less than x
            if arr[mid] < x:
                left = mid + 1
            else:
                # Otherwise, move left pointer to the middle
                right = mid

        # Adjust left pointer for the two pointer expansion
        left -= 1
        right = left + 1

        # Expand left and right pointers to find k closest elements
        while right - left - 1 < k:
            # If left pointer goes beyond the beginning, only move right pointer
            if left == -1:
                right += 1
            # If right pointer goes beyond the end or the left element is closer to x, move left pointer
            elif right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                # Otherwise, move right pointer
                right += 1

        # Return the sublist of arr from left+1 to right-1 (inclusive)
        return arr[left + 1:right]


# Description:
'''
To solve the problem "Find K Closest Elements", we need to find the k closest integers to a 
given integer x in a sorted array arr. The result should also be sorted in ascending order. 
The approach to solve this problem involves binary search and two pointers.

Here's how we can approach the problem:
----------------------------------------
    Find the Right Start Position:
        Use binary search to find the closest element to x in arr. This will be our starting point.

    Two Pointers Expansion:
      -  Initialize two pointers: left and right. Initially, left is the index found by binary search, 
         and right is left + 1.
      -  Expand these pointers outwards to find the k closest elements.
      -  Choose the closer element to x when expanding. If two elements are equally close, prefer the 
         smaller element (which will be on the left).

    Form the Result:
        Once we have found the k closest elements, create a list from arr[left] to arr[right - 1] (inclusive).

Testing the Solution:
--------------------------------
    Test Case 1: arr = [1,2,3,4,5], k = 4, x = 3
        The 4 closest elements to 3 are [1,2,3,4].

    Test Case 2: arr = [1,2,3,4,5], k = 4, x = -1
        The 4 closest elements to -1 are [1,2,3,4].

This solution uses binary search to efficiently find the starting position and two pointers to 
expand and find the k closest elements, ensuring optimal performance with sorted input.
         
'''
