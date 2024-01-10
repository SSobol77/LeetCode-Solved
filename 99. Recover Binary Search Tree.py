# 99. Recover Binary Search Tree.

# Topic: Tree, Depth-First Search, Binary Search Tree, Binary Tree.


'''
# Task:
------------
You are given the root of a binary search tree (BST), where the values of exactly two nodes of 
the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

Constraints:
The number of nodes in the tree is in the range [2, 1000].
-2^31 <= Node.val <= 2^31 - 1
 
Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?


# Testcase:
--------------
[1,3,null,null,2]
[3,1,4,null,null,2]

# Code:
--------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

'''
# Solution:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # Morris Traversal function to find the two swapped nodes
        def morrisTraversal(root):
            x = y = predecessor = pred = None
            
            while root:
                if root.left:
                    # Finding the rightmost node in the left subtree (predecessor)
                    predecessor = root.left
                    while predecessor.right and predecessor.right != root:
                        predecessor = predecessor.right

                    # Making the current node as the right child of its predecessor
                    if not predecessor.right:
                        predecessor.right = root
                        root = root.left
                    else:
                        # Detecting the swapped nodes during the in-order traversal
                        if pred and root.val < pred.val:
                            y = root
                            if not x:
                                x = pred
                        pred = root

                        # Restoring the tree structure by undoing the changes made earlier
                        predecessor.right = None
                        root = root.right
                else:
                    # Similar check for swapped nodes in the case where there's no left child
                    if pred and root.val < pred.val:
                        y = root
                        if not x:
                            x = pred
                    pred = root
                    root = root.right
            return x, y

        # Function to swap values of two nodes
        def swap(x, y):
            x.val, y.val = y.val, x.val
        
        # Performing Morris Traversal to find the nodes to be swapped
        x, y = morrisTraversal(root)
        # Swapping values of the identified nodes
        if x and y:
            swap(x, y)

# Example Test Cases
sol = Solution()
root1 = TreeNode(1, TreeNode(3, None, TreeNode(2)))
sol.recoverTree(root1)
# ... traverse root1 to verify the tree is recovered ...

root2 = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
sol.recoverTree(root2)
# ... traverse root2 to verify the tree is recovered ...


# Description:

'''
Comments Explained:
-Morris Traversal Function: This function traverses the tree without using extra space. It temporarily modifies 
the tree by pointing the rightmost node of the left subtree (predecessor) to the current node. This enables the
function to return to each node after traversing its left subtree.
-Detecting Swapped Nodes: During the traversal, the function looks for two pairs of nodes where the value of the 
first node is greater than the second. These are the swapped nodes, identified as x and y.
-Restoring Tree Structure: The tree's original structure is restored by setting the right pointer of the predecessor
nodes back to None.
-Swapping Node Values: Once the swapped nodes are identified, their values are swapped back to correct the BST.
- O(1) Space Complexity: This method does not use additional space for stack or recursion, thus achieving constant 
 space complexity.

This implementation is efficient and meets the problem's requirement for constant space complexity.
The Morris Traversal is a clever way to conduct an in-order traversal without additional space, making it ideal 
for this scenario.

'''