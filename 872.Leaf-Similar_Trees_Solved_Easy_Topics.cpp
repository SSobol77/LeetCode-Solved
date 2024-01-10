// 872.Leaf-Similar_Trees_Solved_Easy_Topics.

/*
## Task:
---------
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

#Example 1:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

#Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

#Constraints:
The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].

## Testcase:872.Leaf-Similar_Trees_Solved_Easy_Topics
-------------
[3,5,1,6,2,9,8,null,null,7,4]
[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
[1,2,3]
[1,3,2]
*/


// Solution:
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
 */
class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leaves1, leaves2;
        
        // Traverse the first tree and collect leaf values
        dfs(root1, leaves1);
        
        // Traverse the second tree and collect leaf values
        dfs(root2, leaves2);
        
        // Compare the leaf value sequences
        return leaves1 == leaves2;
    }
    
    void dfs(TreeNode* node, vector<int>& leaves) {
        if (!node) return;
        
        if (!node->left && !node->right) {
            // If it's a leaf node, add its value to the vector
            leaves.push_back(node->val);
        }
        
        // Recursively traverse left and right subtrees
        dfs(node->left, leaves);
        dfs(node->right, leaves);
    }
};

/*
To solve this problem, you need to traverse both binary trees and collect the leaf values in the 
same order for both trees. Then, compare the leaf value sequences to check if they are the same. 
You can achieve this using a depth-first traversal approach.

This code defines a leafSimilar function that takes two tree nodes as input and returns true if 
their leaf value sequences are the same. It uses a depth-first search (DFS) approach to collect 
leaf values from both trees and then compares the sequences.

*/
