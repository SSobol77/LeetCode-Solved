# 1657. Determine if Two Strings Are Close.

# Topic: Hash Table, String, Sorting, Counting.


"""
### Task: 
---
Two strings are considered close if you can attain one from the other using the following operations:

- Operation 1: Swap any two existing characters.
    - For example, abcde -> aecdb
- Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
    - For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

#Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

#Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

#Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 
#Constraints:
1 <= word1.length, word2.length <= 10^5
word1 and word2 contain only lowercase English letters.

Hint 1:
Operation 1 allows you to freely reorder the string.
Hint 2:
Operation 2 allows you to freely reassign the letters' frequencies.

### Testcase:
---
"abc"
"bca"
"a"
"aa"
"cabbba"
"abbccc"

### Code:
---
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
"""
### Solution: -----------------------------------------------------------------------------------------------

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        # Create dictionaries to store character frequencies for both words
        freq1 = {}
        freq2 = {}
        
        # Calculate character frequencies for word1
        for char in word1:
            freq1[char] = freq1.get(char, 0) + 1
        
        # Calculate character frequencies for word2
        for char in word2:
            freq2[char] = freq2.get(char, 0) + 1
        
        # Check if both words have the same set of characters
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        # Check if both words have the same character frequencies
        freq1_values = sorted(list(freq1.values()))
        freq2_values = sorted(list(freq2.values()))
        
        return freq1_values == freq2_values


# Description: ----------------------------------------------------------------------------------------------
'''
To determine if two strings are "close" according to the given operations, we can follow these steps:

1. Check if both words have the same set of characters (i.e., the same character frequencies). If they don't have the same set of 
   characters, they can't be made equal, so return False.

2. Check if both words have the same character frequencies. If they have the same set of characters but different character frequencies, 
   they can't be made equal, so return False.

3. If both conditions above are met, return True because it means the words can be made equal using the given operations.


This code first checks if the lengths of both words are equal, as it's a necessary condition for the words to be "close." Then, 
it calculates the character frequencies for both words and compares their sets of characters and character frequencies. If both 
conditions are met, it returns True; otherwise, it returns False.

'''
