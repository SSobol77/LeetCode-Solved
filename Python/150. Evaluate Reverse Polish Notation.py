# 150. Evaluate Reverse Polish Notation.

# Topic: Array, Math, Stack.

"""
### Task:
---
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
    - The valid operators are '+', '-', '*', and '/'.
    - Each operand may be an integer or another expression.
    - The division between two integers always truncates toward zero.
    - There will not be any division by zero.
    - The input represents a valid arithmetic expression in a reverse polish notation.
    - The answer and all the intermediate calculations can be represented in a 32-bit integer.
    
Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:
1 <= tokens.length <= 10^4
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].



### Testcase:
---
["2","1","+","3","*"]
["4","13","5","/","+"]
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


### Code:
---
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
"""
### Solution: --------------------------------------

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Define a stack to keep track of operands
        stack = []
        
        # Define a function for each operator
        def add(x, y):
            return x + y
        
        def subtract(x, y):
            return x - y
        
        def multiply(x, y):
            return x * y
        
        def divide(x, y):
            # Perform integer division, truncate towards zero
            return int(x / y)
        
        # Map each operator to its corresponding function
        operators = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
        }
        
        # Iterate over each token
        for token in tokens:
            if token in operators:
                # Pop the last two operands from the stack
                operand2 = stack.pop()
                operand1 = stack.pop()
                # Perform the operation and push the result back onto the stack
                stack.append(operators[token](operand1, operand2))
            else:
                # Convert token to integer and push onto the stack
                stack.append(int(token))
                
        # The final element in the stack is the result
        return stack.pop()


### Description: ===================================
'''
To solve the problem of evaluating an expression given in Reverse Polish Notation (RPN), we can use a stack to keep track of the operands. When we encounter an operator, we pop the last two operands from the stack, perform the operation, and push the result back onto the stack. This process continues until we have processed all elements in the `tokens` array. The final result will be the last remaining element in the stack.

Here's a step-by-step approach to implement the solution:

1. Initialize an empty stack.
2. Iterate over each token in the `tokens` array.
   - If the token is an operand (i.e., a number), convert it to an integer and push it onto the stack.
   - If the token is an operator, pop the last two operands from the stack. Perform the operation indicated by the operator with these operands. Push the result of the operation back onto the stack.
3. After processing all tokens, the stack will contain only one element, which is the result of the RPN expression. Pop and return this element as the result.


This code snippet defines a class `Solution` with a method `evalRPN` that takes a list of string tokens representing an RPN expression and returns its evaluated integer result. The solution uses a stack to process the tokens in the given order, applying the appropriate arithmetic operation for each operator encountered.

'''
