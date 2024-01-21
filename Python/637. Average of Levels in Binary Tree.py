# 637. Average of Levels in Binary Tree

# Topic: Tree, Depth-First Search, Breadth-First Search, Binary Tree.

'''
Task:
-----
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers 
within 10-5 of the actual answer will be accepted.
 
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1

# Testcase:
-----------
[3,9,20,null,null,15,7]
[3,9,20,15,7]

# Code:
-------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
   
'''
# Solution:
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Check if the root is None, return an empty list if true.
        if root is None:
            return []
        
        # Initialize a deque (double-ended queue) with the root node.
        # Deque is used for efficient popping from the front of the queue.
        queue = deque([root])

        # This list will store the average of each level.
        result = []

        # Continue looping until the queue is empty.
        while queue:
            # Temporary list to store the values of nodes at the current level.
            tmp = []

            # Iterate over all nodes at the current level.
            for i in range(len(queue)):
                # Pop the front node from the queue.
                node = queue.popleft()

                # If the node is not None, add its value to the temporary list.
                if node:
                    tmp.append(node.val)

                    # Add the left child to the queue if it exists.
                    if node.left:
                        queue.append(node.left)

                    # Add the right child to the queue if it exists.
                    if node.right:
                        queue.append(node.right)

            # Calculate the average of the current level and add it to the result list.
            # sum(tmp) calculates the sum of values at the current level,
            # len(tmp) gives the number of nodes at this level.
            result.append(sum(tmp) / len(tmp))
        
        # Return the list of averages for each level.
        return result



# *** Description:
'''
This Python code defines a Solution class with a method averageOfLevels to calculate the average values of nodes
at each level of a binary tree. The method takes a binary tree's root node as its input and returns a list of 
floating-point numbers representing the average values at each level of the tree.

Key components of the code include:

1. Checking for an Empty Tree: The method first checks if the input root is None. If the tree is empty, it returns 
   an empty list.

2. Queue Initialization: A deque (double-ended queue) from the collections module is initialized with the root node. 
   The deque is used for efficiently performing breadth-first traversal of the tree.

3. Breadth-First Traversal: The code employs a while loop to traverse the tree level by level. At each level, it uses 
   a for loop to iterate through all the nodes at that level, which are stored in the deque.

4. Node Processing: For each node in the deque, the code:

    - Pops the node from the front of the deque.
    - Adds the node's value to a temporary list if the node is not None.
    - Appends the node's left and right children to the deque if they exist.

5. Average Calculation: After processing all nodes at a particular level, the code calculates the average value of that level.
   This is done by dividing the sum of the node values at that level by the count of the nodes.

6. Result Accumulation: The average value for each level is appended to the result list, which is eventually returned after 
  all levels of the tree have been processed.

The method averageOfLevels thus provides a way to compute the average value of nodes for each level in a binary tree, 
utilizing a breadth-first search algorithm.

'''