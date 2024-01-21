# 1347. Minimum Number of Steps to Make Two Strings Anagram.

# Topic: Hash Table, String, Counting.

"""
### Task:
---
You are given two strings of the same length s and t. In one step you can choose any character of t and 
replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

#Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

#Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

#Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
 
#Constraints:
1 <= s.length <= 5 * 10^4
s.length == t.length
s and t consist of lowercase English letters only.

Hint 1:
Count the frequency of characters of each string.
Hint 2:
Loop over all characters if the frequency of a character in t is less than the frequency of the same character in s then 
add the difference between the frequencies to the answer.


### Testcase:
---
"bab"
"aba"
"leetcode"
"practice"
"anagram"
"mangaar"


### Code:
---
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
"""
### Solution: ---------------------------------------------------------------------------------------------------

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        Calculates the minimum number of steps to make 't' an anagram of 's'.

        Args:
        s (str): The first string.
        t (str): The second string, which needs to be modified.

        Returns:
        int: The minimum number of steps required.
        """
        # Count the frequency of each character in 's'
        freq_s = {}
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1

        # Count how many characters in 't' need to be replaced
        replace_count = 0
        for char in t:
            if freq_s.get(char, 0) > 0:
                freq_s[char] -= 1
            else:
                replace_count += 1

        return replace_count




### Description: ------------------------------------------------------------------------------------------------
'''
To solve this problem, we need to determine how many characters in string `t` must be replaced to make `t` an anagram of `s`. 
An anagram is a rearrangement of characters, so the frequency of each character in `s` should match the frequency in `t`. 
The minimum number of steps is the total number of character replacements needed to equalize these frequencies.

### Algorithm:
1. **Count Character Frequencies:**
   - Create a frequency count for each character in string `s`. 
   - Use a dictionary where keys are characters and values are their frequencies.

2. **Compare Frequencies with `t`:**
   - Iterate through each character in string `t`.
   - Reduce the frequency of each character in the frequency dictionary created from string `s`.
   - If a character in `t` is not in the frequency dictionary or its frequency is zero, it's a character that needs to be replaced.

3. **Calculate the Number of Replacements:**
   - Add up the number of characters in `t` that need to be replaced.


### Description:
- **Frequency Count for 's':** We create a frequency dictionary for all characters in `s`.
- **Iterating over 't':** For each character in `t`, we decrease its frequency in the `s` frequency dictionary. If the character is not 
    present or its frequency is zero, it's counted as a character to be replaced.
- **Calculating Replacements:** The `replace_count` gives the total number of characters in `t` that need to be replaced to make `t` 
    an anagram of `s`.

This solution effectively counts the number of 'extra' characters in `t` that don't match with `s`, which is the number of replacements needed.

- for making `t` an anagram of `s`. The algorithm is efficient, with a time complexity of O(n), where n is the length of the strings, 
as it involves iterating through each string once. This approach ensures accuracy in calculating the minimum number of steps for 
the given task.

'''