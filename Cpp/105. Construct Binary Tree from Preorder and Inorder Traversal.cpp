// 105. Construct Binary Tree from Preorder and Inorder Traversal.


// Topic: Array, Hash Table, Divide and Conquer, Tree, Binary Tree.

/*
### Task:
---
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.


### Testcase:
---
[3,9,20,15,7]
[9,3,15,20,7]
[-1]
[-1]


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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        
    }
};
*/
// Solution: --------------------------------------

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
    // Hash table to store the indices of each value in the inorder array for quick lookup.
    unordered_map<int, int> inorderMap;

    // Helper function to recursively build the binary tree.
    TreeNode* buildTreeHelper(vector<int>& preorder, int preorderStart, int preorderEnd, vector<int>& inorder, int inorderStart, int inorderEnd) {
        // Base case: when there are no elements to construct the subtree.
        if (preorderStart > preorderEnd || inorderStart > inorderEnd) return nullptr;

        // The first element in the current preorder segment is the root of the subtree.
        TreeNode* root = new TreeNode(preorder[preorderStart]);

        // Retrieve the index of the root from the inorder array using the hash table.
        int inorderRootIndex = inorderMap[root->val];
        // Calculate the number of nodes in the left subtree to split the preorder array accordingly.
        int numsLeft = inorderRootIndex - inorderStart;

        // Recursively build the left subtree using the left segment of the preorder and inorder arrays.
        root->left = buildTreeHelper(preorder, preorderStart + 1, preorderStart + numsLeft, inorder, inorderStart, inorderRootIndex - 1);
        // Recursively build the right subtree using the right segment of the preorder and inorder arrays.
        root->right = buildTreeHelper(preorder, preorderStart + numsLeft + 1, preorderEnd, inorder, inorderRootIndex + 1, inorderEnd);

        // Return the constructed subtree rooted at 'root'.
        return root;
    }

public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        // Populate the hash table with indices of inorder elements for O(1) lookup.
        for (int i = 0; i < inorder.size(); ++i) {
            inorderMap[inorder[i]] = i;
        }

        // Start the recursive tree construction using the entire range of preorder and inorder arrays.
        return buildTreeHelper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }
};



// Description: ===================================
/*
To enhance the understanding of the solution, I will insert precise and detailed comments within the code. 
These comments will explain the purpose of each significant part of the code and how it contributes to constructing 
the binary tree from preorder and inorder traversal arrays.

### Enhanced Comments Explanation:

- **Hash Table Initialization**: The comment explains the purpose of the `inorderMap` hash table, which is to store the indices of elements from the inorder traversal for quick access during tree construction.

- **Recursive Helper Function**: The `buildTreeHelper` function is annotated to describe its role in recursively building the binary tree. It includes the base case scenario where the recursion ends, and it clarifies how the root of the subtree is determined from the preorder array.

- **Root Identification**: The comment details the process of identifying the root node for the current subtree and finding its index in the inorder array using the hash table, which is crucial for dividing the tree into left and right subtrees.

- **Subtree Construction**: The recursive calls for constructing the left and right subtrees are explained, highlighting how the segments of the preorder and inorder arrays are chosen based on the number of nodes in the left subtree.

- **Main Function Logic**: In the `buildTree` function, the comment clarifies the initialization of the hash table with the inorder array's elements. It also describes the initiation of the recursive process to construct the binary tree using the full range of the preorder and inorder arrays.

These comments aim to provide a clear understanding of each step involved in constructing the binary tree from the given preorder and inorder traversal arrays, following the divide and conquer approach.


The algorithm to construct a binary tree from given preorder and inorder traversal arrays involves a divide and conquer approach, leveraging the unique properties of tree traversals. Here's a step-by-step description of the algorithm:



### Algorithm Description:

1. **Initialize a Hash Table**: Create a hash table (also known as a map or dictionary in some languages) to store the indices of elements from the inorder array. This allows for O(1) lookup times when finding the position of an element in the inorder array, which is crucial for efficiently identifying the root and dividing the tree into left and right subtrees.

2. **Define a Recursive Helper Function**: Implement a recursive function, `buildTreeHelper`, that takes subsets of the preorder and inorder arrays as arguments, along with their respective start and end indices. This function will construct the binary tree and return the root node of the constructed subtree.

3. **Identify the Root Node**: For each recursive call, the first element in the current subset of the preorder array represents the root node of the subtree being constructed. Create a new tree node with this value.

4. **Locate the Root in the Inorder Array**: Use the hash table to find the index of the current root node in the inorder array. This index divides the inorder array into elements that belong to the left subtree and elements that belong to the right subtree.

5. **Divide into Left and Right Subtrees**:
    - Calculate the number of elements in the left subtree as the difference between the root's index in the inorder array and the start index of the current inorder subset.
    - Recursively call `buildTreeHelper` for the left subtree using the next element in the preorder array and the corresponding subset of the inorder array that represents the left subtree.
    - Similarly, recursively call `buildTreeHelper` for the right subtree, adjusting the indices to use the remaining elements in the preorder array and the corresponding subset of the inorder array for the right subtree.

6. **Reconstruct the Tree**: Connect the left and right subtrees to the current root node. This step is part of the post-processing work of each recursive call.

7. **Handle Base Cases**: If the current subset of the preorder or inorder array is empty (indicated by the start index being greater than the end index), return `nullptr`. This condition serves as the base case for the recursion, ensuring the function terminates.

8. **Initiate the Recursive Construction**: Call the `buildTreeHelper` function with the entire preorder and inorder arrays to start the recursive construction of the binary tree. This initial call will construct the entire tree and return the root node of the tree.

9. **Return the Constructed Tree**: The final result of the initial call to the helper function is the root node of the fully constructed binary tree, which is then returned as the final output of the algorithm.


### Key Concepts:

- **Preorder Array**: The first element is always the root of the tree or subtree, providing a straightforward way to identify roots at each stage of the recursion.
- **Inorder Array**: Divides the tree into left and right subtrees, allowing the algorithm to determine which elements belong to each subtree.
- **Divide and Conquer**: The tree is constructed recursively by dividing the problem into smaller subproblems (subtrees) and combining their solutions (connecting subtrees to their roots).

This algorithm efficiently constructs the binary tree by utilizing the unique properties of preorder and inorder traversals, with the aid of a hash table for quick index lookups in the inorder array.

*/
