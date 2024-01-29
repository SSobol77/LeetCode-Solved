// 94. Binary Tree Inorder Traversal.


// Topic : Stack, Tree, Depth-First Search, Binary Tree

/*
# Task:
---------
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


# Testcase:
------------
[1,null,2,3]
[]
[1]


# Code:
------------
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
    vector<int> inorderTraversal(TreeNode* root) {
        
    }
};
*/
// Solution: -----------------------------------------------------------------------------------

#include <vector>
#include <stack>

// Note: The TreeNode structure is already defined in the environment, so it's not redefined here.

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nodes;
        stack<TreeNode*> stack;
        TreeNode* current = root;

        // Traverse the tree
        while (current != nullptr || !stack.empty()) {
            // Reach the left most Node of the current Node
            while (current != nullptr) {
                // Place pointer to a tree node on the stack before traversing the node's left subtree
                stack.push(current);
                current = current->left;
            }

            // Current must be nullptr at this point
            current = stack.top();
            stack.pop();
            nodes.push_back(current->val); // Add the node's value to the traversal result

            // We have visited the node and its left subtree. Now, it's right subtree's turn
            current = current->right;
        }

        return nodes;
    }
};


// Description:  ==========================================================================================
/*
The algorithm for performing an inorder traversal of a binary tree iteratively using a stack can be described as follows:

### Algorithm Description:

1. **Initialize**:
    - Create an empty stack to keep track of the nodes to visit.
    - Initialize a pointer `current` to the root of the binary tree.

2. **Traverse to the Leftmost Node**:
    - While `current` is not `nullptr` (indicating we haven't reached the leftmost node):
        - Push `current` onto the stack. This action records the node for later access after visiting its left subtree.
        - Move `current` to its left child (`current = current->left`).

3. **Process Node and Move Right**:
    - Once you cannot go left anymore (`current` is `nullptr`):
        - Pop the top node from the stack. This node is the one that needs to be processed next (it has no left children, or they have already been processed).
        - Add the value of the popped node to the result list, as this is the inorder position for this node.
        - Set `current` to the right child of the popped node (`current = current->right`) to process its right subtree.

4. **Repeat or Terminate**:
    - Repeat steps 2 and 3 until `current` is `nullptr` and the stack is empty. This condition indicates that every node has been visited in its inorder position.

5. **Return Result**:
    - Once the entire tree has been traversed, return the result list containing the values of the nodes in their inorder traversal order.

### Key Points:

- **Inorder Traversal Order**: In an inorder traversal of a binary tree, each node is visited in the following order: left child, node itself, right child. This algorithm adheres to this order by using a stack to manage the traversal sequence.
- **Stack Usage**: The stack is crucial for remembering the nodes that have been visited but not yet processed, especially when traversing back up the tree after reaching the leftmost nodes.
- **No Recursion**: Unlike recursive solutions that rely on the call stack, this algorithm explicitly uses a data structure (stack) to manage the traversal, which can offer more control and possibly reduce stack space usage for very deep trees.

This iterative approach with a stack is efficient and particularly useful for scenarios where recursion might lead to stack overflow errors for very deep trees, or where explicit stack management is preferred for other reasons.

*/