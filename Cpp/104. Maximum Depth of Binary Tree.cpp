// 104. Maximum Depth of Binary Tree.


// Topic: Tree, Depth-First Search, Breadth-First Search, Binary Tree.

/*
## Task:
---------
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root 
node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100



## Testcase:
-------------
[3,9,20,null,null,15,7]
[1,null,2]


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
    int maxDepth(TreeNode* root) {
        
    }
};
*/
// Solution ---------------------------------------------------------------------------

//Depth-First Search (DFS) Solution:
class Solution {
public:
    int maxDepth(TreeNode* root) {
        // Base case: if the current node is null, the depth is 0
        if (!root) return 0;

        // Recursive case: the depth of the current node is 1 plus the maximum depth of its left and right subtrees
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};


/*
To find the maximum depth of a binary tree, we can use either Depth-First Search (DFS) or Breadth-First Search (BFS) approaches.
Below, both methods are outlined with their C++ implementations.

### Depth-First Search (DFS) Solution:

DFS involves recursively traversing down each branch of the tree and counting the depth as we go, ultimately returning the maximum 
depth encountered. This is a straightforward and elegant recursive solution.

*/

// Breadth-First Search (BFS) Solution:
#include <queue>

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0; // If the tree is empty, the depth is 0

        queue<TreeNode*> q;
        q.push(root);
        int depth = 0;

        while (!q.empty()) {
            int levelSize = q.size(); // Number of nodes at the current level

            for (int i = 0; i < levelSize; ++i) {
                TreeNode* node = q.front();
                q.pop();

                // Add the child nodes of the current node to the queue
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }

            // Increment depth after processing all nodes at the current level
            depth++;
        }

        return depth;
    }
};

/*
### Breadth-First Search (BFS) Solution:

BFS iteratively traverses the tree level by level, counting the number of levels traversed, which corresponds to the maximum 
epth of the tree.

Both solutions effectively compute the maximum depth of a binary tree. The choice between DFS and BFS can depend on the specific 
characteristics of the tree (e.g., balanced vs. unbalanced) and personal preference. DFS is more succinct and usually the go-to 
for this problem, but BFS can be more intuitive in terms of visualizing the level-by-level traversal.

*/
