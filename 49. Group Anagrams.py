# 49. Group Anagrams

# Topic: Array, Hash Table, String, Sorting.

'''
# Task:
-------
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically 
using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
 
Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

# Testcase:
-----------
["eat","tea","tan","ate","nat","bat"]
[""]
["a"]

# Code:
--------
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
'''
# Solution:
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using defaultdict to automatically handle new keys
        anagrams = defaultdict(list)

        # Iterate over each string in the list
        for s in strs:
            # Sort the string and use it as a key
            sorted_str = ''.join(sorted(s))

            # Append the original string to the corresponding list
            anagrams[sorted_str].append(s)

        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())

# Test cases
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(solution.groupAnagrams([""]))                                  # [[""]]
print(solution.groupAnagrams(["a"]))                                 # [["a"]]


# Description:
'''
We use defaultdict from the collections module, which simplifies the code by removing the need to check 
if a key exists in the dictionary.
The use of defaultdict(list) means that if a key doesn't exist, it will automatically create a new list 
for that key, which simplifies the logic inside the loop.
The core algorithm remains the same because it's already optimized for this problem. The sorting of strings 
and grouping based on sorted strings is the most efficient approach for this problem.

'''
