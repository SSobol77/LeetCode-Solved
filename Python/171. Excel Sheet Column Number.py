# 171. Excel Sheet Column Number.

# Topic:

'''
# Task:
-----------------------------
Given a string columnTitle that represents the column title as appears in an Excel sheet, return 
its corresponding column number.

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
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701

Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].


# Testcase:
----------------------
"A"
"AB"
"ZY"


# Code:
----------------------
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """

'''

# Solution:
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        # Initialize result
        result = 0

        # Iterate over each character in the column title
        for char in columnTitle:
            # Convert the character to its corresponding number (A->1, B->2, ..., Z->26)
            # and update the result using the formula for base 26 numbers
            result = result * 26 + (ord(char) - ord('A') + 1)

        return result

# Test cases
sol = Solution()
test1 = "A"  # Example 1
test2 = "AB"  # Example 2
test3 = "ZY"  # Example 3

output1 = sol.titleToNumber(test1)
output2 = sol.titleToNumber(test2)
output3 = sol.titleToNumber(test3)

output1, output2, output3

# Description:
'''
The Python solution correctly calculates the column number corresponding to a given Excel sheet column title.

For the provided test cases, the outputs are as follows:

- For the input "A", the output is 1. This is correct as A corresponds to the first column in Excel.

- For the input "AB", the output is 28. This correctly matches the Excel column numbering where AB is 
  the 28th column.

- For the input "ZY", the output is 701. This is accurate as per the Excel column numbering, where ZY 
  represents the 701st column

'''
