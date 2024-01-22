// 3014. Minimum Number of Pushes to Type Word I.

/*
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
class Solution {
public:
    int minimumPushes(string word) {

    }
};

*/
// Solution: ----------------------------------

#include <string>
using namespace std;

class Solution {
public:
    int minimumPushes(string word) {
        int length = word.length();
        int pushes = 0;

        // Iterate through each character in the word
        for (int i = 0; i < length; ++i) {
            // Calculate the number of pushes required for this character
            int keysNeeded = (i / 8) + 1;
            // Add to the total number of pushes
            pushes += keysNeeded;
        }

        return pushes;
    }
};

// Test cases
int main() {
    Solution sol;

    cout << sol.minimumPushes("abcde") << endl;      // Should output 5
    cout << sol.minimumPushes("xycdefghij") << endl; // Should output 12

    return 0;
}


// Description: =========================================
/*
To implement the solution for the "Minimum Number of Pushes to Type Word I" problem in C++, we
will create a class `Solution` with a public method `minimumPushes` that takes a string `word`
as its argument and returns an integer representing the minimum number of key presses required
to type the word.

The key idea is to distribute the letters of the word as evenly as possible across the 8 keys on
the keypad, from 2 to 9. Each letter requires a number of key presses corresponding to its position
on the assigned key. To minimize the total number of key presses, we aim to place as many letters
as possible in the first position on each key, then in the second position, and so on.


In this implementation, we iterate through each character of the word, calculating the number of
key presses needed for each one based on its position in the sequence (`i / 8 + 1`). The total number
of key presses is summed up in `pushes`, which is then returned. The `main` function includes test
cases to demonstrate the functionality of the `minimumPushes` method.

*/
