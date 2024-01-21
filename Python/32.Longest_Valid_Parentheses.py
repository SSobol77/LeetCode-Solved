"""
# 32. Longest Valid Parentheses.

# Topic: String, Dynamic Programming, Stack.

# Task:
-----------
Given a string containing just the characters '(' and ')', return the length of the longest 
valid (well-formed) parentheses substring.

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


# Testcase:
------------
"(()"
")()())"
""

# Code:
------------
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        

"""
# Solution:
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize max_length to keep track of the maximum length of a valid substring
        max_length = 0
        # Initialize a stack with -1. This is useful for handling the base case and calculating lengths
        stack = [-1]

        # Iterate through each character in the string
        for i in range(len(s)):
            # If the current character is an opening bracket, push its index onto the stack
            if s[i] == '(':
                stack.append(i)
            else:
                # Pop the top element from the stack
                stack.pop()
                # If the stack is empty after popping, push the current index onto the stack
                if not stack:
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring
                    # Update the max_length if this length is greater than the current max_length
                    max_length = max(max_length, i - stack[-1])

        # Return the maximum length of the valid parentheses substring found
        return max_length


# Description:
'''
To solve the problem of finding the longest valid parentheses in a string, we can use a stack-based approach. 
The idea is to maintain a stack that keeps track of the indices of the parentheses in the string. This approach
helps in keeping track of the matching pairs of parentheses and calculating the lengths of valid substrings.

Here is the step-by-step algorithm:
-----------------------------------------
1. Initialize an empty stack and push -1 onto it. This acts as a base for the first valid substring.

2. Iterate through each character in the string:

- If the current character is '(', push its index onto the stack.
- If the current character is ')':
- Pop the top element from the stack.
- If the stack becomes empty after popping, push the current index onto the stack. This means we're starting a 
  new potential valid substring.
- If the stack is not empty, calculate the length of the current valid substring by subtracting the current index
  with the top element of the stack. Update the maximum length if necessary.

3. Return the maximum length found.

This solution efficiently calculates the length of the longest valid parentheses substring by using a stack to 
keep track of indices and updating the maximum length accordingly. 
It works for all cases, including empty strings and strings with no valid parentheses.

'''
