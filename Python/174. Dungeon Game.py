# 174. Dungeon Game

# Topics: Array, Dynamic Programming, Matrix.

'''
# Task:
-------
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists 
of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight 
his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 
or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering 
these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health 
(represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room 
where the princess is imprisoned.

Example 1:
Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.

Example 2:
Input: dungeon = [[0]]
Output: 1

Constraints:
m == dungeon.length
n == dungeon[i].length
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000


# Testcase:
------------
[[-2,-3,3],[-5,-10,1],[10,30,-5]]
[[0]]

# Code:
--------
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

'''
# Solution
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Get the dimensions of the dungeon
        m, n = len(dungeon), len(dungeon[0])

        # Initialize a DP table with 'infinity' to represent the minimum health needed
        # Extra row and column are added to simplify boundary conditions
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Base case: To rescue the princess at (m-1, n-1), the knight needs at least 1 HP
        dp[m][n - 1] = dp[m - 1][n] = 1

        # Iterate over the dungeon grid in reverse order (from bottom-right to top-left)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Calculate the minimum health needed to enter this room
                # It's the minimum of the health needed for the rooms below and to the right
                # minus the health impact of the current room
                min_health = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]

                # Ensure the knight's health is at least 1 at all times
                dp[i][j] = max(1, min_health)

        # The top-left cell gives the minimum health needed at the start to rescue the princess
        return dp[0][0]

# Testing the solution
sol = Solution()
print(sol.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))  # Expected output: 7
print(sol.calculateMinimumHP([[0]]))  # Expected output: 1


# Description:
'''
In this code, we use a standard dynamic programming approach, starting from the end point 
(where the princess is located) and moving back to the starting point (where the knight is located). 
This method allows you to calculate the minimum amount of health required to enter each room, based 
on the health required to enter adjacent rooms and the value in the current room.

'''

