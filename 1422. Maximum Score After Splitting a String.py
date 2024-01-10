# 1422. Maximum Score After Splitting a String

# Topic: String

'''
# Task:
-----
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings 
(i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right 
substring.

Example 1:
Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:
Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:
Input: s = "1111"
Output: 3
 
Constraints:
2 <= s.length <= 500
The string s consists of characters '0' and '1' only.

Hint 1
Precompute a prefix sum of ones ('1').
Hint 2
Iterate from left to right counting the number of zeros ('0'), then use the precomputed prefix sum for
counting ones ('1'). Update the answer.



# Testcase:
-----------
"011101"
"00111"
"1111"


# Code:
-----
class Solution:
    def maxScore(self, s: str) -> int:
        

'''
# Solution:

import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

class Solution:
    @time_decorator
    def maxScore(self, s: str) -> int:
        ones_total = s.count('1')
        ones_count, zeros_count, max_score = 0, 0, 0
        
        # Iterate through the string (excluding the last character)
        for i in range(len(s) - 1):
            if s[i] == '1':
                ones_count += 1
            else:
                zeros_count = i + 1 - ones_count
            
            score = zeros_count + (ones_total - ones_count)
            max_score = max(max_score, score)
        
        return max_score

# Test cases
solution = Solution()
print(solution.maxScore("011101"))  # Expected output: 5
print(solution.maxScore("00111"))   # Expected output: 5
print(solution.maxScore("1111"))    # Expected output: 3
