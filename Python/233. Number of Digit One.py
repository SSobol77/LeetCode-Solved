# 233. Number of Digit One.

# Topic: Math, Dynamic Programming, Recursion.

'''
# Task:
--------
Given an integer n, count the total number of digit 1 appearing in all non-negative integers 
less than or equal to n.

Example 1:
Input: n = 13
Output: 6

Example 2:
Input: n = 0
Output: 0
 
Constraints:
0 <= n <= 10^9

Hint 1:
Beware of overflow.


# Testcase:
-----------
13
0

# Code:
------------
class Solution:
    def countDigitOne(self, n: int) -> int:

'''
# Solution:
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        count = 0
        factor = 1  # Factor to determine the position of the digit

        while factor <= n:
            digit = (n // factor) % 10  # Current digit
            high = n // (factor * 10)   # Higher part of the number
            low = n % factor            # Lower part of the number

            if digit == 0:
                count += high * factor
            elif digit == 1:
                count += high * factor + low + 1
            else:
                count += (high + 1) * factor

            factor *= 10

        return count

# Test cases
solution = Solution()
print(solution.countDigitOne(13))  # Output: 6
print(solution.countDigitOne(0))   # Output: 0

# Description:
'''
To solve the "Number of Digit One" problem, we can use a mathematical approach combined with 
dynamic programming and recursion. The idea is to count the number of times the digit '1' appears 
at each position from the least significant digit to the most significant digit in all numbers from 1 to n.

We break down the problem into smaller subproblems. For each position in the number, we calculate how many 
times '1' appears at that position across all numbers from 1 to n. The challenge is to handle the different 
cases, such as when the current digit is 0, 1, or greater than 1, and combine these counts correctly.

Here's an outline of the approach:

    1.Iterate over each digit in n, starting from the least significant digit.
    2.Calculate the contribution of '1's from the current digit.
    3.Add this contribution to a running total.
    4.Continue until all digits have been processed.

This code should work efficiently for the given constraints. The time complexity is O(log n) since 
we iterate through each digit of n. This approach avoids overflow issues by working with individual
digits and their contributions.

'''
