# 1026. Maximum Difference Between Node and Ancestor.

# Topic: Tree, Depth-First Search, Binary Tree.

"""
### Task:
---
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b 
where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

#Example 1:
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :

|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3

Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

#Example 2:
Input: root = [1,null,2,null,0,3]
Output: 3
 
#Constraints:
The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 10^5

#Hint 1:
For each subtree, find the minimum value and maximum value of its descendants.


### Testcase:
---
[8,3,10,1,6,null,14,null,null,4,7,13]
[1,null,2,null,0,3]


### Code:
---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

          
"""
### Solution: ---------------------------------------------------------------------------------------------

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the maximum difference between the values of any ancestor-descendant pair in the binary tree.

        Args:
        root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        int: The maximum difference between the values of any ancestor-descendant pair in the tree.
        """

        def dfs(node, cur_max, cur_min):
            """
            Performs a depth-first search to find the maximum difference in the current subtree.

            Args:
            node (TreeNode): The current node in the binary tree.
            cur_max (int): The maximum value found in the current path from root to node.
            cur_min (int): The minimum value found in the current path from root to node.

            Returns:
            int: The maximum difference found in the subtree rooted at 'node'.
            """
            if not node:
                # Base case: if the node is None, return the difference between current max and min
                return cur_max - cur_min

            # Update the current max and min values based on the current node's value
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)

            # Recursively compute the maximum difference in the left and right subtrees
            left_diff = dfs(node.left, cur_max, cur_min)
            right_diff = dfs(node.right, cur_max, cur_min)

            # Return the maximum of the differences found in the left and right subtrees
            return max(left_diff, right_diff)

        # Start the DFS traversal from the root, initializing current max and min with the root's value
        return dfs(root, root.val, root.val)


### Description: --------------------------------------------------------------------------------------------------------------
'''
This problem involves finding the maximum difference in value between an ancestor node and a descendant node in a binary tree. 
The solution can be approached using a depth-first search (DFS) traversal of the tree, while keeping track of the minimum and 
maximum values seen in the current path (from the root to the current node).

### Algorithm:
1. **Depth-First Search (DFS):** 
   - Start DFS from the root node.
   - For each node, we pass the minimum and maximum values encountered so far in the path from the root to that node.

2. **Tracking Min and Max Values:** 
   - At each node, update the minimum and maximum values by comparing the current node's value with the current min and max.

3. **Calculating the Maximum Difference:** 
   - For each node, calculate the difference between the node's value and the current minimum and maximum values. 
   - Update the global maximum difference if either of these differences is larger than the current maximum difference.

4. **Recursive DFS Calls:** 
   - Recursively apply this process to the left and right children of the current node.

5. **Base Case:** 
   - If a node is `None` (indicating the leaf's child), return the current maximum difference.

### Description:

- The `dfs` function traverses each node of the tree.
- `cur_max` and `cur_min` keep track of the maximum and minimum values in the current path.
- At each node, the function calculates the difference with the current maximum and minimum, and recursively does the same for 
  its children.
- The function returns the maximum difference found in the subtree rooted at the current node.
- The `maxAncestorDiff` function initiates the DFS traversal from the root node.

This approach ensures that we consider all possible ancestor-descendant pairs and find the maximum difference among them.

'''
