# 629. K Inverse Pairs Array.       - HARD -

# Topic: Dynamic Programming.

"""
### Task:
---
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are 
exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

Example 1:
Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.

Example 2:
Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
 
Constraints:
1 <= n <= 1000
0 <= k <= 1000


### Testcase:
---
3
0
3
1


### Code:
---
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        
    
"""
### Solution: --------------------------------------

# Define the modulo constant as per the problem statement
MOD = 10**9 + 7

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # Initialize the DP table with dimensions (n+1) x (k+1), filled with 0s
        # dp[i][j] will hold the number of arrays of length i with exactly j inverse pairs
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        # Base case: there's exactly 1 way to arrange 0 elements with 0 inverse pairs
        dp[0][0] = 1

        # Iterate through each number from 1 to n to build up solutions for all subproblems
        for i in range(1, n + 1):
            # Initialize the cumulative sum for the current row (i)
            cumulative_sum = 0
            
            # Iterate through each possible number of inverse pairs from 0 to k
            for j in range(k + 1):
                # Update the cumulative sum with the value from the previous row, same column
                cumulative_sum += dp[i - 1][j]
                
                # If j is large enough to subtract the i-th value, adjust the cumulative sum
                # to exclude values that contribute more than i-1 inverse pairs
                if j >= i:
                    cumulative_sum -= dp[i - 1][j - i]
                
                # Update the current cell with the cumulative sum modulo MOD
                # This represents all the ways to arrange i numbers with exactly j inverse pairs
                dp[i][j] = cumulative_sum % MOD

        # The answer to the problem is the number of ways to arrange n numbers with k inverse pairs
        return dp[n][k]

# Example usage
sol = Solution()
n, k = 1000, 1000  # Large test case
print(sol.kInversePairs(n, k))  # Output: The number of arrays of length n with k inverse pairs modulo 10^9 + 7


### Description: ===================================
"""
The algorithm to solve the "K Inverse Pairs Array" problem using Dynamic Programming involves constructing a 2D table where each entry `dp[i][j]` represents the number of ways to arrange `i` numbers to form `j` inverse pairs. The approach focuses on incrementally building solutions for larger arrays using the solutions for smaller arrays. Here's a step-by-step description of the algorithm:

### Algorithm Steps:

1. **Initialization**:
    - Define a 2D array `dp` with dimensions `(n+1) x (k+1)`, where `n` is the number of elements and `k` is the number of inverse pairs. Initialize all elements to 0.
    - Set `dp[0][0]` to 1, as there is exactly one way (an empty array) to have 0 elements with 0 inverse pairs.

2. **Dynamic Programming Table Construction**:
    - Iterate over the number of elements `i` from 1 to `n`.
    - For each `i`, iterate over the number of inverse pairs `j` from 0 to `k`.
    - Use a running cumulative sum to calculate `dp[i][j]`. For each `j`, update the cumulative sum by adding the value from the previous row `dp[i-1][j]`.
    - If `j` is greater than or equal to `i`, subtract `dp[i-1][j-i]` from the cumulative sum to ensure that the sum only includes sequences where the `i-th` element can be placed to create new inverse pairs without exceeding the total `j`.
    - Update `dp[i][j]` with the cumulative sum modulo \(10^9 + 7\) to avoid integer overflow issues.

3. **Handling Inverse Pairs**:
    - Understand that inserting the `i-th` number into different positions in an array of `i-1` elements can create a varying number of inverse pairs. Specifically, inserting the number at the beginning creates `i-1` new inverse pairs, while inserting it at the end creates 0.
    - Use this understanding to adjust the cumulative sum for each `j` by considering the number of inverse pairs that can be formed when the `i-th` number is inserted into an array of `i-1` elements.

4. **Modulo Operation**:
    - Apply the modulo operation with \(10^9 + 7\) at each step of updating `dp[i][j]` to manage large numbers and prevent overflow.

5. **Returning the Result**:
    - After filling the `dp` table, the answer to the problem is found at `dp[n][k]`. This represents the number of arrays consisting of numbers from 1 to `n` that have exactly `k` inverse pairs.

### Algorithm Complexity:

- **Time Complexity**: \(O(n \times k)\), as the algorithm iterates over `n` elements and up to `k` inverse pairs for each, with constant-time operations within each iteration due to the cumulative sum optimization.
- **Space Complexity**: \(O(n \times k)\), due to the storage requirements of the 2D `dp` array.

### Key Points:

- The algorithm efficiently computes the number of arrangements using dynamic programming and cumulative sums, significantly reducing the computational overhead compared to naive approaches.
- The use of a modulo operation ensures that the algorithm can handle the potentially large numbers that result from combinatorial calculations.
- The approach builds upon the principle of dynamic programming by solving smaller subproblems and using their solutions to construct solutions for larger problems.

### Comments Explanation:
- **MOD**: The modulo value is defined at the beginning to handle large numbers, as required by the problem statement.
- **DP Table Initialization**: A 2D list `dp` is initialized to store the results of subproblems, where `dp[i][j]` represents the number of valid arrays of length `i` with `j` inverse pairs.
- **Base Case**: The base case `dp[0][0] = 1` is set, meaning there's exactly one way to arrange an array of length 0 with 0 inverse pairs (an empty array).
- **Cumulative Sum**: A variable `cumulative_sum` is used to keep track of the sum of values in the DP table, which helps in calculating the number of arrays with `i` elements and `j` inverse pairs without recalculating the sum for each cell.
- **Inner Loop for Inverse Pairs**: Inside the loop for each number `i`, another loop iterates over all possible counts of inverse pairs `j`. The `cumulative_sum` is updated based on the values in the previous row (`dp[i-1]`), taking into account only the valid number of inverse pairs.
- **Adjusting Cumulative Sum**: If the column index `j` is large enough, the cumulative sum is adjusted by subtracting the value `dp[i - 1][j - i]`, ensuring that only the sums of elements that contribute to a valid number of inverse pairs are considered.
- **Final Answer**: The final answer, `dp[n][k]`, is the number of arrays of length `n` with exactly `k` inverse pairs, computed modulo `10^9 + 7` to manage large numbers.

"""
