# 201. Bitwise AND of Numbers Range.

# Topic:  Bit Manipulation

'''
# Task:
--------
Given two integers left and right that represent the range [left, right], return the bitwise AND 
of all numbers in this range, inclusive.

Example 1:
Input: left = 5, right = 7
Output: 4

Example 2:
Input: left = 0, right = 0
Output: 0

Example 3:
Input: left = 1, right = 2147483647
Output: 0

Constraints:
0 <= left <= right <= 2^31 - 1


# Testcase:
-----------
5
7
0
0
1
2147483647


# Code:
---------
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        

'''

# Solution:
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Shift count
        shift = 0

        # Find the common leftmost bits of left and right
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1

        # Shift back to the left by the shift count
        return left << shift

sol = Solution()
print(sol.rangeBitwiseAnd(5, 7))            # Output: 4
print(sol.rangeBitwiseAnd(0, 0))            # Output: 0
print(sol.rangeBitwiseAnd(1, 2147483647))   # Output: 0


'''
To solve the "Bitwise AND of Numbers Range" problem, we need to find the common leftmost bits of left and right. 
The key observation is that if left and right differ at some bit position, all bits to the right of that position
in the range [left, right] will include both 0s and 1s, resulting in a bitwise AND of 0 for those positions.

We can keep shifting both left and right to the right until they are the same, which means we've discarded all 
the differing bits. Then, we shift back to the left by the same number of positions to get the final result. 
This approach is efficient because it minimizes the number of operations needed.
This solution has a time complexity of O(log n), where n is the number of bits in the input numbers. 
It's efficient because it only processes each bit once and stops when left equals right.
This method is both fast and effective for the given task and utilizes bit manipulation efficiently.

'''