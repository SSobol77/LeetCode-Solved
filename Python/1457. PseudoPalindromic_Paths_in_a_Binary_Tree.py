# 1457. Pseudo-Palindromic Paths in a Binary Tree.

# Topic: Bit Manipulation, Tree, Depth-First Search, Breadth-First Search, Binary Tree.

"""
### Task:
---
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example 1:
Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:
Input: root = [9]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 9

Hint 1:
Note that the node values of a path form a palindrome if at most one digit has an odd frequency (parity).
Hint 2:
Use a Depth First Search (DFS) keeping the frequency (parity) of the digits. Once you are in a leaf node check if at most one digit has an odd frequency (parity).


### Testcase:
---
[2,3,1,3,1,null,1]
[2,1,1,1,3,null,null,null,null,null,1]
[9]


### Code:
---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:


"""
### Solution: --------------------------------------

class TreeNode:
    # TreeNode class to represent each node of a binary tree.
    # Each node has a value, a left child, and a right child.
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # Value of the node (an integer)
        self.left = left     # Left child of the node (TreeNode or None)
        self.right = right   # Right child of the node (TreeNode or None)

class Solution:
    # Function to count the number of pseudo-palindromic paths in a binary tree.
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        # Helper function to perform depth-first search (DFS) starting from a given node.
        def dfs(node, path):
            # If the current node is None (base case), return 0 as there is no path.
            if not node:
                return 0

            # Toggle the bit for the current node's value in the path.
            # This step uses bitwise XOR to track the parity (odd/even count) of the node's value.
            path ^= 1 << node.val

            # Check if the current node is a leaf node (no children).
            if not node.left and not node.right:
                # Check if the path can form a palindrome.
                # A path can form a palindrome if at most one bit is set in 'path'.
                # 'path & (path - 1)' is a trick to check if the number has at most one bit set.
                if path & (path - 1) == 0:
                    return 1  # Path is pseudo-palindromic, count this path.
                return 0  # Path is not pseudo-palindromic.

            # If not a leaf node, continue DFS on left and right children and sum the results.
            # This step accumulates the count of pseudo-palindromic paths in the subtree rooted at the current node.
            return dfs(node.left, path) + dfs(node.right, path)

        # Start DFS from the root of the tree with an initial path value of 0.
        return dfs(root, 0)



### Description: ===================================
'''
In this code, the `dfs` function is a recursive function that traverses the tree. The `path` variable,
represented as an integer, uses bitwise operations to efficiently track the parity of the digits encountered
along the path. By checking the condition `path & (path - 1)`, the code efficiently determines if the digits
along a path can be rearranged to form a palindrome, which is the key logic for identifying pseudo-palindromic
paths.

To solve this problem, we can use Depth First Search (DFS) to traverse the binary tree and keep track of the
frequency of digits in the current path. The key idea is to check if a permutation of the path's digits can
form a palindrome. For a sequence of digits to form a palindrome, there can be at most one digit with an
odd count.

Here's a step-by-step approach:

1. **Depth First Search**: Traverse the tree using DFS. At each node, update the frequency count of the node's value.

2. **Checking for Pseudo-Palindrome**: To efficiently check if a path forms a pseudo-palindrome, we can use a bit
   manipulation trick. We maintain an integer where each bit represents whether the count of a digit (1-9) is odd
   or even. We toggle the corresponding bit of a digit when we encounter it. In the end, if at most one bit is set
   in the integer, the path can form a palindrome.

3. **Counting Paths**: When we reach a leaf node, we check if the path can form a pseudo-palindrome using the bit
   manipulation approach. If it can, we increment our count of such paths.


In this code, `path` is an integer used as a bit array. For each digit `d`, the `d`th bit of `path` is toggled
when `d` is encountered. The expression `path & (path - 1)` checks if `path` contains at most one set bit, which
is a condition for being able to form a palindrome.

This solution effectively traverses each path in the tree once, resulting in a time complexity of O(N), where N is
the number of nodes in the tree. The space complexity is O(H), where H is the height of the tree, due to the recursion
stack.

'''
