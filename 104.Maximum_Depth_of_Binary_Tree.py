# 104. Maximum Depth of Binary Tree.

# Topic: Tree, Depth-First Search, Breadth-First Search, Binary Tree.

"""
## Task:
---------
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root 
node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100



## Testcase:
-------------
[3,9,20,null,null,15,7]
[1,null,2]


## Code:
----------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

"""
# Solution ---------------------------------------------------------------------------

## Depth-First Search (DFS) Approach:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the current node is None, return 0 (base case for recursion)
        if not root:
            return 0

        # Recursively find the depth of the left subtree
        left_depth = self.maxDepth(root.left)
        # Recursively find the depth of the right subtree
        right_depth = self.maxDepth(root.right)

        # The depth at the current node is 1 (for the current node) 
        # plus the maximum of the depths of the left and right subtrees
        return 1 + max(left_depth, right_depth)


## Breadth-First Search (BFS) Approach:
    
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        # Return 0 if the tree is empty
        if not root:
            return 0

        # Initialize depth counter
        depth = 0
        # Initialize a queue for level order traversal, starting with the root
        queue = [root]

        # Continue until the queue is empty
        while queue:
            # Increase the depth since we're moving to the next level
            depth += 1

            # Process all nodes at the current level
            for _ in range(len(queue)):
                node = queue.pop(0)

                # Add the left child to the queue if it exists
                if node.left:
                    queue.append(node.left)
                # Add the right child to the queue if it exists
                if node.right:
                    queue.append(node.right)

        # Return the final depth value
        return depth




# Description
'''
To solve the problem of finding the maximum depth of a binary tree, we can use either a depth-first search (DFS) 
or a breadth-first search (BFS) approach. The maximum depth is defined as the number of nodes along the longest 
path from the root node down to the farthest leaf node.

### Depth-First Search (DFS) Approach:
---------------------------------------
1. **Recursive Strategy**: Use recursion to explore each path from the root to the leaves.
2. **Base Case**: If the current node is `None`, return 0. This case handles leaf nodes.
3. **Depth Calculation**: For each node, calculate the depth of the left and right subtrees, then return the 
     maximum of these depths plus 1 (to include the current node).
4. **Starting from Root**: The recursion starts from the root node.

### Breadth-First Search (BFS) Approach:
----------------------------------------
1. **Level-Order Traversal**: Use a queue to perform a level-order traversal of the tree.
2. **Tracking Depth**: Keep track of the depth as we traverse each level of the tree.
3. **Increment Depth per Level**: For each level, increment the depth count.
4. **Continue Until Queue is Empty**: The traversal continues until the queue is empty, which indicates that all 
     levels have been processed.

### In the code:
---------------
- `maxDepth` is the DFS implementation. It recursively calculates the maximum depth by comparing the depth of the 
   left and right subtrees at each node.
- `maxDepthBFS` is the BFS implementation. It uses a queue to traverse the tree level by level, incrementing the 
   depth count with each new level processed.

'''
