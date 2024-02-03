// 543. Diameter of Binary Tree.

// Topic: Tree, Depth-First Search, Binary Tree.


/*
### Task:
---
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-100 <= Node.val <= 100


### Testcase:
---
[1,2,3,4,5]
[1,2]


### Code:
---
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
    int diameterOfBinaryTree(TreeNode* root) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
    int maxDiameter = 0;  // Class-level variable to keep track of the maximum diameter

public:
    int diameterOfBinaryTree(TreeNode* root) {
        maxDepth(root);  // Start the DFS from the root to calculate the max depth and update maxDiameter
        return maxDiameter;
    }

private:
    int maxDepth(TreeNode* node) {
        if (!node) return 0;  // Base case: if the node is null, return 0 as the depth

        int leftDepth = maxDepth(node->left);  // Recursively find the max depth of the left subtree
        int rightDepth = maxDepth(node->right);  // Recursively find the max depth of the right subtree

        // Update maxDiameter at this node if the sum of leftDepth and rightDepth is greater than the current maxDiameter
        maxDiameter = max(maxDiameter, leftDepth + rightDepth);

        // Return the depth of this subtree to the parent call
        return 1 + max(leftDepth, rightDepth);  // Include the current node in the depth count
    }
};


// Description: ===================================
/*
To find the diameter of a binary tree, we need to understand that the diameter may not necessarily pass through the root. 
The diameter is essentially the longest path between any two nodes in the tree, which can be found by calculating the maximum 
depth (height) of the left and right subtrees for each node and adding them together. The maximum value obtained at any node 
during this process is the diameter of the tree.

We can solve this problem using a depth-first search (DFS) approach, where we recursively calculate the height of each subtree. 
At each node, we calculate the diameter as the sum of the heights of the left and right subtrees. We update a global or class-level 
variable to keep track of the maximum diameter found during the traversal.


### Description:

- **Class-Level Variable**: `maxDiameter` is used to keep track of the maximum diameter found during the DFS traversal.

- **diameterOfBinaryTree Function**: This is the main function that initiates the DFS traversal from the root. It doesn't compute 
    the diameter directly but relies on the side effect of updating `maxDiameter` during the traversal.

- **maxDepth Function**: A private helper function that recursively calculates the maximum depth of a subtree rooted at a given node. 
    It returns the depth of the subtree to calculate the diameter at each node's level correctly. The function updates `maxDiameter` 
    with the sum of the depths of the left and right subtrees if it's larger than the current `maxDiameter`.

### Complexity:

- **Time Complexity**: O(N), where N is the number of nodes in the tree. Each node is visited exactly once, and the depth is calculated.
- **Space Complexity**: O(H), where H is the height of the tree. This space is used by the recursion stack. In the worst case (a skewed 
     tree), the space complexity will be O(N).

*/
