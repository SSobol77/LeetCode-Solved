// 3005. Count Elements With Maximum Frequency.


// Topic: Array, Hash Table, Counting.


/*
### Task:
---
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

Example 1:
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100

Hint 1:
Find frequencies of all elements of the array.
Hint 2:
Find the elements that have the maximum frequencies and count their total occurrences.

### Testcase:
---
[1,2,2,3,1,4]
[1,2,3,4,5]


### Code:
---
class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>
#include <unordered_map>

class Solution {
public:
    int maxFrequencyElements(std::vector<int>& nums) {
        // Create an unordered_map to store the frequency of each element.
        // Key: element from nums, Value: frequency of the element.
        std::unordered_map<int, int> frequencyMap;

        // Iterate through each element in nums and update its frequency in the map.
        for (int num : nums) {
            ++frequencyMap[num]; // Increment the frequency of num.
        }

        // Initialize a variable to track the maximum frequency found so far.
        int maxFreq = 0;
        // Iterate through the map to find the maximum frequency among all elements.
        for (const auto& pair : frequencyMap) {
            if (pair.second > maxFreq) {
                maxFreq = pair.second; // Update maxFreq if a higher frequency is found.
            }
        }

        // Initialize a counter to keep track of the total occurrences of elements with the max frequency.
        int count = 0;
        // Iterate through the map again.
        for (const auto& pair : frequencyMap) {
            // If an element's frequency matches the max frequency,
            // add its frequency to the count.
            if (pair.second == maxFreq) {
                count += maxFreq;
            }
        }

        // Return the total count of occurrences of elements with the maximum frequency.
        return count;
    }
};




// Description: ===================================
/*
To tackle this task, we will implement a function `maxFrequencyElements` that takes a vector of integers `nums` as an input and 
returns the total frequencies of elements in `nums` that have the maximum frequency.

We will follow a two-step approach based on the hints provided:
1. Calculate the frequency of all elements in the array using a hash table (unordered_map in C++).
2. Determine the maximum frequency and count the total occurrences of elements having this frequency.

Let's go through the solution step by step:

- First, we declare an `unordered_map<int, int>` to store the frequency of each element. The key will be the element from `nums`, 
  and the value will be its frequency.
- We iterate through each element in `nums` and update its frequency in the map.
- We then iterate through the map to find the maximum frequency.
- Lastly, we iterate through the map again and sum up the frequencies of elements that have the maximum frequency found in the 
  previous step.

### Description:
---
This solution follows a straightforward approach to solve the given problem. It first calculates the frequency of each element in the
input array using a hash table. It then finds the maximum frequency among all elements. Finally, it iterates through the hash table 
again to sum up the frequencies of elements that match the maximum frequency. This sum is the total number of occurrences of elements 
with the maximum frequency in the input array, which is returned as the final result.

*/
