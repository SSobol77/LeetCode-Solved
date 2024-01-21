# 102. Binary Tree Level Order Traversal

# Topic: Tree, Breadth-First Search, Binary Tree

'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, 
level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000


# Testcase:
-----------
[3,9,20,null,null,15,7]
[1]
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
'''
# Solution:

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the root is None, return an empty list, as there are no nodes to traverse.
        if not root:
            return []

        # Initialize a deque to use it as a queue for the BFS.
        # Add the root node to this deque.
        result = []
        queue = deque([root])

        # Continue the loop until the queue is empty, indicating all levels have been processed.
        while queue:
            # This list will hold the values of nodes at the current level.
            level = []

            # Determine the number of nodes at the current level, which is the current size of the queue.
            level_length = len(queue)

            # Iterate through nodes at the current level.
            for _ in range(level_length):
                # Pop the front node from the queue.
                node = queue.popleft()

                # Add the node's value to the level list.
                level.append(node.val)

                # If the node has a left child, add it to the queue.
                if node.left:
                    queue.append(node.left)

                # If the node has a right child, add it to the queue.
                if node.right:
                    queue.append(node.right)

            # After processing all nodes at the current level, add the level list to the result list.
            result.append(level)

        # Return the final list of levels, where each sublist contains the values of nodes at that level.
        return result


# *** Description:
'''
For this problem, the most efficient approach is to use Breadth-First Search (BFS). BFS is well-suited for 
level order traversal of a binary tree. The algorithm uses a queue to keep track of nodes at each level of 
the tree and processes them from left to right.

Here's how you can implement this in Python:

1. Check for an Empty Tree: Initially, check if the root is None. If it is, return an empty list since there are 
no nodes to traverse.

2. Queue Initialization: Use a deque to store the nodes. Initially, add the root node to the deque.

3. Traversal: While the deque is not empty, process the nodes level by level:

    - Determine the number of nodes at the current level (length of the deque).
    - Iterate over these nodes, remove them from the deque, and add their values to a temporary list.
    - For each node, add its left and right children to the deque if they exist.

4. Result Accumulation: After processing each level, add the list of node values for that level to the final result.

This code will perform a level order traversal of the binary tree and return a list of lists containing the values 
of nodes at each level. The time complexity of this solution is O(n), where n is the number of nodes in the tree, 
as each node is processed exactly once.

'''
