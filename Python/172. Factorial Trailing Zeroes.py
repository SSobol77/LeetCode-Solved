# 172. Factorial Trailing Zeroes.

# Topic: Math.

'''
# Task:
-------
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0
 
Constraints:
0 <= n <= 10^4


# Testcase:
-----------
3
5
0

# Code:
--------
class Solution:
    def trailingZeroes(self, n: int) -> int:

'''
# Solution:
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        # Increment the power of 5 and divide n by it each time
        i = 5
        while n // i > 0:
            count += n // i
            i *= 5
        return count

# Test cases
solution = Solution()

print(solution.trailingZeroes(3))  # Output: 0
print(solution.trailingZeroes(5))  # Output: 1
print(solution.trailingZeroes(0))  # Output: 0


'''
Description:
To solve the "Factorial Trailing Zeroes" problem, we need to count how many times the number 10 is a factor 
in the factorial of n. Since 10 is the product of 2 and 5, and there are more factors of 2 than 5 in most 
factorials, the number of trailing zeros is determined by the number of times 5 is a factor in the factorial.

We can count the number of 5s in the factors of all numbers from 1 to n. For example, 5 contributes one 5, 
10 contributes one 5, 15 contributes one 5, and so on. However, numbers like 25 contribute two 5s (since 25 = 5 * 5),
125 contributes three 5s, and so on.

The algorithm is to sum up  |n/5|, |n/25|, |n/125|, etc., until the division results in zero.

This algorithm is efficient as it reduces the problem to a logarithmic time complexity relative to n.




'''
