# 191. Number of 1 Bits.

# Topic: Divide and Conquer, Bit Manipulation.

'''
# Task:
--------
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits
 it has (also known as the Hamming weight).

Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be 
given as a signed integer type. It should not affect your implementation, as the integer's internal binary 
representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3,
the input represents the signed integer. -3.
 

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 
Constraints:
The input must be a binary string of length 32.

Follow up: If this function is called many times, how would you optimize it?


# Testcase:
-----------
00000000000000000000000000001011
00000000000000000000000010000000
11111111111111111111111111111101

# Code:
---------
class Solution:
    def hammingWeight(self, n: int) -> int:
    



'''

# Solution:
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize count of '1' bits
        count = 0

        # Iterate through each of the 32 bits
        for i in range(32):
            # Check if the rightmost bit is '1' and increment count if it is
            if n & 1:
                count += 1
            # Right shift n to process the next bit
            n >>= 1

        return count

sol = Solution()
print(sol.hammingWeight(int("00000000000000000000000000001011", 2)))  # Output: 3
print(sol.hammingWeight(int("00000000000000000000000010000000", 2)))  # Output: 1
print(sol.hammingWeight(int("11111111111111111111111111111101", 2)))  # Output: 31


'''
To count the number of '1' bits (also known as the Hamming weight) in a 32-bit integer, 
we can use a bitwise approach that is efficient and straightforward. The idea is to 
iterate through each of the 32 bits of the integer, checking whether each bit is '1'.

For optimizing repeated calls to this function, a lookup table could be used to store
the Hamming weight of each possible byte (8 bits). However, for a single call, a 
direct calculation is more efficient.

This method iterates through each bit of the integer, using the bitwise AND operation (n & 1) 
to check if the rightmost bit is '1'. After checking each bit, it right shifts the number 
to move on to the next bit.
This implementation is efficient with a time complexity of O(1), as it processes each bit 
in the 32-bit integer once.

'''
