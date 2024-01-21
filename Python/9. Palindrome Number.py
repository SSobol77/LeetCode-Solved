# 9. Palindrome Number

# Topic: Math.

'''
# Task:
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:

-2^31 <= x <= 2^31 - 1
 
Follow up: Could you solve it without converting the integer to a string?


# Testcase:
-----------
121
-121
10


# Code:
-------
class Solution:
    def isPalindrome(self, x: int) -> bool:
       
    
'''

# Solution:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        # Reversing the second half of the number and comparing with the first half
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Checking for both even and odd length numbers
        return x == reversed_half or x == reversed_half // 10
    
sol = Solution()
print(sol.isPalindrome(121))  # Output: True
print(sol.isPalindrome(-121))  # Output: False
print(sol.isPalindrome(10))   # Output: False


'''
Description:
To determine if a number is a palindrome without converting it to a string, we can reverse the second 
half of the number and compare it with the first half. A number is a palindrome if the reversed second 
half is equal to the first half. For negative numbers and numbers that end with zero (except zero itself),
we can immediately return False as they cannot be palindromes.

In this implementation:
We initially handle cases where x is negative or ends with zero.
We reverse the second half of x by repeatedly extracting the last digit and adding it to reversed_half.
The loop continues until the reversed half is greater or equal to the remaining half of x.
Finally, we check if the first half of x matches the reversed second half. For odd-length numbers, we also
check after removing the middle digit from reversed_half.

This solution is efficient, with a time complexity of O(log n) (since we're processing roughly half of the
digits in x), and it adheres to the constraint of not converting the integer to a string.

'''