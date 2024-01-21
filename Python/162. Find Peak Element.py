# 162. Find Peak Element

# Topic: Array, Binary Search.

'''
# Task:
-------
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains
multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be 
strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 
             where the peak element is 6.
 
Constraints:
1 <= nums.length <= 1000
-2^31 <= nums[i] <= 2^31 - 1
nums[i] != nums[i + 1] for all valid i.


# Testcase:
-----------
[1,2,3,1]
[1,2,1,3,5,6,4]

'''
# Solution:
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Define a recursive binary search function
        def binarySearch(left, right):
            # Base case: if only one element is considered, it's a peak
            if left == right:
                return left

            # Find the middle of the current segment
            mid = (left + right) // 2

            # If the middle element is greater than the next element,
            # then the peak lies to the left of (or at) mid
            if nums[mid] > nums[mid + 1]:
                return binarySearch(left, mid)

            # Otherwise, the peak lies to the right of mid
            return binarySearch(mid + 1, right)

        # Start the binary search from the entire range of the array
        return binarySearch(0, len(nums) - 1)

# Test cases
solution = Solution()
print(solution.findPeakElement([1,2,3,1]))  # Output: 2
print(solution.findPeakElement([1,2,1,3,5,6,4]))  # Output: 5 or another peak index



# Description:
'''
In this code:
* A recursive function binarySearch is defined to perform the binary search within a specified range (left, right) of the array.
* The base case of the recursion is when there is only one element left in the search range. This element is considered a peak.
* We calculate the middle index of the current range. If this middle element is greater than its next element, it indicates that
  a peak is in the left half or might be the middle element itself.
* If the middle element is not greater than its next element, the peak must be in the right half.
* The function initiates this recursive search over the entire array and returns the index of a peak element found.

- In the provided solution for finding a peak element in an array, a recursive binary search approach is utilized. 
  This approach is particularly effective due to the nature of the problem and the properties of the array:

- Binary Search Concept: The core idea of binary search is to divide the search space into two halves at each step, 
  significantly reducing the number of comparisons required to find an element. In this case, the search space is 
  halved at each step to locate a peak element.

- Properties of the Array: The array has the distinct property that each element is different from its neighbors, 
  and we can consider elements outside the array bounds as negative infinity. This unique property allows us to 
  guarantee that a peak will always exist and can be found using binary search.

- Recursive Approach: The solution uses recursion to implement the binary search. This involves defining a function 
  (binarySearch) that calls itself with narrowed search boundaries based on the comparison of middle element with its
  adjacent elements.

- Efficiency: This method is efficient with a time complexity of O(log n), where n is the number of elements in the array.
  This efficiency arises because the algorithm consistently halves the search space, leading to logarithmic time complexity.

- Flexibility in Peak Selection: The problem statement allows for the return of any peak element. The binary search approach
  naturally fits this requirement as it finds an arbitrary peak without needing to scan the entire array.

- Handling Edge Cases: The solution appropriately handles edge cases, such as arrays with a single element or when the peak
  is at the beginning or end of the array.

- Overall, the recursive binary search is a fitting choice for this problem, leveraging the sorted nature of the array and 
  efficiently narrowing down the search space to find a peak element.

'''
