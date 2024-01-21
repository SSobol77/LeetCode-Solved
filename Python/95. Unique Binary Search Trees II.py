# 95. Unique Binary Search Trees II.

# Topic: Dynamic Programming, Backtracking, Tree, Binary Search Tree, Binary Tree.

'''
# Task:
----------
Given an integer n, return all the structurally unique BST's (binary search trees), which has 
exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 8


# Testcase:
-------------
3
1


# Code:
-------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        

'''
# Solution:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # Handle the edge case where n is 0
        if n == 0:
            return []

        # Helper function to generate all unique BSTs for a range of values
        def generate(start, end):
            # Base case: if start exceeds end, there's no tree, hence return [None]
            if start > end:
                return [None]

            all_trees = []
            # Iterate through each number in the range as a potential root
            for i in range(start, end + 1):
                # Recursively generate all possible left and right subtrees
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)

                # Connect each left and right subtree with the root 'i'
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)

            return all_trees

        # Generate and return all unique BSTs from 1 to n
        return generate(1, n)

# Test Cases:
def treeToString(root: TreeNode) -> str:
    if not root:
        return "null"
    leftStr = treeToString(root.left)
    rightStr = treeToString(root.right)
    return f"[{root.val}, {leftStr}, {rightStr}]"

# Test Case 1
sol = Solution()
trees1 = sol.generateTrees(3)
for tree in trees1:
    print(treeToString(tree))

# Test Case 2
trees2 = sol.generateTrees(1)
for tree in trees2:
    print(treeToString(tree))

# Description:
'''
To solve the problem of generating all structurally unique BSTs for a given n, we can use a combination of 
recursion and dynamic programming. The idea is to consider each number from 1 to n as the root, and then 
recursively construct the left and right subtrees.

The process involves the following steps:

1. Iterate through each number i from 1 to n.
2. For each i, recursively generate all possible left subtrees with root nodes less than i and all possible 
   right subtrees with root nodes greater than i.
3. Combine each left and right subtree with the root i to form a BST.
4. Use dynamic programming (memoization) to store and reuse subtrees that have already been computed.

Explanation:

- The generate function is a recursive function that generates all unique BSTs for a given range (start, end).
- For each i in the range, it generates all possible left subtrees (with roots less than i) and right subtrees 
  (with roots greater than i).
- It then connects each combination of left and right subtrees to the root i to form unique BSTs.
- The solution caters to the constraint (1 ≤ n ≤ 8) and uses efficient recursion with a straightforward approach 
  to generate all BSTs.

'''