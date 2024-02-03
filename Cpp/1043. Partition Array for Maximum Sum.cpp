// 1043. Partition Array for Maximum Sum.


// Topic: Array, Dynamic Programming.

/*
### Task:
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]

Example 2:
Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83

Example 3:
Input: arr = [1], k = 1
Output: 1

Constraints:
1 <= arr.length <= 500
0 <= arr[i] <= 10^9
1 <= k <= arr.length

Hint 1:
Think dynamic programming: dp[i] will be the answer for array A[0], ..., A[i-1].
Hint 2:
For j = 1 .. k that keeps everything in bounds, dp[i] is the maximum of dp[i-j] + max(A[i-1], ..., A[i-j]) * j .


### Testcase:
[1,15,7,9,2,5,10]
3
[1,4,1,5,7,3,6,1,9,9,3]
4
[1]
1


### Code:
class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        
    }
};


*/
// Solution:

#include <vector>
#include <algorithm>  // Include algorithm library for using max function

using namespace std;

class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n = arr.size();  // Get the size of the input array
        vector<int> dp(n + 1, 0);  // Initialize DP array with n+1 elements, all set to 0

        // Iterate over the array to fill in the DP table
        for (int i = 1; i <= n; ++i) {
            int maxElement = 0;  // Initialize the max element in the current subarray to 0
            int maxSum = 0;  // Initialize the maximum sum for the current position

            // Consider all possible lengths of the last subarray up to k
            for (int j = 1; j <= k && i - j >= 0; ++j) {
                // Update the maximum element found in the last subarray of length j
                maxElement = max(maxElement, arr[i - j]);
                // Update the maximum sum by comparing the current maxSum with the sum calculated for the subarray ending at i-j
                maxSum = max(maxSum, dp[i - j] + maxElement * j);
            }

            dp[i] = maxSum;  // Update the DP table with the maximum sum for the subarray ending at i
        }

        return dp[n];  // Return the maximum sum for partitioning the entire array, which is stored in dp[n]
    }
};


// Description:
/*

### Comments Explanation:

- **Algorithm Library**: The `algorithm` library is included to use the `max` function, which finds the maximum of two values.
- **DP Array Initialization**: A DP array `dp` is initialized with `n+1` elements all set to 0. This array will hold the maximum sums for subarrays ending at each index. The size is `n+1` to conveniently represent subarrays ending at each index from `1` to `n`, with `dp[0]` representing an empty subarray.
- **Outer Loop**: The outer loop iterates through the array elements, starting from `1` up to `n`, to fill in the DP table with the maximum sums.
- **Inner Loop**: The inner loop considers all possible lengths for the last subarray, limited by `k` and the current position `i`. It calculates the maximum element in this subarray and the maximum sum obtainable by partitioning the array up to this point.
- **Updating DP Table**: After considering all possible lengths for the last subarray, the maximum sum calculated is stored in `dp[i]`.
- **Return Statement**: The method returns the value of `dp[n]`, which represents the maximum sum obtainable by partitioning the entire array.


To solve the problem of partitioning an array for maximum sum with constraints on subarray lengths, we will employ a dynamic 
programming approach. We define `dp[i]` as the maximum sum we can obtain by partitioning the subarray `arr[0..i-1]`. 
To compute `dp[i]`, we consider all possible lengths of the last subarray that ends at position `i-1`, limited by `k`. 
For each of these lengths `j`, we calculate the sum of the last subarray by identifying the maximum element in this last 
subarray and multiplying it by `j`. We then add this sum to `dp[i-j]`, which represents the maximum sum obtainable for the 
partition of the array ending before the last subarray starts. The maximum of all these values computed for different `j` 
values will be the value of `dp[i]`. 

The base case `dp[0]` is 0, as there is no element to partition in an empty subarray. Finally, `dp[arr.size()]` will give us 
the maximum sum after partitioning the entire array.

### Description:

This C++ solution defines a class `Solution` with a public method `maxSumAfterPartitioning`, which takes a vector of integers 
`arr` and an integer `k` as arguments. The method initializes a DP array `dp` of size `n+1` to store the maximum sums for 
subarrays ending at each index. It then iterates through the array, considering all possible lengths for the last subarray, 
up to `k`. For each possible length, it calculates the maximum sum obtainable and updates `dp[i]` with the maximum value found. 
The method finally returns the maximum sum for partitioning the entire array, stored in `dp[n]`.

*/
