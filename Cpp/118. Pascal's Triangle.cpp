// 118. Pascal's Triangle.


// Topic: Array, Dynamic Programming


/*
### Task:
---
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30

### Testcase:
---
5
1

### Code:
---
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle;

        // Base case; first row is always [1].
        triangle.push_back({1});

        for (int i = 1; i < numRows; i++) {
            vector<int> row(i + 1, 1);  // Create a row with all elements initialized to 1

            // Calculate the values for the inner elements of the row
            for (int j = 1; j < i; j++) {
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }

            // Add the constructed row to the triangle
            triangle.push_back(row);
        }

        return triangle;
    }
};


// Description: ===================================
/*
To generate Pascal's triangle for a given number of rows (`numRows`), we can use a dynamic programming approach. Each row in Pascal's triangle is constructed based on the previous row, with the exception of the first row, which is always `[1]`. The elements of each row are determined as follows: the first and last elements of every row are `1`, and every other element at position `i` in a row is the sum of the elements at positions `i` and `i-1` in the previous row.

Here's how to implement this in C++:

### Step-by-Step Approach:
1. Initialize a vector of vectors of integers `result` to store the rows of Pascal's triangle.
2. Iterate from `0` to `numRows - 1`. For each iteration:
   - Create a new vector `row` with the size of the current row index + 1, and set the first and last elements to `1`.
   - For each element in the `row` from the second element to the second-to-last element, set `row[j]` to the sum of `result[i-1][j-1]` and `result[i-1][j]`, where `i` is the current row index and `j` is the current element index within the row.
   - Add the constructed `row` to the `result`.
3. Return the `result`.

### Description:
- **Line 7:** The first row `[1]` is added to the triangle as the base case.
- **Lines 9-16:** For each subsequent row (`i`), a new row is initialized with `1`s. The elements between the first and last are computed by adding the appropriate elements from the previous row (`triangle[i - 1]`).
- **Line 15:** The constructed row is added to the triangle.
- **Line 18:** The complete Pascal's triangle up to `numRows` is returned.

This solution efficiently constructs Pascal's triangle row by row, reusing the results from the previous rows to calculate the new row, adhering to the principle of dynamic programming.

*/
