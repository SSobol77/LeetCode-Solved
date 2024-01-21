"""
# 51. N-Queens.

# Topic: Array, Backtracking.

# Task:
----------------
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens 
attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in 
any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both 
indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9


# Testcase:
----------------
4
1


# Code:
----------------
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
"""

# Solution:
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Function to create the board from the current state
        def createBoard():
            # Constructs each row of the board with a queen (Q) at the column indicated in the state
            return ['.' * col + 'Q' + '.' * (n - col - 1) for col in state]

        # Recursive function to place queens
        def solve(row):
            # Base case: if all queens are placed, add the board to the solutions list
            if row == n:
                solutions.append(createBoard())
                return

            # Iterate over each column in the current row
            for col in range(n):
                # Check if the current column and diagonals are not under attack
                if not (cols[col] or diag1[row + col] or diag2[row - col + n - 1]):
                    # Place the queen at the current position
                    state.append(col)
                    # Mark the column and diagonals as under attack
                    cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True

                    # Recurse for the next row
                    solve(row + 1)

                    # Backtrack: remove the queen and unmark the column and diagonals
                    state.pop()
                    cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

        # Initialize solutions list and state (current configuration of queens)
        solutions, state = [], []
        # Initialize arrays to mark columns and diagonals under attack
        cols, diag1, diag2 = [False] * n, [False] * (2 * n), [False] * (2 * n)
        # Start the recursion with the first row
        solve(0)
        # Return all found solutions
        return solutions


# Description:
'''
In this commented code:

- createBoard is a helper function that constructs the board representation from the current state.

- solve is the main recursive function for placing queens. It checks for conflicts using auxiliary arrays 
  for columns (cols) and diagonals (diag1 and diag2).

- cols keeps track of columns under attack, diag1 for the left-to-right diagonals, and diag2 for the 
  right-to-left diagonals.

- The state is represented as a list where the index represents the row, and the value at each index represents 
  the column position of the queen in that row.

- Backtracking is done by removing the last placed queen and unmarking the respective column and diagonal entries.

- The base case is reached when all rows have a queen placed, and the current board configuration is added to 
  the solutions list.

- The function starts by attempting to place a queen in the first row and continues recursively for subsequent rows.

'''
