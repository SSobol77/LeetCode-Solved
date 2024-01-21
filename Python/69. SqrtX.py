# 69. Sqrt(x)

# Topic:

'''
# Task:
-------
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:
0 <= x <= 2^31 - 1

Hint 1:
Try exploring all integers.
Hint 2:
Use the sorted property of integers to reduced the search space. 


# Testcase:
-----------
Case1 
x=4
Case2
x=8

# Code:
-------
class Solution:
    def mySqrt(self, x: int) -> int:


'''

# Solution:
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # The square root of 0 and 1 is the number itself

        # Binary search initialization
        left, right = 2, x // 2

        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid

            if squared == x:
                return mid  # Found the exact square root
            elif squared < x:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half

        # When the loop ends, right is smaller than left, so right is the integer part of the sqrt
        return right

# Test cases
solution = Solution()
print(solution.mySqrt(4))  # Case 1: Expected output is 2
print(solution.mySqrt(8))  # Case 2: Expected output is 2


'''
Description:
To solve the square root problem without using any built-in exponent functions, we can employ a binary search 
algorithm, which is efficient for this kind of problem. Since the square roots of integers are sorted, we can
use binary search to find the square root of a given number x. The idea is to search for the square root in 
the range from 0 to x.

Explanation:
Special Case for Small Numbers: For x < 2, the square root is the number itself (0 or 1).
Binary Search Initialization: We set our search boundaries between 2 and x // 2 because the square root of any 
number x greater than 4 is always less than x // 2.

Binary Search Loop: We repeatedly narrow down the search space based on the squared value of the midpoint:
If mid * mid equals x, we've found the exact square root.
If mid * mid is less than x, the square root must be in the right half.
If mid * mid is greater than x, the square root must be in the left half.
Return Value: When the loop ends, right is the integer part of the square root of x.

This solution efficiently finds the integer square root of a number, using a binary search algorithm which has a 
time complexity of O(log n), making it suitable for large values of x.

'''