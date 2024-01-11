# 121. Best Time to Buy and Sell Stock.

# Topic: Array, Dynamic Programming.

"""
## Task:
---------
You are given an array prices where prices[i] is the price of a given stock on the i^th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in 
the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

#Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

#Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4

## Testcase:
-------------
[7,1,5,3,6,4]
[7,6,4,3,1]

## Code:
----------
class Solution:
    def maxProfit(self, prices: List[int]) -> int:   

"""
# Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]  # Initialize the minimum price to the first day's price
        max_profit = 0  # Initialize the maximum profit to 0
        
        for price in prices:
            # Update the minimum price if a lower price is encountered
            min_price = min(min_price, price)
            
            # Calculate the profit if selling at the current price
            profit = price - min_price
            
            # Update the maximum profit if the current profit is greater
            max_profit = max(max_profit, profit)
        
        return max_profit


# Description
'''
To solve this problem, you can use a simple dynamic programming approach. The idea is to keep track of the minimum
price you've seen so far while iterating through the prices array. Then, for each day, you can calculate the profit 
you would make if you sold the stock on that day (the current price minus the minimum price seen so far), and update 
the maximum profit accordingly.

You can call the maxProfit method of the Solution class with the prices list as an argument to get the maximum profit. 
This algorithm has a time complexity of O(n) where n is the length of the prices array, making it efficient for large 
input arrays.

'''
