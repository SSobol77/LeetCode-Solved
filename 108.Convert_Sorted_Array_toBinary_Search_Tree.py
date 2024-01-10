# 108. Convert Sorted Array to Binary Search Tree

# Topic: Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree.


"""
## Task:
---------
Given an integer array nums where the elements are sorted in ascending order, convert 
it to a height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in a strictly increasing order.


## Testcase:
-------------
[-10,-3,0,5,9]
[1,3]


## Code:
----------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        

"""
# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # TreeNode class constructor to create a new node
        # 'val' is the value of the node
        # 'left' and 'right' are pointers to the left and right children, respectively
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Helper function to convert a portion of the list to a BST
        def convertListToBST(left, right):
            # Base case: if the 'left' index is greater than 'right', the subarray is empty
            if left > right:
                return None

            # Find the middle element to make it the root of the BST
            # Using (left + right) // 2 could lead to overflow, so we use left + (right - left) // 2
            mid = left + (right - left) // 2

            # Create a new tree node with the middle element
            node = TreeNode(nums[mid])

            # Recursively build the left subtree using the left half of the current array
            node.left = convertListToBST(left, mid - 1)

            # Recursively build the right subtree using the right half of the current array
            node.right = convertListToBST(mid + 1, right)

            # Return the node, now connected with its left and right subtrees
            return node
        
        # Start the recursion from the first to the last element of the array
        return convertListToBST(0, len(nums) - 1)


# Description
'''
To address the problem of converting a sorted array into a height-balanced binary search tree (BST), the key lies 
in understanding both the properties of a BST and the concept of a height-balanced tree. A BST ensures that for 
each node, all elements in its left subtree are smaller, and all elements in its right subtree are larger. 
A height-balanced tree is one where the depth of the left and right subtrees of any node differ by no more than one.

The solution employs a divide-and-conquer approach. The central idea is to construct the BST by repeatedly choosing 
the middle element of the current segment of the array as the root. This strategy guarantees that the tree remains 
balanced. The process is as follows:

1. **Identify the Base Case**: When the segment of the array to consider is empty (indicated by the "start" index being 
     greater than the "end" index), the function returns `None`. This condition serves as the recursion's base case.

2. **Select the Middle Element**: The middle index of the array or subarray segment is computed. This element becomes 
     the root of the BST or subtree, ensuring a balanced distribution of nodes.

3. **Construct the Root Node**: A new tree node is created with the value of the middle element, establishing it as the root.

4. **Recursive Construction of Subtrees**: 
    - The function recursively builds the left subtree using the left half of the array segment.
    - Similarly, it constructs the right subtree using the right half of the segment.

5. **Assemble and Return the Tree**: The root node, now linked to its left and right subtrees, forms the BST, which is 
     then returned.

This method ensures that each element of the array contributes to forming the tree, resulting in a height-balanced BST. 
The balanced nature of the tree is a direct outcome of always choosing the central element as the root, thereby evenly 
distributing the remaining elements into the left and right subtrees. The implementation in Python encapsulates this 
logic efficiently, making use of recursion to handle the repetitive task of subtree creation.

'''
