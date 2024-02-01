# 199. Binary Tree Right Side View

# Topic: Tree, Depth-First Search, Breadth-First Search, Binary Tree.

'''
Task:
-----
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes 
you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

# Testcase:
-----------
[1,2,3,null,5,null,4]
[1,null,3]
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
   
'''
# Solution: ---------------------------------------------------------

class TreeNode:
    # TreeNode class definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Value of the node
        self.left = left  # Left child
        self.right = right  # Right child

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize the result list to store the right side view of the tree.
        res = []

        # Define a recursive depth-first search (DFS) function that traverses the tree.
        # n is the current node, and d is the current depth in the tree.
        def dfs(n, d):
            if n:
                # If this is the first node we are visiting at depth d,
                # it is the rightmost node at this depth, so we add it to the result list.
                if d == len(res):
                    res.append(n.val)

                # Recurse on the right child first to ensure right side nodes are processed first.
                # This gives us the right side view when looking from the top to the bottom of the tree.
                dfs(n.right, d+1)

                # Then, recurse on the left child. Nodes on the left will only be added to the result list
                # if there are no nodes on the right at the same depth.
                dfs(n.left, d+1)

        # Start the DFS from the root node at depth 0.
        dfs(root, 0)

        # Return the list containing the right side view of the binary tree.
        return res


### Description:
"""
The provided Python code implements a solution to find the right side view of a binary tree using a depth-first search (DFS) strategy. The algorithm traverses the tree, ensuring that at each depth, the rightmost node is visible and captured. Here's a detailed description of how this algorithm works:

### Algorithm Description:

1. **TreeNode Class**: Defines the structure of the tree nodes, where each node has a value `val`, a left child `left`, and a right child `right`.

2. **Solution Class and rightSideView Method**: The `Solution` class contains the method `rightSideView`, which takes the root of a binary tree as input and returns a list of values representing the right side view of the tree.

3. **Result List**: The `res` list is initialized to store the values of the nodes visible from the right side. It will hold one value per tree level, corresponding to the rightmost node at that depth.

4. **Depth-First Search (DFS) Function**: A nested helper function `dfs` is defined within `rightSideView`. It takes a node `n` and its depth `d` as arguments. The function recursively explores the tree in a depth-first manner.

5. **DFS Invocation**: The `dfs` function is initially called with the root node and a depth of 0.

6. **DFS Logic**:
    - **Base Case**: If the current node `n` is not `None`, the function proceeds; otherwise, it returns, ending the recursion for that path.
    - **Rightmost Node at Each Depth**: If the current depth `d` is equal to the length of the `res` list, it means this is the first time the function is visiting a node at this depth, and hence, `n` is the rightmost node at this depth seen so far. The value of `n` is appended to the `res` list.
    - **Recursive Calls**: The function first recurses on the right child (`dfs(n.right, d+1)`) and then on the left child (`dfs(n.left, d+1)`). This order ensures that right children are processed before left children at each level, giving precedence to right nodes when populating the `res` list.

7. **Result Compilation**: After the DFS completes, the `res` list contains the values of the rightmost nodes at each depth, in top-to-bottom order. This list is returned as the final result.

### Key Points:

- **DFS Precedence**: By traversing the right subtree before the left subtree at each node, the algorithm ensures that the rightmost nodes are encountered first at each depth, which aligns with the goal of capturing the right side view.
- **Depth Tracking**: The depth parameter `d` in the DFS function is crucial for determining when to add a node's value to the `res` list. It ensures that only the first node encountered at each depth (which, due to the traversal order, is the rightmost node) is added.
- **In-Place Updates**: The `res` list is updated in place during the DFS, eliminating the need for additional data structures to hold intermediate results.

This algorithm efficiently computes the right side view of a binary tree with a time complexity proportional to the number of nodes in the tree, as each node is visited exactly once during the DFS.    

"""
