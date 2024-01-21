"""
# 17. Letter Combinations of a Phone Number.


# Topic: Hash Table, String, Backtracking.


# Task:
-------------
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that 
the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does 
not map to any letters.

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

# Testcase:
--------------------
"23"
""
"2"

# Code:
--------------------
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
"""
# Solution:
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, return an empty list.
        if not digits:
            return []
        
        # Mapping from digits to letters as on a telephone keypad.
        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        # Recursive function to perform backtracking.
        def backtrack(index, path):
            # If the current path length equals the digits length, add the combination.
            if index == len(digits):
                combinations.append(''.join(path))
                return
            
            # Get the letters corresponding to the current digit.
            letters = digit_to_letters[digits[index]]
            # Loop through these letters.
            for letter in letters:
                # Add the letter to the current path.
                path.append(letter)
                # Recurse with the next digit.
                backtrack(index + 1, path)
                # Backtrack: remove the last added letter and try the next one.
                path.pop()

        # List to store all the combinations.
        combinations = []
        # Start the backtracking process from the first digit.
        backtrack(0, [])
        # Return the generated combinations.
        return combinations


# Description:
'''
To solve the "Letter Combinations of a Phone Number" problem, we need to generate all possible letter 
combinations for a given string of digits, where each digit maps to a set of letters as it would appear 
on a telephone keypad. The problem can be effectively solved using backtracking.

Here's a step-by-step approach:
------------------------------------
Mapping: 
First, we need a mapping from digits to their corresponding letters. For example, '2' maps to 'abc', 
'3' maps to 'def', and so on.

Base Case: 
If the input string is empty, we should return an empty list, as there are no combinations possible.

Backtracking Function: 
We'll use a recursive function that takes the current combination of letters and the next digit to process.
It will add each possible letter from the current digit to the current combination and then call itself 
recursively with the next digit.

Iterating through Digits: 
Start from the first digit, use the mapping to get the corresponding letters, and for each letter, recurse 
for the next digit.

In this code:
-------------
    digit_to_letters is a dictionary mapping each digit to its corresponding letters.
    backtrack is a recursive function that builds combinations.
    We maintain a path list to keep track of the current combination of letters.
    When the length of the path equals the length of digits, we add the combination to the result.
    The main function, letterCombinations, initializes the process and returns the final list of combinations.

This solution covers all the constraints and should work efficiently for digit strings up to length 4.

 
'''
