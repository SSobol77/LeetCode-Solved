// 880. Decoded String at Index.


// Topic: String, Stack.


/*
### Task:
---
You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

    If the character read is a letter, that letter is written onto the tape.
    If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.

Given an integer k, return the kth letter (1-indexed) in the decoded string.

Example 1:
Input: s = "leet2code3", k = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".

Example 2:
Input: s = "ha22", k = 5
Output: "h"
Explanation: The decoded string is "hahahaha".
The 5th letter is "h".

Example 3:
Input: s = "a2345678999999999999999", k = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.
The 1st letter is "a".
 
Constraints:
2 <= s.length <= 100
s consists of lowercase English letters and digits 2 through 9.
s starts with a letter.
1 <= k <= 10^9
It is guaranteed that k is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 2^63 letters.


### Testcase:
---
"leet2code3"
10
"ha22"
5
"a2345678999999999999999"
1


### Code:
---
class Solution {
public:
    string decodeAtIndex(string s, int k) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    string decodeAtIndex(string s, int k) {
        long size = 0;
        int n = s.length();

        // Calculate the size of the decoded string
        for (char c : s) {
            if (isdigit(c))
                size *= c - '0';
            else
                size++;
        }

        for (int i = n - 1; i >= 0; --i) {
            k %= size;  // Adjust k for repetitive segments
            if (k == 0 && isalpha(s[i])) {
                // If k is 0 and we're at a letter, we've found our answer
                return string(1, s[i]);
            }

            // Update size based on the current character
            if (isdigit(s[i]))
                size /= s[i] - '0';
            else
                size--;
        }

        // This line is never reached because the solution always returns from within the loop
        return "";
    }
};


// Description: ===================================
/*
To address the "Decoded String at Index" task, we can utilize a more efficient approach than fully decoding the string, which may lead to a string size exceeding the memory limits. The key insight is to work backwards from the desired index `k`, since the size of the decoded string can grow exponentially with each digit encountered, and decoding it entirely is impractical.

### Approach:
1. **Size Calculation:** First, calculate the size of the decoded string without actually decoding it. Iterate through the input string, and for each character:
   - If it's a letter, increment the size by 1.
   - If it's a digit, multiply the current size by the digit.

2. **Backward Traversal:** Once we have the total size, we iterate backwards through the input string and adjust `k` accordingly:
   - If `k` is greater than the size, it means `k` is pointing to a repetitive segment, so we take `k % size` to find the equivalent position in the original segment.
   - If we encounter a digit, we divide the size by that digit to revert to the size before this repetitive segment.
   - If we encounter a letter and `k % size == 0`, we've found our target letter.

### Explanation:
- The variable `size` represents the total length of the decoded string at any point. It increases when encountering a letter and multiplies by the digit when encountering a digit.
- By iterating backwards and adjusting `k` with `k % size`, we effectively find the position of the desired letter in the original (non-repetitive) segment of the string.
- When `k` becomes 0 at a letter during the backward iteration, it means this is the letter we're looking for, as `k` is 1-indexed.
- Dividing `size` by a digit when encountering it during the backward traversal undoes the effect of that digit on the size, taking us back to the size before the last repetition.

*/
