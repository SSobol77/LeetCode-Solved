// 48. Rotate Image.


// Topic: Array, Math, Matrix.


/*
### Task:
---
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

### Testcase:
---
[[1,2,3],[4,5,6],[7,8,9]]
[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]


### Code:
---
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        
        // Step 1: Transpose the matrix
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {  // Start from 'i' to avoid re-transposing
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        
        // Step 2: Horizontal flip
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n / 2; ++j) {  // Only iterate halfway for a flip
                swap(matrix[i][j], matrix[i][n - j - 1]);
            }
        }
    }
};

// Description: ===================================
/*
Rotating an image (or a 2D matrix) by 90 degrees clockwise in-place involves two main steps: a transpose operation followed by a horizontal flip. The transpose operation swaps the matrix elements along its diagonal, converting rows into columns. The horizontal flip then reverses the order of elements in each row, achieving the desired rotation.

### Steps to Rotate the Matrix:
1. **Transpose the Matrix**: Iterate over the matrix and swap the element at `matrix[i][j]` with the element at `matrix[j][i]`, effectively transposing the matrix. This step is only performed for one half of the matrix to avoid re-transposing the elements back to their original positions.
   
2. **Horizontal Flip**: For each row in the matrix, reverse the elements in the row. This can be done by swapping the elements at `matrix[i][j]` with `matrix[i][n - j - 1]`, where `n` is the length of the row.


### Explanation:
- The `swap(matrix[i][j], matrix[j][i])` operation in the transpose step changes rows to columns. For example, the first row becomes the first column, the second row becomes the second column, and so on.
- The `swap(matrix[i][j], matrix[i][n - j - 1])` operation in the horizontal flip step reverses each row. For example, the first element in a row is swapped with the last, the second with the second last, and so on, until the middle of the row is reached.
- Together, these two steps rotate the matrix 90 degrees clockwise.

### Constraints Handling:
- This solution works for any `n x n` matrix, adhering to the given constraints of `1 <= n <= 20`.
- The in-place operations ensure that no additional matrix is allocated, satisfying the requirement to modify the matrix directly.

### Time and Space Complexity:
- **Time Complexity**: O(n^2), where `n` is the number of rows (or columns) in the matrix. Each element is accessed a constant number of times.
- **Space Complexity**: O(1), as the rotation is done in-place with only a constant amount of extra space used for swapping elements.

*/
