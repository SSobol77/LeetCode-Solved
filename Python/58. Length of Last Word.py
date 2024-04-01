# 58. Length of Last Word/

# Topic: String.

'''
# Task:
---
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.

# Testcase:
---
"Hello World"
"   fly me   to   the moon  "
"luffy is still joyboy"

# Code:
---
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
'''
## Solution: ----------------------------------------------------------

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Trim the string to remove leading/trailing spaces
        trimmed_str = s.strip()
        
        # Split the trimmed string into a list of words
        words = trimmed_str.split()
        
        # Get the last word
        last_word = words[-1]
        
        # Return the length of the last word
        return len(last_word)


## Description: =======================================================
'''
It seems that the solution to the "Length of Last Word" problem isn't explicitly detailed in the documents you've uploaded. 
However, based on Python programming principles and best practices, I can help you understand how to solve this problem 
effectively. The task is to find the length of the last word in a given string, where a word is defined as a maximal substring 
consisting only of non-space characters.

Here's a step-by-step solution and explanation:

1. **Trim the String**: The first step is to remove any leading or trailing spaces from the string to ensure that the first 
and last characters we deal with are meaningful characters and not spaces. This can be done using the `strip()` method in Python, 
which removes any leading and trailing whitespaces.

2. **Split the String into Words**: Next, we can split the trimmed string into a list of words. In Python, the `split()` method 
by default splits a string by spaces, which suits our needs perfectly for this task.

3. **Find the Last Word**: Once we have the list of words, the last word will be the last element of this list. We can access 
it using negative indexing.

4. **Calculate the Length**: Finally, we can use the `len()` function to find the length of the last word.

This solution is straightforward and utilizes basic Python string methods and list indexing. It first ensures that any spaces 
at the beginning or end of the string do not interfere with identifying the last word. Then, by splitting the string into a list 
of words, we can easily access the last word and calculate its length. This approach is efficient and leverages Python's high-level 
built-in functions for string manipulation.

'''
