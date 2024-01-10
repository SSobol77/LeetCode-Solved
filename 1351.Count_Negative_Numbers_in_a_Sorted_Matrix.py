# 1351. Count Negative Numbers in a Sorted Matrix.

# Topic: Array, Binary Search, Matrix.

'''
# Task:
-----------------
Given a m x n matrix grid which is sorted in non-increasing order both row-wise 
and column-wise, return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 
Follow up: Could you find an O(n + m) solution?

Hint 1
Use binary search for optimization or simply brute force.

# Testcase:
-----------------
[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
[[3,2],[1,0]]


# Code:
-----------------
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
'''
# Solution:
from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the matrix
        m, n = len(grid), len(grid[0])

        # Initialize row and column pointers. Start from the top-right corner of the matrix
        row, col = 0, n - 1
        count = 0  # To count the number of negative numbers

        # Loop until either row or column pointers go out of bounds
        while row < m and col >= 0:
            # Check if the current element is negative
            if grid[row][col] < 0:
                # All elements below the current element are also negative
                # Add the count of all these elements to 'count'
                count += (m - row)

                # Move to the left column as we have counted all negatives in the current column
                col -= 1
            else:
                # Move down to the next row if the current element is non-negative
                row += 1

        # Return the total count of negative numbers found in the grid
        return count

# Test cases
sol = Solution()
print(sol.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))  # Output: 8
print(sol.countNegatives([[3,2],[1,0]]))  # Output: 0



# Description:
'''
To solve this problem efficiently in O(n + m) time complexity, we can leverage the sorted nature
 of the matrix. Since the rows and columns are sorted in non-increasing order, we can start from 
 the top-right corner of the matrix and work our way towards the bottom-left corner.

Here's the plan:

1. Start from the Top-Right Corner: Initialize two pointers, row to 0 and col to the last column.
2. Traverse the Matrix:
   - If the current element is negative, all the elements below it in the same column are also 
     negative (due to the sorted nature of the matrix). So, add the number of elements below 
     (including the current one) to the count, and move one column to the left.
   - If the current element is non-negative, move one row down.
3. Counting Negative Numbers: Keep counting the negative numbers until either the row or column 
   index goes out of bounds.
4. Return the Count: Once we traverse through the matrix, return the count.

This code provides an efficient solution to find the count of negative numbers in a sorted matrix. 
The logic takes advantage of the matrix's sorted nature, starting from the top-right corner and 
moving either left or down based on the value of the current element. This approach ensures that 
we traverse each row and column at most once, resulting in an O(n + m) time complexity, where n and 
m are the number of rows and columns in the matrix, respectively.

'''
