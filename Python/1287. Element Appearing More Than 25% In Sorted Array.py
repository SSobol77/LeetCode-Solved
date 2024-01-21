# 1287. Element Appearing More Than 25% In Sorted Array

# Topic: Array

'''
# Task:
--------
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array 
that occurs more than 25% of the time, return that integer.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:
Input: arr = [1,1]
Output: 1
 
Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5

Hint 1
Divide the array in four parts [1 - 25%] [25 - 50 %] [50 - 75 %] [75% - 100%]
Hint 2
The answer should be in one of the ends of the intervals.
Hint 3
In order to check which is element is the answer we can count the frequency with binarySearch.

# Testcase:
------------
[1,2,2,6,6,6,6,7,10]
[1,1]

'''
# Solution:
from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        # Define the key positions that must be checked
        # These are the quartile positions in the sorted array
        possible_positions = [n // 4, n // 2, 3 * n // 4]

        for pos in possible_positions:
            # Element at the current position
            element = arr[pos]

            # Find the first and last occurrence of this element using binary search
            first_occurrence = self.binary_search(arr, element, True)
            last_occurrence = self.binary_search(arr, element, False)

            # Check if the element occurs more than 25% of the time
            if last_occurrence - first_occurrence + 1 > n // 4:
                return element

        # Theoretically, this line should not be reached as per the problem statement
        return -1

    def binary_search(self, arr, target, find_first):
        # Generic binary search algorithm
        left, right = 0, len(arr) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                result = mid
                # If finding the first occurrence, move left; otherwise, move right
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

# Test cases
solution = Solution()
print(solution.findSpecialInteger([1,2,2,6,6,6,6,7,10]))  # Output: 6
print(solution.findSpecialInteger([1,1]))  # Output: 1


# Description:
'''
In this code:
- The findSpecialInteger function takes a sorted array and looks for the element that occurs more than 25% of the time.
- 'possible_positions' are the key positions in the array where the special element is likely to be found, based on the 
  quartile positions.
- For each possible position, it finds the first and last occurrence of the element at that position using a modified 
  binary search (binary_search method).
- If the frequency of the element (calculated from first and last occurrence) is more than 25% of the array's length, 
  it returns that element.
- The binary_search method is a generic binary search algorithm, which can find either the first or last occurrence of
  a target element, depending on the find_first flag.

'''
