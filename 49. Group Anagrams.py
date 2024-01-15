# 49.  Group Anagrams.

# Topic: Array, Hash Table, String, Sorting.

"""
### Task:
---
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically 
using all the original letters exactly once.

#Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

#Example 2:
Input: strs = [""]
Output: [[""]]

#Example 3:
Input: strs = ["a"]
Output: [["a"]]

#Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


### Testcase:
---
["eat","tea","tan","ate","nat","bat"]
[""]
["a"]


### Code:
---
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
"""
### Solution:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to store anagrams
        anagram_groups = {}
        
        for word in strs:
            # Sort the characters of the word to create a unique key
            sorted_word = ''.join(sorted(word))
            
            # If the sorted_word is not in the dictionary, add it with an empty list as the value
            if sorted_word not in anagram_groups:
                anagram_groups[sorted_word] = []
            
            # Append the original word to the list of anagrams for the sorted_word
            anagram_groups[sorted_word].append(word)
        
        # Return the values of the dictionary as a list of lists
        return list(anagram_groups.values())


### Description:
'''
To group anagrams together efficiently, you can use a dictionary where the keys are sorted versions of the words, and the 
values are lists of anagrams

This code iterates through each word in the input list strs, sorts its characters to create a sorted key, and then adds 
the original word to the list of anagrams associated with that key in the anagram_groups dictionary.

The result is a list of lists where each inner list contains all the anagrams of a specific group. This solution has a 
time complexity of O(n * k * log(k)), where n is the number of words and k is the maximum length of a word.

'''