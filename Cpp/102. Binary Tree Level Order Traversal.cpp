// 102. Binary Tree Level Order Traversal.

// Topic: Tree, Breadth-First Search, Binary Tree



/*
# Task:

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, 
level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        
    }
};    
*/
// Solution:

#include <vector>
#include <queue>

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> levels;
        if (!root) return levels; // If the tree is empty, return an empty list

        queue<TreeNode*> q;
        q.push(root); // Start with the root

        while (!q.empty()) {
            int levelSize = q.size(); // Number of nodes at the current level
            vector<int> currentLevel;

            for (int i = 0; i < levelSize; ++i) {
                TreeNode* node = q.front();
                q.pop(); // Remove the node from the queue
                currentLevel.push_back(node->val); // Add the node's value to the current level's result

                // Enqueue child nodes of the current node
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }

            // After processing all nodes at the current level, add the level's result to the levels list
            levels.push_back(currentLevel);
        }

        return levels;
    }
};

// Description:
/*
For the task of performing a level order traversal of a binary tree, the ideal approach is to use Breadth-First Search (BFS). 
This method involves using a queue to traverse the tree level by level, ensuring that nodes are visited from left to right at each level.

Here's a step-by-step guide on how to implement this in C++:

1. **Initialize**: If the root is null, return an empty result as there are no levels to traverse.
2. **Queue for BFS**: Use a queue to keep track of nodes and their levels. Start by enqueuing the root node.
3. **Level Order Traversal**: While the queue is not empty, process each level of the tree:
   - Determine the number of nodes at the current level (size of the queue at the start of the loop iteration).
   - For each node at this level, remove it from the queue, add its value to the current level's result, and enqueue its children 
     (left first, then right).
   - After processing all nodes at the current level, add the level's result to the final list of levels.

This solution efficiently performs a level order traversal of a binary tree, ensuring that all nodes are visited in the correct order 
from left to right at each level.

*/
