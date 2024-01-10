# 101. Symmetric Tree.

# Topic: Tree, Depth-First Search, Breadth-First Search, Binary.

"""
## Task:
---------
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?


## Testcase:
-------------
[1,2,2,3,4,4,3]
[1,2,2,null,3,null,3]


## Code:
------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        

"""
# Solution:

## Recursive Implementation:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # If root is None, the tree is symmetric
        if not root:
            return True
        
        # Recursive helper function to check if two trees are mirror images
        def isMirror(left, right):
            # Both are None, symmetric
            if not left and not right:
                return True
            # One is None and the other is not, not symmetric
            if not left or not right:
                return False
            # Check values are the same and recursively check subtrees
            return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        # Start the recursive checking from the root
        return isMirror(root.left, root.right)


## Iterative Implementation:
    
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        # Tree is symmetric if root is None
        if not root:
            return True
        
        # Initialize a queue for level-order traversal
        queue = [root.left, root.right]
        while queue:
            # Pop two nodes for comparison
            left = queue.pop(0)
            right = queue.pop(0)
            
            # Continue if both are None
            if not left and not right:
                continue
            # If one is None or values are different, tree is not symmetric
            if not left or not right or left.val != right.val:
                return False
            
            # Enqueue children for the next level of comparison
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        
        # If all comparisons passed, the tree is symmetric
        return True


# Description:
'''
To solve the problem of determining whether a binary tree is symmetric, we can approach it both recursively and iteratively. 
The key idea is to compare the left and right subtrees of the tree and check if they are mirror images of each other.

### Recursive Approach:

1. **Base Case**: If the root is `None`, the tree is symmetric.
2. **Symmetry Check Function**: Define a helper function (e.g., `isMirror`) that takes two nodes as input and checks 
     if they are mirrors of each other.
3. **Comparisons**: In `isMirror`, check if:
   - Both nodes are `None` (symmetric case).
   - One of them is `None` and the other isn't (asymmetric case).
   - The values of the two nodes are the same, and the left subtree of one is the mirror of the right subtree of the 
     other, and vice versa.
4. **Initial Call**: Call `isMirror` with the left and right children of the root.

### Iterative Approach:

1. **Queue for Level Order Traversal**: Use a queue to perform a level-order traversal of the tree, comparing nodes 
     at each level.
2. **Enqueue**: Initially, enqueue the left and right children of the root.
3. **Level-wise Symmetry Check**: At each step, dequeue two nodes and compare them. Then enqueue the children of 
     these nodes in a specific order: left child of the first node with the right child of the second node, and 
     right child of the first node with the left child of the second node.
4. **Continue Until Queue is Empty**: If at any point the comparison fails, return `false`. If the queue is empty
     and all comparisons have passed, return `true`.

### In the code:
----------------
- `isSymmetric` implements the recursive approach.
- `isSymmetricIterative` implements the iterative approach using a queue. 
- Both methods start by checking if the root is `None`. If it is, the tree is symmetric by definition.
- The recursive `isMirror` function and the loop in `isSymmetricIterative` perform the actual symmetry checks as described.

'''