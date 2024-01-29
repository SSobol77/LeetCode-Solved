// 98. Validate Binary Search Tree.

// Topic: Tree, Depth-First Search, Binary Search Tree, Binary Tree.

/*
# Task:
-------
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 
Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1


# Testcase:
-----------
[2,1,3]
[5,1,4,null,null,3,6]


# Code:
-------
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
    bool isValidBST(TreeNode* root) {
        
    }
};
*/
// Solution:

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return validate(root, LONG_MIN, LONG_MAX);
    }

private:
    bool validate(TreeNode* node, long lower_limit, long upper_limit) {
        if (!node) return true; // An empty tree is a valid BST

        // Check if the current node's value falls within the valid range
        if (node->val <= lower_limit || node->val >= upper_limit) return false;

        // Recursively validate the left subtree with updated upper limit
        // and the right subtree with updated lower limit
        return validate(node->left, lower_limit, node->val) && 
               validate(node->right, node->val, upper_limit);
    }
};


// Description:
/*
To determine if a binary tree is a valid Binary Search Tree (BST), we must ensure that all nodes fulfill the BST property: the value of all nodes in the left subtree must be less than the node's value, and the value of all nodes in the right subtree must be greater than the node's value. Additionally, this rule must apply recursively to all subtrees in the tree.

A common approach to solve this problem is to perform a depth-first traversal (such as inorder traversal) while maintaining a range (`lower_limit`, `upper_limit`) for each node's value to ensure that it falls within a valid range. Initially, the range is infinite (`-∞` to `+∞`). As we traverse down the tree, the range narrows based on parent node values.

### Explanation:

1. **Base Case**: If the current node is `nullptr`, we've reached a leaf's child, and by definition, a null tree is a valid BST, so return `true`.

2. **Validation Check**: For each node, we check if its value is within the allowed range (`lower_limit` < node's value < `upper_limit`). If not, return `false`.

3. **Recursive Calls**:
    - For the left child, we make a recursive call with an updated `upper_limit` because all values in the left subtree must be less than the current node's value. The `lower_limit` remains the same.
    - For the right child, we make a recursive call with an updated `lower_limit` because all values in the right subtree must be greater than the current node's value. The `upper_limit` remains the same.

4. **Return Value**: The current subtree is a valid BST if both the left and right subtrees are valid BSTs, hence the use of the logical AND operator.

This solution ensures that every node in the tree is checked against the BST properties with the correct range of values, effectively validating the BST.

*/
