# 1496. Path Crossing

# Topic: Hash Table, String

'''
# Task:
-------
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east,
or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have 
previously visited. Return false otherwise.

Example 1:
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.

Constraints:
1 <= path.length <= 10^4
path[i] is either 'N', 'S', 'E', or 'W'.


# Testcase:
-----------
"NES"
"NESWW"

# Code:
-------
class Solution:
    def isPathCrossing(self, path: str) -> bool:
   
'''
# Solution:

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Dictionary of lambda functions for each direction
        f = {'N': lambda x, y: (x, y - 1), 
             'S': lambda x, y: (x, y + 1), 
             'W': lambda x, y: (x - 1, y), 
             'E': lambda x, y: (x + 1, y)}

        # Initialize starting position and set of visited positions
        pos = (0, 0)
        path_pos = {pos}

        # Iterate through the path
        for d in path:
            # Update position based on the direction
            pos = f[d](*pos)
            # Check if the new position has been visited
            if pos in path_pos:
                return True
            # Add the new position to the set of visited positions
            path_pos.add(pos)

        # Return False if no crossing is found
        return False

# Testing the solution
sol = Solution()
print(sol.isPathCrossing("NES"))  # Expected output: False
print(sol.isPathCrossing("NESWW"))  # Expected output: True


# Description:
'''
The solution to the "Path Crossing" problem is designed to efficiently track the movement of a path on a 2D plane 
and determine if the path crosses itself at any point. The code achieves this through the following key components:

Tracking Visited Positions:

The code uses a Python set, path_pos, to keep track of all the positions that have been visited so far.
Sets in Python are highly efficient for membership testing, which means checking if a position has already
been visited is done in constant time, O(1).
Each position is represented as a tuple (x, y), where x and y are the coordinates on the 2D plane.
Lambda Functions for Direction Handling:

The code defines a dictionary f where each key is a character representing a direction ('N', 'S', 'E', 'W') and
each value is a lambda function.
These lambda functions take the current position (x, y) as input and return a new position based on the direction.
For example, 'N' (North) decreases the y-coordinate by 1, 'E' (East) increases the x-coordinate by 1, and so on.
This approach allows for concise and readable handling of direction changes.
Path Iteration and Crossing Check:

The code iterates through each character in the path string. Each character represents a step in a certain direction.
For each step, the code updates the current position using the corresponding lambda function from the f dictionary.
After updating the position, the code checks if this new position already exists in the path_pos set. If it does, 
this means the path has crossed itself, and the function returns True.
If the position is new, it is added to the path_pos set, and the iteration continues.
Return Value:

If the function completes the iteration without finding any crossing (i.e., no repeated position), it returns False,
indicating that the path does not cross itself.

'''
