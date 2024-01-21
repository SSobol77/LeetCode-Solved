# 427. Construct Quad Tree

'''
Task:
------

Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.
A Quad-Tree is a tree data structure in which each internal node has exactly four children. 

Besides, each node has two attributes:
val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. 
     Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

1. If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
2. If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
3. Recurse for each of the children with the proper sub-grid.
If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:
You don't need to read this section for solving the problem. This is only if you want to understand the output format here. The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.
It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].
If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.

Example 2:
Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:

Constraints:
n == grid.length == grid[i].length
n == 2^x where 0 <= x <= 6


# Testcase:
-----------
[[0,1],[1,0]]
[[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]


# Code:
-------
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        

'''
# Solution
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isUniform(x, y, length):
            # Check if all values in the square are the same
            return all(grid[i][j] == grid[x][y] for i in range(x, x + length) for j in range(y, y + length))

        def constructQuadTree(x, y, length):
            if length == 1 or isUniform(x, y, length):
                # If the grid is uniform or of length 1, return a leaf node
                return Node(grid[x][y] == 1, True, None, None, None, None)
            
            # Divide the grid into four parts and construct each recursively
            half = length // 2
            return Node('*', False, 
                        constructQuadTree(x, y, half),
                        constructQuadTree(x, y + half, half),
                        constructQuadTree(x + half, y, half),
                        constructQuadTree(x + half, y + half, half))

        return constructQuadTree(0, 0, len(grid))

'''
*** In this solution:

To construct a Quad Tree from a given grid, we need to implement a recursive 
solution. The idea is to check whether all values in the current grid section
are the same. If they are, we create a leaf node; otherwise, we split the grid
into four equal parts and recursively construct the Quad Tree for each part.

The isUniform function checks if all elements in a square section of the grid 
starting at (x, y) with a given length are the same.
The constructQuadTree function recursively constructs the Quad Tree. If the 
current section of the grid is uniform or of length 1, it returns a leaf node. 
Otherwise, it splits the grid into four equal parts and recursively constructs 
the Quad Tree for each part.
The root of the Quad Tree is constructed by calling constructQuadTree with the 
entire grid.
This solution efficiently constructs a Quad Tree for the given grid, dividing 
the problem into smaller subproblems until the base case is reached. The time 
complexity of this solution is O(n^2) for a grid of size n x n, as it potentially
needs to check every cell of the grid in the worst case.

'''