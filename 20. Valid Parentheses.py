# 20. Valid Parentheses.  Easy

# Topic: String, Stack.

"""
### Task;
---
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
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

Hint 1
Use a stack of characters.
Hint 2
When you encounter an opening bracket, push it to the top of the stack.
Hint 3
When you encounter a closing bracket, check if the top of the stack was the opening for it. 
If yes, pop it from the stack. Otherwise, return false.


### Testcase:
---
"()"
"()[]{}"
"(]"

### Code:
---
class Solution(object):
    def isValid(self, s):
        '''
        :type s: str
        :rtype: bool
        '''   

"""
### Solution;
class Solution(object):
    def isValid(self, s):
        '''
        :type s: str
        :rtype: bool
        '''
        # Dictionary to hold the mapping of closing and opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        # Initialize an empty stack
        stack = []

        # Iterate through each character in the string
        for char in s:
            if char in bracket_map:
                # Pop element from stack if it's not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'

                # Check if the popped element is the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push to stack
                stack.append(char)

        # If the stack is empty, all brackets are properly closed
        return not stack


### Description:
'''
To solve the "Valid Parentheses" problem, we can use a stack to ensure that each closing bracket matches 
the most recent corresponding opening bracket. The algorithm is as follows:

1. **Initialize a Stack**: Create an empty stack to keep track of opening brackets.

2. **Iterate through the String**: For each character in the string:
   - If it's an opening bracket ('(', '{', '['), push it onto the stack.
   - If it's a closing bracket (')', '}', ']'), then check if the stack is not empty and the top of the s
     tack is the matching opening bracket. If so, pop the top of the stack. Otherwise, return `false` as the 
     string is not valid.

3. **Check if the Stack is Empty**: After processing all characters, if the stack is empty, then all opening 
     brackets have been properly closed, and the string is valid. Otherwise, return `false`.


This solution correctly handles the cases provided in the examples and follows the hints given:

- Hint 1 and 2 are addressed by using a stack to track opening brackets.
- Hint 3 is implemented by checking if the closing bracket matches the top element of the stack and popping it
  if it does.

The time complexity is O(n), where n is the length of the input string, as we iterate through the string once. 
The space complexity is also O(n) in the worst case, when all characters are opening brackets that get pushed 
onto the stack.

'''
