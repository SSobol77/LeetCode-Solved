"""
# 438. Find All Anagrams in a String.

# Topic: Hash Table, String, Sliding Window.

# Task:
--------
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or 
phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.


# Testcase:
------------
"cbaebabacd"
"abc"
"abab"
"ab"


# Code:
--------
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
"""
# Solution:
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Handle the edge case where p's length is greater than s's length
        if len(p) > len(s): 
            return []

        # Count the frequency of each character in p
        p_count = Counter(p)

        # Initialize a counter for the sliding window in s
        s_count = Counter()

        # List to store the starting indices of anagrams of p in s
        result = []
        
        for i in range(len(s)):
            # Add the current character to the sliding window's character count
            s_count[s[i]] += 1

            # Remove the character that moves out of the sliding window
            # This happens when our window size exceeds the length of p
            if i >= len(p):
                # If the character count becomes zero, remove it from the counter
                if s_count[s[i - len(p)]] == 1:
                    del s_count[s[i - len(p)]]
                else:
                    # Else, just decrease the count of that character
                    s_count[s[i - len(p)]] -= 1

            # After adjusting the window, compare the character counts in the window and p
            # If they are the same, it means the substring is an anagram of p
            if s_count == p_count:
                # Add the start index of this window to the result
                result.append(i - len(p) + 1)

        # Return the list of start indices of all anagrams of p in s
        return result


# Description:
'''
To solve this problem, we can use the sliding window technique along with a hash table (or an array to store character counts). 
The main idea is to slide a window of length equal to p over s, and at each step, check if the character composition in the 
window matches that of p. If it does, we add the start index of the window to our result list.

Here's a step-by-step approach:
-------------------------------
1. Count Characters in p: Create a hash table to count the occurrences of each character in p. This will help us quickly 
   check if a substring in s is an anagram of p.

2. Initialize Character Count for Sliding Window: Create another hash table to keep track of the character count in the 
   current window of s.

3. Slide Window and Compare Counts:
   *    Start with a window of size p and slide it over s.
   *    Update the character count for the current window.
   *    If the window character count matches p's character count, add the start index of the window to the result list.
   *    Each time the window slides, update the character counts (add the new character and remove the old one).

4. Return the Result: After processing all windows, return the list of starting indices.

In this code:
-----------------------
- We first check if p is longer than s. If it is, there cannot be any anagrams of p in s, so we return an empty list.
- The Counter objects p_count and s_count are used to efficiently store and compare the frequency of each character 
  in p and the current window of s, respectively.
- We iterate through s using a for loop, effectively sliding the window across s. For each position, we update s_count 
  to reflect the current window's character frequencies.
- When the window size exceeds the length of p, we start removing the character that is no longer in the window from s_count. 
  This is done by decreasing its count, and if the count drops to zero, we remove the character from s_count entirely.
- At each step, we compare s_count with p_count. If they are equal, it indicates that the current window is an anagram of p, 
  and we record the starting index of this window.
- Finally, we return the list result, which contains the starting indices of all the anagrams of p in s.

'''
