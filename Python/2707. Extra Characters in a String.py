# 2707. Extra Characters in a String.

# Topic: Array, Hash Table, String, Dynamic Programming, Trie.

"""
### Task:
---
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings 
such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

Example 1:
Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused 
character (at index 4), so we return 1.

Example 2:
Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at 
indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
 
Constraints:
1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words

Hint 1:
Can we use Dynamic Programming here?
Hint 2:
Define DP[i] as the min extra character if breaking up s[0:i] optimally.


### Testcase:
---
"leetscode"
["leet","code","leetcode"]
"sayhelloworld"
["hello","world"]


### Code:
---
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
"""
### Solution: --------------------------------------

from functools import cache
from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
        Calculate the minimum number of extra characters left over after breaking up
        the string s into substrings found in dictionary.

        This is achieved by using dynamic programming to find the minimum number
        of characters that cannot be used to form words from the dictionary.

        Args:
        s (str): The input string.
        dictionary (List[str]): A list of valid substrings.

        Returns:
        int: The minimum number of extra characters not used in the substrings.
        """
        # Convert dictionary list into a set for faster lookups
        word_set = set(dictionary)
        n = len(s)

        @cache
        def dp(i: int) -> int:
            """
            Dynamic programming function to find the minimum extra characters for the substring s[:i].

            It uses memoization to store and reuse the results of subproblems, thereby reducing the
            computational complexity.

            Args:
            i (int): The current position in the string s.

            Returns:
            int: The minimum number of extra characters for the substring s[:i].
            """
            # Base case: no extra characters if i is 0
            if i == 0:
                return 0

            # Assume that all characters up to i are extra, then subtract for each matching word
            # dp(i - 1) + 1 represents the scenario where the current character is considered extra
            min_extra = dp(i - 1) + 1

            # Iterate through each word in the dictionary and check if it matches a substring
            # ending at the current position i
            for word in word_set:
                word_len = len(word)
                if i >= word_len and s[i - word_len:i] == word:
                    # If a word is found, update min_extra to the minimum of its current value
                    # and the value of dp at the position where the word starts (i - word_len)
                    min_extra = min(min_extra, dp(i - word_len))

            return min_extra

        # Compute the result for the entire string and clear the cache
        result = dp(n)
        dp.cache_clear()

        return result

# Test cases
solution = Solution()
print(solution.minExtraChar("leetscode", ["leet", "code", "leetcode"]))  # Output: 1
print(solution.minExtraChar("sayhelloworld", ["hello", "world"]))  # Output: 3


### Description: ===================================
'''
### Algorithm Description:

1. **Dictionary Conversion:** The list of dictionary words is converted to a set for efficient lookups.

2. **Dynamic Programming Function (`dp`):** This function computes the minimum number of extra characters for each 
   substring `s[:i]` (from the start of the string `s` up to the position `i`). It uses memoization to store results of subproblems.

3. **Base Case:** If `i` is 0 (start of the string), there are no extra characters, so it returns 0.

4. **Initialization of `min_extra`:** For each position `i`, it initially assumes that every character up to `i` is extra. 

5. **Checking Substrings Against Dictionary Words:** For each word in the dictionary, the function checks if there is a match at the 
   end of the current substring `s[:i]`. If a match is found, it updates the `min_extra` to the minimum of its current value and the 
   value from the start of the matched word.

6. **Result Computation:** The function `dp(n)` computes the result for the entire string. The cache is then cleared to free up memory.

7. **Return Value:** The function returns the minimum number of extra characters that are left over after optimally breaking up the 
   string `s` into substrings found in the dictionary. 

This solution efficiently computes the minimum extra characters using dynamic programming, making it suitable for larger strings and
dictionaries.

'''
