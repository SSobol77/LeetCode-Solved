# 2483. Minimum Penalty for a Shop.

# Topic: String, Prefix Sum.

"""
### Task:
---
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only
of characters 'N' and 'Y':

- if the ith character is 'Y', it means that customers come at the ith hour
- whereas 'N' indicates that no customers come at the ith hour.

If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

- For every hour when the shop is open and no customers come, the penalty increases by 1.
- For every hour when the shop is closed and customers come, the penalty increases by 1.

Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

Example 1:
Input: customers = "YYNY"
Output: 2
Explanation:

    - Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
    - Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
    - Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
    - Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
    - Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.

Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.

Example 2:
Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.

Example 3:
Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.

Constraints:
1 <= customers.length <= 10^5
customers consists only of characters 'Y' and 'N'.

Hint 1:
At any index, the penalty is the sum of prefix count of ‘N’ and suffix count of ‘Y’.
Hint 2:
Enumerate all indices and find the minimum such value.

### Testcase:
---
"YYNY"
"NNNNN"
"YYYY"


### Code:
---
class Solution:
    def bestClosingTime(self, customers: str) -> int:

"""
### Solution: --------------------------------------

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)  # Length of the customers string

        # Compute prefix sums of 'N'
        # prefix_N[i] stores the number of 'N's from the start of the string up to the ith index
        prefix_N = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_N[i] = prefix_N[i - 1] + (customers[i - 1] == 'N')

        # Compute suffix sums of 'Y'
        # suffix_Y[i] stores the number of 'Y's from the ith index to the end of the string
        suffix_Y = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_Y[i] = suffix_Y[i + 1] + (customers[i] == 'Y')

        # Find the minimum penalty
        min_penalty = float('inf')  # Initialize minimum penalty as infinity
        best_hour = 0  # Initialize the best hour to close the shop
        for j in range(n + 1):
            # Calculate penalty for closing at hour j
            penalty = prefix_N[j] + suffix_Y[j]
            # If the calculated penalty is less than the current minimum, update min_penalty and best_hour
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = j

        return best_hour  # Return the best hour to minimize the penalty

# Test cases
sol = Solution()
print(sol.bestClosingTime("YYNY"))  # Output: 2, best to close after the 2nd hour
print(sol.bestClosingTime("NNNNN"))  # Output: 0, best to close immediately as no customers come
print(sol.bestClosingTime("YYYY"))  # Output: 4, best to stay open as customers come every hour



### Description: ===================================
'''
This Python code defines a class `Solution` with a method `bestClosingTime` that aims to find the optimal closing
hour for a shop to minimize the penalty, based on customer visits. Let's break down the code with comments for better
understanding:

### Code Explanation:

- The `bestClosingTime` method calculates the penalty for closing the shop at different hours based on customer visit
  patterns.
- `prefix_N` and `suffix_Y` arrays are used to optimize the computation of penalties. They store the cumulative count
  of 'N' and 'Y' up to and after each index, respectively.
- The loop iterates over each possible closing hour, calculates the penalty, and updates the minimum penalty and
  corresponding hour.
- Finally, the method returns the hour at which closing the shop results in the minimum penalty.

This approach efficiently calculates the best closing time by reducing the problem to prefix and suffix sums, thereby
avoiding recalculating the penalty from scratch for each possible closing hour.

To solve this problem, we need to find the optimal closing time for the shop that minimizes the penalty.
The penalty is based on the number of hours the shop is open without customers (`'N'`) and the number of
hours the shop is closed while customers come (`'Y'`). As the hints suggest, this can be achieved by
computing the prefix and suffix sums of `'N'` and `'Y'` in the `customers` string, respectively.

### Solution Steps:

1. **Compute Prefix Sums**: Calculate the cumulative count of `'N'` characters from the beginning of the string for each
   index. This represents the penalty for hours the shop is open without customers.
2. **Compute Suffix Sums**: Calculate the cumulative count of `'Y'` characters from the end of the string for each index.
   This represents the penalty for hours the shop is closed while customers come.
3. **Calculate Total Penalty for Each Hour**: For each hour `j`, the total penalty is the sum of the prefix sum up to `j`
   and the suffix sum from `j+1` to the end.
4. **Find Minimum Penalty**: Iterate through these total penalties to find the minimum value and the corresponding hour.


### Explanation:

- The `prefix_N` array keeps track of the number of 'N' characters seen from the start up to each index.
- The `suffix_Y` array counts the number of 'Y' characters from the end of the string up to each index.
- We then iterate over all possible closing hours (including closing just after the last hour, hence `n + 1`), c
  alculating the total penalty at each point.
- The hour with the minimum penalty is the optimal closing time.

This solution efficiently calculates the minimum penalty and determines the best closing hour by utilizing prefix
and suffix sums.

'''
