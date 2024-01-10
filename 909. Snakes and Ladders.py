# 909. Snakes and Ladders

# Topic: Graph BFS, Array, Breadth-First Search, Matrix

'''
# Task:
-------
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless 
of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is
board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of 
another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the 
ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

Example 1:
Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

Example 2:
Input: board = [[-1,-1],[-1,3]]
Output: 1

Constraints:
n == board.length == board[i].length
2 <= n <= 20
board[i][j] is either -1 or in the range [1, n2].
The squares labeled 1 and n2 do not have any ladders or snakes.


# Testcase:
-----------
[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
[[-1,-1],[-1,3]]

# Code:
-------
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
      


'''
# Solution
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_index(s):
            # Convert the square number to board coordinates (r, c)
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if row % 2 != n % 2 else n - 1 - rem
            return row, col

        # Initialize BFS
        queue = deque([(1, 0)])  # (square, moves)
        visited = set([1])  # Track visited squares

        while queue:
            s, moves = queue.popleft()
            if s == n * n:  # Reached the end
                return moves
            for next_s in range(s + 1, min(s + 6, n * n) + 1):
                r, c = get_index(next_s)
                if board[r][c] != -1:  # Check for snakes or ladders
                    next_s = board[r][c]
                if next_s not in visited:
                    visited.add(next_s)
                    queue.append((next_s, moves + 1))

        return -1  # Impossible to reach the end

# Testing the solution
sol = Solution()
print(sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1],
                            [-1,35,-1,-1,13,-1],
                            [-1,-1,-1,-1,-1,-1],
                            [-1,15,-1,-1,-1,-1]]))  # Expected output: 4
print(sol.snakesAndLadders([[-1,-1],
                            [-1,3]]))  # Expected output: 1

# Description:
'''
Description of the "Snakes and Ladders" Solution:
The provided Python code offers a solution to the "Snakes and Ladders" problem using a Breadth-First Search (BFS)
algorithm. The goal is to find the minimum number of moves required to reach the end of the game board, considering
the presence of snakes and ladders that can alter the player's position.

Key Components of the Solution:
Board Conversion: The game board, a 2D grid, is navigated using a single integer to represent each square. The get_index 
function converts this integer into corresponding row and column coordinates on the board. This conversion accounts for
the Boustrophedon style of the board, where the direction of numbering alternates with each row.

BFS Initialization: The BFS algorithm is initialized with a queue (deque) that stores pairs of the current square and 
the number of moves taken to reach it. The visited set tracks the squares that have already been explored to avoid 
revisiting them.

BFS Loop:

The loop continues until the queue is empty.
In each iteration, the algorithm dequeues an element (representing the current square and the number of moves taken to 
reach it).
If the current square is the last square on the board (n * n), the function returns the number of moves, as the goal is 
reached.
The loop then explores up to six possible next moves (simulating a dice roll) and updates the next square based on the 
presence of snakes or ladders.
Snakes and Ladders Handling: If a snake or ladder is encountered (indicated by board[r][c] != -1), the player's position
is updated to the end of the snake or ladder.

Tracking Visited Squares: Squares that have been visited are added to the visited set to prevent redundant processing.

Return Value: If the end of the board is unreachable, the function returns -1. Otherwise, it returns the minimum number 
of moves required to reach the end.

Testing the Solution:
The code includes test cases to validate its functionality. It tests the algorithm on different board configurations to
ensure it correctly calculates the minimum number of moves, considering the complexities of snakes and ladders.

Efficiency of the Solution:
Time Complexity: The algorithm has a time complexity of O(n^2), where n is the dimension of the board. Each square is 
visited at most once.
Space Complexity: The space complexity is also O(n^2), primarily due to the storage of the board and the visited set.
This solution effectively utilizes BFS to navigate the "Snakes and Ladders" board, providing an efficient method to 
determine the minimum moves required to win the game.

'''
