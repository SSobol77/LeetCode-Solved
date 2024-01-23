// 22. Generate Parentheses.


// Topic: String, Dynamic Programming, Backtracking.



/*
### Task:
---
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8

### Testcase:
---
3
1


### Code:
---
class Solution {
public:
    vector<string> generateParenthesis(int n) {

    }
};

*/
// Solution: --------------------------------------

#include <vector>
#include <string>

class Solution {
public:
    // Main function to generate all combinations of well-formed parentheses
    std::vector<std::string> generateParenthesis(int n) {
        std::vector<std::string> result; // To store all valid combinations
        std::string current; // Current parenthesis string being formed
        backtrack(result, current, 0, 0, n); // Starting the backtracking process
        return result;
    }

private:
    // Helper function to perform backtracking
    void backtrack(std::vector<std::string>& result, std::string& current, int open, int close, int max) {
        // If the current string is a valid combination, add it to the result
        if (current.length() == max * 2) {
            result.push_back(current);
            return;
        }

        // Add an open parenthesis if we haven't reached the maximum number of open parentheses
        if (open < max) {
            current.push_back('(');
            backtrack(result, current, open + 1, close, max); // Recurse with one more open parenthesis
            current.pop_back(); // Backtrack by removing the last parenthesis
        }

        // Add a close parenthesis if we have more open than close parentheses
        if (close < open) {
            current.push_back(')');
            backtrack(result, current, open, close + 1, max); // Recurse with one more close parenthesis
            current.pop_back(); // Backtrack by removing the last parenthesis
        }
    }
};



// Description: ===================================
/*

### Comments Explanation:

- **Main Function**: A comment explains the purpose of the `generateParenthesis` function.

- **Initialization**: Comments describe the roles of `result` and `current`.

- **Backtracking Function**: An explanation of the `backtrack` helper function is given, detailing its role in the
  recursive generation of valid parentheses combinations.

- **Base Case**: A comment indicates when a valid combination is identified and added to the result.

- **Adding Parentheses**: Comments explain the conditions under which an open or close parenthesis is added to the
  current string.

- **Recursive Calls and Backtracking**: Each recursive call and subsequent backtracking step is explained.

These comments should make the code more readable and help others understand the logic and flow of the backtracking
algorithm used to generate well-formed parentheses.

To solve the problem of generating all combinations of well-formed parentheses for a given number `n`, we will
utilize backtracking. Backtracking is a suitable approach here as we need to explore all possible ways to arrange
parentheses and ensure they form a valid sequence. Let's implement the solution in C++:


### Explanation:

1. **Backtracking Function**: The `backtrack` function is designed to recursively build the string of parentheses.

2. **Base Case**: When the length of the current string is twice `n`, it implies a valid sequence is formed and it's
   added to the result vector.

3. **Adding Open Parentheses**: As long as the number of open parentheses is less than `n`, an open parenthesis `'('`
   can be added to the current string. Then the function is called recursively with incremented count of open parentheses.

4. **Adding Close Parentheses**: A close parenthesis `')'` is added only if the count of close parentheses is less than
   the count of open ones. This ensures the sequence remains valid. The function is then called recursively with
   incremented count of close parentheses.

5. **Backtracking**: After each recursive call, the last character is popped from the current string to backtrack and
   explore other possibilities.

This implementation efficiently generates all possible combinations of well-formed parentheses using a backtracking
approach, maintaining the constraints that the number of open and close parentheses should be equal and the sequence
should be valid at every stage of the recursion.



*/
