# 872. Leaf-Similar Trees.

# Topic: Tree, Depth-First Search, Binary Tree.

"""
## Task:
---------
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

Constraints:
The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].


## Testcase:
-------------
[3,5,1,6,2,9,8,null,null,7,4]
[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
[1,2,3]
[1,3,2]


## Code:
----------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        

"""
# Solution
class Solution:
    # Define a method 'leafSimilar' that takes two binary tree nodes 'root1' and 'root2' as input
    # and returns a boolean value indicating whether they have the same sequence of leaf values.
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Define a nested generator function 'dfs' that performs a depth-first traversal of a binary tree
        def dfs(node):
            if node:
                # If the current node is a leaf (has no left or right children),
                # yield its value as a leaf value.
                if not node.left and not node.right:
                    yield node.val
                # Recursively traverse the left and right subtrees.
                yield from dfs(node.left)
                yield from dfs(node.right)

        # Create two generators 'gen1' and 'gen2' using the 'dfs' function for the two input trees.
        gen1, gen2 = dfs(root1), dfs(root2)

        # Iterate through the leaf values from 'gen1' and compare them to 'gen2'.
        for val1 in gen1:
            val2 = next(gen2, None)
            # If the values are not equal or 'gen2' is exhausted, return False.
            if val1 != val2 or val2 is None:
                return False

        # Check if there are any remaining leaves in the second tree ('gen2').
        # If there are remaining leaves in 'gen2', return False; otherwise, return True.
        try:
            next(gen2)
            return False
        except StopIteration:
            return True


# Description
'''
You're right, the previous solution does not handle the case when one tree has more leaves than the other correctly. 
The `zip` function stops when the shortest input iterable is exhausted, which means if one tree has more leaves than 
the other, those extra leaves are not considered in the comparison.

To fix this, we need to ensure that both trees have the same number of leaves and their corresponding leaves are equal. 

In summary, this code uses a depth-first traversal approach to extract leaf values from both binary trees and compares 
their sequences. If the sequences are the same and there are no remaining leaves in the second tree, the method returns 
True, indicating that the trees have similar leaf sequences. Otherwise, it returns False.

In this solution:
--------------------
- We iterate through the leaf values of the first tree (`gen1`).
- For each leaf value in the first tree, we get the corresponding leaf value in the second tree (`gen2`). If the values 
  are not equal or if `gen2` is exhausted (`val2 is None`), we return `False`.
- After iterating through all leaves in the first tree, we check if there are any remaining leaves in the second tree by
  calling `next(gen2)`. If `next(gen2)` raises a `StopIteration` exception, it means both trees had the same number of 
  leaves and all corresponding leaves were equal, so we return `True`. If it doesn't raise the exception, it means the 
  second tree has more leaves, so we return `False`. 

This solution accurately compares the leaf sequences of the two trees, taking into account the number of leaves in each tree.

'''
