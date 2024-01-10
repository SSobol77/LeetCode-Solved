# 94. Binary Tree Inorder Traversal

# Topic : Stack, Tree, Depth-First Search, Binary Tree

'''
# Task:
---------
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


# Testcase:
------------
[1,null,2,3]
[]
[1]


# Code:
------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       
'''
# Solution:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize the result list to store the traversal and a stack to manage nodes
        result = []
        stack = []

        # Start with the root node
        current = root

        # Continue traversing as long as there are nodes to process
        while current or stack:
            # If the current node is not None, push it to the stack and move to its left child
            if current:
                stack.append(current)
                current = current.left
            else:
                # If current is None, it means we've reached a leaf node,
                # so backtrack: pop from stack and process the node
                current = stack.pop()
                result.append(current.val)  # Add the node's value to the result list

                # Move to the right child of the processed node
                current = current.right

        # Return the final in-order traversal result
        return result

# Description:
'''
This code is an efficient implementation of the in-order traversal of a binary tree. It uses an iterative 
approach instead of recursion, which is beneficial for large trees to avoid stack overflow issues. The use 
of a stack data structure here allows for an elegant solution that mimics the system call stack of a recursive 
approach. The algorithm ensures that each node is visited in the order of left child, node itself, and then 
right child, which is the essence of in-order traversal.

'''
