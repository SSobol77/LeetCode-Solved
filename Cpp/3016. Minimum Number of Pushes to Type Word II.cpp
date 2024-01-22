// 3016. Minimum Number of Pushes to Type Word II.


/*
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
class Solution {
public:
    int minimumPushes(string word) {

    }
};

*/
// Solution: -------------------------------------------


#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <cmath>

class Solution {
public:
    int minimumPushes(std::string word) {
        // Map to store the frequency of each letter
        std::unordered_map<char, int> freqMap;

        // Count the frequency of each letter in the word
        for (char c : word) {
            freqMap[c]++;
        }

        // Create a vector from elements of the map
        // This will store pairs of characters and their frequencies
        std::vector<std::pair<char, int>> freqList(freqMap.begin(), freqMap.end());

        // Sort the vector by frequency in descending order
        std::sort(freqList.begin(), freqList.end(), [](const auto &a, const auto &b) {
            return a.second > b.second;
        });

        // Initialize total pushes
        int totalPushes = 0;
        int keys = 8;  // Total number of keys available (2 to 9)

        // Assign letters to keys and calculate pushes
        for (int i = 0; i < freqList.size(); ++i) {
            // Determine the position of the letter on its key
            int pushes = (i / keys) + 1;
            // Add the total number of pushes for this letter
            totalPushes += freqList[i].second * pushes;
        }

        return totalPushes;
    }
};

// Test cases
int main() {
    Solution sol;
    std::cout << sol.minimumPushes("abcde") << std::endl;              // Output: 5
    std::cout << sol.minimumPushes("xyzxyzxyzxyz") << std::endl;       // Output: 12
    std::cout << sol.minimumPushes("aabbccddeeffgghhiiiiii") << std::endl;  // Output: 24
    return 0;
}

// Desciption:
/*

### In this code:

- We first use an `unordered_map` to count the frequency of each character in the word. This is done in the `for` loop where we iterate through each character in the word and update its count in the map.
- The map is then converted into a vector of pairs (`freqList`), each pair containing a character and its frequency. This allows us to sort the characters based on their frequency.
- The `std::sort` function is used to sort the vector in descending order of frequency. We use a lambda function as the comparator to specify that we want to sort based on the second element of each pair (the frequency).
- We iterate through this sorted vector, calculating the total number of pushes needed to type the word. The position of each letter on the keypad is determined by dividing its index in the sorted list by the number of keys and adding 1 to this quotient.
- The `main` function demonstrates the functionality of the `minimumPushes` method with test cases, printing the result for each test case.

To solve the "Minimum Number of Pushes to Type Word II" problem in C++, we will follow a strategy similar to the Python
and Java solutions. The key idea is to efficiently distribute the characters in the word across the keys of a telephone
keypad, so that the total number of key presses is minimized. This is achieved by assigning the most frequent characters
to positions on the keys that require the fewest presses.

Here's how we can implement this in C++:

### Strategy:

1. **Count Letter Frequencies**: Count the frequency of each letter in the word.
2. **Sort Letters by Frequency**: Sort the letters in descending order of their frequencies.
3. **Assign Letters to Keys**: Distribute the letters across the keys from 2 to 9. Each key can hold multiple letters,
     and the position of the letter on a key determines the number of pushes required to type it.
4. **Calculate Total Pushes**: Iterate through the sorted list of letters and calculate the total number of pushes needed.

*/
