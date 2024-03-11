# 241. Different Ways to Add Parentheses.

# Topic: Math, String, Dynamic Programming, Recursion, Memoization.

"""
### Task:
---
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 10^4.

Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 
Constraints:
1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].


### Testcase:
---
2-1-1"
"2*3-4*5"


### Code:
---
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
    
"""
### Solution: --------------------------------------

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Base case: if the expression is just a number, return it as an integer in a list
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        # Iterate through each character in the expression
        for i, char in enumerate(expression):
            # If the character is an operator, we divide the expression into two parts
            if char in "-+*":
                # Recursively solve the left part of the expression
                left = self.diffWaysToCompute(expression[:i])
                # Recursively solve the right part of the expression
                right = self.diffWaysToCompute(expression[i+1:])
                
                # Combine the results from the left and right parts using the current operator
                for l in left:
                    for r in right:
                        if char == '+':
                            results.append(l+r)
                        elif char == '-':
                            results.append(l-r)
                        else:  # char == '*'
                            results.append(l*r)
        # Return the list of all possible results
        return results

# Example usage
sol = Solution()
print(sol.diffWaysToCompute("2-1-1"))  # Output: [0, 2]


### Description: ===================================
'''
To tackle the problem of evaluating all possible outcomes of an arithmetic expression by adding parentheses in various positions, 
a recursive approach can be highly effective. The core idea revolves around partitioning the expression at each operator encountered 
('+', '-', '*'), which results in two separate expressions: one to the left and another to the right of the operator. Each of these 
sub-expressions can contain further operators, leading to more potential splits and subsequent recursive calls.

The process unfolds as follows:

1. **Iterate Through the Expression**: Scan the given expression character by character, identifying operators that serve as potential 
     points for division.

2. **Recursive Division**: Upon encountering an operator, recursively invoke the solution method on the left and right segments of the 
     expression, demarcated by the operator. This recursive action continues until reaching sub-expressions that contain no operators, 
     effectively boiling down to individual numbers.

3. **Combine Results**: With the results from the left and right sub-expressions at hand (each possibly containing multiple outcomes due 
     to different parenthetical groupings within), apply the current operator to pair up results from both sides. This operation yields 
     all possible outcomes for the current division.

4. **Base Case**: The recursion's base case is reached when a sub-expression is purely numerical, devoid of any operators. At this 
     juncture, the numerical value is directly returned as the sole result.

5. **Memoization (Optional Enhancement)**: To optimize performance, especially for expressions with repeated sub-expressions, memoization 
     can be employed. This technique involves caching the results of sub-expressions to prevent redundant calculations in future recursive 
     calls.

This recursive strategy effectively explores all conceivable ways to insert parentheses into the original expression, calculating the 
distinct results each configuration yields. The method is comprehensive, ensuring that no potential grouping is overlooked, thereby 
providing a complete set of possible outcomes.

'''
