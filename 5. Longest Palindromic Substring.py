# 5. Longest Palindromic Substring.

# Topic: String, Dynamic Programming.

'''
# Task:
--------
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.

Hint 1:
How can we reuse a previously computed palindrome to compute a larger palindrome?
Hint 2:
If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
Hint 3:
Complexity based hint:
If we use brute-force and check whether for every start and end position a substring is
a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce
the time for palindromic checks to O(1) by reusing some previous computation.


# Testcase:
-------------
"babad"
"cbbd"


# Code:
------------
class Solution:
    def longestPalindrome(self, s: str) -> str:

'''
# Solution:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # If the string is less than 2 characters, it's already a palindrome
        if len(s) < 2:
            return s

        # Variables to store the starting position and length of the longest palindrome found
        start, max_length = 0, 1

        # Helper function to expand around a potential center and find the longest palindrome
        def expandAroundCenter(left, right):
            # Expand as long as the substring is a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the start and length of the palindrome
            return left + 1, right - left - 1

        for i in range(len(s)):
            # Check for odd-length palindrome by expanding from a single center
            left, length = expandAroundCenter(i, i)
            if length > max_length:
                start = left
                max_length = length

            # Check for even-length palindrome by expanding from between two centers
            left, length = expandAroundCenter(i, i + 1)
            if length > max_length:
                start = left
                max_length = length

        # Return the longest palindrome found
        return s[start:start + max_length]

# Testcases
sol = Solution()
print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(sol.longestPalindrome("cbbd"))   # Output: "bb"


# Description:
'''
Certainly! Here's a description of the optimized solution for finding the longest palindromic substring in a given string:

**Concept**: The optimized solution is based on the idea of expanding around potential centers of palindromes. Unlike the 
  dynamic programming approach, which requires additional space for storing intermediate results, this method focuses on 
  checking each character and the gap between characters as possible centers of palindromes.

**Implementation Details**:
-----------------------------

1. **Check for Base Case**: If the string length is less than 2, the string itself is the longest palindrome.

2. **Initialization**: Define variables `start` and `max_length` to keep track of the starting index and length of the longest 
     palindromic substring found.

3. **Expand Around Centers**:
   - Define a helper function `expandAroundCenter(left, right)` which expands around the center defined by `left` and `right` 
     indices. The expansion continues as long as the substring remains a palindrome. The function returns the starting index 
     and length of the palindrome found.

   - Iterate through each character in the string, using each character and the gap to its right as potential centers. For 
     each center:
      - Call `expandAroundCenter` with indices `(i, i)` for odd-length palindromes.
      - Call `expandAroundCenter` with indices `(i, i + 1)` for even-length palindromes.

   - Update `start` and `max_length` if a longer palindrome is found.

4. **Return Longest Palindrome**: Return the substring from `start` to `start + max_length`, which is the longest palindromic 
     substring.

**Key Advantage**:
-------------------
- **Time Efficiency**: This approach significantly reduces the time complexity to O(n^2) and the space complexity to O(1), 
    making it more efficient, especially for longer strings.

**Test Cases**:
- The provided test cases, such as `"babad"` and `"cbbd"`, demonstrate the function's ability to handle both odd and even 
  length palindromes and return a valid longest palindromic substring.

This method offers a more efficient and straightforward way to find the longest palindromic substring by directly exploring 
potential palindrome centers, thereby avoiding the complexity of maintaining a DP table.

'''
