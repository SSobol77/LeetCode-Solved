// 230. Kth Smallest Element in a BST.


// Topic: Tree, Depth-First Search, Binary Search Tree, Binary Tree.


/*
### Task:
---
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of 
all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 10^4
0 <= Node.val <= 10^4
 
Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find 
the kth smallest frequently, how would you optimize?

Hint 1:
Try to utilize the property of a BST.
Hint 2:
Try in-order traversal. (Credits to @chan13)
Hint 3:
What if you could modify the BST node's structure?
Hint 4:
The optimal runtime complexity is O(height of BST).


### Testcase:
---
[3,1,4,null,2]
1
[5,3,6,2,4,null,null,1]
3


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
    int kthSmallest(TreeNode* root, int k) {
        
    }
};
*/


// Solution: --------------------------------------
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        int count = 0;  // Counter for the number of nodes processed
        int result = 0;  // Variable to store the kth smallest value

        // Recursive function to perform in-order traversal
        inorderTraversal(root, k, count, result);
        return result;
    }

private:
    void inorderTraversal(TreeNode* node, int k, int &count, int &result) {
        if (node == nullptr) return;  // Base case: if the node is null, return

        // Recurse on the left child
        inorderTraversal(node->left, k, count, result);

        // Process the current node
        ++count;  // Increment the count of nodes visited
        if (count == k) {  // If count equals k, we've found the kth smallest element
            result = node->val;  // Update the result with the current node's value
            return;  // No need to continue further
        }

        // Recurse on the right child
        inorderTraversal(node->right, k, count, result);
    }
};




// Description: ===================================
/*

To resolve the compile error due to the redefinition of `TreeNode`, we'll assume that the `TreeNode` structure is already 
defined in the environment you're working in, typically provided in online coding platforms like LeetCode. Therefore, we 
won't redefine `TreeNode` but use the existing definition.

### Description:

This solution defines a `Solution` class with a public function `kthSmallest` that returns the kth smallest element in a 
Binary Search Tree (BST). The function utilizes an in-order traversal strategy to explore the tree nodes in ascending order, 
relying on the BST property that in-order traversal yields nodes in a sorted sequence.

### Algorithm:

1. **Initialization**: Start with a count set to 0 and a variable to store the result. These variables will be updated during the traversal.

2. **In-Order Traversal**: Define a private helper function, `inorderTraversal`, which will perform an in-order traversal of the tree. The function will recursively visit left children, process the current node, and then visit right children.

   - **Visiting Left Child**: The function first calls itself on the left child of the current node. This ensures that the nodes are visited in ascending order.

   - **Processing Current Node**: Upon returning from the left subtree (or if the left child is null), the current node is processed. Increment the count of nodes visited. If the count equals `k`, the current node's value is the kth smallest, and it's stored in the result variable.

   - **Visiting Right Child**: The function then proceeds to the right child, continuing the in-order traversal.

3. **Base Case**: The base case for the recursion is when the current node is null. In this case, the function simply returns, as there's nothing to process.

4. **Result**: Once the traversal is complete, and the kth smallest element has been found, the value stored in the result variable is returned by the `kthSmallest` function.

This approach efficiently finds the kth smallest element by leveraging the sorted nature of the BST, with a time complexity of O(k) for reaching the kth smallest element and a space complexity of O(h), where h is the height of the tree, to account for the recursion stack.


*/
