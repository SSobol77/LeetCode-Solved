// 101. Symmetric Tree.


// Topic: Tree, Depth-First Search, Breadth-First Search, Binary.

/*
## Task:
---------
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?


## Testcase:
-------------
[1,2,2,3,4,4,3]
[1,2,2,null,3,null,3]


## Code:
------------
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
    bool isSymmetric(TreeNode* root) {
        
    }
};     

*/
// Solution 1:

// The recursive solution can be implemented:

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true; // An empty tree is symmetric
        return isMirror(root->left, root->right);
    }

private:
    bool isMirror(TreeNode* left, TreeNode* right) {
        if (!left && !right) return true; // Both nodes are null
        if (!left || !right) return false; // Only one of the nodes is null
        if (left->val != right->val) return false; // Node values are different

        // Check if the outer and inner pairs are symmetric
        return isMirror(left->left, right->right) && isMirror(left->right, right->left);
    }
};


/*
To check whether a binary tree is symmetric around its center, we can compare the left and right subtrees to ensure they are mirror images of each other. This can be done both recursively and iteratively. 

### Recursive Solution:
The recursive approach involves a helper function that takes two nodes to compare. Initially, it will be called with the left and right children of the root. The function will then check the following conditions for symmetry:
1. Both nodes are null, which is a base case for symmetry.
2. One node is null and the other is not, which breaks symmetry.
3. The values of the two nodes are different, which breaks symmetry.
4. Recursively check the outer and inner pairs of the subtrees: the left child of the left subtree with the right child of the right subtree, and the right child of the left subtree with the left child of the right subtree.

*/

// Solution2:
// The iterative solution using a queue:

```cpp
#include <queue>

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        std::queue<TreeNode*> q;
        q.push(root);
        q.push(root);

        while (!q.empty()) {
            TreeNode* t1 = q.front(); q.pop();
            TreeNode* t2 = q.front(); q.pop();

            if (!t1 && !t2) continue;
            if (!t1 || !t2) return false;
            if (t1->val != t2->val) return false;

            q.push(t1->left);
            q.push(t2->right);
            q.push(t1->right);
            q.push(t2->left);
        }

        return true;
    }
};

/*
### Iterative Solution:

The iterative approach can use a queue or stack to compare the nodes at each level. The idea is to enqueue or push two nodes at 
a time and then compare them, ensuring that they are symmetric. This process is then repeated for the children of these nodes, 
enqueuing them in opposite order (left child of the left node with right child of the right node, and vice versa).

Both solutions effectively check if the binary tree is symmetric around its center by comparing the left and right subtrees for 
mirror symmetry, either recursively or iteratively.

*/


