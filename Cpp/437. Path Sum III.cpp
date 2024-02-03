//437. Path Sum III.


// Topic: Tree, Depth-First Search, Binary Tree.


/*
### Task:
---
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along 
the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent 
nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-10^9 <= Node.val <= 10^9
-1000 <= targetSum <= 1000


### Testcase:
---
[10,5,-3,3,2,null,11,3,-2,null,1]
8
[5,4,8,11,null,13,4,7,2,null,null,5,1]
22


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
    int pathSum(TreeNode* root, int targetSum) {
        
    }
};
*/


// Solution: --------------------------------------

class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        if (!root) return 0; // Base case: if the current node is null, return 0

        // Count paths starting from the current node, then recurse for left and right children
        return countPaths(root, targetSum) + 
               pathSum(root->left, targetSum) + 
               pathSum(root->right, targetSum);
    }

private:
    // Helper function to count paths starting from the current node that sum up to the target
    int countPaths(TreeNode* node, int targetSum, long currentSum = 0) {
        if (!node) return 0; // Base case: if the node is null, return 0

        currentSum += node->val; // Add the current node's value to the running sum

        // Count the current path if it matches the target sum, then continue checking for more paths
        return (currentSum == targetSum) + 
               countPaths(node->left, targetSum, currentSum) + 
               countPaths(node->right, targetSum, currentSum);
    }
};


// Description: ===================================
/*
To solve the problem of finding the number of paths that sum to a given target in a binary tree, we can employ a recursive 
depth-first search (DFS) strategy. The key idea is to explore all possible paths from each node and accumulate the sum along 
each path, checking if it equals the target sum. Since paths do not need to start or end at the root or a leaf, we must consider
paths that start from all nodes along the way.

A straightforward approach is to use a recursive function that traverses the tree, and for each node, it does two things:
1. Counts the paths that start from the current node and sum up to the target sum.
2. Recursively checks for paths starting from the left and right children, treating each as potential starting points for new paths.

For counting paths starting from the current node, we can use another recursive function that accumulates the sum along the path 
and increases the count whenever the sum equals the target sum.

### Description:

- **pathSum Function**: This is the main function that initiates the DFS traversal. It counts the paths that sum up to the target 
    starting from the current node (`root`) and then does the same for all nodes in the tree by recursively calling itself for the 
    left and right children of `root`.

- **countPaths Function**: This helper function counts the number of paths that start from a given node and sum up to the target. 
    It uses a running sum (`currentSum`) to keep track of the sum along the current path. If `currentSum` equals `targetSum`, it 
    counts as a valid path. The function then recursively explores further down the left and right subtrees to find additional paths 
    that start from the current node.

### Complexity:

- **Time Complexity**: O(N^2) in the worst case, where N is the number of nodes in the tree. This worst-case scenario occurs in 
    an unbalanced tree where the function systematically explores all paths from each node.
- **Space Complexity**: O(H) for the recursion stack, where H is the height of the tree. In the worst case (a skewed tree), 
    the space complexity will be O(N).

*/
