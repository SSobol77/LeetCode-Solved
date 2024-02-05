// 32. Longest Valid Parentheses.       - HARD - 

// Topic: String, Dynamic Programming, Stack.


/*
### Task:
---
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
 
Constraints:
0 <= s.length <= 3 * 10^4
s[i] is '(', or ')'.


### Testcase:
---
"(()"
")()())"
""

### Code:
---
class Solution {
public:
    int longestValidParentheses(string s) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    int longestValidParentheses(string s) {
        int maxLen = 0; // To keep track of the maximum length of valid parentheses
        stack<int> indices; // Stack to store the indices of '(' and the last unmatched ')'
        int start = -1; // Start index of a valid substring

        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '(') {
                // Push the index of '(' onto the stack
                indices.push(i);
            } else {
                if (indices.empty()) {
                    // No matching '(' for this ')', update start index
                    start = i;
                } else {
                    // Pop the matching '(' index
                    indices.pop();
                    if (indices.empty()) {
                        // If stack is empty, calculate length from the start index
                        maxLen = max(maxLen, i - start);
                    } else {
                        // Calculate length using the top index in the stack
                        maxLen = max(maxLen, i - indices.top());
                    }
                }
            }
        }

        return maxLen;
    }
};


// Description: ===================================
/*
To solve the "Longest Valid Parentheses" problem, we can use a stack to keep track of the indices of '(' characters 
and the start of a potential valid substring. The stack will help us match parentheses and find the lengths of valid substrings.

Here's a step-by-step approach to implementing the `longestValidParentheses` function:

1. **Initialize a Stack**: The stack will hold the indices of '(' characters and the last unmatched ')' character.
2. **Initialize Variables**: We need variables to keep track of the maximum length of valid parentheses found so 
     far (`maxLen`) and the start index of a potential valid substring (`start`).
3. **Iterate through the String**: For each character in the string, we do the following:
    - If the character is '(', we push its index onto the stack.
    - If the character is ')', we pop from the stack. If the stack is empty, this ')' has no matching '(', so we update 
      the start position to the next index. If the stack is not empty, we found a matching pair, and we update `maxLen` 
      to the maximum of its current value and the current index minus the top of the stack (to get the length of the valid substring).

### Description:

- The stack is used to track the positions of '(' characters. When we encounter a ')', we attempt to pop a '(' from the stack to match it. 
  If the stack is empty, it means the ')' does not have a matching '(' before it, so we update `start` to `i`, marking a new potential 
   start for a valid substring.

- If the stack is not empty after popping, it means we've found a valid pair of parentheses. We then calculate the length of this valid 
  substring. If the stack is empty after popping, it indicates that the current valid substring extends from the `start` position to the 
  current position `i`, so we calculate the length accordingly.

- The use of `maxLen = max(maxLen, i - indices.top());` ensures we always have the maximum length of a valid substring found so far. 
  The top of the stack either represents the index of the last unmatched '(', which serves as the beginning of the current valid 
  substring, or the last unmatched ')', which marks the start of the next valid substring.

- This solution has a time complexity of O(n), where n is the length of the string, because we traverse the string once. The space 
  complexity is O(n) in the worst case when all characters are '(' and need to be stored in the stack.

*/
