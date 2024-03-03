// 76. Minimum Window Substring.         - HARD -


// Topic: Hash Table, String, Sliding Window.


/*
### Task:
---
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.
 
Follow up: Could you find an algorithm that runs in O(m + n) time?

Hint 1:
Use two pointers to create a window of letters in s, which would have all the characters from t.
Hint 2:
Expand the right pointer until all the characters of t are covered.
Hint 3:
Once all the characters are covered, move the left pointer and ensure that all the characters are still covered to minimize the subarray size.
Hint 4:
Continue expanding the right and left pointers until you reach the end of s.

### Testcase:
---
"ADOBECODEBANC"
"ABC"
"a"
"a"
"a"
"aa"

### Code:
---
class Solution {
public:
    string minWindow(string s, string t) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    string minWindow(string s, string t) {
        // Check for empty strings
        if (s.empty() || t.empty()) return "";

        // Array to store the frequency of characters in 't'
        int charFreq[52] = {0};
        // Populate the array with character counts from 't'
        for (char c : t) charFreq[charIndex(c)]++;

        // 'required' keeps track of the number of characters from 't' needed in the window
        int required = t.size();
        // Variables for keeping track of the minimum window
        int minLen = INT_MAX, minLeft = 0;
        // Pointers for the sliding window
        int left = 0, right = 0;

        // Expand the window to the right
        while (right < s.size()) {
            // Decrement the count of the current character in 'charFreq'
            // If the character is in 't', decrement 'required'
            if (charFreq[charIndex(s[right])]-- > 0) required--;

            // When all required characters are included in the window
            while (required == 0) {
                // Check if the current window is smaller than the minimum found so far
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minLeft = left;
                }

                // Increment the count of the leftmost character in 'charFreq'
                // If the character is needed for 't', increment 'required'
                if (++charFreq[charIndex(s[left])] > 0) required++;

                // Shrink the window from the left
                left++;
            }

            // Continue expanding the window to the right
            right++;
        }

        // Return the minimum window or an empty string if no valid window was found
        return minLen == INT_MAX ? "" : s.substr(minLeft, minLen);
    }

private:
    // Helper function to convert a character to an index in the 'charFreq' array
    // Maps 'A'-'Z' to 0-25 and 'a'-'z' to 26-51
    int charIndex(char c) {
        if (c >= 'A' && c <= 'Z') return c - 'A';
        return c - 'a' + 26;
    }
};


// Description: ===================================
/*
### Comments Explanation:

- **Initialization**: The function begins by checking for empty input strings, as no window is possible in such cases.

- **Character Frequency Array**: A fixed-size array `charFreq` is used to store the frequency of each character in `t`. The `charIndex` helper function is used to map characters to their corresponding indices in this array.

- **Sliding Window**: Two pointers, `left` and `right`, are used to define the sliding window within `s`. The window is expanded by moving the `right` pointer to include more characters and contracted by moving the `left` pointer to exclude characters.

- **Required Characters**: The variable `required` tracks how many characters from `t` are still needed in the current window. When `required` is zero, all characters from `t` are included in the window.

- **Updating Minimum Window**: Whenever a valid window is found that includes all characters from `t`, the code checks if this window is smaller than the smallest window found so far. If so, it updates the minimum window size and its starting position.

- **Character Indexing**: The `charIndex` function provides a way to convert characters to array indices efficiently, avoiding the overhead of a hash table.


The solution to the "Minimum Window Substring" problem employs a sliding window mechanism alongside a direct character frequency mapping 
strategy to efficiently find the smallest substring in `s` that encompasses all characters of `t`, including repetitions. The core of the 
solution lies in the usage of a 52-element array (`charFreq`) to track the frequency of each character in `t`, leveraging the fact that 
the input consists solely of uppercase and lowercase English letters. This array serves a dual purpose: it initially counts the occurrences 
of each character in `t`, and during the sliding window process, it aids in determining whether the current window in `s` contains all 
necessary characters from `t`.

The algorithm advances through `s` with two pointers, `left` and `right`, which define the current window. As the `right` pointer moves, 
it decreases the count for the encountered character in `charFreq`. When a character from `t` is fully accounted for in the window, the 
algorithm checks if the window can be minimized by incrementing the `left` pointer, thereby removing characters from the start while still 
retaining all `t` characters in the window. The minimum window size and its starting index are updated whenever a smaller valid window is 
identified.

This approach is optimized for both time and space complexity. The fixed-size array for character frequency tracking eliminates the 
overhead associated with hash tables, offering direct indexing based on character ASCII values, which is more efficient for the given 
character set. The `charIndex` helper function facilitates this mapping from characters to array indices, contributing to the solution's 
overall efficiency. This method ensures linear time complexity relative to the lengths of `s` and `t`, making it highly effective for 
large inputs. The solution is also marked by its clarity and ease of understanding, thanks to comprehensive inline comments that elucidate 
the purpose and functionality of each segment of the code.

*/
