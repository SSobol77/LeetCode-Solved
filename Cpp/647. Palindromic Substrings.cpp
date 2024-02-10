// 647. Palindromic Substrings
 

// Topic: String, Dynamic Programming.


/*
### Task:
---
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
    1 <= s.length <= 1000
    s consists of lowercase English letters.

Hint 1:
How can we reuse a previously computed palindrome to compute a larger palindrome?
Hint 2:
If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
Hint 3:
Complexity based hint:
If we use brute force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation?

### Testcase:
---
"abc"
"aaa"

### Code:
---
class Solution {
public:
    int countSubstrings(string s) {
        
    }
};


*/
// Solution: --------------------------------------
class Solution {
public:
    int countSubstrings(string s) {
        int n = s.length(); // Get the length of the string
        // Initialize a 2D dynamic programming table to store palindromic substring information
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        int count = 0; // This will hold the count of palindromic substrings

        // Every single character is a palindrome, so mark all substrings of length 1 as true
        for (int i = 0; i < n; ++i) {
            dp[i][i] = true;
            count++; // Increment count for each character
        }
        
        // Check all substrings of length 2 and mark as true if the characters are equal
        for (int i = 0; i < n - 1; ++i) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = true;
                count++; // Increment count for each 2-character palindrome
            }
        }
        
        // Check for palindromes of length greater than 2
        for (int len = 3; len <= n; ++len) { // Start with length 3 to n
            for (int i = 0; i < n - len + 1; ++i) { // Iterate over all possible starting points
                int j = i + len - 1; // Calculate the ending index of the substring

                // Check if the current substring is a palindrome
                // The substring is a palindrome if the outer characters are the same
                // and the inner substring (i+1, j-1) is also a palindrome
                if (s[i] == s[j] && dp[i + 1][j - 1]) {
                    dp[i][j] = true; // Mark this substring as a palindrome
                    count++; // Increment the count of palindromic substrings
                }
            }
        }
        
        return count; // Return the total count of palindromic substrings
    }
};




// Description: ===================================
/*
To solve the problem of counting palindromic substrings in a given string `s`, we can utilize dynamic programming. The key idea is to build a table that stores whether a substring is a palindrome and then use this information to efficiently count all palindromic substrings.

### Algorithm:
1. Initialize a 2D array `dp` of size `n x n` where `n` is the length of the string `s`. `dp[i][j]` will be `true` if the substring from `i` to `j` (inclusive) is a palindrome, and `false` otherwise.
2. For all substrings of length 1, set `dp[i][i] = true`. Every single character is a palindrome by itself.
3. For all substrings of length 2, set `dp[i][i+1] = true` if `s[i] == s[i+1]`. This checks for palindromes of length 2.
4. For substrings longer than 2, use the following logic: If `s[i] == s[j]` and `dp[i+1][j-1]` is true (meaning the substring from `i+1` to `j-1` is a palindrome), then set `dp[i][j] = true`.
5. Use a counter to count the number of `true` entries in the `dp` table. This count represents the total number of palindromic substrings.


### Complexity Analysis:
- **Time Complexity:** O(n^2) where `n` is the length of the string. This is because we are iterating through all possible substrings and checking each for palindrome properties.
- **Space Complexity:** O(n^2) due to the 2D array `dp` used to store information about palindromic substrings.



*/
