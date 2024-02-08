// 279. Perfect Squares.

// Topic: Math, Dynamic Programming, Breadth-First Search.

/*
# Task:
---------
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is 
the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 
Constraints:
1 <= n <= 10^4


# Testcase:
------------
12
13

# Code:
----------
class Solution {
public:
    int numSquares(int n) {
        
    }
};   

*/
// Solution:

class Solution {
public:
    int numSquares(int n) {
        // dp[i] will hold the least number of perfect square numbers which sum to i
        vector<int> dp(n + 1, INT_MAX); // Initialize with maximum int value
        dp[0] = 0; // Base case
        
        // Precompute all perfect squares less than or equal to n
        vector<int> squares;
        for(int i = 1; i * i <= n; ++i) {
            squares.push_back(i * i);
        }

        // Dynamic programming to fill up the dp array
        for(int i = 1; i <= n; ++i) {
            for(int square : squares) {
                if(i >= square) {
                    dp[i] = min(dp[i], dp[i - square] + 1);
                }
            }
        }

        return dp[n]; // The least number of perfect square numbers that sum to n
    }
};

// Description:
/*
To solve the problem of finding the least number of perfect square numbers that sum to `n`, we can use dynamic programming. The dynamic programming approach aims to break down this problem into smaller subproblems and use the results of the smaller problems to efficiently solve the larger problem.

We can define `dp[i]` as the least number of perfect square numbers that sum to `i`. Our goal is to find `dp[n]`.

The base case would be `dp[0] = 0` because the sum of zero perfect square numbers is 0. For each `i` from 1 to `n`, we can iterate through all perfect squares less than or equal to `i` and update `dp[i]` as the minimum of `dp[i]` and `dp[i - square] + 1`, where `square` is a perfect square number.

This code snippet defines a `Solution` class with a `numSquares` function that implements the dynamic programming approach to solve the problem. It initializes a `dp` array with size `n+1` and sets all elements to `INT_MAX` (representing infinity) because initially, we don't know the minimum number of squares that sum up to each number. It then sets the base case `dp[0] = 0` and precomputes all perfect squares up to `n` to avoid redundant calculations. Finally, it iterates through each number up to `n`, updating the `dp` array based on the previously computed values and the current perfect square numbers.
*/