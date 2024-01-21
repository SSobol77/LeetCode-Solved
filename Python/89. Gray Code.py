# 89. Gray Code.

# Topic: Math, Backtracking, Bit Manipulation.

'''
# Task:
----------
An n-bit gray code sequence is a sequence of 2n integers where:

    Every integer is in the inclusive range [0, 2n - 1],
    The first integer is 0,
    An integer appears no more than once in the sequence,
    The binary representation of every pair of adjacent integers differs by exactly one bit, and
    The binary representation of the first and last integers differs by exactly one bit.

Given an integer n, return any valid n-bit gray code sequence.

Example 1:
Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit

Example 2:
Input: n = 1
Output: [0,1]

Constraints:
1 <= n <= 16

# Testcase:
------------
2
1

# Code:
------------
class Solution:
    def grayCode(self, n: int) -> List[int]:
   
'''
# Solution:
class Solution:
    def grayCode(self, n: int) -> List[int]:
        # Base gray code sequence for n = 0
        gray_code_sequence = [0]

        # Build up the sequence for larger n
        for i in range(n):
            # Reflect the existing sequence and add 1 at the beginning of reflected numbers
            gray_code_sequence += [x + (1 << i) for x in reversed(gray_code_sequence)]

        return gray_code_sequence

# The Solution class and grayCode method are now defined. 
# Below are the test cases to validate the implementation.

# Test cases
sol = Solution()

# Test case 1: n = 2
print(sol.grayCode(2))  # Expected output: [0, 1, 3, 2] or any other valid sequence

# Test case 2: n = 1
print(sol.grayCode(1))  # Expected output: [0, 1]


# Description:
'''
To generate an n-bit Gray code sequence, we can use a method based on the concept of reflection and bitwise operations.
The idea is to start with a base case (when n = 0, the Gray code sequence is just [0]) and build up the sequence for 
larger n by reflecting the existing sequence and adding a 1 at the beginning of the reflected numbers (in their binary form).

Here is how the algorithm works for n = 2:

1.    Start with n = 0: Gray code sequence is [0].
2.    For n = 1, reflect [0] to get [0, 1].
3.    For n = 2, reflect [0, 1] to get [00, 01, 11, 10].

We can implement this approach in Python, utilizing list comprehension and bitwise operations. As of Python 3.11, there 
are no specific new language features that would significantly change how we implement this solution compared to older
Python versions.

In this code:

The grayCode method generates the Gray code sequence for a given n.
We start with a base case for n = 0 and iteratively build the sequence for larger n.
The use of bit shifting (1 << i) and list comprehension makes the code concise and efficient.
The test cases validate the implementation for n = 2 and n = 1. The output may vary as there 
can be multiple valid Gray code sequences for a given n.

'''