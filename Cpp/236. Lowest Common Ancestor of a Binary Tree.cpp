// 236. Lowest Common Ancestor of a Binary Tree.


// Topic: Tree, Depth-First Search, Binary Tree


/*
### Task:
---
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p 
and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the tree.


### Testcase:
---
[3,5,1,6,2,0,8,null,null,7,4]
5
1
[3,5,1,6,2,0,8,null,null,7,4]
5
4
[1,2]
1
2


### Code:
---
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 *//*
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
    }
};
*/

// Solution: --------------------------------------

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // Base case: if root is NULL, or root is one of p or q, return root
        if (root == NULL || root == p || root == q) {
            return root;
        }

        // Search for p and q in the left and right subtrees
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);

        // If both left and right are non-NULL, p and q are found in different subtrees, root is the LCA
        if (left != NULL && right != NULL) {
            return root;
        }

        // If only one of the subtrees contains p or q, return that subtree's LCA result
        // If neither subtree contains p or q, return NULL (left and right will both be NULL)
        return left != NULL ? left : right;
    }
};


// Description: ===================================
/*
To find the Lowest Common Ancestor (LCA) of two given nodes in a binary tree, we can use a recursive approach. The idea is 
to traverse the tree starting from the root and use the properties of a binary tree to find the LCA. 

We will perform a depth-first search (DFS) and at each step, we will consider three cases:

1. If the current node is `NULL`, we return `NULL` since there's no LCA possible in an empty subtree.
2. If the current node matches either of the two nodes (`p` or `q`), we return the current node. This is because if one of 
   the nodes is an ancestor of the other, it should be considered the LCA.
3. Otherwise, we recursively search for the LCA in the left and right subtrees.

After the recursive calls, there are three possible outcomes:
- Both calls returned a non-NULL value, which means each of the nodes `p` and `q` were found in different subtrees. Thus, 
  the current node is their LCA.
- Only one of the calls returned a non-NULL value, meaning both `p` and `q` are located in the same subtree. The value 
  returned by the call is the LCA.
- Both calls returned NULL, indicating that neither `p` nor `q` were found in the current subtree. We return NULL in this case.

### Description:

This solution defines a `Solution` class with a public function `lowestCommonAncestor` to find the LCA of two given nodes in a 
binary tree. The function uses recursion to traverse the tree and determine the LCA based on the properties of the binary tree 
and the definition of LCA. The key to this solution is understanding that the LCA of two nodes in a binary tree is the lowest 
node that has both nodes as descendants, considering that a node can be a descendant of itself. This approach ensures that the 
function efficiently finds the LCA with a time complexity of O(n), where n is the number of nodes in the tree, and a space 
complexity of O(h), where h is the height of the tree, due to the recursion stack.

*/
