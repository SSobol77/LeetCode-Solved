# 235. Lowest Common Ancestor of a Binary Search Tree.

# Topic: Tree, Depth-First Search, Binary Search Tree, Binary Tree.


"""
### Task:
---
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the BST.


### Testcase:
---
[6,2,8,0,4,7,9,null,null,3,5]
2
8
[6,2,8,0,4,7,9,null,null,3,5]
2
4
[2,1]
2
1


### Code:
---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
    
"""
### Solution: --------------------------------------

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x  # Node's value
        self.left = None  # Left child
        self.right = None  # Right child

class Solution:
    # Function to find the lowest common ancestor of two nodes in a BST
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Start from the root node of the BST
        current = root
        
        # Loop until we find the LCA
        while current:
            # If both p and q are greater than the current node's value,
            # it means both are located in the right subtree.
            if p.val > current.val and q.val > current.val:
                # Move to the right child of the current node.
                current = current.right
            # If both p and q are less than the current node's value,
            # it means both are located in the left subtree.
            elif p.val < current.val and q.val < current.val:
                # Move to the left child of the current node.
                current = current.left
            else:
                # If we reach here, it means one of the following is true:
                # 1. One of p or q equals the current node, which means the current node is the LCA.
                # 2. p is on one side of the current node and q is on the other, making the current node the LCA.
                # So, we return the current node as the LCA.
                return current


### Description: ===================================
'''
To find the lowest common ancestor (LCA) of two nodes in a binary search tree (BST), you can use the following approach, which leverages 
the BST's properties:

1. **Start at the root node**: Begin your search from the root of the BST.

2. **Compare the values**: For the current node being considered, compare the values of the given nodes `p` and `q` with the current node's value.

3. **Decision making**:
   - If both `p` and `q` are greater than the current node's value, move to the right child of the current node and continue the search.
   - If both `p` and `q` are less than the current node's value, move to the left child of the current node and continue the search.
   - If one of `p` or `q` is less than the current node's value and the other is greater, or if one of them matches the current node's value, the current node is the LCA.

This approach works because, in a BST, for any node `n`, all nodes in the left subtree of `n` are less than `n`, and all nodes in the 
right subtree are greater than `n`. Therefore, the first node where `p` and `q` "diverge" in the tree is their lowest common ancestor.

This code defines a `TreeNode` class for tree nodes and a `Solution` class with the `lowestCommonAncestor` method to find the LCA. 
The method iterates through the tree, moving left or right depending on the values of `p` and `q` relative to the current node, and 
returns the LCA when found .

'''
