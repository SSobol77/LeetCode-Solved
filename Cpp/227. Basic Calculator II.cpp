// 227. Basic Calculator II.


// Topic:


/*
### Task:
---
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2^31, 2^31 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5

Constraints:
1 <= s.length <= 3 * 10^5
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
The answer is guaranteed to fit in a 32-bit integer.


### Testcase:
---
"3+2*2"
" 3/2 "
" 3+5 / 2 "


### Code:
---
class Solution {
public:
    int calculate(string s) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    int calculate(string s) {
        long long result = 0, num = 0, lastNum = 0; // Initialize variables
        char op = '+'; // Start with '+' to handle the first number
        
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            
            // If c is a digit, update num
            if (isdigit(c)) {
                num = num * 10 + (c - '0');
            }
            
            // If c is an operator or we're at the end of the string
            if (!isdigit(c) && !isspace(c) || i == s.length() - 1) {
                switch (op) {
                    case '+': result += lastNum; lastNum = num; break;
                    case '-': result += lastNum; lastNum = -num; break;
                    case '*': lastNum *= num; break;
                    case '/': lastNum /= num; break;
                }
                op = c; // Update the operator
                num = 0; // Reset num for the next number
            }
        }
        
        result += lastNum; // Add the last number to the result
        return result; // Return the evaluated result
    }
};


// Description: ===================================
/*
To evaluate the expression given in string `s` without using any built-in function, we can implement a basic calculator using 
a stack to handle the precedence of operators ('+', '-', '*', '/'). The algorithm processes the string from left to right, 
performing operations based on the current operator and the next number in the sequence.

### Steps to Solve:

1. **Initialize Variables**: Start with a variable to keep the current number (`num`), the last number (`lastNum`), and the 
     result (`result`). Also, initialize an operator variable (`op`) to '+' to handle the first number correctly.

2. **Iterate Through `s`**: Loop through each character in the string. If it's a digit, update `num` accordingly. If it's 
     an operator or you're at the end of the string, perform the operation based on the current `op`:

   - For '+', add `lastNum` to `result`, update `lastNum` to `num`, and reset `num`.
   - For '-', add `lastNum` to `result`, update `lastNum` to `-num`, and reset `num`.
   - For '*', multiply `lastNum` with `num`, update `lastNum`, and reset `num`.
   - For '/', divide `lastNum` by `num`, update `lastNum`, and reset `num`.

3. **Handle Whitespace**: Ignore any whitespace characters.

4. **Final Calculation**: After the loop, add `lastNum` to `result` to include the operation on the last number.

5. **Return Result**: The `result` variable now holds the evaluated value of the expression.


### Description:

This solution methodically processes the expression string, handling numbers and operators as they appear, and accounting for 
operator precedence using the `lastNum` variable. The algorithm smartly adds or subtracts the `lastNum` to the `result` only 
when it encounters a '+' or '-' operator, ensuring that multiplication and division are handled immediately with `lastNum`. 
This approach efficiently evaluates the given mathematical expression without using any built-in evaluation functions, adhering 
to the constraints of the task.

*/
