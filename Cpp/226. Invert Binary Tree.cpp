// 226. Invert Binary Tree.

// Topic: Tree, Depth-First Search, Breadth-First Search, Binary Tree.


/*
## Task:
---------
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


## Testcase:
-------------
[4,2,7,1,3,6,9]
[2,1,3]
[]


## Code:
----------
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
    TreeNode* invertTree(TreeNode* root) {
        
    }
};   

*/
// Solution:  --------------------------------------------------------------------


class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty or we reach a leaf node, return the node itself
        if (!root) return root;

        // Swap the left and right children of the current node
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;

        // Recursively invert the left subtree
        invertTree(root->left);
        
        // Recursively invert the right subtree
        invertTree(root->right);

        // Return the root of the inverted tree
        return root;
    }
};


// Descroption:  ===================================================================
/*
To invert a binary tree, we need to swap the left and right children for every node in the tree. This can be done using 
either a depth-first search (DFS) or a breadth-first search (BFS) approach. Here, I'll provide a DFS solution using recursion,
which is straightforward and intuitive.


### Solution Explanation:

1. **Base Case**: The recursion ends when `root` is `nullptr`, which occurs if the tree is empty or if a leaf node is reached. In this case, the function simply returns `root`.

2. **Swapping Children**: For each node visited, its left and right children are swapped. This is achieved by temporarily storing one child in a variable `temp`, assigning the other child to its place, and then assigning the `temp` to the other child.

3. **Recursive Calls**: The function then makes recursive calls to invert the left and right subtrees. Since the children have been swapped, the "left" subtree is actually the original right subtree, and vice versa.

4. **Inversion Process**: The inversion starts from the root and progresses downwards, with each level of the tree being inverted before moving on to the next level. This ensures that all nodes in the tree are processed.

5. **Returning the Root**: After all recursive calls complete, the root of the now-inverted tree is returned. This root is the same as the original tree's root, but its descendants have been rearranged due to the inversions.

This DFS approach to inverting a binary tree is effective and concise, making it a common solution for this problem. 
It systematically traverses the tree, ensuring that each subtree is inverted, and eventually results in the entire tree being inverted.

*/