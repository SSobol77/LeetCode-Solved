"""
# 240. Search a 2D Matrix II.


# Topic: Array, Binary Search, Divide and , Matrix.



# Task:
-------------
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.
 
Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matrix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9


# Testcase:
-------------
[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
5
[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
20


# Code:
-------------
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
 
"""
# Solution:

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Check if the matrix is empty or if the first row is empty
        if not matrix or not matrix[0]:
            return False  # Return False for empty matrix

        # Initialize the starting position at the top-right corner
        row, col = 0, len(matrix[0]) - 1

        # Iterate through the matrix
        while row < len(matrix) and col >= 0:
            # Check the current element in the matrix
            if matrix[row][col] == target:
                return True  # Target found, return True
            # If the current element is greater than the target, move left
            elif matrix[row][col] > target:
                col -= 1  # Decrease column index to move left
            # If the current element is less than the target, move down
            else:
                row += 1  # Increase row index to move down

        # If the loop exits without finding the target, it's not in the matrix
        return False  # Target not found, return False


# Description:
'''
To solve the problem of searching for a target value in a 2D matrix with sorted rows and columns, we can 
leverage the sorted properties of the matrix for an efficient solution. A brute force approach would involve 
checking every element, but this would not be efficient, especially for large matrices.

A more efficient strategy is to start from either the top-right corner or the bottom-left corner of the matrix. 
The sorted properties of the matrix allow us to eliminate either a row or a column in each step, leading to 
a time complexity of O(m + n), where m is the number of rows and n is the number of columns.


Detailed Explanation:
--------------------------------

1. Check Matrix Validity (Lines 3-4): 
   The code first checks whether the matrix or the first row is empty. If so, it returns False immediately, as 
   an empty matrix does not contain any elements, including the target.

2. Initialize Position (Line 7): The search starts from the top-right corner of the matrix. This position is 
   strategic because it allows us to move either left or down based on the comparison with the target.

3. Search Logic (Lines 9-16):

  * If the current element matches the target (matrix[row][col] == target), we return True as we've found the target.

  * If the current element is greater than the target (matrix[row][col] > target), we move left (decrease col) because 
    all elements to the right will be greater.

  * If the current element is smaller than the target (matrix[row][col] < target), we move down (increase row) because 
    all elements above will be smaller.

4. Target Not Found (Line 19): If the loop exits without returning True, it means the target is not present in the matrix, so the function returns False.

'''
