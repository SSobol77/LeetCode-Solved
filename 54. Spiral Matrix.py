# 54. Spiral Matrix.

# Topic: Array, Matrix, Simulation.

"""
### Task:
---
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

Hint 1:
Well for some problems, the best way really is to come up with some algorithms for simulation. Basically, you need to simulate what 
the problem asks us to do.
Hint 2:
We go boundary by boundary and move inwards. That is the essential operation. First row, last column, last row, first column, and 
then we move inwards by 1 and repeat. That's all. That is all the simulation that we need.
Hint 3:
Think about when you want to switch the progress on one of the indexes. If you progress on i out of [i, j], you'll shift in the same 
column. Similarly, by changing values for j, you'd be shifting in the same row. Also, keep track of the end of a boundary so that you can move inwards and then keep repeating. It's always best to simulate edge cases like a single column or a single row to see if anything breaks or not.


### Testcase:
---
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3,4],[5,6,7,8],[9,10,11,12]]


### Code:
---
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
"""
### Solution: -----------------------------------------------------------------------------------------------
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []  # Return an empty list for an empty matrix

        result = []  # Initialize the result list to store the spiral order elements
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse the top row from left to right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Traverse the rightmost column from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Check if there is still a valid row to traverse
            if top <= bottom:
                # Traverse the bottom row from right to left
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # Check if there is still a valid column to traverse
            if left <= right:
                # Traverse the leftmost column from bottom to top
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result



# Description: ----------------------------------------------------------------------------------------------
'''
## Description of the solution to the "Spiral Matrix" problem:

**Problem Description:**

Given an m x n matrix, the task is to return all elements of the matrix in spiral order. In other words, you need to traverse the matrix in a spiral fashion, starting from the top-left corner and moving towards the right, down, left, and up, repeating this pattern until all elements are visited.

**Solution Approach:**

The solution follows a systematic approach to traverse the matrix in a spiral order while maintaining four boundary pointers: `top`, `bottom`, `left`, and `right`. These pointers help in defining the boundaries of the current spiral layer within the matrix.

1. Initialize `top`, `bottom`, `left`, and `right` to represent the boundaries of the entire matrix.

2. Use a while loop to iterate as long as there are valid rows and columns within the boundaries.

3. Inside the loop:
   - Traverse the top row from left to right, adding each element to the result.
   - Move `top` down by 1 to indicate that the top row has been processed.
   - Traverse the rightmost column from top to bottom, adding each element to the result.
   - Move `right` left by 1 to indicate that the rightmost column has been processed.
   - Check if there is still a valid row (`top` is less than or equal to `bottom`) and traverse the bottom row from right to left if applicable.
   - Move `bottom` up by 1 to indicate that the bottom row has been processed.
   - Check if there is still a valid column (`left` is less than or equal to `right`) and traverse the leftmost column from bottom to top if applicable.
   - Move `left` right by 1 to indicate that the leftmost column has been processed.

4. Repeat the process until all elements have been processed.

5. Finally, return the result, which contains the elements of the matrix in spiral order.

**Time Complexity:**

The time complexity of this solution is O(m * n), where m is the number of rows and n is the number of columns in the matrix. The algorithm visits each element exactly once, making it an efficient way to traverse the matrix in spiral order.
'''