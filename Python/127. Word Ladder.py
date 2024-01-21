# 127. Word Ladder
'''
# Task:
-------
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words 
beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest 
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.

# Testcase:
-----------
"hit"
"cog"
["hot","dot","dog","lot","log","cog"]
"hit"
"cog"
["hot","dot","dog","lot","log"]

# Code:
-------
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

'''
# Solution:
from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Return 0 immediately if the endWord is not in the wordList
        if endWord not in wordList:
            return 0

        # Convert wordList to a set for efficient access
        wordList = set(wordList)
        # Initialize sets for the two ends of the bidirectional search
        beginSet, endSet = {beginWord}, {endWord}
        # Set to keep track of visited words to avoid revisiting
        visited = set()
        # Starting length of the transformation sequence
        length = 1

        # Continue the loop until both sets are non-empty
        while beginSet and endSet:
            # Swap the sets if beginSet is larger to always iterate over the smaller set
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            # Set to store the next level of words in the transformation sequence
            nextSet = set()
            for word in beginSet:
                # Generate all possible one-letter mutations of the current word
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        # If the mutated word is in the endSet, return the current length + 1
                        if next_word in endSet:
                            return length + 1
                        # If the mutated word is valid and not visited, add it to the next level
                        if next_word in wordList and next_word not in visited:
                            nextSet.add(next_word)
                            visited.add(next_word)
            # Update the beginSet for the next iteration and increment the length
            beginSet = nextSet
            length += 1

        # Return 0 if no transformation sequence exists
        return 0

# Testing the solution
sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Expected output: 5
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))  # Expected output: 0


# Description:
'''
This code efficiently implements a bidirectional BFS approach to find the shortest transformation sequence 
from beginWord to endWord. By exploring from both ends and meeting in the middle, it often reaches the solution 
faster than a standard BFS, especially in cases where the word graph is large.
'''