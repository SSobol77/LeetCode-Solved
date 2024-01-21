"""
# 22. Generate Parentheses.


# Topic: String, Dynamic Programming, Backtracking.


# Task:
----------------
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8



# Testcase:
---------------
3
1

# Code:
---------------
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    
"""
# Solution:
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Define a helper function to generate combinations
        def backtrack(current_str, open_count, close_count):
            # If the current string has the desired length, add it to the result
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            # If we can add an open parenthesis, do so and recurse with an incremented open_count
            if open_count < n:
                backtrack(current_str + '(', open_count + 1, close_count)
            # If we can add a close parenthesis, do so and recurse with an incremented close_count
            if close_count < open_count:
                backtrack(current_str + ')', open_count, close_count + 1)

        result = []  # Initialize a list to store the generated combinations
        backtrack('', 0, 0)  # Start the recursion with an empty string and both counts at 0
        return result  # Return the list containing all well-formed parentheses combinations


# Description:
'''
In this code:

1. We define a helper function backtrack that takes three parameters:
   - current_str: the current string being constructed.
   - open_count: the count of open parentheses.
   - close_count: the count of close parentheses.

2. In the backtrack function:
   - If the length of current_str is equal to 2 * n, we have generated a valid combination of well-formed 
     parentheses, so we append it to the result.
   - If the open_count is less than n, we can add an open parenthesis and call the backtrack function 
     recursively with an incremented open_count.
   - If the close_count is less than the open_count, we can add a close parenthesis and call the backtrack 
     function recursively with an incremented close_count.

3. We initialize an empty list result to store the generated combinations.

4. We call the backtrack function initially with an empty string and both open_count and close_count set to 0.

5. Finally, we return the result list containing all the well-formed parentheses combinations.

You can use this Solution class to call the generateParenthesis method and pass in the value of n as an 
argument to generate the desired combinations.

'''
