# 67. Add Binary

# Topic: Math, String, Bit Manipulation, Simulation.

'''
# Task:
--------
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

# Testscase:
-----------
"11"
"1"
"1010"
"1011"


# Code
-------
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
'''

# Solution:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers
        x, y = int(a, 2), int(b, 2)

        # Iterate until there is no carry
        while y:
            # Carry now contains common set bits of x and y
            carry = x & y
            # Sum of bits of x and y where at least one of the bits is not set
            x = x ^ y
            # Carry is shifted by one so that adding it to x gives the required sum
            y = carry << 1
        
        # Convert the result back to binary string
        return bin(x)[2:]
    
sol = Solution()
print(sol.addBinary("11", "1"))     # Output: "100"
print(sol.addBinary("1010", "1011"))  # Output: "10101"

'''
Description:
This solution is expected to be fast as it minimizes the use of string operations and 
leverages efficient bitwise operations. The conversion from binary string to integer 
and back is done only once, and the main loop operates purely on integers using bitwise logic.

'''
