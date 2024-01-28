// 3019. Number of Changing Keys.

// Topic:

/*
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
class Solution {
public:
    int countKeyChanges(string s) {
        
    }
};

*/


// Solution:   -------------------------------------------------------------------------------------------


#include <string> // Include the string library to use the std::string type
#include <algorithm> // Include the algorithm library for std::tolower function

// Define a Solution class to encapsulate the solution
class Solution {
public:
    // Function to count the number of key changes while typing a given string
    int countKeyChanges(std::string s) {
        // Check if the input string is empty; return 0 as no key changes are possible
        if (s.empty()) return 0;

        // Initialize count to 0 to keep track of the number of key changes
        int count = 0;
        // Convert the first character to lowercase and store it as the last character used
        char lastChar = std::tolower(s[0]);

        // Iterate through the string starting from the second character
        for (int i = 1; i < s.size(); ++i) {
            // Convert the current character to lowercase
            char currentChar = std::tolower(s[i]);
            // Check if the current character is different from the last character used
            if (currentChar != lastChar) {
                ++count; // Increment the key change count
                lastChar = currentChar; // Update the last character used to the current character
            }
        }

        // Return the total count of key changes
        return count;
    }
};



// Description:
/*

In this C++ code defines a class named `Solution` with a member function `countKeyChanges` that calculates the number of times
a user changes keys while typing a given string. The algorithm operates as follows:

1. **Initial Check**: The function begins by checking if the input string `s` is empty. If it is, the function immediately 
     returns `0`, indicating that no key changes have occurred because no keys were pressed.

2. **Initialization**: The function initializes a variable `count` to `0`. This variable will keep track of the number of 
     key changes. It also initializes a variable `lastChar` to the lowercase version of the first character in the string. 
     This is done using the `std::tolower` function, which converts a given character to its lowercase equivalent. The purpose 
     of converting characters to lowercase is to ignore changes between uppercase and lowercase versions of the same letter, 
     as per the problem statement.

3. **Iteration**: The function then enters a loop that iterates over the string starting from the second character (index `1`) 
     to the end of the string. For each character, it performs the following steps:

   - Converts the current character to lowercase and stores it in `currentChar`.

   - Compares `currentChar` with `lastChar`. If they are different, it indicates a key change, so the function increments `count` 
     by `1` and updates `lastChar` to `currentChar` to track the most recent key used.

4. **Return Result**: After iterating through the entire string, the function returns the total `count` of key changes.

In summary, the algorithm converts each character to lowercase to neutralize the effect of shift or caps lock modifiers and counts 
the number of times consecutive characters differ, which indicates a key change.

*/
