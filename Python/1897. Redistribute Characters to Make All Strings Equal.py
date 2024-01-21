# 1897. Redistribute Characters to Make All Strings Equal.

# Topic: Hash Table, String, Counting.

'''
# Task:
------------
You are given an array of strings words (0-indexed).
In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any 
character from words[i] to any position in words[j].
Return true if you can make every string in words equal using any number of operations, and false otherwise.

Example 1:
Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.

Example 2:
Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.

Hint 1:
Characters are independent—only the frequency of characters matters.
Hint 2:
It is possible to distribute characters if all characters can be divided equally among all strings.


# Testcase:
-------------------
["abc","aabc","bc"]
["ab","a"]

# Code:
-------------------
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
'''
#  Solution:
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        from collections import Counter

        # Count the frequency of each character across all strings.
        # The join() method concatenates all the strings in 'words' into a single string,
        # and Counter() then counts the frequency of each character in this combined string.
        char_count = Counter("".join(words))

        # Iterate over each character and its count in the character count dictionary.
        for char, count in char_count.items():
            # Check if the frequency of each character is divisible by the number of words.
            # If it's not divisible, return False, as it's impossible to evenly distribute
            # this character across all strings.
            if count % len(words) != 0:
                return False

        # If all character counts are divisible by the number of words,
        # it means we can redistribute the characters to make all strings equal.
        # Therefore, return True.
        return True

# Test cases
solution = Solution()
print(solution.makeEqual(["abc", "aabc", "bc"]))  # Expected Output: True
print(solution.makeEqual(["ab", "a"]))            # Expected Output: False

# Description:
'''
To solve this task, we need to determine whether the characters in all strings in the words list 
can be redistributed to form strings of equal content. The key point is that each character's 
frequency must be divisible by the number of strings in words for this to be possible.

Here's how we can implement this logic in Python:

  1.  Count the frequency of each character across all strings in words.
  2.  Check if each character's frequency is divisible by the length of the words list.

In this code, we use Python's Counter class from the collections module to count the frequency of 
each character. Then, we iterate over these counts and check if each count is divisible by the number
of words. If we find a character whose count is not divisible, we immediately return False. If all 
counts are divisible, we return True.

This solution efficiently addresses the problem using hash table (via Counter) and follows the hints
provided, focusing on the frequency of characters rather than their position in the strings.

If both conditions are met for every character, we can return True; otherwise, False.
Each part of the code is explained in the comments, helping to understand how it works step by step.
This includes how the characters are counted, the logic behind checking divisibility, and why these 
checks lead to the final conclusion of whether it's possible to redistribute characters to make all 
strings equal.

'''
