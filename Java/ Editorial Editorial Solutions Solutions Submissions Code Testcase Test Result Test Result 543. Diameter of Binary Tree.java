//  543. Diameter of Binary Tree.


// Topic: Tree, Depth-First Search, Binary Tree.


/*
### Task:
---
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-100 <= Node.val <= 100

### Testcase:
---
[1,2,3,4,5]
[1,2]

### Code:
---

// * Definition for a binary tree node.
// * public class TreeNode {
// *     int val;
// *     TreeNode left;
// *     TreeNode right;
// *     TreeNode() {}
// *     TreeNode(int val) { this.val = val; }
// *     TreeNode(int val, TreeNode left, TreeNode right) {
// *         this.val = val;
// *         this.left = left;
// *         this.right = right;
// *     }
// * }

class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        
    }
}
*/
// Solution: --------------------------------------


class Solution {
    int diameter = 0; // Global variable to store the diameter of the tree

    public int diameterOfBinaryTree(TreeNode root) {
        height(root); // Initialize the height calculation from the root
        return diameter;
    }

    private int height(TreeNode node) {
        if (node == null) return -1; // Base case: An empty tree has height -1
        
        int leftHeight = height(node.left); // Height of left subtree
        int rightHeight = height(node.right); // Height of right subtree
        
        // Update the diameter if the path through node is longer
        diameter = Math.max(diameter, 2 + leftHeight + rightHeight);

        // Return the height of the tree rooted at this node
        return 1 + Math.max(leftHeight, rightHeight);
    }
}


// Description: ===================================
/*
To solve the problem of finding the diameter of a binary tree, we will implement a depth-first search (DFS) strategy. The diameter of a tree is the length of the longest path between any two nodes, which may or may not pass through the root. The key insight is that for any node, the longest path through it is the sum of the heights of its left and right subtrees.

We will define a recursive helper function `height(TreeNode node)` that returns the height of a subtree rooted at `node`, and in the process, update the diameter. The diameter is maintained as a global variable, which is updated with the sum of the heights of the left and right subtrees at each node if that sum is greater than the current diameter.

Here's the detailed strategy:

1. **Base Case:** If the node is null, the height of the subtree is -1 (since we count the number of edges, and an empty tree has no edges).

2. **Recursive Step:** For each node, recursively find the height of its left and right subtrees.

3. **Update Diameter:** At each node, the potential diameter is the sum of the heights of the left and right subtrees. If this is greater than the current diameter, update the diameter.

4. **Return Height:** To facilitate the recursive calculation, each call to `height` returns the height of the tree rooted at the given node, which is 1 plus the maximum height of its left and right subtrees.

5. **Result:** The diameter is the maximum length found during the traversal.


**Description:**

- We start by calling the `height` function from the root of the binary tree.
- The `height` function computes the height of a tree in a depth-first manner and uses the heights of the left and right subtrees to compute the diameter at each node.
- The `diameter` is updated whenever a longer path is found. The path length is calculated as the sum of the heights of the left and right subtrees plus 2 (to account for the edges connecting the node to its children).
- Finally, the `diameterOfBinaryTree` function returns the maximum diameter found during the traversal.

*/
