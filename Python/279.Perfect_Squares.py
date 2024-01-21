"""
# 279. Perfect Squares.

# Topic: Math, Dynamic Programming, Breadth-First Search.


# Task:
---------
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is 
the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 
Constraints:
1 <= n <= 10^4


# Testcase:
------------
12
13

# Code:
----------
class Solution:
    def numSquares(self, n: int) -> int:
        

"""
# Solution:
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        # Generate all possible square numbers less than n
        squares = [i * i for i in range(1, int(n**0.5) + 1)]

        # Queue for BFS: each element is a tuple (value, numSquares)
        queue = deque([(0, 0)])
        
        # Set to track visited nodes
        visited = set()

        while queue:
            value, numSquares = queue.popleft()
            # For each square number, reach the next node
            for square in squares:
                nextVal = value + square
                # If the next node is n, return the path length
                if nextVal == n:
                    return numSquares + 1
                # If it's less than n and not yet visited, add it to the queue
                if nextVal < n and nextVal not in visited:
                    visited.add(nextVal)
                    queue.append((nextVal, numSquares + 1))

        # If somehow n isn't reachable (shouldn't happen with correct input), return -1
        return -1


# Description:
'''
For the best runtime performance solving the "Perfect Squares" problem, a well-known approach is to use the Breadth-First 
Search (BFS) algorithm. This approach considers each number as a node in a graph and each square number jump as an edge to 
another node. The BFS will efficiently find the shortest path from 0 to n, representing the least number of perfect squares.

This method is often faster in practice for this problem because it doesn't necessarily explore all combinations like the 
dynamic programming approach. Instead, it stops as soon as it finds the target n.

Here's how you implement this optimized solution:
--------------------------------------------------
-   Initialize BFS: Use a queue for BFS, starting from 0.

-   Perform BFS: For each step, try all possible square number jumps from the current number. 
    If you reach n, you've found the minimum path.

-   Track Visited Nodes: To avoid repetitive work, keep track of visited nodes.

    
In this optimized code:

-   We use BFS to find the shortest path to n, where each path step consists of adding a square number to the current total.
-   The queue in BFS stores pairs of the current sum and the number of steps taken to reach it.
-   We iterate until the queue is empty, but we will almost always break early when we reach n.
-   The visited set is crucial for ensuring we don't revisit nodes, significantly speeding up the search.

This approach is generally more efficient than dynamic programming for this problem, especially when n is large, because it 
will stop as soon as it finds the solution without needing to fill out an entire DP array.
    
'''