// 451. Sort Characters By Frequency.


// Topic: Hash Table, String, Sorting, Heap (Priority Queue), Bucket Sort, Counting.


/*
### Task:
---
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Constraints:
1 <= s.length <= 5 * 10^5
s consists of uppercase and lowercase English letters and digits.


### Testcase:
---
"tree"
"cccaaa"
"Aabb"


### Code:
---
class Solution {
public:
    string frequencySort(string s) {
        
    }
};

*/
// Solution: --------------------------------------

#include <string>
#include <unordered_map>
#include <queue>
#include <vector>

class Solution {
public:
    string frequencySort(string s) {
        // Step 1: Count the frequency of each character
        std::unordered_map<char, int> freqMap;
        for (char c : s) {
            freqMap[c]++;
        }

        // Step 2: Use a priority queue to sort by frequency
        auto comp = [](const std::pair<char, int>& a, const std::pair<char, int>& b) {
            return a.second < b.second; // Max heap
        };
        std::priority_queue<std::pair<char, int>, std::vector<std::pair<char, int>>, decltype(comp)> maxHeap(comp);

        for (const auto& pair : freqMap) {
            maxHeap.push(pair);
        }

        // Step 3: Build the result string
        std::string result;
        while (!maxHeap.empty()) {
            auto [character, count] = maxHeap.top();
            maxHeap.pop();
            result += std::string(count, character); // Append 'character' 'count' times
        }

        return result;
    }
};

// Description: ===================================
/*
To solve the "Sort Characters By Frequency" problem, you can use a hash table to count the frequency of each character, 
then sort the characters by their frequencies, and finally construct the result string. Here's a step-by-step approach:

1. **Count Frequencies**: Use a hash table (like `std::unordered_map<char, int>`) to count the frequency of each character in the string.
2. **Sort Characters by Frequency**: There are multiple ways to do this. One approach is to use a priority queue (max heap) that stores pairs of characters and their frequencies, sorted by frequency. Another approach is to use bucket sort, where the index represents the frequency, and each bucket contains characters with that frequency.
3. **Build the Result String**: Based on the sorted characters by frequency, construct the result string by appending each character to the result string the number of times it appears.

This solution involves:

- A hash table to count character frequencies.
- A priority queue to sort characters by their frequency in descending order.
- Constructing the result string by repeatedly appending each character according to its frequency.

This approach efficiently sorts characters by frequency and constructs the resulting string, adhering to the given constraints and examples.



*/