// 240. Search a 2D Matrix II.


// Topic: Array, Binary Search, Divide and Conquer, Matrix.


/*
### Task:
---
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


### Testcase:
---
[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
5
[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
20


### Code:
---
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Start from the top-right corner
        int row = 0;
        int col = matrix[0].size() - 1;

        // While within the bounds of the matrix
        while (row < matrix.size() && col >= 0) {
            if (matrix[row][col] == target) {
                // Target found
                return true;
            } else if (matrix[row][col] > target) {
                // Target cannot be in this column
                col--;
            } else {
                // Target cannot be in this row
                row++;
            }
        }
        // Target not found
        return false;
    }
};

// Description: ===================================
/*
To efficiently search for a target value in a 2D matrix with the given properties, we can leverage the sorted nature of the rows and columns to eliminate portions of the matrix that do not need to be searched. A common approach is to start from the top-right corner (or bottom-left corner) of the matrix and work our way towards finding the target value.

Here's a step-by-step approach starting from the top-right corner:

1. **Initialize the position**: Start from the top-right corner of the matrix. Let's denote our current position as `(row, col)`.

2. **Navigate the matrix**:
   - If the target is greater than the value at the current position, it cannot be in the current row because all the values to the left are smaller. Move down to the next row (`row++`).
   - If the target is less than the value at the current position, it cannot be in the current column because all the values below are larger. Move left to the previous column (`col--`).

3. **Repeat the navigation** until the target is found or the limits of the matrix are exceeded.


### Description:

This solution efficiently searches for a target value in a 2D matrix that has its rows and columns sorted in ascending order. By starting the search from the top-right corner, we can make a decision at each step to move either left or down, effectively reducing the search space. This decision is based on the comparison between the target value and the current element:

- If the target is larger than the current element, we move down because all the elements in the current row to the left are smaller and cannot be the target.
- If the target is smaller than the current element, we move left because all the elements in the current column below are larger and cannot be the target.

This algorithm ensures that at each step, we are moving closer to the position where the target value might be, if it exists in the matrix. The time complexity of this approach is O(m + n), where m is the number of rows and n is the number of columns in the matrix, making it a highly efficient solution for the problem.



*/