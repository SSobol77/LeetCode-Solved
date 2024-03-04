# 140. Word Break II.       - HARD -


# Topic: Array, Hash Table, String, Dynamic Programming, Backtracking, Trie, Memoization.


"""
### Task:
---
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Constraints:
1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 10^5.


### Testcase:
---
"catsanddog"
["cat","cats","and","sand","dog"]
"pineapplepenapple"
["apple","pen","applepen","pine","pineapple"]
"catsandog"
["cats","dog","sand","and","cat"]


### Code:
---
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    
  
"""
### Solution: --------------------------------------

class Solution:
    def wordBreak(self, s, wordDict):
        memo = {}  # Cache for storing results for substrings to avoid recomputation
        wordSet = set(wordDict)  # Convert the list of words into a set for faster existence checks
        
        # Function to check if the substring s[start:] can be segmented into words from wordDict
        def canBreak(s, wordSet):
            dp = [False] * (len(s) + 1)  # dp[i] will be True if s[:i] can be segmented
            dp[0] = True  # Empty string can be segmented trivially
            for i in range(1, len(s) + 1):
                for j in range(i):
                    # If s[:j] can be segmented and s[j:i] is in wordDict, set dp[i] to True
                    if dp[j] and s[j:i] in wordSet:
                        dp[i] = True
                        break
            return dp[-1]  # Return True if the whole string can be segmented

        def backtrack(start):
            if start in memo:  # Return cached result if available
                return memo[start]
            if start == len(s):  # Base case: reached the end of the string
                return [""]
            
            sentences = []  # List to store all sentences formed from s[start:]
            for end in range(start + 1, len(s) + 1):
                # If the current substring is a valid word, continue to build sentences
                if s[start:end] in wordSet:
                    remainderSentences = backtrack(end)  # Recursively process the remaining string
                    for sentence in remainderSentences:
                        # Append the current word to the sentences from the remainder, and strip to remove any leading/trailing spaces
                        sentences.append((s[start:end] + " " + sentence).strip())
            
            memo[start] = sentences  # Cache the result before returning
            return sentences
        
        # Pre-check if the string can be segmented into words from the dictionary
        if not canBreak(s, wordSet):
            return []  # If not, return an empty list
        
        return backtrack(0)  # Start backtracking from the beginning of the string

# Test cases
solution = Solution()
print(solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(solution.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))



### Description: ===================================
'''
The "Word Break II" solution employs a combination of dynamic programming, backtracking, and memoization to generate all possible 
sentences from a given string `s` using a list of valid words `wordDict`. The core idea revolves around segmenting `s` into subsequences 
that match the words in `wordDict` and recursively constructing sentences from these valid segments.

### Key Components:

1. **Dynamic Programming Pre-Check (`canBreak` function)**: Before attempting to construct sentences, a dynamic programming approach 
checks whether the given string `s` can be segmented into words found in `wordDict`. This step helps avoid unnecessary recursive calls 
for strings that cannot be fully segmented, thereby improving efficiency.

2. **Backtracking (`backtrack` function)**: This recursive function explores all possible ways to break the string `s` into words 
from `wordDict`, starting from a given index. It builds sentences by appending valid words and recursively processing the remaining 
substring. The function utilizes backtracking to explore different combinations of word segments, constructing potential sentences 
from these segments.

3. **Memoization**: To enhance performance, the solution caches the results of the `backtrack` function for each starting index of 
the string `s`. This memoization prevents the repeated processing of the same substring, significantly reducing the overall 
computation time.

4. **Word Set**: The `wordDict` is converted into a set to enable O(1) lookup times when checking if a substring is a valid word, 
further optimizing the solution.

### Process Flow:

- The solution starts by checking if `s` can be segmented using the `canBreak` function. If segmentation is not possible, it returns an empty list.
- If segmentation is possible, the solution proceeds with the `backtrack` function, which explores all segmentations starting from the beginning of `s`.
- As it progresses, `backtrack` builds sentences by appending valid words to the current sentence and recursively calling itself with the remaining substring.
- The `backtrack` function uses memoization to store results for each starting index, avoiding redundant computations.
- Finally, the solution returns a list of all valid sentences formed by concatenating words from `wordDict`.

This approach ensures that all unique combinations of words that can form valid sentences are considered, while also optimizing the solution to handle the complexities associated with backtracking and recursion. The use of memoization and a dynamic programming pre-check significantly improves the efficiency, making it a robust solution for the "Word Break II" problem.



'''
