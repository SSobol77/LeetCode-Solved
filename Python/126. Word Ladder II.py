# 126. Word Ladder II.

# Topic: Hash Table, String, Backtracking, Breadth-First Search.

'''
# Task:
----------
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 500
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
The sum of all shortest transformation sequences does not exceed 10^5.


# Testcase:
-------------
"hit"
"cog"
["hot","dot","dog","lot","log","cog"]
"hit"
"cog"
["hot","dot","dog","lot","log"]


# Code:
-------------
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

'''
# Solution:
from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # Return an empty list if the endWord is not in the wordList
        if endWord not in wordList:
            return []

        # Create a set of words for faster lookup and add the beginWord to it
        wordSet = set(wordList)
        wordSet.add(beginWord)

        # Dictionary to keep track of all parents (predecessors) of a given word
        parent_map = defaultdict(set)

        # Perform BFS to find the shortest path length from beginWord to endWord
        # and to build the parent_map
        queue = deque([beginWord])
        level = {beginWord: 0}  # Dictionary to keep track of the level (distance from beginWord) of each word
        min_level = float('inf')  # Initialize the minimum level to infinity

        while queue:
            word = queue.popleft()
            current_level = level[word]

            # Update min_level if endWord is found
            if word == endWord:
                min_level = min(min_level, current_level)

            # Explore all possible one-letter transformations of the current word
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet:
                        # If next_word is not visited, set its level and add to queue
                        if next_word not in level:
                            level[next_word] = current_level + 1
                            if level[next_word] <= min_level:
                                queue.append(next_word)
                        # If next_word is on the same level, update the parent_map
                        if level[next_word] == current_level + 1:
                            parent_map[next_word].add(word)

        # Backtrack function to construct paths from endWord to beginWord
        def backtrack(word):
            # Base case: if the current word is beginWord, return a path containing just beginWord
            if word == beginWord:
                return [[beginWord]]
            paths = []
            # Iterate over all parents of the current word
            for parent in parent_map[word]:
                # For each parent, recursively construct paths
                for path in backtrack(parent):
                    # Append the current word to each path and add to the paths list
                    paths.append(path + [word])
            return paths

        # Start backtracking from the endWord
        return backtrack(endWord)

# Test cases
solution = Solution()
print(solution.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Expected output
print(solution.findLadders("hit", "cog", ["hot","dot","dog","lot","log"]))       # Expected output


# Discription:
'''
One approach is to use a two-step process:

 1. Find the Shortest Path Length: First, run a BFS to find the shortest path length from beginWord 
    to endWord without storing all paths.

 2. Backtrack to Find All Shortest Paths: Use this information to perform a depth-limited DFS (or BFS) 
    to construct the paths. This way, we only generate paths up to the shortest path length, significantly
    reducing memory usage.

This implementation first finds the shortest path length using a BFS and constructs a parent_map that maps
each word to its potential predecessors in the shortest path. Then, a DFS is used to backtrack from endWord 
to beginWord, constructing all the shortest paths. This approach should mitigate the memory issues encountered
with the previous solution.

In this implementation, the findLadders function uses BFS to find the shortest path length from beginWord
to endWord and constructs a parent_map for each word along the way. The backtrack function then uses this
parent_map to recursively build all the shortest transformation sequences from endWord to beginWord. Finally,
the paths are returned in reverse order, from beginWord to endWord.

'''
