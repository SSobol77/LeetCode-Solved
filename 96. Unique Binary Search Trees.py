# 96. Unique Binary Search Trees.

# Topic: Math, Dynamic Programming, Tree, Binary Search Tree, Binary Tree

'''
# Task:
-------
Given an integer n, return the number of structurally unique BST's (binary search trees) 
which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 19

# Testcase:
------------
3
1

# Code:
------------
class Solution:
    def numTrees(self, n: int) -> int:
        
'''
# Solution:
class Solution:
    def numTrees(self, n: int) -> int:
        # Base case: If n is less than 2, the number of unique BSTs is 1
        if n < 2:
            return 1

        # Initialize the dynamic programming table
        # dp[i] will hold the number of unique BSTs that can be formed with i nodes
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1  # With 0 or 1 node, there is only 1 unique BST

        # Calculate the number of unique BSTs for each number up to n
        for i in range(2, n + 1):
            # Loop through all possible root nodes for the BST
            # We only go up to half (i // 2) because of symmetry
            for j in range(1, i // 2 + 1):
                # Add the number of BSTs formed by the left and right subtrees
                # dp[j - 1] is the number of BSTs for the left subtree
                # dp[i - j] is the number of BSTs for the right subtree
                dp[i] += dp[j - 1] * dp[i - j]

            # Double the count since we only calculated one half (symmetry)
            dp[i] *= 2

            # If i is odd, add the middle combination (which isn't doubled)
            if i % 2 == 1:
                mid = i // 2
                dp[i] += dp[mid] * dp[mid]

        # Return the total number of unique BSTs for n nodes
        return dp[n]

# Description:
'''
To solve the problem of counting the number of structurally unique BSTs (Binary Search Trees) for a given n, 
we can use dynamic programming. This problem is a classic example of the Catalan number, a sequence of natural 
numbers that have applications in combinatorial mathematics.

The number of unique BSTs for a given n is the nth Catalan number, calculated using the formula:
Cn= 1/(n+1)*(2n/n)

Alternatively, it can be calculated using dynamic programming where each C[i] is computed as the 
sum of C[j-1] * C[i-j] for j from 1 to i.

In this code:

The dynamic programming table dp is used to store the number of unique BSTs that can be created with i nodes.
We handle the cases where n is 0 or 1 at the beginning since there's only one possible BST in these cases.
For each i from 2 to n, we use a for-loop to calculate the number of unique BSTs. The inner loop goes up 
to i // 2 to leverage the symmetry in the problem (the number of trees formed with j as the root is the
same as the number of trees formed with i - j as the root).
We double the result of the inner loop's computation since it only covers half of the cases due to symmetry.
For odd values of i, we handle the middle combination separately, as it's not symmetrical.
The final result dp[n] is the total number of unique BSTs that can be formed with n nodes.

'''