# 70. Climbing Stairs.

# Topic: Math, Dynamic Programming, Memoization.

'''
# Task:
--------
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45

Hint 1
To reach nth step, what could have been your previous steps? 


# Testcase:
------------
2
3


# Code:
--------
class Solution:
    def climbStairs(self, n: int) -> int:
  

'''
# Solution:
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # Starting values for the Fibonacci sequence
        a, b = 1, 2

        for _ in range(3, n + 1):
            # Calculate the next number in the sequence
            a, b = b, a + b

        return b  # The n+1th Fibonacci number

# Test cases
solution = Solution()
print(solution.climbStairs(2))  # Expected output: 2
print(solution.climbStairs(3))  # Expected output: 3


'''
Description:

To solve the climbing stairs problem efficiently, we can utilize a mathematical approach 
based on the Fibonacci sequence. The number of ways to climb to the nth step is actually 
the n+1th Fibonacci number. The Fibonacci sequence is a series of numbers where each number 
is the sum of the two preceding ones, usually starting with 0 and 1.

We can calculate the Fibonacci sequence using an iterative approach, which is more efficient
than recursion in terms of time and space complexity. Python 3.11 doesn't introduce specific
new features that would significantly alter the approach for this problem, but we can make use 
of good programming practices for clarity and efficiency.

Explanation:
- Base Cases: If n is 1 or 2, we return n directly.
- Iterative Fibonacci Computation: We use two variables a and b to store the last two numbers of
  the Fibonacci sequence, starting with a = 1 (Fibonacci[1]) and b = 2 (Fibonacci[2]). For each 
  step from 3 to n, we update a and b to the next two Fibonacci numbers.
- Final Result: The result b is the n+1th Fibonacci number, which is the number of ways to climb n steps.

This method is fast and efficient, with a time complexity of O(n) and space complexity of O(1), making it
suitable for values of n up to 45.

'''


















'''
