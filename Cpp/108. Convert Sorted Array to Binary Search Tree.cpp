// 108. Convert Sorted Array to Binary Search Tree.

// Topic: Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree


/*
### Task:
---
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 
Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in a strictly increasing order.


### Testcase:
---
[-10,-3,0,5,9]
[1,3]


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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    // Helper function to construct BST from nums[start..end]
    TreeNode* sortedArrayToBST(vector<int>& nums, int start, int end) {
        if (start > end) return nullptr; // Base case: no elements to form a subtree

        // Middle element to maintain height balance
        int mid = start + (end - start) / 2;

        // Create root node with middle element
        TreeNode* node = new TreeNode(nums[mid]);

        // Recursively construct left subtree from left half of the current segment
        node->left = sortedArrayToBST(nums, start, mid - 1);

        // Recursively construct right subtree from right half of the current segment
        node->right = sortedArrayToBST(nums, mid + 1, end);

        return node; // Return the constructed subtree rooted at 'node'
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        // Call helper function with the whole range of nums
        return sortedArrayToBST(nums, 0, nums.size() - 1);
    }
};


// Description: ===================================
/*
To convert a sorted array to a height-balanced binary search tree (BST), we can use a divide and conquer approach, 
similar to binary search. The key idea is to select the middle element of the array as the root of the BST, which 
ensures that the tree remains height-balanced. The elements to the left of the middle element will form the left 
subtree, and the elements to the right will form the right subtree. By recursively applying this strategy, we can 
construct a height-balanced BST.



### Description of the Solution:

1. **Recursive Approach**: The solution utilizes a recursive helper function that constructs a BST from a segment 
     of the `nums` array defined by `start` and `end` indices.

2. **Selecting the Root**: For each call to the helper function, the middle element of the current segment is 
     selected as the root of the subtree to ensure the BST remains height-balanced.

3. **Constructing Subtrees**: The array is effectively divided into two halves around the middle element. The 
     left half is used to recursively construct the left subtree, and the right half is used to construct the 
     right subtree.

4. **Base Case**: The recursion terminates when the `start` index exceeds the `end` index, indicating there are 
     no elements left to include in the subtree, at which point `nullptr` is returned.

5. **Building the Tree**: Starting with the entire array, the function recursively constructs the BST, splitting 
     the array around the selected root for each subtree until the base case is reached.

6. **Returning the Result**: The initial call to the helper function starts with the full range of the array, and 
     the root of the fully constructed BST is returned as the final result.

This approach ensures that the constructed BST is height-balanced, as it consistently selects the middle element 
as the root, thereby minimizing the maximum depth of the tree.

*/
