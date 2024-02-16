// 1481. Least Number of Unique Integers after K Removals.


// Topic: Array, Hash Table, Greedy, Sorting, Counting.


/*
### Task:
---
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

Constraints:
1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length

Hint 1:
Use a map to count the frequencies of the numbers in the array.
Hint 2:
An optimal strategy is to remove the numbers with the smallest count first.

### Testcase:
---
[5,5,4]
1
[4,3,1,1,3,3,2]
3

### Code:
---
class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        // Step 1: Count the frequency of each integer
        unordered_map<int, int> freqMap;
        for (int num : arr) {
            freqMap[num]++;
        }

        // Step 2: Store frequencies in a vector
        vector<int> frequencies;
        for (auto& [num, freq] : freqMap) {
            frequencies.push_back(freq);
        }

        // Step 3: Sort the frequencies in ascending order
        sort(frequencies.begin(), frequencies.end());

        // Step 4: Remove elements with the smallest frequencies first
        int uniqueInts = frequencies.size(); // Initial count of unique integers
        for (int freq : frequencies) {
            if (k >= freq) {
                k -= freq; // Remove 'freq' elements
                uniqueInts--; // Decrease the count of unique integers
            } else {
                break; // Cannot remove more elements
            }
        }

        // Step 5: Return the remaining count of unique integers
        return uniqueInts;
    }
};


// Description: ===================================
/*
To solve this problem, we'll follow the hints provided. First, we'll count the frequency of each integer in the array using a hash table (e.g., `std::unordered_map` in C++). Then, we'll sort these frequencies in ascending order because we want to remove the integers with the smallest frequencies first to minimize the number of unique integers left.

Here's a step-by-step solution:

1. Count the frequency of each integer in the array using a hash table.
2. Store these frequencies in a vector because we want to sort them by frequency.
3. Sort the vector of frequencies in ascending order.
4. Iterate over the sorted frequencies, and for each frequency, remove as many elements as possible until `k` becomes 0 or less. Each time we remove elements corresponding to a frequency, we decrease the count of unique integers.
5. The remaining count of unique integers is our answer.

This code defines a class `Solution` with a method `findLeastNumOfUniqueInts` that takes a vector of integers `arr` and an integer `k` as input and returns the least number of unique integers after removing `k` elements following the optimal strategy.

*/
