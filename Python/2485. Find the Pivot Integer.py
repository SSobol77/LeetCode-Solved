# 2485. Find the Pivot Integer.

# Topic: Math, Prefix Sum.

"""
### Task:
---
Given a positive integer n, find the pivot integer x such that:

    - The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.

Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

Example 1:
Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.

Example 3:
Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.

Constraints:
1 <= n <= 1000

Hint 1:
Can you use brute force to check every number from 1 to n if any of them is the pivot integer?
Hint 2:
If you know the sum of [1: pivot], how can you efficiently calculate the sum of the other parts?

### Testcase:
---
8
1
4

### Code:
---
class Solution:
    def pivotInteger(self, n: int) -> int:
      

"""


### Solution: --------------------------------------------------------------------------------------------------------

class Solution:
    def pivotInteger(self, n: int) -> int:
        # Calculate the total sum from 1 to n
        total_sum = n * (n + 1) // 2

        left_sum = 0
        for x in range(1, n + 1):
            # Subtract x from total_sum to get the sum from x+1 to n
            right_sum = total_sum - left_sum - x

            # If left sum equals right sum, x is the pivot
            if left_sum == right_sum:
                return x

            # Update left_sum for the next iteration
            left_sum += x

        # If no pivot found, return -1
        return -1

solution = Solution()

# Test cases
print(solution.pivotInteger(8))  # Expected Output: 6
print(solution.pivotInteger(1))  # Expected Output: 1


### Description: =======================================================================================================

'''
The solution to find the pivot integer `x` in a sequence of positive integers from 1 to `n` involves calculating the sum 
of integers on either side of `x`, excluding `x` itself, and checking for equality. Specifically, we seek an `x` where 
the sum of integers from 1 to `x-1` equals the sum of integers from `x+1` to `n`.

Here's how the solution works:

1. **Initialize Variables**: We start by calculating the total sum of integers from 1 to `n` using the formula 
    `total_sum = n * (n + 1) // 2`. We also initialize `left_sum` to 0, which will be used to keep track of the 
    sum of integers from 1 to `x-1`.

2. **Iterate Through the Sequence**: We loop through each integer `x` in the sequence from 1 to `n`. For each `x`, 
     we calculate `right_sum`, which represents the sum of integers from `x+1` to `n`. This is obtained by subtracting 
     `left_sum` and the value of `x` from `total_sum`.

3. **Check for Pivot Integer**: In each iteration, we compare `left_sum` and `right_sum`. If they are equal, we have 
     found our pivot integer `x`, and it is immediately returned.

4. **Update `left_sum`**: After checking each `x`, we update `left_sum` by adding `x` to it, preparing it for the next 
     iteration's comparison.

5. **Return Result**: If the loop completes without finding a pivot integer, the function returns -1, indicating no such 
     integer exists that satisfies the condition.

This approach efficiently finds the pivot integer (if one exists) by leveraging the arithmetic progression sum formula 
and maintaining a running sum for the left side of the pivot. The use of a single loop with simple arithmetic operations 
ensures that the solution is both time-efficient and easy to understand.

'''
