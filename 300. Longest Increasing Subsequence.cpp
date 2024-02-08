// 300. Longest Increasing Subsequence.

// Topic: Array, Binary Search, Dynamic Programming

/*
# Task:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

# Testcase:
[10,9,2,5,3,7,101,18]
[0,1,0,3,2,3]
[7,7,7,7,7,7,7]


# Code:
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        
    }
};

*/
// Solution:

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> tails; // Array to hold the smallest tail of all increasing subsequences

        for (int num : nums) {
            // Binary search to find the insertion point of num in tails
            auto it = lower_bound(tails.begin(), tails.end(), num);
            if (it == tails.end()) {
                // If num is greater than all elements in tails, append it to tails
                tails.push_back(num);
            } else {
                // If an element in tails is greater than or equal to num, replace it with num
                *it = num;
            }
        }

        // The size of tails will be the length of the longest increasing subsequence
        return tails.size();
    }
};

// Description:
/*
To solve the problem of finding the length of the longest strictly increasing subsequence (LIS) in an integer 
array `nums`, we can employ a dynamic programming approach that runs in \(O(n^2)\) time complexity. However, 
to achieve the follow-up challenge of reducing the time complexity to \(O(n \log n)\), we need to use a combination 
of binary search and a smart way of building the subsequence.

The \(O(n \log n)\) approach involves maintaining an array `tails`, where each element `tails[i]` represents the 
smallest tail of all increasing subsequences of length `i+1` in the array. We iterate through each number in `nums` 
and use binary search to find the position in `tails` where this number should be placed. The key idea is that if 
a number is larger than all tails, it extends the longest subsequence by one. If a number is smaller than some tails, 
it could potentially be a better candidate for a future sequence by providing a smaller tail.

This code snippet defines a `Solution` class with a `lengthOfLIS` function that takes an array of integers `nums` as 
input. It initializes an empty array `tails` to keep track of the smallest tail of all increasing subsequences. For 
each number in `nums`, it uses binary search (`lower_bound`) to find the appropriate position in `tails` where the 
number should be placed. If the number is larger than all elements in `tails`, it extends the `tails` array. If the 
number is smaller than some elements, it replaces the first element that is greater than or equal to it, potentially 
leading to a longer increasing subsequence in future iterations. The length of the `tails` array at the end of the 
iteration represents the length of the longest increasing subsequence.

*/
