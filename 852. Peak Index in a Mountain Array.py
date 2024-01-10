# 852. Peak Index in a Mountain Array.

# Topic: Array, Binary Search.

'''
Task:
-----
An array arr is a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1
 
Constraints:
3 <= arr.length <= 10^5
0 <= arr[i] <= 10^6
arr is guaranteed to be a mountain array.


# Testcase:
-----------
[0,1,0]
[0,2,1,0]
[0,10,5,2]


# Code:
-------
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
       

'''
# Solution:
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left

sol = Solution()

# Test cases
print(sol.peakIndexInMountainArray([0,1,0]))  # Expected output: 1
print(sol.peakIndexInMountainArray([0,2,1,0]))  # Expected output: 1
print(sol.peakIndexInMountainArray([0,10,5,2]))  # Expected output: 1

# Description:
'''
To find the peak index in a mountain array efficiently, you can use a binary search algorithm. This approach has a 
time complexity of O(log n), where n is the length of the array, making it suitable for the given constraints.

Here's how the binary search approach works for this problem:

1. Initialize two pointers, left and right, to the start and end of the array, respectively.
2. While left is less than right:
    * Find the middle index, mid, of the current range.
    * Check the elements at mid and mid + 1.
    * If arr[mid] < arr[mid + 1], it means the peak is to the right of mid, so update left to mid + 1.
    * Otherwise, the peak is to the left of mid, so update right to mid.
3. The peak index is the position where left and right converge.

This implementation should efficiently solve the problem within the specified constraints.
'''