# 190. Reverse Bits

# Topic: Divide and Conquer, Bit Manipulation.

'''
# Task:
--------
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both 
input and output will be given as a signed integer type. They should not affect your implementation,
as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in 
Example 2 above, the input represents the signed integer -3 and the output represents the signed 
integer -1073741825.
 

Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned 
integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned
integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 
Constraints:
The input must be a binary string of length 32
 
Follow up: If this function is called many times, how would you optimize it?

# Testcase:
------------
00000010100101000001111010011100
11111111111111111111111111111101


# Code:
-------
class Solution:
    def reverseBits(self, n: int) -> int:
      

'''

# Solution:

class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize the result variable
        result = 0

        # Iterate over the bits
        for i in range(32):
            # Shift result to the left to make room for the new bit
            result <<= 1
            # Add the rightmost bit of n to result
            result |= n & 1
            # Shift n to the right to process the next bit
            n >>= 1

        return result

sol = Solution()
# Convert binary string to int
print(sol.reverseBits(int("00000010100101000001111010011100", 2)))  # Output: 964176192
print(sol.reverseBits(int("11111111111111111111111111111101", 2)))  # Output: 3221225471



'''
Description:
------------
To efficiently reverse the bits of a 32-bit unsigned integer, we can use bitwise operations. 
The goal is to swap each bit with its opposite position (e.g., swap the 1st bit with the 
32nd bit, 2nd bit with the 31st, and so on). This can be achieved by iterating over half of 
the bits (since swapping is symmetric) and performing the necessary swaps.

In this solution:
- We iterate 32 times, once for each bit in the 32-bit integer.
- In each iteration, we left shift result to make room for the new bit.
- We use n & 1 to get the rightmost bit of n and OR it with result.
- We right shift n to move to the next bit for the next iteration.

'''
