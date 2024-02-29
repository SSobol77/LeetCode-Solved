// 1609. Even Odd Tree.

// Topic: Tree, Breadth-First Search, Binary Tree.

/*
### Task:
---
A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

Example 1:
Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
Explanation: The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.

Example 2:
Input: root = [5,4,2,3,3,7]
Output: false
Explanation: The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.

Example 3:
Input: root = [5,9,1,3,5,7]
Output: false
Explanation: Node values in the level 1 should be even integers.

Constraints:
The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 10^6

Hint 1:
Use the breadth-first search to go through all nodes layer by layer.

### Testcase:
---
[1,10,4,3,null,7,9,12,8,6,null,null,2]
[5,4,2,3,3,7]
[5,9,1,3,5,7]

### Code:
---
// Definition for a binary tree node.
// struct TreeNode {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };

class Solution {
public:
    bool isEvenOddTree(TreeNode* root) {
        
    }
};

*/

// Solution: ----------------------------------------------------------------------------------------------------

class Solution {
public:
    bool isEvenOddTree(TreeNode* root) {
        // Return true for empty trees (vacuously true)
        if (!root) return true;
        
        // Queue to hold pairs of TreeNode and its level
        queue<pair<TreeNode*, int>> q;
        // Start with the root node at level 0
        q.push({root, 0});
        
        // Continue until there are no more nodes to process
        while (!q.empty()) {
            int levelSize = q.size(); // Number of nodes at the current level
            // Initialize prevValue based on the parity of the level
            // For even levels, we start with the smallest possible value (INT_MIN)
            // For odd levels, we start with the largest possible value (INT_MAX)
            int prevValue = (q.front().second % 2 == 0) ? INT_MIN : INT_MAX;
            
            // Process all nodes at the current level
            for (int i = 0; i < levelSize; ++i) {
                auto [node, level] = q.front(); q.pop();
                
                // Check if the node value violates the even-odd level rule
                // Even levels should have odd values, and odd levels should have even values
                if (level % 2 == node->val % 2) return false;
                
                // Check for strictly increasing (even levels) or decreasing (odd levels) order
                // For even levels, the current value must be greater than the previous
                // For odd levels, the current value must be less than the previous
                if ((level % 2 == 0 && (node->val <= prevValue)) || (level % 2 != 0 && (node->val >= prevValue))) return false;
                
                // Update the previous value for the next node comparison
                prevValue = node->val;
                
                // Enqueue the left child if it exists, along with its level (current level + 1)
                if (node->left) q.push({node->left, level + 1});
                // Enqueue the right child if it exists, along with its level
                if (node->right) q.push({node->right, level + 1});
            }
        }
        
        // If all levels satisfy the conditions, the tree is an Even-Odd tree
        return true;
    }
};


// Description: ===========================================================================================================
/*
To solve the problem of determining if a binary tree is an Even-Odd tree, we can use a breadth-first search (BFS) strategy. 
This involves iterating through the tree level by level and checking the values of the nodes at each level against the conditions 
specified for Even-Odd trees.

Here's a step-by-step approach:

1. **Initialize**: Start with a queue to facilitate BFS and enqueue the root node along with its level information (starting from 0).

2. **BFS Iteration**: While the queue is not empty, repeatedly dequeue nodes and process them. For each node processed, enqueue its 
     children (if any) along with their level information.

3. **Level-wise Processing**: For each level, we need to check two conditions based on whether the level is even or odd:
    - For even-indexed levels, nodes must contain odd values in strictly increasing order.
    - For odd-indexed levels, nodes must contain even values in strictly decreasing order.

4. **Validation Checks**:
    - Ensure that values at even levels are odd and vice versa.
    - Compare each node's value with the previous node's value in the same level to ensure strict ordering (increasing for even levels, 
    decreasing for odd levels).

5. **Edge Cases**: Pay attention to edge cases, such as levels with a single node, to ensure that the strict ordering condition is not 
falsely violated.

6. **Result**: If all levels satisfy their respective conditions, return `true`; otherwise, return `false`.

This solution iterates through each node exactly once, making the time complexity \(O(N)\), where \(N\) is the number of nodes in the tree.
The space complexity is also \(O(N)\) due to the queue used for BFS, which in the worst case might contain all nodes at the last level of 
a perfectly balanced tree.

*/
