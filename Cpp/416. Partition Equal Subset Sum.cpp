// 416. Partition Equal Subset Sum.

// Topic:Array, Dynamic Programming.

/*
### Task:
---
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements 
in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100


### Testcase:
---
[1,5,11,5]
[1,2,3,5]


### Code:
---
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        
        // If totalSum is odd, it's impossible to partition into two equal subsets
        if (totalSum % 2 != 0) return false;
        
        int subsetSum = totalSum / 2;
        vector<bool> dp(subsetSum + 1, false);
        dp[0] = true; // Base case: a subset sum of 0 is always possible
        
        // Dynamic programming to find if a subset with sum = subsetSum exists
        for (int num : nums) {
            for (int i = subsetSum; i >= num; --i) {
                dp[i] = dp[i] || dp[i - num];
            }
        }
        
        // If dp[subsetSum] is true, a valid partition exists
        return dp[subsetSum];
    }
};

// Description: ===================================
/*
To solve the "Partition Equal Subset Sum" problem, we can use a dynamic programming approach similar to the 0/1 Knapsack problem. 
The key idea is to determine if there's a subset of the given numbers that sums up to half of the total sum of all numbers in the 
array. If such a subset exists, then the remaining numbers form another subset with the same sum, thus achieving the partition.

First, we need to check if the total sum of the array is even because it's impossible to partition the array into two subsets 
with equal sums if the total sum is odd. If the total sum is even, we proceed to find a subset with a sum equal to half of the 
total sum.

This code snippet defines a `Solution` class with a `canPartition` function that takes an array of integers `nums` as input. 
It calculates the total sum of all numbers in `nums` and checks if it's even. If the total sum is odd, the function immediately 
returns `false`. Otherwise, it proceeds to check if there's a subset with a sum equal to half of the total sum.

The function initializes a boolean dynamic programming array `dp` of size `subsetSum + 1` and sets `dp[0] = true` as the base case, 
indicating that it's always possible to form a subset with sum 0. Then, for each number in `nums`, the function iterates backwards 
from `subsetSum` to the current number, updating `dp[i]` to be `true` if `dp[i]` was already `true` or if `dp[i - num]` was `true`, 
indicating that a subset with sum `i` is possible either with or without the current number.

If `dp[subsetSum]` is `true` at the end of the iterations, it means a subset with the required sum exists, and the function returns
`true`, indicating that the array can be partitioned into two subsets with equal sums.

*/
