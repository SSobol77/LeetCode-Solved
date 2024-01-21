# 168. Excel Sheet Column Title.

# Topic: Math, String.

'''
# Task:
---------

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...


Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"

Constraints:
    1 <= columnNumber <= 2^31 - 1


# Testcase:
-----------
1
28
701

# Code:
----------
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """    

'''
# Solution:
class Solution:
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""  # Initialize an empty string for the result

        while columnNumber > 0:
            # Adjust column number and find the character
            columnNumber -= 1
            char = chr(columnNumber % 26 + ord('A'))
            result = char + result  # Prepend the character to the result

            columnNumber //= 26  # Update column number for next iteration

        return result

# Test cases
solution = Solution()
print(solution.convertToTitle(1))   # Example 1
print(solution.convertToTitle(28))  # Example 2
print(solution.convertToTitle(701)) # Example 3

# Description:
'''
To solve this problem, we need to convert the given column number to a string representing its 
corresponding column title in an Excel sheet. This is akin to converting a number to a base-26 
representation, where each digit is represented by a letter from A to Z. The challenge here is 
that Excel's column numbering is not a straightforward base-26 system because it doesn't have 
a symbol for zero. Instead, it goes directly from 1 (A) to 26 (Z), then continues with 27 (AA),
and so on.

Here's the approach we'll take:

1. Initialize an empty string result that will store the column title.
2. While columnNumber is greater than zero, perform the following steps:
    - Subtract 1 from columnNumber to adjust for the fact that Excel columns start at 1 instead of 0.
    - Calculate the remainder (mod) when columnNumber is divided by 26. This gives us the rightmost 
    - character in the current column title.
    - Prepend the corresponding character (A to Z) to result.
    - Update columnNumber by dividing it by 26 (integer division) for the next iteration.
3. Return the result string, which now contains the column title.

This code converts the given column number to its corresponding Excel column title efficiently and correctly.
The while loop iterates as many times as the number of characters in the final string, ensuring that the 
solution works well within the given constraints.

'''
