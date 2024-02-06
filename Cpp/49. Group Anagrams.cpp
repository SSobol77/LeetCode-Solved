// 49. Group Anagrams

// Task:
// 
// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
// Example 1:
// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
// 
// Example 2:
// Input: strs = [""]
// Output: [[""]]
//
// Example 3:
// Input: strs = ["a"]
// Output: [["a"]]

// Constraints:
// 1 <= strs.length <= 10^4
// 0 <= strs[i].length <= 100
// strs[i] consists of lowercase English letters.

/*
### Testcase:
["eat","tea","tan","ate","nat","bat"]
[""]
["a"]


### Code:
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
    }
};

*/
// Solution:  -------------------------------------------------------------

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Create a hash table to map each sorted string to its list of anagrams
        unordered_map<string, vector<string>> map;

        // Iterate over each string in the input array
        for (string s : strs) {
            // Sort the string to use as a key. Anagrams will produce the same sorted string
            string key = s; // Copy the original string to avoid modifying it
            sort(key.begin(), key.end()); // Sort the copied string to get the key

            // Append the original string to the vector of anagrams corresponding to the sorted key
            // If the key doesn't exist, a new entry is created automatically
            map[key].push_back(s);
        }

        // Prepare the final result container
        vector<vector<string>> result;

        // Iterate over the map to extract each group of anagrams and add it to the result
        for (auto& pair : map) {
            // Each 'pair' consists of a sorted string (key) and its corresponding anagrams (value)
            // Here, we're only interested in the anagrams (the value part of the pair)
            result.push_back(pair.second); // Add the group of anagrams to the final result
        }

        // Return the grouped anagrams
        return result;
    }
};


// Description: ===============================================
/*
To solve the "Group Anagrams" problem, we can utilize a hash table (in C++, an `unordered_map`) to group strings that are 
anagrams of each other. The key idea is to use the sorted version of each string as the key in our hash table, since anagrams 
will result in the same string when sorted. Here's how we can implement this:

1. Iterate over each string in the input array `strs`.
2. Sort each string to form the key. All anagrams will result in the same key when sorted.
3. Append the original string to the vector corresponding to its sorted key in the hash table.
4. Once all strings are processed, iterate over the hash table and add each group of anagrams to the final result.

### Explanation:
- **Line 4:** We declare an `unordered_map` named `map` where each key is a sorted string and each value is a vector of strings that 
    are anagrams of the key.
- **Lines 5-8:** We iterate over each string in the input vector. For each string, we sort it to generate the key and then add 
    the original string to the vector corresponding to this key in our map.
- **Lines 10-13:** We iterate over the map and add each vector of anagrams (which is a map value) to our result vector.
- **Line 15:** We return the result vector containing groups of anagrams.

This solution efficiently groups anagrams together using a hash table and has a time complexity that is dominated by the sorting 
of strings, making it O(NKlogK) where N is the number of strings in the input array and K is the maximum length of a string in the array.

*/