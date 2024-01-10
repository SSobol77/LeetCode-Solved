# 894. All Possible Full Binary Trees.

# Topic: Dynamic Programming, Tree, Recursion, Memoization, Binary Tree.

'''
# Task:
---------------
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each 
tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of 
trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Example 1:
Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

Example 2:
Input: n = 3
Output: [[0,0,0]]

Constraints:
1 <= n <= 20


# Testcase:
-----------------
7
3


# Code:
----------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

'''

# Solutions:

# 1 ----------------------------------------------------------------

# Definition of the TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child

class Solution:
    def allPossibleFBT(self, n: int):
        # Full binary trees can only be constructed with an odd number of nodes
        if n % 2 == 0:
            return []  # Return an empty list for even n

        # Base case: if n is 1, the only full binary tree is a single node
        if n == 1:
            return [TreeNode(0)]

        # List to store all possible full binary trees
        trees = []

        # Iterate over possible combinations of left and right subtrees
        for left_nodes in range(1, n, 2):  # Increment by 2 to ensure odd numbers
            right_nodes = n - 1 - left_nodes  # Remaining nodes for the right subtree

            # Recursive call for constructing all combinations of left and right subtrees
            for left in self.allPossibleFBT(left_nodes):
                for right in self.allPossibleFBT(right_nodes):
                    root = TreeNode(0)  # Create a new root node
                    root.left = left  # Assign left subtree
                    root.right = right  # Assign right subtree
                    trees.append(root)  # Append the newly formed tree to the list

        return trees  # Return the list of all possible full binary trees

# Description 1:
'''
The provided code is a solution for generating all possible full binary trees with a given 
number of nodes. The solution involves using recursion and handling base cases effectively. 

Description of the Solution:

*   TreeNode Class: Represents a node in a binary tree. Each node has a value (always 0 as per 
    the problem statement) and pointers to its left and right children.

*   Recursive Solution: The allPossibleFBT method recursively generates all full binary trees 
    for a given number of nodes n. The method returns a list of TreeNode objects, each representing 
    the root of a possible full binary tree.

*   Handling Even n: Full binary trees can only be constructed with an odd number of nodes. Therefore, 
    if n is even, the method returns an empty list.

*   Base Case: The base case of the recursion is when n is 1. In this case, the only possible tree 
    is a single node, so the method returns a list containing one TreeNode.

*   Building Trees: For odd values of n greater than 1, the method iterates over all odd numbers less 
    than n to split the nodes between the left and right subtrees. For each split, it recursively 
    generates all combinations of left and right subtrees and then combines them with a new root node 
    to form full binary trees.

*   Efficient Construction: By dividing the problem into smaller subproblems (left and right subtrees), 
    the solution efficiently constructs all possible full binary trees.

This approach is an excellent demonstration of the divide-and-conquer technique and recursion in solving 
complex problems in tree structures.

'''

# 2 -------------------------------------------------------------------------------------------------------

class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        # Full binary trees can only be constructed with an odd number of nodes
        if n % 2 == 0:
            return []  # Return an empty list for even n

        # Initialize a DP table with empty lists
        dp = [[] for _ in range(n + 1)]
        dp[1].append(TreeNode(0))  # Base case with a single node
        
        # Iterate over odd counts from 3 to n
        for count in range(3, n + 1, 2):
            # Split the count into two parts, i and count - 1 - i
            for i in range(1, count - 1, 2):
                # Iterate through all possible left and right subtrees stored in the DP table
                for left in dp[i]:
                    for right in dp[count - 1 - i]:
                        # Create a new root node with left and right children
                        root = TreeNode(0, left, right)
                        # Add the new tree to the DP table
                        dp[count].append(root)
                        
        # Return the list of all possible full binary trees with n nodes
        return dp[n]

# Description 2:
'''
The provided code is an alternative solution to the "All Possible Full Binary Trees" problem using 
dynamic programming (DP) for optimization. This approach stores previously computed results to avoid 
redundant calculations in recursive calls.

Description of the Solution:

*   Dynamic Programming (DP) Table: The solution uses a DP table (dp) to store the results of 
    subproblems. Each entry dp[i] contains a list of all possible full binary trees with i nodes.

*   Base Case: For a single node (n = 1), the only possible tree is a single node. This case is 
    handled explicitly by adding a TreeNode with value 0 to dp[1].

*   Iterating Over Possible Trees: The algorithm iterates over every odd number from 3 to n. For 
    each number (count), it tries different splits between the left and right subtrees.

*   Building Trees Using Previous Results: For each split, the algorithm iterates through all 
    combinations of left and right subtrees that have been previously computed and stored in 
    the DP table. It then creates a new tree for each combination by creating a new root node 
    and assigning the left and right subtrees.

*   Optimization: This DP approach significantly reduces the number of redundant calculations 
    compared to a purely recursive solution. It is especially efficient when multiple calls are
    made with the same n value.

*   Returning the Result: The method returns dp[n], which is a list of all possible full binary 
    trees with n nodes.

This approach is an efficient way to solve the problem as it leverages the overlapping subproblems 
property, which is a hallmark of problems where dynamic programming can provide optimization.

'''
