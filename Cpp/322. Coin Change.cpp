// 322. Coin Change.

// Topic:Array, Dynamic Programming, Breadth-First Search.

/*
# Task:
You are given an integer array coins representing coins of different denominations and an integer amount 
representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be 
made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4

# Testcase:
[1,2,5]
11
[2]
3
[1]
0


# Code:
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        
    }
};

*/
// Solution:

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // Initialize dp array with amount+1, as this is more than the maximum possible number of coins
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0; // Base case: 0 coins are needed to make up the amount 0

        // Build up the solution for each amount from 1 to amount
        for (int i = 1; i <= amount; ++i) {
            for (int coin : coins) {
                // If it's possible to include this coin (i.e., i - coin >= 0)
                if (i - coin >= 0) {
                    // Update dp[i] to the minimum of its current value and 1 + dp[i - coin]
                    dp[i] = min(dp[i], 1 + dp[i - coin]);
                }
            }
        }

        // If dp[amount] is still amount + 1, then it was not possible to make up the amount
        return dp[amount] > amount ? -1 : dp[amount];
    }
};

// Description:
/*
To solve the "Coin Change" problem, we can use a dynamic programming approach. The idea is to build up a solution for the total 
amount from solutions for smaller amounts. We define `dp[i]` as the fewest number of coins needed to make up the amount `i`. 
If `i` can't be made up by any combination of the coins, `dp[i]` will be set to a value that indicates it's impossible (for example, 
`amount + 1` which is surely more than any possible number of coins needed).

This code snippet defines a `Solution` class with a `coinChange` function that takes an array of integers `coins` representing 
different coin denominations and an integer `amount` representing the total amount of money. It initializes a dynamic programming 
array `dp` with size `amount + 1` and fills it with `amount + 1` (indicating an impossible situation). The base case `dp[0] = 0` 
indicates that no coins are needed to make up the amount 0. The function then iterates through each amount from 1 to `amount`, and 
for each amount, it iterates through the available coins, updating `dp[i]` to the minimum number of coins needed to make up the 
amount `i`. If `dp[amount]` remains `amount + 1` after the iterations, it means it's impossible to make up the amount with the given 
coins, and the function returns -1. Otherwise, it returns `dp[amount]`, the minimum number of coins needed to make up the amount.

*/
