"""
# 124. Binary Tree Maximum Path Sum.

# Topic: Dynamic Programming, Tree, Depth-First Search, Binary Tree.


# Task:
---------------
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node 
can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
The number of nodes in the tree is in the range [1, 3 * 10^4].
-1000 <= Node.val <= 1000


# Testcase:
[1,2,3]
[-10,9,20,null,null,15,7]


# Code:
-----------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
    
"""
# Solution:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Define a recursive function to traverse the tree
        def dfs(node):
            if not node:
                # Base case: If the node is None, return 0 (no contribution to the path sum)
                return 0
            
            # Recursively calculate the max path sum for the left subtree
            # If the calculated sum is negative, reset it to 0 as we don't want to decrease the total path sum
            left_max = max(dfs(node.left), 0)

            # Similarly, calculate the max path sum for the right subtree
            right_max = max(dfs(node.right), 0)
            
            # Update the global maximum path sum
            # This includes the current node's value and the maximum path sums from its left and right subtrees
            # We consider the current node as the "root" of a potential max-sum path
            self.max_sum = max(self.max_sum, node.val + left_max + right_max)
            
            # Return the maximum sum of a path starting from the current node and going down
            # This is used to compute the max path sum for the parent nodes
            return node.val + max(left_max, right_max)
        
        # Initialize the global maximum path sum to a very small number
        self.max_sum = float('-inf')

        # Start DFS traversal from the root
        dfs(root)

        # Return the global maximum path sum found during the traversal
        return self.max_sum



# Description:
'''
The "Binary Tree Maximum Path Sum" problem is a classic binary tree problem that can be efficiently solved using a depth-first 
search (DFS) approach. The key idea is to compute the maximum path sum for each node recursively and keep track of the overall
maximum path sum.

Here's a step-by-step approach to solving this problem:

1. Define the Recursive Function:

For each node, consider two quantities:
Local Max Path Sum: The maximum sum of a path that starts at the current node and extends down to any of the children.
Global Max Path Sum: The maximum sum of any path in the tree. This is what we need to return at the end.

2. Recursive DFS Logic:

At each node, recursively calculate the maximum sum from the left and right children.
The local max path sum at the current node is the node's value plus the maximum of the two child sums. If a child sum is negative,
we don't include it (since we want to maximize the sum).
Update the global max path sum. It is the maximum of the current global max and the sum of the current node's value and both child 
sums (if they are positive).

3. Handling the Edge Cases:

If a node is None, return 0 (base case for the recursion).
The initial global maximum can be set to a very small number or the root's value.

4. Return the Result:

Start the recursion from the root and return the global max path sum.


In this code:
-------------------
We use a depth-first search (DFS) approach to traverse the tree. For each node, we calculate two things: the maximum path sum that 
includes the node and extends downward, and the overall maximum path sum encountered so far in the tree. The dfs function is designed
to return the maximum sum of a path that starts at a given node and goes down, which is then used to compute the max path sum for its 
parent nodes. The global maximum path sum is updated at each node if the sum of the node's value and its children's maximum path sums 
is greater than the current global maximum.

'''
