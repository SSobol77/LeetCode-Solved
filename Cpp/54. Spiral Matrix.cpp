// 54. Spiral Matrix.


// Topic: Array, Matrix, Simulation.


/*
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
Well for some problems, the best way really is to come up with some algorithms for simulation. Basically, you need to simulate what the 
problem asks us to do.
Hint 2:
We go boundary by boundary and move inwards. That is the essential operation. First row, last column, last row, first column, and then 
we move inwards by 1 and repeat. That's all. That is all the simulation that we need.
Hint 3:
Think about when you want to switch the progress on one of the indexes. If you progress on i out of [i, j], you'll shift in the same column.
Similarly, by changing values for j, you'd be shifting in the same row. Also, keep track of the end of a boundary so that you can move 
inwards and then keep repeating. It's always best to simulate edge cases like a single column or a single row to see if anything breaks or 
not.

### Testcase:
---
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3,4],[5,6,7,8],[9,10,11,12]]


### Code:
---
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.empty()) return {};

        vector<int> spiral;
        int rows = matrix.size(), cols = matrix[0].size();
        int top = 0, bottom = rows - 1, left = 0, right = cols - 1;

        while (top <= bottom && left <= right) {
            // Traverse from left to right
            for (int j = left; j <= right; ++j) spiral.push_back(matrix[top][j]);
            ++top;

            // Traverse downwards
            for (int i = top; i <= bottom; ++i) spiral.push_back(matrix[i][right]);
            --right;

            if (top <= bottom) {
                // Traverse from right to left
                for (int j = right; j >= left; --j) spiral.push_back(matrix[bottom][j]);
                --bottom;
            }

            if (left <= right) {
                // Traverse upwards
                for (int i = bottom; i >= top; --i) spiral.push_back(matrix[i][left]);
                ++left;
            }
        }

        return spiral;
    }
};


// Description: ===================================
/*
To return all elements of the matrix in spiral order, we can simulate the process of walking the spiral path. This involves traversing the matrix's outer perimeter and gradually moving inwards, following a right → down → left → up pattern until all elements have been visited.

### Algorithm Steps:
1. **Initialize Boundaries**: Set up initial boundaries for the top, bottom, left, and right edges of the matrix.
2. **Loop Until Done**: Continue traversing the matrix in a spiral until all elements are visited. Keep track of the count of visited elements or adjust boundaries to avoid revisiting.
3. **Rightward Movement**: Traverse from the left boundary to the right boundary along the top row, then move the top boundary one row down.
4. **Downward Movement**: Traverse from the top boundary to the bottom boundary along the right column, then move the right boundary one column to the left.
5. **Leftward Movement**: Traverse from the right boundary to the left boundary along the bottom row, then move the bottom boundary one row up.
6. **Upward Movement**: Traverse from the bottom boundary to the top boundary along the left column, then move the left boundary one column to the right.
7. **Boundary Adjustment**: After completing each direction, adjust the respective boundary to gradually move inwards.
8. **Termination Condition**: The loop terminates when the boundaries cross each other, indicating that the entire matrix has been traversed in spiral order.

### Explanation:
- The algorithm ensures all elements are visited exactly once by adjusting the boundaries after each direction's traversal.
- The checks `if (top <= bottom)` and `if (left <= right)` before the leftward and upward traversals are crucial to handle cases where the spiral collapses into a single row or column, preventing over-traversal.
- The `spiral` vector collects the elements in their spiral order as the algorithm traverses the matrix.

### Complexity:
- **Time Complexity**: O(m * n), where m is the number of rows and n is the number of columns in the matrix. Each element is visited exactly once.
- **Space Complexity**: O(1), not counting the space used for the output vector. The space for the output is O(m * n) and is required for the problem's output, but the algorithm itself uses constant extra space.

*/
