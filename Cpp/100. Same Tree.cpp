// 100. Same Tree.


// Topic: Tree, Depth-First Search, Breadth-First Search, Binary Tree.


/*
### Task:
---
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4

### Testcase:
---
[1,2,3]
[1,2,3]
[1,2]
[1,null,2]
[1,2,1]
[1,1,2]


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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        
    }
};
*/

// Solution: --------------------------------------

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // Base case: both nodes are null, trees are identical at this point
        if (!p && !q) return true;

        // If one of the nodes is null, or the values don't match, trees are not identical
        if (!p || !q || p->val != q->val) return false;

        // Recursively check the left and right subtrees
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};

// Description: ===================================
/*
The "Same Tree" problem is a fundamental question in computer science focusing on the comparison of two binary trees. 
The task is to determine whether two binary trees are identical in structure and in node values. This problem is typically solved 
using tree traversal techniques such as Depth-First Search (DFS) or Breadth-First Search (BFS).

In the provided solution, a recursive DFS approach is employed to explore both trees simultaneously. The algorithm follows a 
straightforward logic:

1. **Base Case**: If both current nodes are `nullptr`, it signifies that we've reached the end of both branches simultaneously, 
     indicating that up to this point, the trees are structurally identical. Thus, the function returns `true`.

2. **Mismatch Detection**: The function checks for three conditions that would indicate a mismatch:
   - One node is `nullptr` while the other is not, indicating a structural difference.
   - The values of the two nodes differ, indicating a value mismatch.
   
   If any of these conditions are met, the function concludes that the trees are not the same and returns `false`.

3. **Recursive Exploration**: If neither base case nor mismatch conditions are met, the function recursively checks:
   - The left subtree of both trees.
   - The right subtree of both trees.
   
   The trees are considered the same if both the left subtrees and the right subtrees are identical, hence the recursive calls are 
   combined using a logical AND operation.

This method is efficient and succinct, with a time complexity of O(n), where n is the number of nodes in the smaller of the two trees. 
This is because, in the worst case, each node in both trees must be visited once. The space complexity is O(h), where h is the height 
of the deeper tree, due to the stack space used by the recursive calls. This solution elegantly leverages recursion to simplify the 
comparison process, making it a classic example of applying DFS for tree-related problems.

*/
