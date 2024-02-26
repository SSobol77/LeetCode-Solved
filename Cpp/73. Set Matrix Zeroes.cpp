// 73. Set Matrix Zeroes.


// Topic: Array, Hash Table, Matrix.


/*
### Task:
---
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1
 
Follow up:
- A straightforward solution using O(mn) space is probably a bad idea.
- A simple improvement uses O(m + n) space, but still not the best solution.
- Could you devise a constant space solution?

Hint 1:
If any cell of the matrix has a zero we can record its row and column number using additional memory. But if you don't want to use extra memory then you can manipulate the array instead. i.e. simulating exactly what the question says.
Hint 2:
Setting cell values to zero on the fly while iterating might lead to discrepancies. What if you use some other integer value as your marker? There is still a better approach for this problem with 0(1) space.
Hint 3:
We could have used 2 sets to keep a record of rows/columns which need to be set to zero. But for an O(1) space solution, you can use one of the rows and and one of the columns to keep track of this information.
Hint 4:
We can use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero.


### Testcase:
---
[[1,1,1],[1,0,1],[1,1,1]]
[[0,1,2,0],[3,4,5,2],[1,3,1,5]]


### Code:
---
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int rows = matrix.size(); // Number of rows in the matrix
        int cols = matrix[0].size(); // Number of columns in the matrix
        bool firstRowZero = false; // Flag to check if the first row contains a zero
        bool firstColZero = false; // Flag to check if the first column contains a zero

        // Step 1: Check if the first row or column needs to be zeroed
        for (int i = 0; i < rows; i++) {
            if (matrix[i][0] == 0) {
                firstColZero = true; // Set flag if zero is found in the first column
                break;
            }
        }

        for (int j = 0; j < cols; j++) {
            if (matrix[0][j] == 0) {
                firstRowZero = true; // Set flag if zero is found in the first row
                break;
            }
        }

        // Step 2: Use first row and column as flags
        // Iterate over the matrix starting from cell (1,1)
        for (int i = 1; i < rows; i++) {
            for (int j = 1; j < cols; j++) {
                if (matrix[i][j] == 0) {
                    // Mark the corresponding first row and first column cells as zero
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // Step 3: Zero out rows and columns based on flags
        // Iterate over the matrix starting from cell (1,1) again
        for (int i = 1; i < rows; i++) {
            for (int j = 1; j < cols; j++) {
                // If the first cell of the row or column is zero,
                // set the current cell to zero
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        // Step 4: Zero out the first row and column if needed
        // If the first row needs to be zeroed, set all its cells to zero
        if (firstRowZero) {
            for (int j = 0; j < cols; j++) matrix[0][j] = 0;
        }

        // If the first column needs to be zeroed, set all its cells to zero
        if (firstColZero) {
            for (int i = 0; i < rows; i++) matrix[i][0] = 0;
        }
    }
};



// Description: ===================================
/*
To solve the "Set Matrix Zeroes" problem, we can utilize the hints provided to devise a solution that does not require additional space 
for storage, achieving O(1) space complexity. The key idea is to use the first row and the first column of the matrix itself to keep 
track of which rows and columns need to be set to zero, thus eliminating the need for additional storage.

Here's a step-by-step approach:

1. **Determine if the first row and first column need to be zeroed**: Before using the first row and column as storage, we need to know if 
they originally contained any zeros. This information will be used in the last step to set the first row and column to zeros if necessary.

2. **Use the first row and column as flags**: Iterate through the matrix, and for each cell that is zero, set the corresponding element in 
the first row and first column to zero. These flags will later be used to zero out the respective rows and columns.

3. **Zero out rows and columns based on flags**: Iterate through the matrix starting from the second row and second column, and for each 
cell, check its corresponding first row and first column flags. If any of these flags are zero, set the cell to zero.

4. **Zero out the first row and column if needed**: Based on the information obtained in step 1, zero out the first row and/or first column 
if they originally contained zeros.

### Description:

This solution efficiently sets entire rows and columns to zeroes in a given matrix when a zero is encountered, without using additional 
storage. It cleverly repurposes the first row and column of the matrix to serve as indicators (flags) for whether the rest of the row or 
column should be zeroed, thus achieving constant space complexity. Initially, the algorithm determines whether the first row and column 
contain any zeros themselves, so they can be properly handled at the end. Then, it iterates over the matrix, using the first row and column 
to mark which rows and columns should be zeroed. After marking, it zeroes out the appropriate rows and columns, and finally, it zeroes 
out the first row and column if they originally contained zeros. This approach ensures that the space complexity remains O(1), making it 
an elegant and efficient solution for the problem.

*/
