 # 1239. Maximum Length of a Concatenated String with Unique Characters

# Topic: Array, String, Backtracking,Bit Manipulation.

"""
### Task:
---
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr
that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without
changing the order of the remaining elements.

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.

Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.

Hint 1
You can try all combinations and keep mask of characters you have.
Hint 2
You can use DP.


### Testcase:
---
["un","iq","ue"]
["cha","r","act","ers"]
["abcdefghijklmnopqrstuvwxyz"]


### Code:
---
class Solution:
    def maxLength(self, arr: List[str]) -> int:

"""
### Solution: --------------------------------------

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Recursive function to perform backtracking
        def backtrack(index, current_mask):
            # Base case: if we have considered all strings
            if index == len(arr):
                # Count the number of set bits (unique characters) and return
                return bin(current_mask).count('1')

            # Calculate maximum length without including the current string
            max_length = backtrack(index + 1, current_mask)
            string_mask = 0  # Bit mask for the current string
            is_unique = True  # Flag to check if characters are unique

            # Create a bit mask for the current string
            for char in arr[index]:
                char_index = ord(char) - ord('a')  # Map character to bit position
                if string_mask & (1 << char_index):  # Check for duplicate character
                    is_unique = False
                    break
                string_mask |= (1 << char_index)  # Add character to mask

            # If the string has unique characters and does not conflict with the current mask
            if is_unique and not (current_mask & string_mask):
                # Include the string in the combination and calculate the length
                max_length = max(max_length, backtrack(index + 1, current_mask | string_mask))

            return max_length

        # Start backtracking from the first string with an empty mask
        return backtrack(0, 0)

# Example usage
sol = Solution()
print(sol.maxLength(["un","iq","ue"]))  # Output: 4


### Description: ===================================
'''

### Comments Explanation:

- **Backtracking Function**: `backtrack` is a recursive function that takes two parameters: the current index in the array `arr` and a bit mask `current_mask` representing the characters used so far in the concatenation.
- **Base Case**: When `index` equals the length of `arr`, the function returns the count of unique characters in the current concatenation.
- **Bit Masking**: For each string, a bit mask `string_mask` is created to represent its characters. This is done by setting the bit corresponding to each character's position in the alphabet.
- **Unique Characters Check**: The function checks if the current string introduces duplicate characters by comparing `string_mask` with `current_mask`.
- **Recursive Calls**: The function makes two recursive calls:
  - One to calculate the maximum length without including the current string (`backtrack(index + 1, current_mask)`).
  - Another to calculate the maximum length including the current string, if it's valid (`backtrack(index + 1, current_mask | string_mask)`).
- **Maximum Length**: The function returns the maximum length found among all combinations.

This commented code provides clarity on the algorithm's steps and the logic behind each part of the code, making it easier to understand and maintain.


To solve the problem of finding the maximum length of a concatenated string with unique characters, we can use a combination of backtracking and bit manipulation. The approach involves trying all combinations of the given strings while ensuring that no character is repeated in the concatenated result. The hints suggest using a mask of characters and possibly leveraging dynamic programming.

Let's break down the solution:

1. **Backtracking**: We'll explore all possible combinations of the strings in `arr`. For each string, we have two choices: include it in the current combination or exclude it. We only include a string if it doesn't introduce a duplicate character.

2. **Bit Manipulation**: To efficiently check for unique characters and maintain the current state, we'll use an integer as a bit mask. Each bit in the mask represents whether a particular character ('a' to 'z') is present in the current combination. This allows us to quickly check for duplicates and update the mask when adding a new string.

3. **Dynamic Programming**: This approach can be optimized by remembering the results of previous combinations to avoid recomputation (memoization), although in this specific problem, the straightforward backtracking approach is typically sufficient due to the small size of the input.


### Explanation:

- The `backtrack` function explores all combinations starting from a given index.
- `current_mask` keeps track of the characters used so far.
- For each string in `arr`, we create a `string_mask` representing its characters.
- If `string_mask` has no common bits with `current_mask` (no duplicate characters), we recursively call `backtrack` including this string.
- The base case of recursion is when the index reaches the length of `arr`. At this point, we count the number of bits in `current_mask` (which represents the length of the unique character string formed) and return it.
- The solution computes the maximum length among all possible combinations.

This approach ensures that we consider all possible unique character combinations and efficiently compute the maximum length.

'''
