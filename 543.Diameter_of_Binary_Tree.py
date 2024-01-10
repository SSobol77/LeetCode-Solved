"""
# 543. Diameter of Binary Tree.

# Topic: Tree, Depth-First Search, Binary Tree.

# Task:
---------
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-100 <= Node.val <= 100


# Testcase:
------------
[1,2,3,4,5]
[1,2]


# Code:
----------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
  

"""
# Solution:
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum diameter
        self.max_diameter = 0

        def height(node):
            # Base case: return -1 for null nodes
            if not node:
                return -1

            # Recursively find the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            # Update the maximum diameter
            # Diameter at this node = left height + right height + 2 edges
            self.max_diameter = max(self.max_diameter, 2 + left_height + right_height)

            # Return the height of the current node
            # Height is max of left/right height plus 1 for the current node's edge
            return 1 + max(left_height, right_height)

        # Start the recursive process from the root
        height(root)

        # Return the maximum diameter found during the traversal
        return self.max_diameter


# Description:
'''
To solve the problem of finding the diameter of a binary tree, we need to understand that the diameter of a binary tree is the length of 
the longest path between any two nodes in the tree. This path may or may not pass through the root. The length of a path is represented 
by the number of edges between the nodes.

The approach to find the diameter involves a depth-first search (DFS) on the tree. We can define a helper function that computes the height 
of each node, and as it does so, it calculates the longest path through each node (which is the sum of the heights of its left and right subtrees).

Here is the step-by-step approach:
-------------------------------------
1. Define a Recursive Function: Create a function height that computes the height of a node and updates the diameter. The height of a node is 
   the number of edges in the longest path from it down to a leaf node.

2. Calculate Diameter at Each Node: As we calculate the height of each node, we can also calculate the potential diameter at that node, which 
   is the sum of the height of its left subtree and the height of its right subtree.

3. Keep Track of Maximum Diameter: Maintain a variable to keep track of the maximum diameter seen so far.

4. Traverse the Entire Tree: Perform a DFS traversal of the tree, calculating height and updating the diameter at each node.

5. Return the Maximum Diameter: After the traversal, return the maximum diameter obtained.

In this code:
---------------
*    The height function is defined inside the diameterOfBinaryTree method. It calculates the height of a node while also updating 
     the maximum diameter found so far.
*    The height function returns -1 for null nodes because the height of a non-existent subtree is one less than a leaf node, which
     has a height of 0.
*    The diameter at each node is calculated as the sum of the heights of its left and right subtrees, plus 2 (for the edges 
     connecting the node to its children).
*    The overall diameter of the tree is the maximum diameter found during the traversal of the tree.

'''
