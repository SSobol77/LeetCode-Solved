# 118. Pascal's Triangle.

# Topic: Array, Dynamic Programming.

"""
## Task:
---------
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

            1
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1
       
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30


## Testcase:
-------------
5
1


## Code:
----------
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
"""
# Solution

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        # First row is always [1]
        pascal_triangle = [[1]]

        for i in range(1, numRows):
            row = [1]  # Start each row with a 1
            for j in range(1, i):
                # Each element is the sum of the two elements above it
                row.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j])
            row.append(1)  # End each row with a 1
            pascal_triangle.append(row)

        return pascal_triangle


# Description
'''
## Pascal's Triangle - Solution Explanation:

Pascal's triangle is a triangular array of numbers where each number is the sum of the two numbers directly above it.
The rows of Pascal's triangle are conventionally enumerated starting with row \( n = 0 \) at the top (the 0th row). 
The entries in each row are numbered from the left beginning with \( k = 0 \) and are usually staggered relative to 
the numbers in the adjacent rows. The triangle may be constructed in the following manner: In row 0 (the topmost row), 
there is a unique nonzero entry 1. Each entry of each subsequent row is constructed by adding the number above and to 
the left with the number above and to the right, treating blank entries as 0. The initial number of each row is 1.

To generate Pascal's triangle for `numRows` rows, we can use dynamic programming. The idea is to iterate through each 
row and calculate each element as the sum of the elements diagonally above it.

### Explanation:
----------------

1. **Base Case**: If `numRows` is 0, return an empty list.

2. **First Row Initialization**: The first row of Pascal's triangle is always `[1]`.

3. **Iterate Through Rows**: Starting from the second row (index 1), iterate until `numRows`.

    - Initialize each row with a `[1]` at the beginning.
    - For each position `j` in the row (starting from 1 to one less than the row index `i`), calculate the element 
      as the sum of the elements diagonally above it (`pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]`).
    - Add a `[1]` at the end of each row.

4. **Build the Triangle**: Append each newly created row to `pascal_triangle`.

5. **Return the Result**: Once all rows are computed, return `pascal_triangle`.

This implementation ensures that the generated Pascal's triangle will have `numRows` rows, and each row is constructed 
based on the rules of Pascal's triangle.

'''
