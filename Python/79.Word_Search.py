"""
# 79. Word Search.

# Topic: Array, Backtracking, Matrix.

# Task:
------------
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?


# Testcase:
--------------
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCCED"
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"SEE"
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCB"



# Code:
----------
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

"""
# Solution:
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Count the frequency of each character in the board and the word
        board_chars = collections.Counter(ch for row in board for ch in row)
        word_chars = collections.Counter(word)
        # If any character in 'word' is more frequent than in 'board', return False
        if any(word_chars[ch] > board_chars[ch] for ch in word_chars):
            return False

        # Store the number of rows and columns in the board
        rows, cols = len(board), len(board[0])
        # Define the directions for moving to adjacent cells (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Recursive function to perform backtracking
        def backtrack(row, col, index):
            # If the current index equals the length of the word, the word is found
            if index == len(word):
                return True
            # Check boundaries and character match
            if not (0 <= row < rows and 0 <= col < cols) or board[row][col] != word[index]:
                return False

            # Save the current character and mark the cell as visited
            temp, board[row][col] = board[row][col], '#'

            # Recursively explore adjacent cells in all four directions
            # 'any' returns True if the word is found in any direction
            found = any(backtrack(row + dr, col + dc, index + 1) for dr, dc in directions)

            # Restore the original character in the cell after exploring
            board[row][col] = temp
            return found

        # Iterate through each cell of the board to start the search
        for row in range(rows):
            for col in range(cols):
                # Start backtracking from the current cell
                if backtrack(row, col, 0):
                    # If the word is found, return True
                    return True
        # Return False if the word is not found in the board
        return False


# Description:
'''
Description of the Solution:
---------------------------------
1. Character Frequency Check: The solution begins by counting the frequency of each character in the word and 
   the board. If any character in the word has a higher frequency than in the board, it returns False, as the
   word cannot be formed.

2. Board Dimensions and Directions: The rows and columns of the board are stored for easy access. A directions
   array is used to simplify moving to adjacent cells.

3. Backtracking Function: The backtrack function is the core of the solution. It checks whether the current 
   path can form the word. The function is called recursively to explore all possible paths in the grid.

    *   Base Case: If the index reaches the length of the word, it means the entire word is found, and the 
        function returns True.
    *   Boundary and Match Check: It checks if the current cell is within the grid and if the cell's 
        character matches the current character of the word.
    *   Marking Visited Cells: To avoid revisiting the same cell, it is temporarily marked with a special 
        character ('#').
    *   Exploring Directions: The function explores all four directions (up, down, left, right) from the 
        current cell.
    *   Restoring Cell State: After exploring all directions, the original character of the cell is restored.

4. Starting the Search: The solution iterates over each cell of the board, using each cell as a potential 
   starting point for the word. If the backtrack function returns True for any cell, the word is found in 
   the board, and True is returned.

5. Conclusion: If no path forms the word, the function returns False, indicating that the word cannot be 
   formed from the board.

This solution efficiently searches for the word in the board, using backtracking to explore all possible
paths and pruning paths early when they don't lead to a solution.


Additional Comments Explained:
---------------------------------
    
* Character Frequency Check: Before starting the backtracking, the code first checks if the word can be 
  formed from the characters available on the board. This is done by comparing the frequency of each 
  character in the word with its frequency on the board.

* Storing Board Dimensions: The number of rows and columns in the board are stored in rows and cols for 
  easy reference.

* Directions Array: The directions array represents the four possible moves from any cell (right, down, 
  left, up). This array is used to simplify the logic for moving to adjacent cells.

* Backtracking Function (backtrack):

    -    The function is called for each cell in the grid.
    -    It first checks if the current index in the word is equal to the word's length, indicating that 
         the entire word has been found.
    -    It then checks if the current cell is within the grid boundaries and if the character in the cell 
         matches the current character in the word.
    -    The current cell is temporarily marked as visited by replacing its character with '#'.
    -    The function explores all adjacent cells recursively. The any function is used to return True as 
         soon as one of the recursive calls finds the complete word.
    -    After exploring all directions, the cell is restored to its original character.

* Starting the Search: The outer loop iterates through each cell of the board, treating each cell as a 
  potential starting point for the word.

* Returning the Result: If the word is found starting from any cell, True is returned. If the loop 
  completes without finding the word, False is returned, indicating that the word is not present 
  in the grid.

This detailed commenting helps to understand the logic and flow of the code more clearly, particularly 
how backtracking is used to explore all possible paths in the grid to find the word.

'''
