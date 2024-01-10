# 214. Shortest Palindrome.

# Topics: String, Rolling Hash, String Matching, Hash Function.

'''
# Task:
---------
You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: s = "abcd"
Output: "dcbabcd"

Constraints:
0 <= s.length <= 5 * 10^4
s consists of lowercase English letters only.


# Testcase:
------------
"aacecaaa"
"abcd


# Code:
-------------
class Solution:
    def shortestPalindrome(self, s: str) -> str:
    
'''

# Solution:
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        base, mod = 131, 10**9 + 7
        max_len, forward_hash, reverse_hash, power = 0, 0, 0, 1

        for i in range(len(s)):
            forward_hash = (forward_hash * base + ord(s[i])) % mod
            reverse_hash = (reverse_hash + ord(s[i]) * power) % mod
            power = (power * base) % mod

            if forward_hash == reverse_hash:
                max_len = i + 1

        return s[max_len:][::-1] + s

# Test cases
solution = Solution()
print(solution.shortestPalindrome("aacecaaa"))  # Output: "aaacecaaa"
print(solution.shortestPalindrome("abcd"))      # Output: "dcbabcd"

# Description:
'''
To solve the "Shortest Palindrome" problem, we need an efficient way to find the longest 
palindrome that starts at the beginning of the given string s. Once we find this palindrome, 
we can simply reverse the remaining part of the string and append it to the beginning to form 
the shortest palindrome.

A rolling hash is a good choice for this task. It allows us to efficiently compute hash values 
for substrings of s, which we can use to check for palindromes. We will use two hashes, one from 
the beginning of the string and one from the end, and compare them to find the longest palindrome
starting at the beginning.

Here's a step-by-step approach:

1. Initialize two hash values (for forward and reverse hashes) and two constants for the base and 
   modulus to avoid overflow.
2. Iterate over the string, updating the forward and reverse hash values.
3. At each step, check if the forward hash equals the reverse hash. If it does, update the length 
   of the longest palindrome found so far.
4. After finding the longest palindrome, append the reverse of the remaining substring to the 
   beginning of s.
   
This code should work efficiently for the given constraints. The time complexity is O(n) where n 
is the length of the string, as we iterate over the string once. The rolling hash approach allows 
us to check for palindromes in constant time at each step.

'''

