// 139. Word Break.


// Topic:Array, Hash Table, String, Dynamic Programming, Trie, Memoization.


/*
### Task:
---
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence 
of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 
Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

### Testcase:
---
"leetcode"
["leet","code"]
"applepenapple"
["apple","pen"]
"catsandog"
["cats","dog","sand","and","cat"]


### Code:
---
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        
    }
};

*/
// Solution: --------------------------------------
#include <string>
#include <vector>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        // Convert the word dictionary into a hash set for O(1) lookup time.
        std::unordered_set<std::string> dict(wordDict.begin(), wordDict.end());

        // Calculate the minimum and maximum word lengths in wordDict to optimize the search.
        int minWordLength = INT_MAX, maxWordLength = 0;
        for (const auto& word : wordDict) {
            minWordLength = std::min(minWordLength, static_cast<int>(word.length()));
            maxWordLength = std::max(maxWordLength, static_cast<int>(word.length()));
        }

        // Initialize the DP array with false values, with dp[0] set to true.
        // dp[i] will be true if the substring s[0..i-1] can be segmented into dictionary words.
        std::vector<bool> dp(s.size() + 1, false);
        dp[0] = true;

        // Iterate through the string, updating the DP array based on previous computations and dictionary lookups.
        for (int i = 1; i <= s.size(); ++i) {
            // Start j from the maximum of 0 and i - maxWordLength to avoid unnecessary checks.
            // End at i - minWordLength to not consider substrings shorter than the shortest word in the dictionary.
            for (int j = std::max(i - maxWordLength, 0); j <= i - minWordLength; ++j) {
                // If dp[j] is true and the substring s[j..i-1] is in the dictionary, set dp[i] to true.
                if (dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                    dp[i] = true;
                    break; // Break early since dp[i] being true is sufficient to move on.
                }
            }
        }

        // Return whether the entire string can be segmented into dictionary words.
        return dp[s.size()];
    }
};


// Description: ===================================
/*

### Solution:

The "Word Break" problem requires determining if a given string `s` can be segmented into a sequence of one or more words found in a given dictionary `wordDict`. To solve this problem efficiently, we employ dynamic programming with some key optimizations:

1. **Dynamic Programming Array (`dp`)**: We use a boolean array `dp` where `dp[i]` indicates whether the substring `s[0..i-1]` can be segmented into dictionary words. The array is initialized with all `false` values except for `dp[0]`, which is set to `true` to represent the base case of an empty substring.

2. **Dictionary Set**: The word dictionary is converted into a hash set for constant-time lookups, facilitating efficient checks to see if a substring matches a dictionary word.

3. **Min/Max Word Length**: By determining the minimum and maximum word lengths in the dictionary, we can avoid unnecessary checks for substrings that are either too short or too long to match any dictionary word. This optimization significantly reduces the number of iterations in the inner loop.

4. **Substring Checks**: For each position `i` in the string, we iterate backward from `i`, starting from the maximum possible word length and ending at the minimum word length, checking if any substring `s[j..i-1]` can form a valid segmentation. If such a substring is found and `dp[j]` is already `true`, we set `dp[i]` to `true` and break out of the loop early to avoid redundant checks.

5. **Early Stopping**: The inner loop breaks as soon as `dp[i]` is set to `true`, optimizing runtime by avoiding unnecessary checks once a valid segmentation is found for a given position.

The solution returns the value of `dp[s.size()]`, which represents whether the entire string `s` can be segmented into dictionary words. This approach ensures an efficient and optimized solution to the "Word Break" problem, taking advantage of dynamic programming and strategic optimizations to improve runtime and memory usage.



*/