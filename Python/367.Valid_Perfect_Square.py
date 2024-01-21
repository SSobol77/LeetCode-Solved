"""
# 367. Valid Perfect Square


# Topic: Math, Binary Search.

# Task:
----------------
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

Constraints:
1 <= num <= 2^31 - 1


# Testcase:
----------------
16
14

# Code:
----------------
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
     
"""

# Solution:

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Initialize the left and right pointers for binary search.
        # The potential square root of num is between 1 and num.
        left, right = 1, num

        while left <= right:
            # Calculate the mid-point to check if its square equals num.
            mid = left + (right - left) // 2
            square = mid * mid

            if square == num:
                # If the square of mid is equal to num, mid is the square root of num,
                # and num is a perfect square.
                return True
            elif square < num:
                # If the square of mid is less than num, 
                # then the square root must be greater than mid.
                left = mid + 1
            else:
                # If the square of mid is greater than num,
                # then the square root must be less than mid.
                right = mid - 1

        # If the loop completes without finding a perfect square, return False.
        return False


# Description:
'''
To determine if a given number num is a perfect square, we can use a binary search approach. 
This method is efficient and avoids using any built-in square root functions.

Approach:
---------
    Initialize: Start with two pointers, left as 1 and right as num.

    Binary Search:
        While left <= right, calculate the mid-point mid.
        Compute the square of mid and compare it with num.
        If the square is equal to num, return true, indicating num is a perfect square.
        If the square is less than num, move the left pointer to mid + 1.
        If the square is greater than num, move the right pointer to mid - 1.

    Result: If the loop exits without finding a perfect square, return false.

Explanation:
------------
    Initialization of left and right: Sets up the range for binary search.
    While loop (binary search): Continues searching as long as left is less than or equal to right.
    Calculation of mid and square: Computes the middle number and its square.
    Comparison with num: Determines if the square is equal, less than, or greater than num.
        If equal, num is a perfect square.
        If less, the perfect square must be higher.
        If greater, the perfect square must be lower.
    Return false if not found: If the loop ends without finding a perfect square, return false.

Complexity Analysis:
--------------------
    Time Complexity: O(log n), as binary search halves the search space each time.
    Space Complexity: O(1), as we only use a few variables for calculation and no additional data structures.
    
'''
