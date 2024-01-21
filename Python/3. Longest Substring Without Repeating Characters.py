# 3. Longest Substring Without Repeating Characters.

# Topic: Hash Table, String, Sliding Window.

"""
### Task:
---
Given a string s, find the length of the longest 
substring
 without repeating characters.

#Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

#Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

#Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

#Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.

### Testcase:
---
"abcabcbb"
"bbbbb"
"pwwkew"

### Code:
---
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
"""
### Solution: -----------------------------------------------------------------------------------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_index = {}  # Hash table to store the index of characters
        max_length = 0  # Maximum substring length
        start = 0  # Start of the current substring

        for end in range(len(s)):
            # If the character is already in the hash table and its index is greater than or equal to the start
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1  # Move the start to the next index of the repeating character
            char_index[s[end]] = end  # Update the index of the current character
            max_length = max(max_length, end - start + 1)  # Update the maximum substring length

        return max_length


# Description: ----------------------------------------------------------------------------------------------
'''
To find the length of the longest substring without repeating characters, you can use a sliding window approach with a hash table 
to keep track of character occurrences.

Here's how the solution works:

1. Initialize a hash table `char_index` to store the index of characters in the input string `s`.
2. Initialize `max_length` to 0, which will keep track of the maximum substring length without repeating characters.
3. Initialize `start` to 0, which represents the start of the current substring.
4. Iterate through the characters of the string using a sliding window approach. The `end` pointer represents the end of the current substring.
5. If the current character `s[end]` is already in the `char_index` hash table and its index is greater than or equal to 
   `start`, it means we have a repeating character in the current substring. In this case, we move the `start` pointer to the next index of the 
   repeating character.
6. Update the `char_index` with the index of the current character `s[end]`.
7. Update `max_length` with the maximum of its current value and the length of the current substring (`end - start + 1`).
8. Repeat steps 4-7 until you reach the end of the string.
9. Return `max_length` as the length of the longest substring without repeating characters.

This solution has a time complexity of O(N), where N is the length of the input string `s`, and it uses a hash table to efficiently track character
occurrences.

'''
