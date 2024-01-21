# 120. Triangle.

# Topic: Array, Dynamic Programming.

'''
# Task:
-------
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on 
index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-10^4 <= triangle[i][j] <= 10^4

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?

# Testcase:
-----------
[[2],[3,4],[6,5,7],[4,1,8,3]]
[[-10]]

# Code:
-------
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
    

'''
# Solution:
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second last row of the triangle and move upwards
        for row in range(len(triangle) - 2, -1, -1):  # len(triangle) - 2 is the second-to-last row
            for col in range(len(triangle[row])):  # Iterate through all elements in the current row
                # Update the current cell's value. The new value is the sum of the current cell's value
                # and the minimum of the two adjacent numbers in the row below.
                # This represents the minimum sum achievable from this cell to the bottom of the triangle.
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

        # After completing the loop, the top element of the triangle (triangle[0][0]) contains
        # the minimum path sum from the top to the bottom of the triangle.
        return triangle[0][0]

# Test cases
solution = Solution()
print(solution.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # Expected output: 11
print(solution.minimumTotal([[-10]]))                                  # Expected output: -10


'''
Description:
To solve the Triangle problem, we can use dynamic programming. The goal is to find the minimum path sum 
from the top to the bottom of the triangle. We will start from the bottom row and work our way up to the
top, updating each cell with the minimum sum achievable from that cell.

To optimize space, instead of using a separate DP array, we can modify the triangle array itself, since 
we only need information from the row directly below the current cell. This will ensure that the solution 
uses only O(n) extra space.

Explanation:
* Bottom-Up Approach: We start from the second-to-last row and work our way up to the top of the triangle.
  This way, each cell is updated based on the minimum path sum from that cell to the bottom of the triangle.
* Updating Each Cell: For each cell in the current row, update its value to the sum of its current value and 
  the minimum of the two adjacent cells in the row below. This represents choosing the path with the minimum 
  sum at each step.
* Final Answer: After processing all rows, the top element of the triangle (triangle[0][0]) will contain 
  the minimum total path sum from top to bottom.

This approach modifies the input triangle array in-place and does not use any additional space beyond the input, 
achieving the space complexity of O(n), where n is the number of rows in the triangle. The time complexity is O(n^2), 
as we traverse each element of the triangle once.

'''
