# 230. Kth Smallest Element in a BST

# Topic: Tree, Depth-First Search, Binary Search Tree, Binary Tree.

'''
# Tsak:
-------
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 10^4
0 <= Node.val <= 10^4
 
Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to 
find the kth smallest frequently, how would you optimize?

Hint 1
Try to utilize the property of a BST.
Hint 2
Try in-order traversal. (Credits to @chan13)
Hint 3
What if you could modify the BST node's structure?
Hint 4
The optimal runtime complexity is O(height of BST).


# Testcase:
-----------
[3,1,4,null,2]
1
[5,3,6,2,4,null,null,1]
3


# Code:
-------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
'''

# Solution:
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrderTraversal(node):
            if not node:
                return
            # Recursively traverse the left subtree
            inOrderTraversal(node.left)
            # Decrease k when visiting a node
            nonlocal k
            k -= 1
            # If k reaches zero, it means we have found the kth smallest value
            if k == 0:
                nonlocal result
                result = node.val
                return
            # Recursively traverse the right subtree
            inOrderTraversal(node.right)
        
        result = None  # Variable to store the result
        inOrderTraversal(root)  # Call the traversal function with the root of the tree
        return result

# Test case 1
root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.left.right = TreeNode(2)
k1 = 1
output1 = Solution().kthSmallest(root1, k1)  # Should return 1

# Test case 2
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(6)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.left.left.left = TreeNode(1)
k2 = 3
output2 = Solution().kthSmallest(root2, k2)  # Should return 3

# Print test results
print(output1)  # 1
print(output2)  # 3


# Description:
'''
- This code defines a class Solution that provides a method kthSmallest for finding the kth smallest 
  value (1-indexed) in a binary search tree (BST).
- The algorithm employs an in-order traversal of the BST, which guarantees that nodes are visited in 
  ascending order of their values.
- As the traversal progresses, the code decreases the value of k for each visited node.
- When k reaches zero, it means that the kth smallest value has been found and is stored in the result
  variable.
- Finally, the method returns the value stored in result.

'''
