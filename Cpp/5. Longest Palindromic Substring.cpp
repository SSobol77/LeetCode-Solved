// 5. Longest Palindromic Substring.

// Topic: String, Dynamic Programming


/*
### Task:
---
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.

Hint 1:
How can we reuse a previously computed palindrome to compute a larger palindrome?
Hint 2:
If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
Hint 3:
Complexity based hint:
If we use brute-force and check whether for every start and end position a substring is a palindrome we 
have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks 
to O(1) by reusing some previous computation.

### Testcase:
---
"babad"
"cbbd"


### Code:
---
class Solution {
public:
    string longestPalindrome(string s) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    // Function to find the longest palindromic substring in s
    string longestPalindrome(string s) {
        // Handle the edge case where the string is empty
        if (s.empty()) return "";
        
        // Variables to keep track of the start and end indices of the longest palindrome found
        int start = 0, end = 0;

        // Iterate through each character in the string
        for (int i = 0; i < s.length(); ++i) {
            // Find the length of the longest palindrome with center at i (odd length)
            int len1 = expandAroundCenter(s, i, i);
            // Find the length of the longest palindrome with center between i and i+1 (even length)
            int len2 = expandAroundCenter(s, i, i + 1);

            // Determine the longer palindrome between len1 and len2
            int len = max(len1, len2);

            // Update the start and end indices if a longer palindrome is found
            if (len > end - start) {
                start = i - (len - 1) / 2; // Calculate the start index of the palindrome
                end = i + len / 2; // Calculate the end index of the palindrome
            }
        }

        // Extract and return the longest palindromic substring
        return s.substr(start, end - start + 1);
    }

private:
    // Helper function to expand around the center and find the length of the palindrome
    int expandAroundCenter(const string& s, int left, int right) {
        // Expand while the characters at left and right are the same and within the string bounds
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            --left; // Move left pointer backwards
            ++right; // Move right pointer forwards
        }
        // Return the length of the palindrome
        return right - left - 1;
    }
};


// Description: ===================================
/*
To solve the task of finding the longest palindromic substring within a given string, we can utilize dynamic programming 
to efficiently determine palindromic substrings and expand around their centers to find the longest one. This approach 
involves checking each character and the pair of characters in the string as potential centers of palindromes and expanding 
around them while the characters on both sides are equal.

We will implement the `longestPalindrome` function which iterates through the string, treating each character and each pair 
of consecutive characters as the center of a potential palindrome. For each center, we expand outwards and check for the 
longest palindrome. We keep track of the start index and the maximum length of the found palindrome to eventually return 
the longest palindromic substring.

### Description:
- The `expandAroundCenter` helper function takes the string and two indices, `left` and `right`, as parameters. It expands 
  around the center between `left` and `right` and checks for palindrome by comparing characters at `left` and `right` indices, 
  decrementing `left` and incrementing `right` until the characters are not equal or the indices go out of bounds. It then 
  returns the length of the palindrome found.
- In the `longestPalindrome` function, we iterate through each character of the string, treating each character (`i`) and each 
  pair of characters (`i`, `i+1`) as the center of a potential palindrome. We use the `expandAroundCenter` function to find 
  the length of the palindrome for both cases.
- We keep track of the maximum length of the palindrome found and its starting index. Finally, we return the substring from `start` 
  to `end` as the longest palindromic substring.

This solution has a time complexity of O(n^2), where n is the length of the string, since we are expanding around each center 
and the expansion itself takes up to O(n) time in the worst case. The space complexity is O(1) as we are not using any significant 
extra space.

*/
