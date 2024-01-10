# 107. Binary Tree Level Order Traversal II

# Topic

'''
# Taks:
--------
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' 
values. (i.e., from left to right, level by level from leaf to root).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

# Testcase:
-----------
[3,9,20,null,null,15,7]
[1]
[]


# Code:
---------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
  
    
'''
# Solution:
class TreeNode:
    # A basic tree node structure with a value and left/right children
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(nodes):
    # This function builds a binary tree from a list of values
    if not nodes:
        return None  # Return None if the list is empty

    root = TreeNode(nodes[0])  # Initialize the root with the first element
    queue = [root]  # A queue to manage tree nodes for level order insertion
    front = 0  # Index to keep track of the current node in the queue
    index = 1  # Index to traverse the nodes list

    # Loop through nodes list and build the tree
    while index < len(nodes):
        node = queue[front]  # Get the current node from the queue
        front += 1

        # Process the left child
        leftVal = nodes[index]
        index += 1
        if leftVal is not None:
            node.left = TreeNode(leftVal)
            queue.append(node.left)

        if index >= len(nodes): break  # Break if no more nodes to process

        # Process the right child
        rightVal = nodes[index]
        index += 1
        if rightVal is not None:
            node.right = TreeNode(rightVal)
            queue.append(node.right)

    return root  # Return the root of the constructed tree

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # Return an empty list if the tree is empty

        from collections import deque
        queue = deque([root])  # Initialize a queue with the root node
        result = []

        # Perform level order traversal
        while queue:
            level = []  # List to store nodes values of the current level
            level_length = len(queue)

            # Process each node of the current level
            for _ in range(level_length):
                node = queue.popleft()  # Remove and get the first node in the queue
                level.append(node.val)  # Add the node value to the level list

                # Add the children of the current node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)  # Add the current level to the result

        return result[::-1]  # Reverse the result for bottom-up order

# Test cases
solution = Solution()

# Building the binary tree from the list representation and then testing
tree1 = buildTree([3, 9, 20, None, None, 15, 7])
print(solution.levelOrderBottom(tree1))  # Expected Output: [[15, 7], [9, 20], [3]]

tree2 = buildTree([1])
print(solution.levelOrderBottom(tree2))  # Expected Output: [[1]]

tree3 = buildTree([])
print(solution.levelOrderBottom(tree3))  # Expected Output: []


# Description:
'''
In this code, we define a TreeNode class for the binary tree nodes, a buildTree function to 
build the tree from a list, and the Solution class with the levelOrderBottom method to perform 
the bottom-up level order traversal. The traversal uses a queue for level order processing and 
adds the levels to the result in reverse order. The test cases demonstrate how to use these 
functions.

'''
