// 368. Largest Divisible Subset.


// Topic: Array, Math, Dynamic Programming, Sorting.


/*
### Task:
---
Given a set of distinct positive integers nums, return the largest subset answer such that every 
pair (answer[i], answer[j]) of elements in this subset satisfies:

    answer[i] % answer[j] == 0, or
    answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.

Example 1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]

Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 10^9
All the integers in nums are unique.

### Testcase:
---
[1,2,3]
[1,2,4,8]


### Code:
---
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size(); // Store the size of the input array
        sort(nums.begin(), nums.end()); // Sort the array to ensure divisibility checks are straightforward

        // Initialize DP and parent arrays:
        // dp[i] holds the size of the largest divisible subset ending with nums[i]
        // parent[i] keeps track of the index of the previous element in the subset for backtracking
        vector<int> dp(n, 1), parent(n, -1), result;
        int max_size = 1; // Initialize the size of the largest subset found so far to 1 (minimum possible size)
        int max_index = 0; // Initialize the index of the last element of the largest subset to 0

        // Iterate over each element in the array starting from the second element
        for (int i = 1; i < n; ++i) {
            // Check each element nums[i] against all previous elements nums[j] to find divisible pairs
            for (int j = 0; j < i; ++j) {
                // If nums[i] is divisible by nums[j] and including nums[i] in the subset ending at nums[j] makes it larger
                if (nums[i] % nums[j] == 0 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1; // Update the size of the largest subset ending with nums[i]
                    parent[i] = j; // Record nums[j] as the predecessor of nums[i] in the subset
                }
            }
            // Update max_size and max_index if a larger subset ending with nums[i] is found
            if (dp[i] > max_size) {
                max_size = dp[i];
                max_index = i;
            }
        }

        // Backtrack from max_index to construct the largest divisible subset
        for (int i = 0; i < max_size; ++i) {
            result.insert(result.begin(), nums[max_index]); // Insert the current element at the beginning of the result vector
            max_index = parent[max_index]; // Move to the predecessor of the current element
        }

        return result; // Return the constructed largest divisible subset
    }
};



// Description: ===================================
/*

### Solution Description

The solution to finding the largest divisible subset within a set of distinct positive integers involves a strategic application of dynamic programming (DP) techniques combined with initial array sorting. The essence of the solution lies in identifying subsets where each pair of elements satisfies the condition of mutual divisibility, i.e., for any two elements `x` and `y` in the subset, either `x % y == 0` or `y % x == 0` holds true.

### Algorithm

1. **Sort the Array**: Begin by sorting the input array in ascending order. This step ensures that any element in the array is only divisible by its preceding elements, simplifying the process of checking for divisibility.

2. **Initialization**: Initialize two auxiliary arrays:
   - `dp[i]` to store the size of the largest divisible subset ending with `nums[i]`.
   - `parent[i]` to track the index of the preceding element in the largest subset ending with `nums[i]`, facilitating the reconstruction of the subset.

3. **Dynamic Programming Iteration**: Iterate through the array, for each element `nums[i]`, and perform the following steps:
   - Iterate through all previous elements `nums[j]` where `j < i`.
   - Check if `nums[i] % nums[j] == 0`. If true, and if including `nums[i]` in the subset increases its size (`1 + dp[j] > dp[i]`), then update `dp[i]` to `1 + dp[j]` and set `parent[i]` to `j`.

4. **Identify the Largest Subset**: After populating the DP table, the size of the largest divisible subset is the maximum value in `dp`, and the subset can be traced back starting from the corresponding index.

5. **Reconstruct the Subset**: Begin with the element corresponding to the maximum value in `dp` and use the `parent` array to trace back through the elements of the subset. Insert each discovered element at the beginning of the result vector until the start of the subset is reached.

6. **Return the Result**: The result vector, now containing the largest divisible subset, is returned as the solution.

### Key Points

- **Sorting**: Sorting the input array is crucial as it allows the DP algorithm to efficiently check for divisibility among elements by only considering previously encountered elements.
- **Dynamic Programming**: The DP approach efficiently computes the size of the largest divisible subset ending with each element by building upon previously computed results, avoiding redundant computations.
- **Subset Reconstruction**: The `parent` array is a pivotal component for backtracking from the end of the largest subset found, allowing for the reconstruction of the subset by tracing each element's predecessor.

This algorithm efficiently tackles the problem by leveraging the sorted nature of the array and dynamic programming to build up the solution incrementally, ensuring that all divisible pairs are considered while maintaining optimal time complexity.

*/
