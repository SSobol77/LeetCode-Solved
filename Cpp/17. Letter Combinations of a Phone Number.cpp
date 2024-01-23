// 17. Letter Combinations of a Phone Number.

// Topic: Hash Table, String, Backtracking.


/*
### Task:
---
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].


### Testcase:
---
"23"
""
"2"


### Code:
---
class Solution {
public:
    vector<string> letterCombinations(string digits) {

    }
};

*/
// Solution: --------------------------------------

#include <vector>
#include <string>
#include <unordered_map>

class Solution {
public:
    // Function to generate all possible letter combinations for a given phone number
    std::vector<std::string> letterCombinations(std::string digits) {
        // Handle the edge case where the input string is empty
        if (digits.empty()) {
            return {};
        }

        // Mapping from digits to their corresponding letters
        std::unordered_map<char, std::string> phoneMap = {
            {'2', "abc"}, {'3', "def"}, {'4', "ghi"},
            {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"},
            {'8', "tuv"}, {'9', "wxyz"}
        };

        std::vector<std::string> result; // Vector to store all the combinations
        std::string currentCombination;  // String to store the current combination
        backtrack(0, digits, currentCombination, result, phoneMap);
        return result;
    }

private:
    // Helper function for backtracking through the digit string
    void backtrack(int index, const std::string& digits, std::string& current, std::vector<std::string>& result, const std::unordered_map<char, std::string>& phoneMap) {
        // If the current index reaches the end of the digit string, add the current combination to the results
        if (index == digits.length()) {
            result.push_back(current);
            return;
        }

        // Get the current digit and its corresponding letters
        char digit = digits[index];
        const std::string& letters = phoneMap.at(digit);

        // Iterate through each letter and perform backtracking
        for (char letter : letters) {
            current.push_back(letter); // Add the letter to the current string
            backtrack(index + 1, digits, current, result, phoneMap); // Move to the next digit
            current.pop_back();  // Backtrack by removing the last character
        }
    }
};

// Description: ===================================
/*
### Comments Explanation:

- **General Description**: Each function and significant block within the function is preceded by a comment explaining its purpose.

- **Edge Case Handling**: A comment explains the handling of the edge case where the input string is empty.

- **Mapping Description**: A comment is added to describe the purpose of the `phoneMap` unordered_map.

- **Recursive Backtracking**: Comments are added within the `backtrack` function to explain each step of the recursive backtracking process, including adding a letter, moving to the next digit, and backtracking by removing the last character.

These comments should make the code more understandable and easier to follow, especially for someone who might be seeing it for the first time.


### Explanation:

1. **Base Case**: If the input string `digits` is empty, we return an empty vector.

2. **Hash Table for Digit-Letter Mapping**: The `phoneMap` unordered_map maps each digit to its corresponding string
   of letters.

3. **Backtracking Function**: The `backtrack` function is used to explore all possible combinations of letters.
   It takes the current index in the digit string, the current string being formed (`current`), and addseach possible
   letter for the current digit to `current`. The function then calls itself recursively for the next digit.

4. **Result**: The vector `result` contains all the possible letter combinations.

This implementation is efficient and adheres to the constraints of the problem. The backtracking approach ensures
that all combinations are explored without any repetitions.

*/
