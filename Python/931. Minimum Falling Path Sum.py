# 931. Minimum Falling Path Sum.

# Topic: Array, Dynamic Programming, Matrix.

"""
### Task:
---
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally 
left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100


### Testcases:
[[2,1,3],[6,5,4],[7,8,9]]
[[-19,57],[-40,-5]]


### Code:
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
"""
### Solution:

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        # Iterate over each row starting from the second row
        for i in range(1, n):
            for j in range(n):
                # Take the value directly above
                min_sum = matrix[i-1][j]

                # Consider the value diagonally left
                if j > 0:
                    min_sum = min(min_sum, matrix[i-1][j-1])

                # Consider the value diagonally right
                if j < n-1:
                    min_sum = min(min_sum, matrix[i-1][j+1])

                # Update the current cell with the minimum sum
                matrix[i][j] += min_sum

        # Return the minimum value from the last row
        return min(matrix[-1])


### Description:
'''
To solve the "Minimum Falling Path Sum" problem, we can use dynamic programming. The idea is to iterate over the matrix and, 
for each cell, calculate the minimum sum needed to reach that cell from the first row, considering the constraints of the falling path.

Here's how the algorithm works:

1. **Initialization**: We start with the first row of the matrix as it is, since the falling path starts from any element in the first row.

2. **Iteration**: For each subsequent row, we calculate the minimum sum to reach each cell in that row. This is done by considering the 
   three possible moves from the previous row: directly above, diagonally left, and diagonally right. We need to handle the edge cases 
   where the cell is in the first or last column (as it won't have a diagonal left or right, respectively).

3. **Final Step**: After filling up the matrix, the answer will be the minimum value in the last row, as it represents the minimum sum to 
    reach the bottom of the matrix from the top, following the falling path rules.


This implementation has a time complexity of O(n^2) and a space complexity of O(1), since we're modifying the input matrix in place. 
If modifying the input matrix is not allowed, we can create a new matrix of the same size for dynamic programming, which would bring 
the space complexity to O(n^2).

'''