# 173. Binary Search Tree Iterator

'''
Task:
-----

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the 
constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the 
smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order 
traversal when next() is called.

 
Example 1:
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
 

Constraints:
The number of nodes in the tree is in the range [1, 10^5].
0 <= Node.val <= 10^6
At most 10^5 calls will be made to hasNext, and next.
 
Follow up:
Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, 
where h is the height of the tree?


#Testcase
----------
["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]
[[[7,3,15,null,null,9,20]],[],[],[],[],[],[],[],[],[]]


# Code:
-------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        

    def next(self) -> int:
        

    def hasNext(self) -> bool:
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

'''

# Solution:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        # Add all left children of the current node to the stack
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        # The top element of the stack is the next smallest element
        topmost_node = self.stack.pop()
        
        # If there is a right child, push all its leftmost children to the stack
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)

        return topmost_node.val

    def hasNext(self) -> bool:
        # If the stack is not empty, there are still elements to be traversed
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
