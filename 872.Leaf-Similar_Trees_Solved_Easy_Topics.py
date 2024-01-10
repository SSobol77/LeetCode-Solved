### 872. Leaf-Similar Trees.

### Topics: Tree, Depth-First Search, Binary Tree.

"""
## Task:
---------
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

#Example 1:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

#Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

#Constraints:
The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].

## Testcase:872.Leaf-Similar_Trees_Solved_Easy_Topics
-------------
[3,5,1,6,2,9,8,null,null,7,4]
[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
[1,2,3]
[1,3,2]


## Code:
----------
/# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
"""
# Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leaves):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
            dfs(node.left, leaves)
            dfs(node.right, leaves)

        leaves1, leaves2 = [], []

        # Traverse the first tree and collect leaf values
        dfs(root1, leaves1)

        # Traverse the second tree and collect leaf values
        dfs(root2, leaves2)

        # Compare the leaf value sequences
        return leaves1 == leaves2


# Description
'''
To solve this problem in Python, you can use a similar approach as the C++ solution mentioned earlier.
You will traverse both binary trees and collect the leaf values in the same order for both trees. 
Then, compare the leaf value sequences to check if they are the same. You can achieve this using a 
depth-first traversal approach.

This code defines a leafSimilar function that takes two tree nodes as input and returns true if their 
leaf value sequences are the same. It uses a depth-first search (DFS) approach to collect leaf values 
from both trees and then compares the sequences.

'''
