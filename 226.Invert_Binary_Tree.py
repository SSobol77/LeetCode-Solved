# 226. Invert Binary Tree

# Topic: Tree, Depth-First Search, Breadth-First Search, Binary Tree.


"""
## Task:
---------
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


## Testcase:
-------------
[4,2,7,1,3,6,9]
[2,1,3]
[]


## Code:
----------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

"""
# Solution

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Check if the root is None (empty tree)
        if not root:
            return None
        
        # Create a queue for level-order traversal
        queue = deque([root])
        
        # Perform a level-order traversal of the tree
        while queue:
            # Get the next node from the queue
            node = queue.popleft()
            
            # Swap the left and right subtrees of the current node
            node.left, node.right = node.right, node.left
            
            # If the left and right children exist, add them to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Return the root of the inverted tree
        return root


# Description
'''
This solution provides an efficient way to invert a binary tree, transforming it into its mirror image. 
The problem is addressed by utilizing a Breadth-First Search (BFS) approach, which traverses the tree 
level by level, swapping the left and right subtrees of each encountered node.

The key components of this solution are as follows:

1. **Initialization**: The algorithm begins by checking if the input tree is empty or if the root node is None. 
     In either case, it returns None, as there is no tree to invert.

2. **Queue for BFS**: A deque (double-ended queue) named `queue` is created to facilitate the level-order traversal 
     of the binary tree. The root node is initially enqueued.

3. **Level-Order Traversal**: The main loop iterates while there are nodes in the queue. During each iteration, it 
     dequeues the next node and proceeds to swap its left and right subtrees by simply exchanging their references. 
     This operation inverts the node's immediate children effectively.

4. **Enqueuing Children**: After swapping, if the left and right children of the current node exist, they are enqueued 
     into the queue. This ensures that their subtrees will also be processed, ensuring the inversion of the entire 
     binary tree.

5. **Completion**: Once all nodes have been processed, the algorithm has effectively inverted the binary tree, converting 
     it into its mirror image. The root of the modified tree is returned.

By employing this iterative BFS approach, the solution avoids the overhead associated with recursive function calls and is 
capable of handling large binary trees efficiently. It guarantees that every node's left and right subtrees are correctly 
swapped, resulting in the desired inverted binary tree as the final output.

'''
