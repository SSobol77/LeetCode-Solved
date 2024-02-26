// 3. Longest Substring Without Repeating Characters.


// Topic: Hash Table, String, Sliding Window.


/*
### Task:
---
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.


### Testcase:
---
"abcabcbb"
"bbbbb"
"pwwkew"


### Code:
---
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
    }
};

*/
// Solution: --------------------------------------


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> charIndexMap; // Hash table to store characters and their indices
        int maxLength = 0; // Store the maximum length of substring found
        int start = 0; // Start of the current window

        for (int end = 0; end < s.length(); end++) {
            // If the character is found in the hash table and its index is within the current window
            if (charIndexMap.find(s[end]) != charIndexMap.end() && charIndexMap[s[end]] >= start) {
                // Move the start to the right of the previous occurrence of the current character
                start = charIndexMap[s[end]] + 1;
            }

            // Update the latest index of the character
            charIndexMap[s[end]] = end;

            // Calculate the length of the current window and update maxLength if necessary
            maxLength = max(maxLength, end - start + 1);
        }

        return maxLength;
    }
};


// Description: ===================================
/*
To find the length of the longest substring without repeating characters in a given string `s`, we can use the Sliding Window 
technique along with a Hash Table to keep track of the characters we have encountered and their indices. This method allows us 
to efficiently expand and shrink the window of consideration based on the presence of repeating characters.

Here's a step-by-step guide to implementing this solution:

1. **Initialize variables**: Start with two pointers, `start` and `end`, which represent the beginning and the end of the current substring window, respectively. Also, initialize a hash table (like `unordered_map` in C++) to store characters and their indices within the window.

2. **Expand the window**: Iterate through the string with the `end` pointer, adding characters to the hash table and checking for duplicates.

3. **Handle duplicates**: If a duplicate character is found, it means the current substring contains repeating characters, and we need to move the `start` pointer to the right of the previous occurrence of this duplicate character to maintain the non-repeating property of the substring.

4. **Calculate the length**: After each iteration, calculate the length of the current substring without repeating characters as `end - start + 1` and update the maximum length if the current length is greater.

5. **Update indices**: Update the index of the current character in the hash table to its latest occurrence.


### Description:

This solution employs the Sliding Window technique combined with a Hash Table to efficiently find the length of the longest substring 
without repeating characters. By maintaining a window of characters that are guaranteed to be unique, the algorithm can dynamically adjust 
the size of this window as it iterates through the string. Whenever a duplicate character is encountered, the window is adjusted by moving 
its start right past the previous occurrence of this character, thus excluding the repeating character and maintaining the non-repeating 
property of the substring. The hash table serves to quickly look up the index of characters within the window, allowing for O(1) access 
time to check for duplicates and update indices. This approach ensures that the algorithm runs in O(n) time complexity, where n is the 
length of the string, as each character is considered at most twice (once when expanding the end of the window and once when moving the 
start).

*/
