// 121. Best Time to Buy and Sell Stock.

// Topic: Array, Dynamic Programming.

/*
### Task:
---
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4

### Testcase:
---
[7,1,5,3,6,4]
[7,6,4,3,1]

### Code:
---
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = INT_MAX; // Initialize minPrice to a very high value
        int maxProfit = 0; // Initialize maxProfit to 0
        
        // Iterate through the prices array
        for (int i = 0; i < prices.size(); i++) {
            // Update minPrice if the current price is lower than the minPrice seen so far
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            } 
            // Update maxProfit if the current profit (current price - minPrice) is greater than the maxProfit seen so far
            else if (prices[i] - minPrice > maxProfit) {
                maxProfit = prices[i] - minPrice;
            }
        }
        
        // Return the maximum profit that can be achieved
        return maxProfit;
    }
};


// Description: ===================================
/*
To solve the "Best Time to Buy and Sell Stock" problem, we can use a simple one-pass approach that iterates through the array 
while keeping track of the minimum price seen so far and the maximum profit that can be achieved. This approach falls under 
the category of dynamic programming because it involves breaking down the problem into smaller subproblems and solving them 
in a way that avoids redundant calculations.


### Description:

- **minPrice**: This variable keeps track of the minimum price seen so far as we iterate through the array. Initially, it is set 
   to `INT_MAX` to ensure that the first price in the array will be considered as the minimum price.

- **maxProfit**: This variable keeps track of the maximum profit that can be achieved. It is initialized to 0 because the minimum 
   profit you can earn is 0 (i.e., if you don't make any transaction or if the prices are in descending order).

- The loop iterates through each price in the `prices` array. For each price, it checks if the current price is lower than `minPrice`.
   If it is, `minPrice` is updated to the current price. This ensures that we always know the lowest price at which we could have bought 
   the stock so far.

- If the current price is not lower than `minPrice`, the algorithm checks if selling the stock at the current price (after buying 
  it at `minPrice`) would result in a higher profit than `maxProfit`. If it would, `maxProfit` is updated to this new profit value.

- After iterating through all prices, `maxProfit` will contain the maximum profit that could have been achieved, and it is returned 
  as the result.

This solution has a time complexity of O(n), where n is the number of days (or the length of the `prices` array), because it only 
requires a single pass through the array. The space complexity is O(1) because only two variables (`minPrice` and `maxProfit`) are 
used, and their space requirement does not depend on the size of the input array.

*/
