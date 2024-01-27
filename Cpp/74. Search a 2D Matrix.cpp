// 74. Search a 2D Matrix.

// Topic: Array, Binary Search, Matrix.


/*
### Task:
---
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


### Testcase:
---
[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
3
[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
13


### Code:
---
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Check for an empty matrix condition
        if (matrix.empty() || matrix[0].empty()) return false;

        int m = matrix.size();    // Number of rows in the matrix
        int n = matrix[0].size(); // Number of columns in the matrix

        // Initialize binary search boundaries
        int left = 0;
        int right = m * n - 1; // Treat the 2D matrix as a 1D sorted array

        // Binary search loop
        while (left <= right) {
            int mid = left + (right - left) / 2; // Calculate mid index to avoid overflow
            // Map the mid index to 2D coordinates in the matrix
            // The division results in the row index, and the modulus results in the column index
            int midValue = matrix[mid / n][mid % n];

            if (midValue == target) {
                // Target value found at the mid position
                return true;
            } else if (midValue < target) {
                // If midValue is less than the target, narrow the search to the upper half
                left = mid + 1;
            } else {
                // If midValue is greater than the target, narrow the search to the lower half
                right = mid - 1;
            }
        }

        // Target not found in the matrix
        return false;
    }
};



// Description: ===================================
/*
To search for a target value in a 2D matrix under the given constraints with an O(log(m * n)) time complexity, we 
can apply a binary search algorithm. The key observation here is that even though the data is in a 2D matrix, the 
sorting properties allow us to treat it as a sorted 1D array. This is because each row is sorted, and the first integer 
of each row is greater than the last integer of the previous row.


### Detailed Explanation:

- The matrix's dimensions are determined by `m` (number of rows) and `n` (number of columns).
- The binary search is initialized with `left` at 0 and `right` at `m * n - 1`, treating the 2D matrix as a 1D array for the 
  purpose of the search.
- Within the while loop, a `mid` index is calculated in the same manner as a standard binary search. The `mid` value is then 
  mapped back to its 2D coordinates in the matrix using `matrix[mid / n][mid % n]`.
- If the `midValue` is equal to the `target`, the function returns `true`.
- If the `midValue` is less than the `target`, the search continues in the upper half by adjusting `left`.
- If the `midValue` is greater than the `target`, the search continues in the lower half by adjusting `right`.
- If the loop completes without finding the target, `false` is returned.

This algorithm efficiently locates the target within the matrix with a time complexity of O(log(m * n)), leveraging the sorted 
properties of the matrix.

*/
