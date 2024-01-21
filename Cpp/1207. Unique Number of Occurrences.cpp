// 1207. Unique Number of Occurrences.

// Topic: Array, Hash Table.

/*
### Task:
---
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 
Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

Hint 1:
Find the number of occurrences of each element in the array using a hash map.
Hint 2:
Iterate through the hash map and check if there is a repeated value.


### Testcase:
---
[1,2,2,1,1,3]
[1,2]
[-3,0,1,-3,1,1,1,-3,10,0]


### Code:
---
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        
    }
};

*/
// Solution:

#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        // Map to store the frequency of each element
        unordered_map<int, int> freq;
        for (int num : arr) {
            freq[num]++;
        }

        // Set to check for unique occurrences
        unordered_set<int> occurrences;
        for (auto const& pair : freq) {
            if (occurrences.find(pair.second) != occurrences.end()) {
                // If the occurrence is already in the set, return false
                return false;
            }
            occurrences.insert(pair.second);
        }

        // If all occurrences are unique, return true
        return true;
    }
};


// Description:
/*
To implement the `uniqueOccurrences` function in C++, we will follow a similar approach as the Python version. 
We'll use a hash map (`std::unordered_map`) to count the occurrences of each element and then use a set (`std::unordered_set`) 
to check if the occurrences are unique.

This C++ implementation will work efficiently for the given problem constraints. The `unordered_map` is used to count the
occurrences of each element in the array, and the `unordered_set` is used to ensure that these counts are unique.

*/
