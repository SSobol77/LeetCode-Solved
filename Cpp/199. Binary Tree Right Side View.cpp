// 199. Binary Tree Right Side View

// Topic: Tree, Depth-First Search, Breadth-First Search, Binary Tree.

/*
Task:
-----
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes 
you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

# Testcase:
-----------
[1,2,3,null,5,null,4]
[1,null,3]
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
    vector<int> rightSideView(TreeNode* root) {
        
    }
};
*/
// Solution: ---------------------------------------------------------------

#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> view; // To store the right side view
        if (!root) return view; // If the tree is empty, return an empty vector

        queue<TreeNode*> q; // Queue for level order traversal
        q.push(root); // Start with the root

        while (!q.empty()) {
            int levelSize = q.size(); // Number of nodes at the current level

            for (int i = 0; i < levelSize; ++i) {
                TreeNode* node = q.front(); // Get the current node
                q.pop();

                // If this is the last node in the current level, add it to the view
                if (i == levelSize - 1) {
                    view.push_back(node->val);
                }

                // Add the child nodes for the next level
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }

        return view; // Return the right side view
    }
};


// Description:
/*
To obtain the right side view of a binary tree, we can perform a level-order traversal (Breadth-First Search, BFS) and capture the last node's value at each level. This approach ensures that we always see the nodes as if we were standing on the right side of the tree.


### Solution Explanation:

1. **Initialization**: Create a vector `view` to store the right side view of the tree.

2. **Base Case**: If the root is `nullptr` (the tree is empty), return the empty `view` vector.

3. **Level Order Traversal**: Use a queue `q` to perform a level-order traversal of the tree. Initially, enqueue the root.

4. **Traversing the Tree**: Process the tree level by level. For each level, determine the number of nodes (`levelSize`) currently in the queue, which represents all nodes at that depth.

5. **Capturing Rightmost Nodes**: Iterate over all nodes at the current level. For each node, dequeue it and check if it is the last node in the level (`i == levelSize - 1`). If it is, add its value to the `view` vector, as this is the node visible from the right side at the current depth.

6. **Enqueuing Child Nodes**: For each dequeued node, enqueue its left and right children (if they exist) to the queue. These nodes will be processed at the next level of the traversal.

7. **Repeating the Process**: Continue the level-order traversal until the queue is empty, indicating that all levels of the tree have been processed.

8. **Returning the Result**: After completing the traversal, the `view` vector contains the values of the rightmost node at each level, representing the right side view of the tree. Return the `view` vector as the final result.

This approach ensures that for each level of the tree, only the rightmost node is included in the right side view, effectively simulating the perspective of an observer standing to the right of the tree and looking at it from top to bottom.
*/