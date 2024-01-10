# 106. Construct Binary Tree from Inorder and Postorder Traversal
'''
# Task:

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and 
postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.

Testcase:
-------------
[9,3,15,20,7]
[9,15,7,20,3]
[-1]
[-1]

Code:
-----

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
 
'''
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        # Create a hash map for quick index lookups in the inorder list
        hash_map = {n: i for i, n in enumerate(inorder)}
        self.i = len(postorder) - 1

        def dfs(left, right):
            # Base case: no subtree to build
            if left > right:
                return None

            # Local variable for the current index in postorder
            index = self.i
            self.i -= 1

            # Create a new node with the current value
            node = TreeNode(postorder[index])
            # Build the right and left subtrees recursively
            node.right = dfs(hash_map[node.val] + 1, right)
            node.left = dfs(left, hash_map[node.val] - 1)

            return node

        return dfs(0, len(inorder) - 1)
