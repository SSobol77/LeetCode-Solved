"""
# 1539. Kth Missing Positive Number

# Topic: Array, Binary Search.

# Task:
------------------
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the k^th positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length

Hint 1:
Keep track of how many positive numbers are missing as you scan the array.



# Testcase:
--------------
[2,3,4,7,11]
5
[1,2,3,4]
2


# Code:
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
  
"""
# Solution:
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Initialize the current number to check and the count of missing numbers
        current = 1
        missingCount = 0
        index = 0  # Index to iterate through the array

        # Loop through the array
        while index < len(arr):
            # If current number is not in array, it's missing
            if arr[index] != current:
                missingCount += 1  # Increment the count of missing numbers
                if missingCount == k:  # If k missing numbers are found, return the current number
                    return current
            else:
                # Move to the next element in the array if the current number is not missing
                index += 1
            # Increment current number to check the next number
            current += 1

        # If kth missing number is not found in the array, calculate it
        # The formula accounts for the additional numbers missing after the largest number in the array
        return current + k - missingCount - 1


# Description:
'''
To solve the "Kth Missing Positive Number" problem, we need to find the k^th positive integer that is missing from a given sorted array arr. Let's break down the steps to solve this problem:

1    Initialize Counters: We need two counters - one for tracking the current number we are checking (current) and another for tracking how many numbers have been missing so far (missingCount).

2    Iterate through the Array: We iterate through the array and for each element in arr:
        While the current number is less than the current element in the array, we increment current and missingCount.
        When current equals the current element in the array, we just increment current and move to the next element in the array.

3    Check for Remaining Missing Numbers: After iterating through the array, if k is still greater than missingCount, it means the k^th missing number is greater than the largest number in the array. We keep incrementing current until missingCount equals k.

4    Return Result: Once missingCount equals k, current - 1 will be our answer as current will be incremented one time more after finding the k^th missing number.

Testing the Solution:
----------------------
    Test Case 1: arr = [2,3,4,7,11], k = 5
        The missing numbers are [1, 5, 6, 8, 9]. The 5th missing number is 9.

    Test Case 2: arr = [1,2,3,4], k = 2
        The missing numbers are [5, 6, 7, ...]. The 2nd missing number is 6.

The solution efficiently finds the k^th missing positive number by iterating through the array only once and is scalable for larger arrays and values of k within the given constraints.




'''

