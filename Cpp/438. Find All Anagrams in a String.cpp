// 438. Find All Anagrams in a String.


// Topic: Hash Tablem, String, Sliding Window.


/*
### Task:
---
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 
Constraints:
1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.


### Testcase:
---
"cbaebabacd"
"abc"
"abab"
"ab"

### Code:
---
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> result;
        if (s.length() < p.length()) return result;

        vector<int> pCount(26, 0), sCount(26, 0);
        // Count the frequency of each character in 'p'
        for (char c : p) pCount[c - 'a']++;

        // Initialize the sliding window's character count
        for (int i = 0; i < p.length(); ++i) {
            sCount[s[i] - 'a']++;
        }

        // If initial window is an anagram
        if (sCount == pCount) result.push_back(0);

        // Start sliding the window
        for (int i = p.length(); i < s.length(); ++i) {
            // Add the new character to the current window
            sCount[s[i] - 'a']++;
            // Remove the character left behind by the window
            sCount[s[i - p.length()] - 'a']--;

            // Check if the current window's character counts match 'p's character counts
            if (sCount == pCount) {
                result.push_back(i - p.length() + 1);
            }
        }

        return result;
    }
};


// Description: ===================================
/*

To solve the "Find All Anagrams in a String" problem, we can use a sliding window approach along with a hash table to efficiently track 
the frequency of characters. The idea is to move a window of length equal to `p` over `s`, and at each step, check if the character 
frequencies within the window match those in `p`. If they do, we've found an anagram and we record the start index of the window.

Here's a step-by-step approach:

1. **Character Frequency Count**: Use a hash table to count the frequency of each character in `p`. This serves as a reference to identify 
anagrams.

2. **Sliding Window Initialization**: Initialize a sliding window of length equal to `p` at the start of `s`. Use another hash table to 
track the frequency of characters within this window.

3. **Sliding the Window**: Move the window across `s`, one character at a time, updating the character frequencies in the window's hash 
table. After each move, compare the window's character frequencies with those in `p`. If they match, add the start index of the window 
to the result list.

4. **Optimizations**:
   - To efficiently compare the two hash tables, keep a count of characters that match between the window in `s` and `p`. Increase this 
      count when a character frequency in the window matches the corresponding frequency in `p`. Decrease it when moving the window causes 
      a mismatch.
   - Instead of using a hash table for `p` and the window, consider an array of fixed size (26 for lowercase English letters) if `s` 
      and `p` consist only of lowercase letters, which can reduce space complexity and improve access time.

5. **Return Result**: After moving the window across the entire string `s`, return the list of start indices that represent anagrams 
of `p` in `s`.


### Description:

This solution efficiently finds all the start indices of anagrams of `p` in `s` by employing a sliding window technique coupled with 
character frequency tracking. By maintaining and comparing the frequency counts of characters within the window and `p`, the algorithm 
identifies matching anagrams without needing to compare each substring directly. The use of fixed-size arrays for frequency counts 
optimizes both space and time complexity, making the solution well-suited for strings consisting of lowercase English letters. This 
approach ensures that the solution is both performant and easy to understand, with linear time complexity relative to the length of `s`.

*/
