# 74. Search a 2D Matrix.

# Topic: Array, Binary Search, Matrix.

'''
# Task:
--------

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4


# Testcase:
[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
3
[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
13


'''

# Solution:

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Check if the matrix is empty
        if not matrix:
            return False

        # Get the number of rows and columns in the matrix
        rows, cols = len(matrix), len(matrix[0])

        # Initialize the left and right boundaries for binary search
        # We treat the matrix as a flattened array for the purposes of binary search
        left, right = 0, rows * cols - 1

        while left <= right:
            # Calculate the middle index for the current left and right boundaries
            mid = (left + right) // 2
            # Convert the 1D index back to 2D matrix indices
            mid_value = matrix[mid // cols][mid % cols]

            if mid_value == target:
                # If the middle value is the target, return True
                return True
            elif mid_value < target:
                # If the middle value is less than the target, search in the right half
                left = mid + 1
            else:
                # If the middle value is greater than the target, search in the left half
                right = mid - 1

        # Return False if the target is not found in the matrix
        return False

# Test cases
solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # Output: true
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))  # Output: false


# Description:
'''
In this code:

We first check if the matrix is empty to handle edge cases.
The number of rows and columns in the matrix are calculated to determine the search space.
The binary search is implemented by treating the 2D matrix as a 1D array, using the indices transformation (mid // cols and mid % cols) to access the matrix elements.
The search narrows down the range based on whether the mid-value is less than or greater than the target.
The function returns True if the target is found, otherwise False.

'''
