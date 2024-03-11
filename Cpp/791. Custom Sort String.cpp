// 791. Custom Sort String.


// Topic: Hash Table, String, Sorting.


/*
### Task:
---
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

Example 1:
Input:  order = "cba", s = "abcd" 
Output:  "cbad" 
Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

Example 2:
Input:  order = "bcafg", s = "abcd" 
Output:  "bcad" 
Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.
Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "bacd" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.

Constraints:
1 <= order.length <= 26
1 <= s.length <= 200
order and s consist of lowercase English letters.
All the characters of order are unique.

### Testcase:
---
"cba"
"abcd"

### Code:
---
class Solution {
public:
    string customSortString(string order, string s) {
        
    }
};


*/
// Solution: --------------------------------------

#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string customSortString(string order, string s) {
        // Step 1: Create a hash table to map each character in 'order' to its index
        // This will allow us to define a custom sorting order based on 'order'
        unordered_map<char, int> orderMap;
        for (int i = 0; i < order.size(); ++i) {
            orderMap[order[i]] = i; // Map character to its position in 'order'
        }

        // Step 2: Count the occurrences of each character in 's' using a hash table
        // This helps in constructing the sorted string based on character counts
        unordered_map<char, int> charCount;
        for (char c : s) {
            charCount[c]++; // Increment count for each character in 's'
        }

        string result; // Initialize an empty string to build the result

        // Step 3: Construct the result string based on the custom order defined in 'order'
        for (char c : order) {
            // Check if the character is present in 's'
            if (charCount.find(c) != charCount.end()) {
                // Append the character to the result string as many times as it occurs in 's'
                result.append(charCount[c], c);
                // Remove the character from the count map to avoid adding it again
                charCount.erase(c);
            }
        }

        // Step 4: Append the remaining characters that are not in 'order' to the result string
        // These characters will maintain their relative order from the original string 's'
        for (auto& pair : charCount) {
            // Append each remaining character to the result string as many times as it occurs
            result.append(pair.second, pair.first);
        }

        return result; // Return the custom sorted string
    }
};



// Description: ===================================
/*

To solve the "Custom Sort String" task, we will use a hash table to map each character in `order` to its respective position, 
providing us a way to sort the characters in `s` according to the custom order defined by `order`. Characters not found in `order` 
will be placed at the end of the result string, maintaining their relative order from `s`. 


### Commentary:

- **orderMap**: This hash table allows us to quickly determine the custom sort order of each character as defined by the string `order`.

- **charCount**: This hash table keeps track of how many times each character appears in `s`. This is crucial for reconstructing the sorted 
    string.

- **result**: This string is constructed by first adding characters in the custom order defined by `order` and then appending the remaining 
    characters from `s`.

- **for-loop over `order`**: This loop ensures that characters are added to `result` in the custom order. If a character from `order` is 
    found in `s`, it's added to `result` as many times as it appears in `s`.

- **for-loop over `charCount`**: After processing all characters in `order`, there may be characters left in `s` that weren't in `order`. 
    This loop adds those remaining characters to `result`, maintaining their order from `s`.


### Steps:

1. **Create a Hash Table**: Map each character in `order` to its index. This will allow us to quickly look up the custom order of each
     character.

2. **Count Characters in `s`**: Use a hash table or an array to count the occurrences of each character in `s`. 

3. **Construct the Result String**: Iterate through `order`, and for each character, add it to the result string as many times as it 
     appears in `s`. This ensures characters are added in the custom order.
     
4. **Add Remaining Characters**: Append the characters not in `order` to the end of the result string, maintaining their order from `s`.

### Description:

- We map each character in `order` to its index to easily determine its custom sort order.
- We count each character in `s` to know how many times to add each character to the result string.
- We construct the result string by iterating through `order` and adding each character the number of times it occurs in `s`.
- We append the remaining characters in `s` that are not in `order` to the end of the result string, preserving their order from `s`.

This approach ensures that the characters in `s` are rearranged according to the custom sort order defined by `order`, with any characters 
not present in `order` appended at the end.

*/
