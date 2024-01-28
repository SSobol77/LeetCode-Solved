# 3019. Number of Changing Keys.

# Topic:

"""
# Task:
You are given a 0-indexed string s typed by a user. Changing a key is defined as using a key different from the last used key. 
For example, s = "ab" has a change of a key while s = "bBBb" does not have any.

Return the number of times the user had to change the key.

Note: Modifiers like shift or caps lock won't be counted in changing the key that is if a user typed the letter 'a' and 
      then the letter 'A' then it will not be considered as a changing of key.

Example 1:
Input: s = "aAbBcC"
Output: 2
Explanation: 
    From s[0] = 'a' to s[1] = 'A', there is no change of key as caps lock or shift is not counted.
    From s[1] = 'A' to s[2] = 'b', there is a change of key.
    From s[2] = 'b' to s[3] = 'B', there is no change of key as caps lock or shift is not counted.
    From s[3] = 'B' to s[4] = 'c', there is a change of key.
    From s[4] = 'c' to s[5] = 'C', there is no change of key as caps lock or shift is not counted.

Example 2:
Input: s = "AaAaAaaA"
Output: 0
Explanation: There is no change of key since only the letters 'a' and 'A' are pressed which does not require change of key.

Constraints:
1 <= s.length <= 100
s consists of only upper case and lower case English letters.

Hint 1:
Change all the characters to lowercase and then return the number of indices where the character does not match with 
the last index character.


# Testcase:
"aAbBcC"
"AaAaAaaA"

# Code:
class Solution:
    def countKeyChanges(self, s: str) -> int:
        

"""
### Solution:   -------------------------------------------------------------------------------------------

class Solution:
    def countKeyChanges(self, s: str) -> int:
        # Check if the string is empty; return 0 as no key changes are possible
        if not s:
            return 0

        # Initialize count to 0 to keep track of the number of key changes
        count = 0
        # Convert the first character to lowercase and store it as the last character used
        last_char = s[0].lower()

        # Iterate through the string starting from the second character
        for i in range(1, len(s)):
            # Convert the current character to lowercase
            current_char = s[i].lower()
            # Check if the current character is different from the last character used
            if current_char != last_char:
                count += 1  # Increment the key change count
                last_char = current_char  # Update the last character used to the current character

        # Return the total count of key changes
        return count


### Description:    ================================================================================================
'''
To solve the "Number of Changing Keys" problem in Python, we'll implement a function `countKeyChanges` that follows the 
logic similar to the C++ solution you provided earlier. This function will iterate through the given string, `s`, and 
count the number of times the character changes from the previous character, ignoring case differences. 

### Description:

his Python solution defines a class `Solution` with a method `countKeyChanges`, which accepts a string `s` as its parameter. 
The method works as follows:

1. It begins by checking if the input string `s` is empty. If it is, the method returns `0`, indicating that no key changes have occurred.
2. It initializes a variable `count` to `0`, which will keep track of the number of key changes.
3. It sets `last_char` to the lowercase version of the first character in the string. This step ensures that changes between uppercase and lowercase versions of the same letter are ignored.
4. The method then iterates through the string starting from the second character. For each character, it converts the character to lowercase and checks if it differs from `last_char`. If so, it increments `count` and updates `last_char` to the current character.
5. After iterating through the entire string, the method returns the total count of key changes.

'''
