# 387. First Unique Character in a String.


# Topic: Hash Table, String, Queue, Counting

"""
### Task:
---
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 10^5
s consists of only lowercase English letters.


### Testcase:
---
"leetcode"
"loveleetcode"
"aabb"


### Code:
---
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
"""
### Solution: --------------------------------------

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Initialize a dictionary to store character counts
        char_count = {}
        
        # Count the occurrences of each character in the string
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Find the first unique character
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index  # Return the index of the first unique character
        
        return -1  # If there's no unique character, return -1


### Description: ===================================
'''
To solve the problem of finding the first unique character in a string, we can use a hash table to efficiently count the occurrences of each character in the string. Once we have the counts, we can iterate through the string again to find the first character that appears exactly once. Here's how you can do it:

1. **Initialize a hash table (dictionary in Python)** to store the count of each character in the string.
2. **Iterate over the string**, and for each character, increase its count in the hash table.
3. **Iterate over the string again** to find the first character that has a count of 1 in the hash table. Return its index.
4. **If no such character is found**, return -1 as specified in the problem statement.

### Description:

- The `char_count` dictionary keeps track of how many times each character appears in the string.
- The first `for` loop iterates through the string, updating the count of each character in `char_count`.
- The second `for` loop (combined with `enumerate` to get both character and index) checks each character in the original order they appear in the string. If a character's count is 1, it means the character is unique, and its index is immediately returned.
- If the loop completes without finding a unique character, `-1` is returned, indicating no such character exists in the string.

This solution efficiently solves the problem with a time complexity of \(O(n)\), where \(n\) is the length of the string, because each character in the string is accessed a constant number of times.



'''
