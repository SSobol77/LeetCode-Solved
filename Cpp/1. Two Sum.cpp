// 1. Two Sum.

// Topic: Array, Hash Table.


/*
### Task:
---
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
 
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:
2 <= nums.length <= 10^4
-109 <= nums[i] <= 10^9
-109 <= target <= 10^9
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

Hint 1:
A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions for just for completeness. It is from these brute force solutions that you can come up with optimizations.
Hint 2:
So, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y which is value - x where value is the input parameter. Can we change our array somehow so that this search becomes faster?
Hint 3:
The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?


### Testcase:
---
[2,7,11,15]
9
[3,2,4]
6
[3,3]
6


### Code:
---
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Create an unordered map to store the indices of elements
        unordered_map<int, int> num_indices;
        
        // Iterate through the array
        for (int i = 0; i < nums.size(); ++i) {
            // Calculate the complement needed to reach the target
            int complement = target - nums[i];
            
            // Check if the complement is already in the map
            if (num_indices.find(complement) != num_indices.end()) {
                // If found, return the indices of the current element and its complement
                return {num_indices[complement], i};
            }
            
            // Otherwise, store the index of the current element in the map
            num_indices[nums[i]] = i;
        }
        
        // If no solution is found, return an empty vector
        return {};
    }
};


// Description: ===================================
/*
The task is to find two numbers in an array such that they add up to a specific target. We need to return the indices of these two numbers.

To solve this problem efficiently, we can use a hash table (unordered map in C++) to store the indices of elements as we iterate through 
the array. This allows us to perform constant time lookups to find the complement needed to reach the target sum.

The algorithm iterates through the array once. For each element, it calculates the complement needed to reach the target sum by subtracting
the current element from the target. It then checks if this complement exists in the hash table.

If the complement is found, it means that we have found the two numbers that add up to the target sum. In this case, we return the indices 
of the current element and its complement.

If the complement is not found, we store the index of the current element in the hash table for future reference.

If no solution is found after iterating through the entire array, we return an empty vector to indicate that no valid pair of numbers 
exists that add up to the target sum.

The use of a hash table allows us to achieve a time complexity of O(n) for the solution, where n is the number of elements in the input 
array. This is because the lookup operation in a hash table is amortized O(1), resulting in overall linear time complexity for the algorithm.

*/
