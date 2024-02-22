// 316. Remove Duplicate Letters.


// Topic: String, Stack, Greedy, Monotonic Stack.


/*
### Task:
---
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

Constraints:
1 <= s.length <= 10^4
s consists of lowercase English letters.
 
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Hint 1:
Greedily try to add one missing character. How to check if adding some character will not cause problems ? Use bit-masks to check 
whether you will be able to complete the sub-sequence if you add the character at some index i.

### Testcase:
---
"bcabc"
"cbacdcbc"


### Code:
---
class Solution {
public:
    string removeDuplicateLetters(string s) {
        
    }
};

*/

// Solution: --------------------------------------


class Solution {
public:
    string removeDuplicateLetters(string s) {
        vector<int> charCount(26, 0); // Count of each character in the string
        vector<bool> inResult(26, false); // Track if a character is in the result
        stack<char> st; // Monotonic stack to build the result

        // Count the occurrences of each character in the string
        for (char c : s) {
            charCount[c - 'a']++;
        }

        for (char c : s) {
            // Decrease the count for the current character
            charCount[c - 'a']--;

            // If the character is already in the result, skip it
            if (inResult[c - 'a']) continue;

            // Remove characters that are greater than the current character
            // and can appear later in the string
            while (!st.empty() && st.top() > c && charCount[st.top() - 'a'] > 0) {
                inResult[st.top() - 'a'] = false; // Mark character as not in result
                st.pop(); // Remove character from the stack
            }

            // Add the current character to the stack and mark it as in the result
            st.push(c);
            inResult[c - 'a'] = true;
        }

        // Build the result string from the stack
        string result = "";
        while (!st.empty()) {
            result = st.top() + result;
            st.pop();
        }

        return result;
    }
};


// Description: ===================================
/*
To solve the "Remove Duplicate Letters" problem, we can use a greedy approach combined with a monotonic stack to ensure that 
the resulting string is the smallest in lexicographical order among all possible results. The key idea is to build the result 
string character by character, making sure that:

1. Each character appears only once.
2. The result is lexicographically smallest.

We can achieve this by iterating through the string and making decisions based on the following rules:

- If the current character is not in the result and is smaller than the last character in the result, and if the last character 
  occurs later in the string, we can pop the last character off and push the current one.

- We must also keep track of the characters that have already been used in the result to avoid duplicates.

### Description:

The solution involves a greedy approach with a monotonic stack to ensure the lexicographical order. We start by counting the 
occurrences of each character in the string. Then, for each character in the string, we decide whether to include it in the result 
based on the current state of the stack and the remaining occurrences of the characters. If a character can replace a previously 
included character to achieve a smaller lexicographical order (and if the replaced character can still appear later), we pop 
characters from the stack until this condition is no longer true, then push the current character onto the stack. Finally, we 
construct the result string from the characters in the stack, ensuring that each character appears once and in the smallest 
lexicographical order.

*/
