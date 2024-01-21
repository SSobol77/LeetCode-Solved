# 73. Set Matrix Zeroes.

# Topic: Array, Hash Table, Matrix.

"""
### Task:
---
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

#Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

#Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

#Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1
 
#Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Hint 1:
If any cell of the matrix has a zero we can record its row and column number using additional memory. But if you don't want to 
use extra memory then you can manipulate the array instead. i.e. simulating exactly what the question says.
Hint 2:
Setting cell values to zero on the fly while iterating might lead to discrepancies. What if you use some other integer value as
your marker? There is still a better approach for this problem with 0(1) space.
Hint 3:
We could have used 2 sets to keep a record of rows/columns which need to be set to zero. But for an O(1) space solution, you can 
use one of the rows and and one of the columns to keep track of this information.
Hint 4:
We can use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero.

### Testcase:
---
[[1,1,1],[1,0,1],[1,1,1]]
[[0,1,2,0],[3,4,5,2],[1,3,1,5]]


### Code:
---
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:     
        '''Do not return anything, modify matrix in-place instead.'''        
        
"""
### Solution: -----------------------------------------------------------------------------------------------
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Do not return anything, modify matrix in-place instead."""  
        if not matrix:
            return

        rows, cols = len(matrix), len(matrix[0])
        first_row_zero, first_col_zero = False, False

        # Check if the first row should be zeroed
        for i in range(cols):
            if matrix[0][i] == 0:
                first_row_zero = True
                break

        # Check if the first column should be zeroed
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use the first row and first column to mark zero conditions
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # Set zeros based on the first row and first column markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set the first row to zeros if needed
        if first_row_zero:
            for i in range(cols):
                matrix[0][i] = 0

        # Set the first column to zeros if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0



# Description: ----------------------------------------------------------------------------------------------
'''
Description of the Solution:

The problem requires modifying a given m x n matrix in-place to set entire rows and columns to zero if any element in the matrix is zero. 
The challenge is to achieve this without using additional memory space, aiming for a constant O(1) space complexity.

Here's a step-by-step description of the solution:

1. First, we initialize two boolean variables, `first_row_zero` and `first_col_zero`, to track whether the first row and the first 
   column should be set to zero.

2. We iterate through the first row to check if any element is zero. If we find any zero in the first row, we set `first_row_zero` 
   to True and break out of the loop.

3. Similarly, we iterate through the first column to check if any element is zero. If we find any zero in the first column, we set 
   `first_col_zero` to True and break out of the loop.

4. Now, we use the first row and the first column of the matrix as markers to identify which rows and columns should be set to zero. 
   Starting from the second row and the second column (matrix[1][1]), we iterate through the matrix. Whenever we encounter a zero at 
   matrix[i][j], we set matrix[i][0] and matrix[0][j] to zero. This way, we use the first row to mark zero conditions for columns and 
   the first column to mark zero conditions for rows.

5. After marking the zero conditions, we iterate through the matrix again, starting from the second row and the second column. For 
   each element matrix[i][j], if either matrix[i][0] or matrix[0][j] is zero, we set matrix[i][j] to zero.

6. At this point, all the rows and columns that need to be zeroed are marked correctly in the matrix, except for the first row and 
   the first column.

7. Finally, if `first_row_zero` is True, we set all elements in the first row to zero, and if `first_col_zero` is True, we set all 
   elements in the first column to zero.

The key idea behind this approach is to use the first row and the first column as flags to keep track of which rows and columns should be zeroed.
By marking the zero conditions without using additional memory, we achieve a constant O(1) space complexity solution to the problem.

'''
