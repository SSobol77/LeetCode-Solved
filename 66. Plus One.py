# 66. Plus One.

# Topic: Array, Math.

'''
You are given a large integer represented as an integer array digits, where each digits[i] 
is the ith digit of the integer. The digits are ordered from most significant to least significant 
in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 
Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.


# Testcase:
-----------
[1,2,3]
[4,3,2,1]
[9]


# Code:
-------
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:  

'''
# Solution:
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse the array from the end to the beginning
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, just increment it and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0 (due to carry)
            digits[i] = 0
        
        # If all digits were 9, the array size increases by one with a leading 1
        return [1] + digits

# Test cases
solution = Solution()

print(solution.plusOne([1,2,3]))  # Output: [1,2,4]
print(solution.plusOne([4,3,2,1]))  # Output: [4,3,2,2]
print(solution.plusOne([9]))  # Output: [1,0]

'''
To solve the "Plus One" problem, we need to increment the number represented by the array digits by one. 
The most efficient way to do this is to traverse the array from the end to the beginning, handling the
carry from digit to digit. When a digit is less than 9, we can simply increment it and return the result.
If the digit is 9, it becomes 0, and we carry the increment to the next digit. If we reach the start of 
the array and still have a carry, we need to add a new digit at the beginning of the array.

'''
