# 103. Binary Tree Zigzag Level Order Traversal.

# Topic: Tree, Breadth-First Search, Binary Tree.

'''
Task:
-----
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left 
to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Check if the root is None, return an empty list if true.
        if not root:
            return []

        # Initialize a deque for BFS and a result list for storing the zigzag order traversal.
        result = []
        queue = deque([root])

        # Flag to keep track of the traversal direction at each level.
        left_to_right = True  

        # Continue the loop until the queue is empty (all nodes are processed).
        while queue:
            # List to store the values of nodes at the current level.
            level = []

            # Determine the number of nodes at the current level.
            level_length = len(queue)

            # Process each node at the current level.
            for _ in range(level_length):
                # Pop the front node from the queue.
                node = queue.popleft()

                # Add the node's value to the level list.
                level.append(node.val)

                # Add the node's children to the queue for the next level.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse the level list if the current traversal is right-to-left.
            if not left_to_right:
                level.reverse()

            # Add the level list to the result.
            result.append(level)

            # Toggle the traversal direction for the next level.
            left_to_right = not left_to_right

        # Return the final zigzag order traversal.
        return result


# ---------------------------------------------------- 
# Helper function to create a binary tree from a list.
def create_tree(lst):
    if not lst:
        return None
    nodes = [None if val is None else TreeNode(val) for val in lst]
    kid_nodes = nodes[::-1]
    root = kid_nodes.pop()
    for node in nodes:
        if node:
            if kid_nodes: node.left = kid_nodes.pop()
            if kid_nodes: node.right = kid_nodes.pop()
    return root

# Test cases
test1 = create_tree([3, 9, 20, None, None, 15, 7])
test2 = create_tree([1])
test3 = create_tree([])

sol = Solution()
result1 = sol.zigzagLevelOrder(test1)
result2 = sol.zigzagLevelOrder(test2)
result3 = sol.zigzagLevelOrder(test3)

result1, result2, result3



# *** Description:
'''
To solve the problem of zigzag level order traversal of a binary tree, you can modify the standard 
Breadth-First Search (BFS) algorithm. In a zigzag traversal, nodes at each level are visited in an 
alternating left-to-right and right-to-left order.

Here's the modified BFS algorithm to achieve zigzag traversal:

1. Check for an Empty Tree: If the root is None, return an empty list as the tree is empty.

2. Queue Initialization: Use a deque to keep track of nodes at each level. Initialize the deque with the root node.

3. Traversal with Zigzag: Use a flag to keep track of the order of traversal for each level.

    - If the flag is set, traverse from left to right; otherwise, traverse from right to left.
    - In each iteration, extract all nodes of the current level, add their children to the queue for the next level,
      and append their values to the level's list.
    - After processing a level, reverse the list if the flag indicates a right-to-left traversal.
    - Toggle the flag at the end of each level.

4. Result Accumulation: Maintain a list of lists, where each inner list contains the values of nodes at a particular 
   level, arranged according to the zigzag order.

This code will perform a zigzag level order traversal of the binary tree and return a list of lists 
containing the values of nodes at each level, arranged according to the zigzag pattern. The time 
complexity of this solution is O(n), where n is the number of nodes in the tree, as each node is 
processed exactly once.

'''