# 105. Construct Binary Tree from Preorder and Inorder Traversal.

# Topic: Array, Hash Table, Divide and Conquer, Tree, Binary Tree.


"""
## Task:
---------
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a 
binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.


## Testcase:
-------------
[3,9,20,15,7]
[9,3,15,20,7]
[-1]
[-1]


## Code:
----------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

"""
# Solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # Creating a hashmap to store the value-index pairs from the inorder list for fast access
        in_map = {val: idx for idx, val in enumerate(inorder)}

        def arrayToTree(left, right):
            # If there are no elements to construct the subtree, return None
            if left > right:
                return None

            # The first element in preorder is always the root of the (sub)tree
            root_val = preorder.pop(0)
            root = TreeNode(root_val)

            # The index of the root element in inorder list divides the list into left and right subtrees
            # Recursively build the left subtree using the elements before the root in inorder
            root.left = arrayToTree(left, in_map[root_val] - 1)
            # Recursively build the right subtree using the elements after the root in inorder
            root.right = arrayToTree(in_map[root_val] + 1, right)

            return root

        # Start the recursion from the full range of the inorder list
        return arrayToTree(0, len(inorder) - 1)

# Example usage
solution = Solution()
print(solution.buildTree([3,9,20,15,7], [9,3,15,20,7]))  # Example 1
print(solution.buildTree([-1], [-1]))  # Example 2



# Description
'''
To solve the problem of constructing a binary tree from its preorder and inorder traversals, we can follow these steps:

1. **Understand the Traversal Orders:**
   - **Preorder Traversal:** Node -> Left -> Right. This means the first element in the preorder list is always the root 
       of the tree.
   - **Inorder Traversal:** Left -> Node -> Right. This order helps us identify the left and right subtrees of any node.

2. **Algorithm:**
   - The first element in the preorder list is the root of the tree.
   - Find this root element in the inorder list. The elements to the left of the root in the inorder list form the left 
     subtree, and the elements to the right form the right subtree.
   - Recursively apply the above steps to construct the left and right subtrees.

3. **Implementation:**
   - We use a helper function that takes the current bounds of the preorder and inorder lists to construct the tree.
   - We also use a hashmap to store the indices of elements in the inorder list for quick look-up, which optimizes 
     the search operation.

4. **Base Case:**
   - If the current range of the preorder or inorder list is empty, we return `None`, indicating no subtree to construct.


This solution efficiently constructs the binary tree by using divide and conquer technique, and its time complexity is O(N) 
where N is the number of nodes in the tree, as it processes each node exactly once. The hashmap used for quick look-ups of 
indices in the inorder list also ensures that the solution is efficient.

'''
