// 131. Palindrome Partitioning.

//Topic: String, Dynamic Programming, Backtracking.

/*
### Task:
---
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.


### Testcase:
---
"aab"
"a"


### Code:
---
class Solution {
public:
    vector<vector<string>> partition(string s) {
        
    }
};

*/
// Solution:  ------------------------------------------------------------------------------

class Solution {
public:
    // Function to check if a string is a palindrome.
    // This function uses dynamic programming to store results of palindrome checks.
    bool isPalindrome(const string &s, int start, int end, vector<vector<int>> &dp) {
        if (start >= end) return true;
        if (dp[start][end] != -1) return dp[start][end];

        dp[start][end] = (s[start] == s[end]) && isPalindrome(s, start + 1, end - 1, dp);
        return dp[start][end];
    }

    // Backtracking function to find all palindrome partitions.
    void backtrack(int start, const string &s, vector<string> &path, vector<vector<string>> &result, vector<vector<int>> &dp) {
        if (start >= s.size()) {
            result.push_back(path);
            return;
        }

        for (int end = start; end < s.size(); end++) {
            if (isPalindrome(s, start, end, dp)) {
                path.push_back(s.substr(start, end - start + 1));
                backtrack(end + 1, s, path, result, dp);
                path.pop_back(); // Backtrack
            }
        }
    }

    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> path;
        vector<vector<int>> dp(s.size(), vector<int>(s.size(), -1)); // Dynamic programming table

        backtrack(0, s, path, result, dp);
        return result;
    }
};





// Description:  ============================================================================
/*
To solve the "Palindrome Partitioning" problem, we can utilize backtracking combined with dynamic programming. 
The goal is to find all the ways we can split a given string such that every substring is a palindrome.

### Approach:
1. **Backtracking**: We use backtracking to explore all possible partitioning of the string.
2. **Check for Palindromes**: For each partitioning, we check if the current substring is a palindrome.
3. **Dynamic Programming for Palindrome Checking**: Use dynamic programming to store the results of palindrome checks 
     for substrings, to avoid redundant calculations.
4. **Partitioning**: Recursively create different partitions and backtrack if the current partition is not a palindrome.

### Explanation:
- `isPalindrome` function checks if a substring is a palindrome. It uses a DP table (`dp`) to store the results of previous 
   checks to avoid redundant calculations.
- `backtrack` function explores all possible partitions of the string. For each partition, it checks if it forms a palindrome. 
   If yes, it proceeds to partition the remaining string.
- In `backtrack`, `path` holds the current partition, and `result` accumulates all valid palindrome partitions.
- `dp` table in `partition` function is initialized with `-1`, indicating that no palindrome checks have been done yet.
- The main function `partition` initializes necessary structures and starts the backtracking process.

### Complexity Analysis:
- **Time Complexity**: O(N * 2^N), where N is the length of the string. In the worst case, we might end up checking every 
    substring for being a palindrome and explore all partitioning.
- **Space Complexity**: O(N^2) for the DP table plus O(N) for the recursion stack, leading to O(N^2) overall. The DP table 
    stores palindrome checks for every possible substring.

*/