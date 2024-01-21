# 98. Validate Binary Search Tree.

# Topic: Tree, Depth-First Search, Binary Search Tree, Binary Tree.

'''
# Task:
-------
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 
Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1



# Testcase:
-----------
[2,1,3]
[5,1,4,null,null,3,6]


# Code:
-------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

'''
# Solution:
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(node, lower=float('-inf'), upper=float('inf')):
            # Base case: If the node is None, it's a valid BST.
            if not node:
                return True

            # Check if the current node's value is within the valid range [lower, upper].
            if node.val <= lower or node.val >= upper:
                return False

            # Recursively check the left and right subtrees with updated boundaries.
            return isBST(node.left, lower, node.val) and isBST(node.right, node.val, upper)

        # Start the recursion with the root node and default boundaries.
        return isBST(root)


# Description:
'''
In this code, we check that the current node is in the acceptable range (lower < node.val < upper) 
and recursively check its left and right subtrees with updated constraints. If the condition is met
for all nodes, the tree is considered a valid binary search tree.

This algorithm works on average in linear time relative to the number of nodes in the tree and is 
one of the fastest ways to verify the validity of BST.

'''
