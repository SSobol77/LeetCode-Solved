// 513. Find Bottom Left Tree Value.

// Topic: Tree, Depth-First Search, Breadth-First Search, Binary Tree.


/*
### Task:
---
Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:
Input: root = [2,1,3]
Output: 1

Example 2:
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1


### Testcase:
---
[2,1,3]
[1,2,3,4,null,5,6,null,null,7]


### Code:
---

// * Definition for a binary tree node.
// * struct TreeNode {
// *     int val;
// *     TreeNode *left;
// *     TreeNode *right;
// *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
// *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
// *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// * };

class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        
    }
};
*/
// Solution: --------------------------------------

class Solution {
public:
    // Finds the leftmost value in the bottom row of a binary tree.
    int findBottomLeftValue(TreeNode* root) {
        int maxDepth = -1; // Initialize maxDepth to keep track of the deepest level reached so far.
        int leftMostValue = 0; // To store the leftmost value at the deepest level.
        
        // Start DFS from the root, with the current depth as 0.
        findBottomLeftValueDFS(root, 0, maxDepth, leftMostValue);
        
        return leftMostValue; // Return the leftmost value found at the deepest level.
    }

private:
    // Helper function to perform DFS traversal.
    // node: current node in the DFS traversal
    // depth: current depth in the binary tree
    // maxDepth: reference to the maximum depth encountered during traversal
    // leftMostValue: reference to store the leftmost value at the deepest level
    void findBottomLeftValueDFS(TreeNode* node, int depth, int& maxDepth, int& leftMostValue) {
        if (node == nullptr) {
            return; // Base case: if the current node is null, return.
        }
        
        // If the current depth is greater than the maximum depth encountered so far,
        // update the maximum depth and the leftmost value.
        if (depth > maxDepth) {
            maxDepth = depth; // Update the maximum depth.
            leftMostValue = node->val; // Update the leftmost value at this new maximum depth.
        }
        
        // Recursive DFS call for the left child. Increment depth by 1.
        findBottomLeftValueDFS(node->left, depth + 1, maxDepth, leftMostValue);
        
        // Recursive DFS call for the right child. Increment depth by 1.
        findBottomLeftValueDFS(node->right, depth + 1, maxDepth, leftMostValue);
    }
};



// Description: ===================================
/*
The solution to find the bottom left value in the last row of a binary tree employs a depth-first search (DFS) strategy, 
which is both efficient and straightforward to implement. Here’s a detailed explanation of how the solution works:

### Approach Overview
The primary goal is to traverse the binary tree to identify the leftmost value at the deepest level. To achieve this, 
the solution involves a recursive DFS function that traverses the tree while keeping track of the current depth and 
updating the maximum depth encountered along with the corresponding leftmost value.

### Key Components
- **Maximum Depth Tracking**: A variable (`maxDepth`) is maintained to keep track of the deepest level reached during the traversal. Initially set to an invalid value (e.g., -1), this variable is updated whenever a deeper level is reached.
- **Leftmost Value Storage**: Another variable (`leftMostValue`) holds the value of the leftmost node at the deepest level encountered so far. This is the value we ultimately want to return.
- **Depth-First Search (DFS) Function**: A helper function (`findBottomLeftValueDFS`) is employed to perform the DFS traversal. This function is recursive, taking the current node and its depth as arguments, along with references to `maxDepth` and `leftMostValue` for tracking purposes.

### Solution Steps
1. **Initialization**: The solution begins by initializing `maxDepth` and `leftMostValue` and then calling the DFS helper function with the root node and an initial depth of 0.
2. **Recursive Traversal**: The DFS function recursively traverses the tree. At each node, it checks if the current depth exceeds `maxDepth`. If so, it updates `maxDepth` to the current depth and sets `leftMostValue` to the value of the current node, as this node is now the new leftmost node at the deepest level found so far.
3. **Depth Increment**: As the function traverses down the tree, it increments the depth by 1 for each level it descends.
4. **Left and Right Subtrees**: The function first traverses the left subtree and then the right subtree. This order ensures that if the leftmost value at the maximum depth is updated, it accurately reflects the leftmost node at that depth.
5. **Base Case**: The base case for the recursion is when the function encounters a `nullptr`, indicating that it has reached a leaf node or the end of a branch. At this point, the function returns, unwinding the recursion stack.

### Conclusion
Once the entire tree has been traversed, `leftMostValue` contains the value of the leftmost node at the deepest level of the tree. 
This value is then returned as the final result. The use of DFS ensures that the solution is efficient, with a time complexity proportional 
to the number of nodes in the tree, and it avoids the extra space that would be required for a breadth-first search implementation, making 
it an optimal solution for this problem.

*/
