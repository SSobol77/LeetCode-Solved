// 124. Binary Tree Maximum Path Sum.


// Topic: Dynamic Programming, Tree, Depth-First Search, Binary Tree.


/*
### Task:
---
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000


### Testcase:
---
[1,2,3]
[-10,9,20,null,null,15,7]


### Code:
---
**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 *
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        
    }
};

*/

// Solution: ----------------------------------------------------------------------------------------------

#include <algorithm> // For std::max
using namespace std;

// Definition for a binary tree node.
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int maxSum = INT_MIN; // Initialize global max sum with the smallest integer value
        maxPathDown(root, maxSum); // Start DFS from the root
        return maxSum; // Return the global maximum path sum found
    }

private:
    // Helper function to recursively find the maximum path sum at each node
    int maxPathDown(TreeNode* node, int& maxSum) {
        if (node == nullptr) return 0; // Base case: If node is null, contribute 0 to the path sum

        // Recursively find the maximum path sum extending from the left child
        int left = max(0, maxPathDown(node->left, maxSum));
        // Recursively find the maximum path sum extending from the right child
        int right = max(0, maxPathDown(node->right, maxSum));

        // Update global max sum considering the current node as the root of a path including both children
        // This checks if including the node forms a path with a greater sum than the current maxSum
        maxSum = max(maxSum, left + right + node->val);

        // Return the maximum sum of a path going through the current node and extending upwards
        // This value will be used by the parent node to compute its maximum path sum
        return max(left, right) + node->val;
    }
};


// Description: ================================================================================================
/*
This code implements the described algorithm, efficiently calculating the maximum path sum in the given binary tree by considering 
all possible paths and updating a global maximum with the highest sum found during the traversal.

The algorithm for finding the maximum path sum in a binary tree involves a depth-first search (DFS) approach that calculates the 
maximum path sum for each node, considering both the continuation of the path upwards through the parent and the possibility of a 
path that spans from the left child, through the node, to the right child. The maximum path sum at each node is the maximum of the 
node's value itself, the node's value plus the maximum path sum from the left child, and the node's value plus the maximum path sum 
from the right child.

### Algorithm Description:

1. **Initialize a Global Variable:** Start with a global variable `maxSum` to keep track of the maximum path sum found during the 
     traversal of the tree. Initialize it with the smallest integer value to handle trees with negative path sums.

2. **Depth-First Search (DFS) Traversal:** Implement a helper function `maxPathDown(TreeNode* node, int& maxSum)` that traverses the 
     tree in a depth-first manner. This function calculates the maximum path sum for each node in a way that the path can either extend 
     upwards to the parent or include the maximum sums from both left and right children.

3. **Calculating Maximum Path Sum at Each Node:**
   - If the current node is `nullptr`, return 0 as the base case.
   - Recursively calculate the maximum path sum from the left and right children. If the calculated sum is negative, consider 
     it as 0 because including a negative path would reduce the overall sum.
   - Update `maxSum` if the sum of the current node's value and the maximum sums from both left and right children is greater 
     han the current `maxSum`. This considers the node as the root of a path that includes both children.
   - Return the maximum sum of a path going through the current node and extending upwards, which is used by the parent 
     node's calculation.

4. **Result:** The global variable `maxSum` will have the maximum path sum of the tree at the end of the traversal.

*/
