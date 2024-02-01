// 114. Flatten Binary Tree to Linked List.

// Topic: Linked List, Stack, Tree, Depth-First Search, Binary Tree.

/*
Task: 
-----
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to the next node in 
the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]
 
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 
Follow up: Can you flatten the tree in-place (with O(1) extra space)?

# Testcase:
[1,2,5,3,4,null,6]
[]
[0]


# Code:
--------
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 *//*
class Solution {
public:
    void flatten(TreeNode* root) {
        
    }
};

*/

// Solution: ------------------------------------------------------------

class Solution {
public:
    void flatten(TreeNode* root) {
        if (!root) return; // Base case: if the tree is empty or we've reached a leaf node

        TreeNode* left = root->left;
        TreeNode* right = root->right;

        // Flatten the left subtree
        flatten(left);
        // Flatten the right subtree
        flatten(right);

        // Set the root's left to null and right to the previously left subtree
        root->left = nullptr;
        root->right = left;

        // Find the last node of the new right subtree
        TreeNode* current = root;
        while (current->right) {
            current = current->right;
        }

        // Attach the previously right subtree to the end of the new right subtree
        current->right = right;
    }
};


// Description:  =========================================================
/*
To flatten a binary tree into a linked list in the same order as a pre-order traversal, we can follow a recursive 
approach that adheres to the in-place requirement with O(1) extra space. The key idea is to traverse the tree in 
a preorder fashion (root, left, right) and rearrange the nodes such that each node's right child points to the next 
node in the preorder traversal, and the left child is always null.


### Solution Explanation:

1. **Recursive Approach**: The function `flatten` is called recursively for each node starting from the root. The recursion 
     flattens the left and right subtrees first before rearranging the nodes to form a linked list.

2. **Flattening Subtrees**: The left and right subtrees of the current node are flattened by recursive calls. After these 
     calls, both subtrees are flattened into linked lists themselves.

3. **Rearranging Nodes**: After flattening the left subtree, the root's left pointer is set to null, and its right pointer 
     is set to the head of the flattened left subtree. This effectively moves the flattened left subtree to the right, 
     maintaining the preorder sequence.

4. **Merging Subtrees**: The algorithm then iterates to the end of the newly formed right subtree (which was originally the 
    left subtree) and attaches the flattened right subtree to the end. This completes the flattening for the current node, 
    ensuring that the preorder traversal order is preserved.

5. **In-Place Transformation**: The tree is transformed in place; no new nodes are created, and the existing pointers are 
     merely rearranged to achieve the flattened structure.

6. **Base Case and Edge Cases**: The recursion has a base case when the current node is null, at which point the function 
     returns. This handles edge cases like an empty tree or reaching the end of a branch.

This solution ensures that the binary tree is flattened into a linked list following the preorder traversal order, with each 
node's right pointer leading to the next node in the list and the left pointer always set to null, achieving the desired 
transformation in place.

*/