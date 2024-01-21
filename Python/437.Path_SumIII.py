# 437. Path Sum III

# Topic: Tree,Depth-First Search, Binary Tree.

"""
## Task:
---------
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum 
of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling 
only from parent nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-10^9 <= Node.val <= 10^9
-1000 <= targetSum <= 1000


## Testcase:
-------------
[10,5,-3,3,2,null,11,3,-2,null,1]
8
[5,4,8,11,null,13,4,7,2,null,null,5,1]
22


## Code:
----------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        

"""
# Solution
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, currSum):
            # Base case: if the current node is null, return 0 (no path)
            if not node:
                return 0

            # Add the value of the current node to the running sum
            currSum += node.val

            # Check if there's a previous running sum that, when subtracted from the current sum,
            # equals the target. This means a valid path is found
            pathCount = prefixSums.get(currSum - targetSum, 0)

            # If the current running sum equals the target, increment path count
            if currSum == targetSum:
                pathCount += 1

            # Store the current running sum in the hash table or increment its count if already exists
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1

            # Recursively call dfs for left and right children, and add their path counts
            pathCount += dfs(node.left, currSum)
            pathCount += dfs(node.right, currSum)

            # Backtrack: remove the current running sum from the hash table before going up the recursive stack
            prefixSums[currSum] -= 1

            # Return the total number of paths found from this node
            return pathCount

        # Hash table to store the frequency of prefix sums
        prefixSums = {}
        # Start DFS from the root with an initial sum of 0
        return dfs(root, 0)


# Description
'''
This code implements the DFS approach to find the number of paths that sum up to a given target in a binary tree. 
It uses a hash table to keep track of the running sums at each node and calculates the number of valid paths accordingly. 
The comments explain each step of the process for clarity.

To solve the "Path Sum III" problem, we need to count the number of paths in a binary tree where the sum of the values 
along the path equals a given target sum. These paths can start and end anywhere in the tree, but they must go downwards, 
from parent nodes to child nodes. We can approach this problem using Depth-First Search (DFS).

## Approach:
-------------
1. **Traverse Each Node**: Start at the root and explore each node in the tree. At each node, we will calculate the number 
     of valid paths that include this node.

2. **Calculate Paths for Each Node**: For each node, we calculate the number of paths that sum up to the target sum. This 
     involves considering all possible paths starting from the current node and going downwards.

3. **Recursive DFS**: Use DFS recursively to explore all child nodes (left and right) of the current node.

4. **Path Count Calculation**:
   - When at a node, we keep a running sum which adds the value of the current node.
   - We check if the running sum equals the target sum. If so, we increment our path count.
   - Additionally, we must consider paths that start from the middle of the tree. To handle this, we can use a hash table 
     to store the frequency of all running sums. If at any point, `runningSum - targetSum` exists in the hash table, it means 
     there is a sub-path (ending at the current node) which sums up to the target sum.
     We add the frequency of `runningSum - targetSum` from the hash table to our path count.

5. **Backtracking**: After processing a node, backtrack by removing the current running sum from the hash 
     table (decrement its frequency) before returning to the parent node. This is important to ensure that only 
     paths from the top to the current node are considered when processing siblings of the current node.

6. **Edge Case**: If the tree is empty, simply return 0 as there are no paths to consider.


This solution has a time complexity of O(N) where N is the number of nodes in the tree, as it visits each node once. 
The space complexity is also O(N), primarily due to the recursion stack and the hash table used for storing prefix sums.

'''
