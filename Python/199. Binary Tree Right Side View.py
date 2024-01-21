# 199. Binary Tree Right Side View

'''
Task:
-----
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes 
you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

# Testcase:
-----------
[1,2,3,null,5,null,4]
[1,null,3]
[]


# Code:
-------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
   
'''
# Solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(n, d):
            if n:
                if d == len(res):
                    res.append(n.val)
                dfs(n.right, d+1)
                dfs(n.left, d+1)
        dfs(root, 0)
        return res

