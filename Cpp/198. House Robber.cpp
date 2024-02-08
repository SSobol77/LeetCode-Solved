// 198. House Robber.

// Topic: Array, Dynamic Programming.

/*
# Task:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money 
stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems 
connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you 
can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400


# Testcase:
[1,2,3,1]
[2,7,9,3,1]


# Code:
class Solution {
public:
    int rob(vector<int>& nums) {
        
    }
};

*/
//Solution:  ---------------------------------------------

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        
        // Vector to store the maximum amount robbed up to each house
        vector<int> dp(n, 0);
        dp[0] = nums[0]; // Base case: only one house to rob
        dp[1] = max(nums[0], nums[1]); // Base case: maximum of robbing the first or the second house

        // Fill in the dp array with the maximum amount of money that can be robbed up to each house
        for (int i = 2; i < n; ++i) {
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2]);
        }

        // The last element of dp array will have the maximum amount of money that can be robbed
        return dp[n - 1];
    }
};

// Description:
/*
To solve the "House Robber" problem, we can use a dynamic programming approach. The key idea is to create a decision at each house:
whether to rob it or not, based on maximizing the amount of money robbed up to that point without triggering the alarm.

We can define `dp[i]` as the maximum amount of money that can be robbed up to the `i-th` house. 

For each house `i`, there are two options:
1. Rob house `i`: In this case, we cannot rob house `i-1`, so the maximum money is the money from house `i` plus the maximum 
   amount robbed up to house `i-2`, i.e., `nums[i] + dp[i-2]`.
2. Do not rob house `i`: The maximum money is the same as the maximum amount robbed up to house `i-1`, i.e., `dp[i-1]`.

The `dp` array is updated as follows: `dp[i] = max(dp[i-1], nums[i] + dp[i-2])`.

This code snippet defines a `Solution` class with a `rob` function that takes an array of integers `nums` as input, 
where `nums[i]` represents the amount of money stashed in the `i-th` house. The function initializes a dynamic programming 
array `dp` to keep track of the maximum amount of money that can be robbed up to each house. It then iterates through each house, 
updating the `dp` array according to the described logic, and finally returns the maximum amount of money that can be robbed, which 
is stored in `dp[n - 1]`.

*/