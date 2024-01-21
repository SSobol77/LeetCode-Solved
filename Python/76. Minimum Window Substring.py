# 76. Minimum Window Substring.  HARD

# Topic: Hash Table, String, Sliding Window.

"""
### Task:
---
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every 
character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

#Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

#Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

#Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

#Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.
 
Follow up: Could you find an algorithm that runs in O(m + n) time?

Hint 1:
Use two pointers to create a window of letters in s, which would have all the characters from t.
Hint 2:
Expand the right pointer until all the characters of t are covered.
Hint 3:
Once all the characters are covered, move the left pointer and ensure that all the characters are still covered 
to minimize the subarray size.
Hint 4:
Continue expanding the right and left pointers until you reach the end of s.

### Testcase:
---
"ADOBECODEBANC"
"ABC"
"a"
"a"
"a"
"aa"

### Code:
---
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
"""
### Solution: -----------------------------------------------------------------------------------------------

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize two pointers for the sliding window
        left, right = 0, 0
        
        # Initialize a dictionary to store the character counts of t
        char_count_t = {}
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1

        # Calculate the number of unique characters in t
        required_chars = len(char_count_t)
        
        # Initialize counters and variables for tracking the minimum window
        current_chars = 0
        min_window_size = float('inf')
        result = ""
        
        # Initialize a dictionary to store character counts in the current window
        char_count_window = {}

        # Start the main loop
        while right < len(s):
            # Expand the right pointer and update character counts in the current window
            if s[right] in char_count_t:
                char_count_window[s[right]] = char_count_window.get(s[right], 0) + 1
                if char_count_window[s[right]] == char_count_t[s[right]]:
                    current_chars += 1
            
            # Try to minimize the window by moving the left pointer
            while current_chars == required_chars and left <= right:
                # Update the minimum window size and result
                if right - left + 1 < min_window_size:
                    min_window_size = right - left + 1
                    result = s[left:right + 1]
                
                # Shrink the window by moving the left pointer
                if s[left] in char_count_t:
                    char_count_window[s[left]] -= 1
                    if char_count_window[s[left]] < char_count_t[s[left]]:
                        current_chars -= 1
                
                left += 1  # Move the left pointer to continue shrinking the window
            
            right += 1  # Move the right pointer to expand the window
        
        return result  # Return the minimum window substring found



# Description: ----------------------------------------------------------------------------------------------
'''
To find the minimum window substring of `s` that contains all characters from `t`, you can use a sliding window approach with
a hash table to keep track of character frequencies.

Solution works:

1. Initialize a hash table `char_count_t` to store character frequencies of the string `t`.
2. Initialize the `left` and `right` pointers to 0, and counters for required characters (`required_chars`) and current characters (`current_chars`).
3. Create a hash table `char_count_window` to keep track of character frequencies in the current window.
4. Iterate through the string `s` using the `right` pointer to expand the window.
5. Update the character frequency in `char_count_window` for characters in `t`.
6. When all required characters are found in the current window (`current_chars` equals `required_chars`), try to minimize the window by moving
   the `left` pointer.
7. Update the minimum window size and result string when a smaller valid window is found.
8. Move the `left` pointer to shrink the window and continue the process until the window no longer contains all required characters.
9. Finally, return the minimum window substring found.

This solution has a time complexity of O(m + n), where m is the length of `s` and n is the length of `t`, as it iterates through 
both strings only once.

'''
