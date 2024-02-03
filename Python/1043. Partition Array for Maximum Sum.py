# 1043. Partition Array for Maximum Sum.

# Topic: Array, Dynamic Programming.

"""
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
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

"""
### Solution:  -------------------------------------------------------------------------------

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Initialize the length of the array and the DP array with an extra space for ease of calculations.
        n = len(arr)
        dp = [0] * (n + 1)  # dp[i] represents the max sum up to the ith element in the array.
        
        # Iterate over each element in the array starting from the first element.
        for i in range(1, n + 1):
            max_val = 0  # To keep track of the maximum element in the current partition.
            
            # Iterate over possible partition sizes, from 1 to k or i (whichever is smaller).
            for j in range(1, min(k, i) + 1):
                # Update max_val to the maximum element in the current partition.
                max_val = max(max_val, arr[i - j])
                
                # Update dp[i] to the maximum of its current value and the sum obtained by adding
                # the current partition's sum (max_val * j) to the maximum sum of the array ending
                # right before the current partition starts (dp[i - j]).
                dp[i] = max(dp[i], dp[i - j] + max_val * j)
        
        # The last element of the DP array contains the maximum sum achievable for the entire array.
        return dp[n]



### Description:  ===============================================================================
"""
To solve the problem "Partition Array for Maximum Sum" using dynamic programming, we need to follow these steps:

1. **Initialize a DP Array**: We create a DP array `dp` of length `len(arr) + 1`, initialized with 0s. `dp[i]` will 
     store the maximum sum we can achieve by partitioning the subarray `arr[0:i]`.

2. **Iterate through the Array**: We iterate through the array starting from the first element. For each element `arr[i]`, 
     we consider all possible partition sizes from 1 to `k` (inclusive) that could end at the current element.

3. **Compute Maximum Sum for Each Partition Size**: For each possible partition size `j` (ranging from 1 to `k`), we do the following:
    - Find the maximum element in the last `j` elements, which will be the value used for all elements in this partition.
    - Calculate the sum for this partition as the maximum element found times the partition size `j`.
    - Add this sum to the maximum sum calculated for the subarray ending just before this partition starts, which is `dp[i - j + 1]`.

4. **Update DP Array**: The value of `dp[i + 1]` is updated to the maximum sum achievable by partitioning the subarray `arr[0:i+1]`. 
     This is the maximum of the current value of `dp[i + 1]` and the sum calculated for the current partition plus the maximum sum for 
     the subarray ending before this partition.

5. **Return the Result**: The last element of the DP array, `dp[len(arr)]`, will contain the maximum sum achievable for the entire array.


This code defines a class `Solution` with a method `maxSumAfterPartitioning` that takes an array `arr` and an integer `k` as input, 
and returns the maximum sum achievable after partitioning the array as described.

"""
