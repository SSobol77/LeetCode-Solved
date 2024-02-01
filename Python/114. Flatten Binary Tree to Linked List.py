# 114. Flatten Binary Tree to Linked List

# Topic: Linked List, Stack, Tree, Depth-First Search, Binary Tree.

'''
Task: 
-----
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to the next node in 
the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]
 
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 
Follow up: Can you flatten the tree in-place (with O(1) extra space)?

# Testcase:
[1,2,5,3,4,null,6]
[]
[0]


# Code:
--------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

'''
# Solution:  ------------------------------------------------------------------

class TreeNode:
    """Definition for a binary tree node"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """Do not return anything, modify root in-place instead."""
        
        current = root
        while current:
            if current.left:
                # Find the rightmost node in the left subtree
                rightmost = current.left
                while rightmost.right:
                    rightmost = rightmost.right

                # Re-wire the connections
                rightmost.right = current.right
                current.right = current.left
                current.left = None

            # Move to the next node
            current = current.right

# Description:
"""
The solution provided for flattening a binary tree into a linked list in place follows a different approach than the recursive solution previously discussed. This solution iteratively modifies the tree by re-wiring the left subtree's rightmost node to the right subtree, ensuring the tree is flattened in a preorder traversal manner. Here's a step-by-step description of how this algorithm works:

### Algorithm Description:

1. **Initialization**: Start with the `current` node set to the root of the tree. The algorithm iterates through the tree starting from the root, moving towards the rightmost node.

2. **Iterating through the Tree**: The algorithm uses a `while` loop to traverse the tree. For each `current` node being processed, it checks if the `current` node has a left child.

3. **Processing the Left Subtree**:
    - If the `current` node has a left child, the algorithm finds the rightmost node in the left subtree. This is done by iterating through the left subtree using a `while` loop until the rightmost node is found.
    - Once the rightmost node in the left subtree is identified, its right pointer is set to the `current` node's right child. This effectively appends the entire right subtree to the end of the left subtree.

4. **Re-wiring Connections**:
    - The `current` node's right pointer is then updated to point to its left child, effectively moving the left subtree to the right side. This maintains the preorder sequence (root, left, right) since the left subtree is now positioned in the place of the right subtree.
    - The `current` node's left pointer is set to `None`, removing the original left subtree.

5. **Moving to the Next Node**: After re-wiring the connections for the `current` node, the algorithm moves to the next node by setting `current` to `current.right`. This step progresses the flattening process to the next node in the preorder sequence.

6. **Continuation Condition**: The loop continues until there are no more nodes to process, i.e., until `current` becomes `None`. At this point, the entire tree has been flattened into a linked list.

7. **In-Place Modification**: Throughout the process, the tree is modified in place. No new nodes are created, and the existing nodes are merely re-wired to achieve the flattened structure.

8. **Termination**: When the `while` loop exits, the tree has been successfully flattened into a linked list following the preorder traversal order, with all nodes' left pointers set to `None` and right pointers leading to the subsequent nodes in the list.

This iterative approach efficiently flattens the binary tree by carefully re-wiring the nodes' pointers, ensuring that the space complexity is kept to O(1) as no additional data structures are used and all modifications are performed in place.
"""
            

