// 20. Valid Parentheses.


// Topic: String, Stack.


/*
### Task:
---
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 
Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.

Hint 1:
Use a stack of characters.
Hint 2:
When you encounter an opening bracket, push it to the top of the stack.
Hint 3:
When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. 
Otherwise, return false.


### Testcase:
---
"()"
"()[]{}"
"(]"


### Code:
---
class Solution {
public:
    bool isValid(string s) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    bool isValid(string s) {
        // Initialize a stack to keep track of opening brackets
        stack<char> stk;

        // Iterate through each character in the string
        for (char c : s) {
            // Use a switch statement to handle each type of bracket
            switch (c) {
                // If the character is an opening bracket, push it onto the stack
                case '(': 
                case '{': 
                case '[':
                    stk.push(c);
                    break;
                // If the character is a closing bracket, check for a matching opening bracket
                case ')': 
                    // If the stack is empty or the top is not a matching opening bracket, return false
                    if (stk.empty() || stk.top() != '(') return false;
                    stk.pop(); // Pop the matching opening bracket from the stack
                    break;
                case '}': 
                    if (stk.empty() || stk.top() != '{') return false;
                    stk.pop();
                    break;
                case ']': 
                    if (stk.empty() || stk.top() != '[') return false;
                    stk.pop();
                    break;
            }
        }

        // After processing all characters, check if the stack is empty
        // An empty stack means all opening brackets were properly matched and closed
        return stk.empty();
    }
};




// Description: ===================================
/*
To solve the "Valid Parentheses" problem, a stack data structure is an ideal choice due to its Last-In-First-Out (LIFO) nature, which aligns perfectly with the requirement to match each closing bracket with its corresponding opening bracket in the correct order. The stack will help keep track of the opening brackets, and for every closing bracket encountered, we can check if it properly matches and closes the most recent opening bracket.

Here's a step-by-step approach:

1. **Initialize a Stack**: Create a stack to store opening brackets as they appear in the string.

2. **Iterate through the String**: Go through each character in the string `s`. For each character:
   - If it's an opening bracket ('(', '{', or '['), push it onto the stack.
   - If it's a closing bracket (')', '}', or ']'), check if the stack is not empty and if the top of the stack is the corresponding 
     opening bracket. If so, pop the top of the stack. Otherwise, return false since the order or type of brackets is incorrect.

3. **Check Stack Emptiness**: After processing all characters in the string, if the stack is empty, it means every opening bracket 
   was properly matched and closed, and hence the string is valid. If the stack is not empty, some opening brackets were not closed, 
   and the string is invalid.


### Description:

This solution leverages a stack to efficiently track opening brackets and ensure they are correctly matched with their corresponding 
closing brackets in the given string. By pushing opening brackets onto the stack and popping them when a matching closing bracket is 
encountered, the algorithm ensures that the brackets are closed in the correct order and of the correct type. The final check of the
stack's emptiness serves as a confirmation that all opening brackets were properly matched and closed, thus determining the validity 
of the parentheses in the string. This approach is both straightforward and effective, providing a clear and concise solution to the 
problem with a time complexity of O(n), where n is the length of the string.

*/
