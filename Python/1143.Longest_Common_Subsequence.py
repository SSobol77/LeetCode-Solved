# 1143. Longest Common Subsequence.


# Topic: String, Dynamic Programming.


"""
## Task:
---------
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no 
common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) 
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

Hint 1:
Try dynamic programming. DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].

Hint 2:
DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise



## Testcase:
-------------
"abcde"
"ace"
"abc"
"abc"
"abc"
"def"


## Code:
----------
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

"""
# Solution
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Swap text1 and text2 if text1 is shorter than text2
        # This is done to use less space since we only keep two rows in memory
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        # Initialize two arrays with length of the shorter string + 1
        # 'prev' will hold the values of the previous row, 'current' for the current row
        prev = [0] * (len(text2) + 1)
        current = [0] * (len(text2) + 1)

        # Iterate through each character of the longer string (text1)
        for i in range(1, len(text1) + 1):
            # Iterate through each character of the shorter string (text2)
            for j in range(1, len(text2) + 1):
                # If characters match, add 1 to the diagonal value in the DP table
                if text1[i - 1] == text2[j - 1]:
                    current[j] = prev[j - 1] + 1
                else:
                    # If no match, take the max value from left or top cell
                    current[j] = max(prev[j], current[j - 1])

            # Swap the rows for the next iteration
            # 'prev' becomes the current row, and 'current' is reset for the next iteration
            prev, current = current, prev

        # The last filled row 'prev' contains the length of the LCS at its last cell
        return prev[len(text2)]



# Description
'''
The problem of finding the longest common subsequence (LCS) between two strings is a classic example of dynamic programming.
The LCS is the longest sequence that can be derived from both strings without reordering any of the characters. 

### Approach
--------------
The dynamic programming approach involves creating a 2D array `DP` where each cell `DP[i][j]` represents the length of the 
longest common subsequence between the first `i` characters of `text1` and the first `j` characters of `text2`.

- Initialize a 2D array `DP` with dimensions `(len(text1) + 1) x (len(text2) + 1)`. Each cell is initialized to 0.
- Iterate through each character in `text1` and `text2`.
  - For each pair of characters `(i, j)`:
    - If `text1[i - 1] == text2[j - 1]`, then `DP[i][j] = DP[i - 1][j - 1] + 1`. This case represents a match, and we add 1 to the LCS found until the previous characters.
    - Otherwise, `DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])`. This case represents no match, and we take the maximum LCS found by either skipping the current character of `text1` or `text2`.
- The value in `DP[len(text1)][len(text2)]` gives the length of the LCS.

### Example:
-------------
Consider `text1 = "abcde"` and `text2 = "ace"`.
- The `DP` array will be initialized with zeros in a 6x4 grid (since we include the 0th index).
- While iterating, when both characters match (like 'a' with 'a', 'c' with 'c', 'e' with 'e'), we add 1 to the diagonal value.
- The final cell `DP[5][3]` will have the value `3`, representing the LCS length `"ace"`.


This solution has a time complexity of O(m*n) and a space complexity of O(m*n), where m and n are the lengths of `text1` and `text2`, respectively.### Optimized Longest Common Subsequence (LCS) Solution

#### Overview
This solution efficiently computes the length of the Longest Common Subsequence (LCS) between two strings, `text1` and `text2`, by employing dynamic programming with optimized space complexity. The LCS is defined as the longest sequence that can be derived from both strings by deleting some characters (possibly none) without reordering the remaining characters.

#### Key Features
- **Space Optimization:** Uses only two 1D arrays (`prev` and `current`), reducing the space complexity to O(min(m, n)), where m and n are the lengths of the input strings. This is a significant improvement over the classic approach that uses a 2D array with space complexity O(m * n).
- **Dynamic Programming:** Continuously updates the LCS length while iterating through the characters of both strings, ensuring an efficient bottom-up calculation.
- **Row Swapping Technique:** Swaps the two arrays (`prev` and `current`) after each iteration to reuse and update the LCS values without the need for a full 2D matrix.

#### How It Works
1. **Initialization:** The solution first ensures that `text1` is the longer string for optimal space usage. Two arrays, `prev` and `current`, each of length equal to the length of the shorter string (`text2`) plus one, are initialized to store LCS lengths.

2. **Character-wise Comparison:** The solution iterates through each character of `text1` and `text2`. For each pair of characters, it calculates the LCS length based on whether the characters match or not.
   - If the characters match, the LCS length is updated by adding 1 to the diagonal value (from `prev`), representing an extension of the LCS found until the previous characters.
   - If they don't match, it takes the maximum LCS length found by either excluding the current character of `text1` or `text2`.

3. **Row Swapping:** After each iteration over `text2`, the roles of `prev` and `current` are swapped. The `prev` row now represents the most recently computed LCS values, and `current` is reset for the next iteration.

4. **Final Output:** The LCS length is obtained from the last cell of the `prev` array, which contains the final computed value.

#### Advantages
- **Improved Performance:** Reduces memory usage, potentially improving cache efficiency and reducing runtime for large input strings.
- **Maintains Accuracy:** Accurately computes the LCS length while optimizing space usage.
- **General Applicability:** Can be applied to a wide range of problems requiring LCS computation, including text comparison, bioinformatics, and more.

This solution is particularly advantageous in scenarios where space complexity is a concern, especially when dealing with large strings.

'''
