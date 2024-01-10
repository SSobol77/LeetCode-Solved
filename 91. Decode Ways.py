# 91. Decode Ways

# Topics

'''
# Task:
--------
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse 
of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

 # Testcase:
 ------------
 "12"
"226"
"06"


# Code:
class Solution:
    def numDecodings(self, s: str) -> int:
    
'''

# Solution:

class Solution:
    def numDecodings(self, s: str) -> int:
        # If the string is empty or starts with '0', there are no valid decodings
        if not s or s[0] == '0':
            return 0

        # Lambda function to check if a substring is a valid encoding
        # It checks if the substring is between '10' and '26'
        isValid = lambda x: '10' <= x <= '26'

        # Dynamic programming array initialization
        # dp[0] is 1 for an empty string, and dp[1] is 1 if the first character is not '0'
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1

        # Iterate through the string starting from the second character
        for i in range(2, len(s) + 1):
            # Calculate the number of ways to decode the string up to the i-th character
            # dp[i-1] is added if the current character is not '0'
            # dp[i-2] is added if the last two characters form a valid encoding
            dp[i] = (dp[i-1] if s[i-1] != '0' else 0) + (dp[i-2] if isValid(s[i-2:i]) else 0)

        # Return the total number of ways to decode the entire string
        return dp[-1]

# Test cases
solution = Solution()
print(solution.numDecodings("12"))  # Output: 2
print(solution.numDecodings("226")) # Output: 3
print(solution.numDecodings("06"))  # Output: 0


# Description:
'''
The isValid lambda function is a concise way to check if a substring of two characters represents a valid encoding within the range '10' to '26'.
The dynamic programming array dp is used to store the number of ways to decode the string up to each position.
The loop iterates through the string, updating dp[i] based on the validity of one-character and two-character substrings ending at the current position.
The final result, dp[-1], gives the total number of ways to decode the entire string.

'''
