# 394. Decode String.       Medium

# Topic: String, Stack, Recursion.

"""
### Task:
---
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being 
repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets 
are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and 
that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].


### Testcase:
---
"3[a]2[bc]"
"3[a2[c]]"
"2[abc]3[cd]ef"

### Code:
---
class Solution(object):
    def decodeString(self, s):
        '''
        :type s: str
        :rtype: str
        '''
"""
### Solution: ----------------------------------------------------------

class Solution(object):
    def decodeString(self, s):
        '''
        :type s: str
        :rtype: str
        '''
        stack = []
        num = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # Build the multiplier
            elif char == '[':
                stack.append(num)  # Push the number (multiplier)
                stack.append(char)  # Push the '['
                num = 0  # Reset the number
            elif char.isalpha():
                stack.append(char)  # Push the character
            elif char == ']':
                # Pop and build the substring
                substring = ''
                while stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop()  # Pop the '['
                multiplier = stack.pop()  # Pop the number (multiplier)
                stack.append(substring * multiplier)  # Push the decoded string

        # Build and return the final decoded string
        return ''.join(stack)



# Description: ---------------------------------------------------------
'''
To solve the "Decode String" problem, we can use a stack to handle the nested structure of the input string. 
The basic idea is to push characters onto the stack until we encounter a closing bracket ']', at which point 
we pop elements to decode the substring and then push the decoded string back onto the stack. Here's a detailed 
approach:

1. **Initialize a Stack**: Create an empty stack to keep track of characters and numbers.

2. **Iterate through the String**: For each character in the string:
   - If the character is a digit, build the multiplier for the following string.
   - If the character is an opening bracket '[', push the built number and the bracket onto the stack and reset t
     he number.
   - If the character is a letter, push it onto the stack.
   - If the character is a closing bracket ']', pop from the stack until the opening bracket '[', decode the 
     substring, and then push the decoded string back onto the stack.

3. **Build the Result**: After processing all characters, pop all elements from the stack and build the result string.


### Explanation

The `decodeString` method works as follows:

1. **Initialization**: A stack and a variable `num` are initialized. The stack is used to store characters and 
    numbers, and `num` is used to build the multiplier for the strings that are inside the brackets.

2. **Iterating through the String**:
   - **Digit Characters**: If the current character is a digit, it is multiplied by 10 and added to `num`. 
       This process builds the multiplier for the string that follows. For example, if the input is '23', it will 
       be processed as `num = 2 * 10 + 3`.
   - **Opening Bracket '['**: When an opening bracket is encountered, the current multiplier `num` and the 
       bracket '[' are pushed onto the stack. Then, `num` is reset to 0 for the next number.
   - **Alphabetic Characters**: If the character is a letter, it is simply pushed onto the stack.
   - **Closing Bracket ']'**: When a closing bracket is encountered, the method pops elements from the stack 
       and builds a substring until it reaches an opening bracket '['. This substring represents the string that
       needs to be repeated. The opening bracket is then popped off, and the next pop gives the multiplier (which 
       was stored before the opening bracket). The substring is then repeated `multiplier` times and pushed back
       onto the stack as a single string.

3. **Building the Result**: After the entire string `s` has been processed, the stack contains parts of the decoded 
     string. The method then pops all elements from the stack, concatenates them in reverse order (as the stack 
     is LIFO - Last In First Out), and returns the decoded string.

This implementation ensures that each character of the input string is processed once, leading to a time complexity 
of O(n), where n is the length of the string. The space complexity is also O(n) in the worst case when the stack 
contains all the characters of the input string. The solution effectively handles nested structures and repetitive 
patterns in the input string.

'''
