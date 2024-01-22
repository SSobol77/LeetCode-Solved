# 3016. Minimum Number of Pushes to Type Word II.

"""
### Task:
---
You are given a string word containing lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.

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
Input: word = "xyzxyzxyzxyz"
Output: 12
Explanation: The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> one push on key 3
"z" -> one push on key 4
Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
It can be shown that no other mapping can provide a lower cost.
Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.

Example 3:
Input: word = "aabbccddeeffgghhiiiiii"
Output: 24
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
"f" -> one push on key 7
"g" -> one push on key 8
"h" -> two pushes on key 9
"i" -> one push on key 9
Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.
It can be shown that no other mapping can provide a lower cost.

Constraints:
1 <= word.length <= 10^5
word consists of lowercase English letters.


### Testcase:
---
"abcde"
"xyzxyzxyzxyz"
"aabbccddeeffgghhiiiiii"

### Code:
---
class Solution:
    def minimumPushes(self, word: str) -> int:


"""
### Solution:

from collections import Counter
from math import ceil

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the frequency of each letter in the word
        freq = Counter(word)

        # Sort letters by frequency in descending order
        # This ensures that the most frequent characters are considered first
        sorted_letters = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Initialize the total pushes counter
        total_pushes = 0
        keys = 8  # Total number of keys available (2 to 9)

        # Iterate through sorted letters and their frequencies
        for i, (_, count) in enumerate(sorted_letters):
            # Calculate the position on the key for each letter
            # The position is determined by the index in the sorted list, adjusted for the number of keys
            # We use ceil to ensure that each new set of 8 letters starts on a new key
            pushes = ceil((i + 1) / keys)

            # Add to the total number of pushes
            # Multiply the count of each letter by the number of pushes required for its key position
            total_pushes += count * pushes

        return total_pushes

# Test cases
sol = Solution()
print(sol.minimumPushes("abcde"))              # Output: 5
print(sol.minimumPushes("xyzxyzxyzxyz"))       # Output: 12
print(sol.minimumPushes("aabbccddeeffgghhiiiiii"))  # Output: 24

### Description:
'''

In this code:

- We first use `Counter` to count the frequency of each letter in the given word.
- The letters are then sorted in descending order based on their frequency, ensuring that the most frequently occurring letters are assigned to keys requiring the fewest pushes.
- We iterate through these sorted letters, and for each letter, we calculate its position on the keypad. This position is determined by dividing the index in the sorted list by the number of keys, using `ceil` to ensure that each set of 8 letters starts on a new key.
- The total number of pushes is calculated by multiplying the frequency of each letter by the number of pushes required for its position on the key.
- Finally, the total number of pushes is returned, representing the minimum number of pushes needed to type the word with an optimally remapped keypad.


Since we can remap the keys, our goal is to assign the most frequent characters to the first position on each key,
then the next most frequent characters to the second position, and so on.

We need to consider that each key can hold multiple letters, and the number of pushes for a letter is determined
by its position on the key.

Here's the revised strategy:

1. Count the frequency of each letter in the word.
2. Sort the letters by frequency in descending order.
3. Distribute the letters across the keys, starting from the first position of the first key (key 2). When the first
   positions of all keys are filled, move to the second positions, and so on.
4. Calculate the total number of pushes by considering the position of each letter on its respective key.


This implementation ensures that the most frequent characters are assigned to keys with the fewest required pushes,
thereby minimizing the total number of pushes.


'''
