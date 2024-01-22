# 3014. Minimum Number of Pushes to Type Word I.

"""
### Task:

You are given a string word containing distinct lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can
be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need
to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be
remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find
the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do
not map to any letters.


Example 1:

Input: word = "abcde"
Output: 5
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.

Example 2:

Input: word = "xycdefghij"
Output: 12
Explanation: The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> two pushes on key 2
"c" -> one push on key 3
"d" -> two pushes on key 3
"e" -> one push on key 4
"f" -> one push on key 5
"g" -> one push on key 6
"h" -> one push on key 7
"i" -> one push on key 8
"j" -> one push on key 9
Total cost is 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = 12.
It can be shown that no other mapping can provide a lower cost.

Constraints:
1 <= word.length <= 26
word consists of lowercase English letters.
All letters in word are distinct.

Hint 1:
We have 8 keys in total. We can type 8 characters with one push each, 8 different characters with two
pushes each, and so on.
Hint 2:
The optimal way is to map letters to keys evenly.

### Testcase:
---
"abcde"
"xycdefghij"


### Code:
---
class Solution:
    def minimumPushes(self, word: str) -> int:

"""
### Solution:  ----------------------------------------------

class Solution:
    def minimumPushes(self, word: str) -> int:
        length = len(word)
        pushes = 0

        # Distribute characters across keys
        for i in range(length):
            # Find the number of keys needed to reach the current character
            keys_needed = (i // 8) + 1
            # Add to the total number of pushes
            pushes += keys_needed

        return pushes

# Test cases
sol = Solution()
print(sol.minimumPushes("abcde"))      # Should output 5
print(sol.minimumPushes("xycdefghij")) # Should output 12


### Description: =============================================
'''
To solve this problem, we can follow the hints provided. We have 8 keys available (keys 2 to 9), and each key
can be mapped to an arbitrary number of characters, but each character must be mapped to exactly one key. The
goal is to minimize the total number of key presses required to type the given word.

The strategy is to distribute the characters of the word as evenly as possible among the keys. The characters
mapped to a key will require a number of pushes corresponding to their position on that key. For example, if a
key is mapped to "a", "b", "c", then typing "a" requires 1 push, "b" requires 2 pushes, and "c" requires 3 pushes.

Here's a step-by-step strategy to implement the `minimumPushes` method:
1. Calculate the length of the word.
2. Distribute the characters as evenly as possible across the 8 keys.
3. Calculate the total number of pushes needed based on this distribution.

We'll implement this strategy in the `minimumPushes` method of the `Solution` class.


This code first calculates the length of the word. Then, it iterates through each character, determining the number
of key presses needed for each character based on its position in the sequence. The total number of key presses is
accumulated in the `pushes` variable, which is returned at the end.

'''
