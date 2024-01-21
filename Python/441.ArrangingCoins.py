"""
# 441. Arranging Coins

# Topic:


# Task:
---------------
You have n coins and you want to build a staircase with these coins. The staircase consists of k 
rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build. 

Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

Constraints:
1 <= n <= 2^31 - 1

# Testcase:
-------------
5
8

# Code:
--------------
class Solution:
    def arrangeCoins(self, n: int) -> int:
     
    
"""
# Solution:
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            mid = left + (right - left) // 2
            # Calculate the total coins required for 'mid' rows
            total = mid * (mid + 1) // 2

            if total == n:
                return mid
            elif total < n:
                left = mid + 1
            else:
                right = mid - 1

        # 'right' will be the number of complete rows that can be built
        return right

# Description:
'''
To solve the problem of finding the number of complete rows that can be built with n coins in 
a staircase pattern, we can use a binary search approach. This problem essentially boils down
to finding the maximum k such that the total number of coins used up to the k-th row is less 
than or equal to n.

The total number of coins used in a staircase of k rows is given by the sum of the first k natural
numbers, which is k * (k + 1) / 2.

Approach:
----------
    Initialize: Start with two pointers, left as 0 and right as n. The maximum possible height of the 
                staircase can't be more than n.

    Binary Search:
        While left <= right, calculate the mid-point mid.
        Compute the total number of coins required to build mid rows (mid * (mid + 1) / 2).
        Compare this number with n.
        If it's equal to or less than n, it means we can potentially build more rows, so move left to mid + 1.
        Otherwise, if it's more than n, it means we've built too many rows, so move right to mid - 1.

    Result: The result is right, as it will point to the largest k for which the sum is less than or equal to n when the loop exits

Explanation:
--------------
    Initialization of left and right: Sets the search range for the number of rows.
    While loop (binary search): Continues searching as long as left is less than or equal to right.
    Calculation of total: Computes the total coins required for mid rows.
    Comparison with n:
        If total is equal to n, mid is the exact number of rows that can be built.
        If total is less than n, more rows can potentially be built, so search in the higher half.
        If total is more than n, too many rows are built, so search in the lower half.
    Return right: The variable right will point to the maximum number of complete rows that can be built when the loop ends.

Complexity Analysis:
----------------------
    Time Complexity: O(log n), as the binary search halves the search space in each iteration.
    Space Complexity: O(1), as a constant amount of space is used.

'''

