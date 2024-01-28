// 1074. Number of Submatrices That Sum to Target.

// Topics: Array, Hash Table, Matrix, Prefix Sum.

/*
#Task:
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:
Input: matrix = [[904]], target = 0
Output: 0

Constraints:
1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8

Hint 1
Using a 2D prefix sum, we can query the sum of any submatrix in O(1) time. Now for each (r1, r2), 
we can find the largest sum of a submatrix that uses every row in [r1, r2] in linear time using a sliding window.


#Testcase:
[[0,1,0],[1,1,1],[0,1,0]]
0
[[1,-1],[-1,1]]
0
[[904]]
0

#Code:
class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        
    }
};
*/
// Solution:
class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int count = 0;
        
        // Calculate the 2D prefix sum array
        vector<vector<int>> prefixSum(rows + 1, vector<int>(cols + 1, 0));
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                // Calculate the sum of elements in the submatrix (0,0) to (i-1,j-1)
                prefixSum[i][j] = matrix[i - 1][j - 1] +
                                prefixSum[i - 1][j] +
                                prefixSum[i][j - 1] -
                                prefixSum[i - 1][j - 1];
            }
        }
        
        // Iterate through all possible pairs of rows (r1, r2)
        for (int r1 = 1; r1 <= rows; r1++) {
            for (int r2 = r1; r2 <= rows; r2++) {
                // Stores the count of prefix sums encountered so far
                unordered_map<int, int> prefixSumCount;
                // Initialize with 0 since no elements have been chosen yet
                prefixSumCount[0] = 1;
                int currentSum = 0;
                
                // Iterate through all possible columns
                for (int c = 1; c <= cols; c++) {
                    // Calculate the sum of the submatrix using the current rows
                    currentSum = prefixSum[r2][c] - prefixSum[r1 - 1][c];
                    
                    // Check if (currentSum - target) exists in prefixSumCount
                    if (prefixSumCount.find(currentSum - target) != prefixSumCount.end()) {
                        // Increment the count by the number of previous occurrences
                        count += prefixSumCount[currentSum - target];
                    }
                    
                    // Update prefixSumCount with the currentSum
                    prefixSumCount[currentSum]++;
                }
            }
        }
        
        return count;
    }
};

// Description:
/*
Certainly! Here's a detailed algorithm description for the solution to the "Number of Submatrices That Sum to Target" problem:

**Algorithm Description:**

1. Initialize necessary variables:
   - `rows` and `cols` to store the number of rows and columns in the given matrix.
   - `count` to keep track of the number of submatrices that sum to the target.
   - Create a 2D array `prefixSum` of size `(rows + 1) x (cols + 1)` to store the prefix sum of the elements in the matrix.

2. Calculate the 2D Prefix Sum:
   - Iterate through each cell of the `prefixSum` array from `(1,1)` to `(rows,cols)` to calculate the sum of elements in the submatrix from `(0,0)` to `(i-1,j-1)` of the original matrix.
   - Update `prefixSum[i][j]` with the cumulative sum of elements up to cell `(i,j)`.

3. Iterate through Pairs of Rows:
   - For each pair of row indices `(r1, r2)` where `r1` ranges from `1` to `rows` and `r2` ranges from `r1` to `rows`:
     - Create an unordered map `prefixSumCount` to store the count of prefix sums encountered so far.
     - Initialize `prefixSumCount[0]` to `1` since there are no elements chosen yet, and their sum is zero.
     - Initialize `currentSum` to zero.

4. Sliding Window Technique:
   - Iterate through all possible columns `c` from `1` to `cols`:
     - Calculate `currentSum` as the sum of elements in the submatrix using rows `(r1, r2)` and columns `(1, c)` from the `prefixSum` array.
     - Check if `(currentSum - target)` exists in `prefixSumCount`. If it does, it means there is a submatrix whose sum is equal to the target.
     - Increment the `count` by the value stored in `prefixSumCount[currentSum - target]` to account for all submatrices that end at column `c` and have the target sum.
     - Update `prefixSumCount[currentSum]` by incrementing it to account for the current prefix sum.

5. Repeat Steps 3 and 4 for all pairs of rows `(r1, r2)`.

6. After all iterations, `count` will contain the total number of non-empty submatrices in the given matrix that sum to the target.

7. Return the `count` as the final result.

**Complexity Analysis:**

- Time Complexity: The algorithm runs in O(rows^2 * cols) time due to the nested loops for pairs of rows and columns.
- Space Complexity: The prefix sum array `prefixSum` has a space complexity of O(rows * cols), and the `prefixSumCount` hashmap uses additional space. Overall, the space complexity is O(rows * cols).

This algorithm efficiently computes the count of submatrices with a target sum in the given matrix by utilizing the prefix sum technique and a sliding window approach, making it a practical solution for the problem.

*/
