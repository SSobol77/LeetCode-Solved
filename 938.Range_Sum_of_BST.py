# 938. Range Sum of BST

# Topic: Tree, Depth-First Search, Binary Search Tree, Binary Tree.

"""
## Task:
---------
Given the root node of a binary search tree and two integers low and high, return the sum of values 
of all nodes with a value in the inclusive range [low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

Constraints:
The number of nodes in the tree is in the range [1, 2 * 10^4].
1 <= Node.val <= 10^5
1 <= low <= high <= 10^5
All Node.val are unique.


## Testcase:
-------------
[10,5,15,3,7,null,18]
7
15
[10,5,15,3,7,13,18,1,null,6]
6
10



## Code:
-------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
"""
# Solution: ---------------------------------------------------

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Define a depth-first search function
        def dfs(node):
            # Base case: If the node is null, return 0
            if not node:
                return 0

            # If the current node's value is less than the low boundary,
            # then we only need to explore the right subtree
            if node.val < low:
                return dfs(node.right)

            # If the current node's value is greater than the high boundary,
            # then we only need to explore the left subtree
            elif node.val > high:
                return dfs(node.left)

            # If the current node's value is within the [low, high] range,
            # sum the value of the current node and recursively check both subtrees
            else:
                return node.val + dfs(node.left) + dfs(node.right)

        # Start the DFS from the root node
        return dfs(root)


# Description:
'''
In this code:
------------
    * TreeNode is a class representing a node in a binary search tree.

    * The Solution class has a method rangeSumBST which calculates the sum of values of all nodes within 
    the given range [low, high].

    * Inside rangeSumBST, we define a helper function dfs for depth-first search.

    * dfs checks if a node is within the specified range and recursively explores the subtrees as needed, 
    optimizing the traversal by skipping irrelevant branches.
    
    * The result of dfs(root) gives the total sum of the values within the specified range in the BST.


This solution involves a depth-first search (DFS) algorithm to efficiently calculate the sum of values of all nodes 
within a specified range in a binary search tree (BST). The algorithm is implemented in Python as a method `rangeSumBST` 
within the `Solution` class.

Key aspects of the solution include:
--------------------------------------
1. **TreeNode Class**: Represents each node in the binary search tree. Each `TreeNode` has a value (`val`) and pointers 
   to its left and right children.

2. **Depth-First Search (DFS)**: A recursive approach to traverse the tree. The DFS function (`dfs`) is defined within 
   the `rangeSumBST` method. It navigates through the tree, summing up the values of nodes that fall within the given 
   range (`low`, `high`). 

3. **Optimization by BST Properties**: The binary search tree property (left child < node < right child) is utilized 
     to optimize the traversal. 
    - If a node's value is less than `low`, the algorithm only explores the right subtree, since all values in the 
      left subtree would be out of the specified range.
    - Conversely, if a node's value is greater than `high`, the algorithm only explores the left subtree.

4. **Summation**: The algorithm adds up the values of nodes that are within the range. This summing occurs in the 
    recursive calls of the `dfs` function.

5. **Base Case**: For the recursive `dfs` function, the base case is when the current node is `None`, at which point 
   it returns 0. This handles leaf nodes and empty subtrees.

6. **Final Computation**: The method `rangeSumBST` calls `dfs` starting from the root of the BST and returns the total 
   sum of the node values that lie within the specified range.

This solution is efficient as it avoids unnecessary traversal of the entire tree, focusing only on nodes that could 
potentially fall within the range. It effectively combines the principles of binary search in a BST with a recursive 
DFS approach.

'''
