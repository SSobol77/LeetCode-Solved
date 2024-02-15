// 560. Subarray Sum Equals K.


// Topic: Array, Hash Table, Prefix Sum.


/*
### Task:
---
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
 
Constraints:
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7

Hint 1:
Will Brute force work here? Try to optimize it.
Hint 2:
Can we optimize it by using some extra space?
Hint 3:
What about storing sum frequencies in a hash table? Will it be useful?
Hint 4:
sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.


### Testcase:
---
[1,1,1]
2
[1,2,3]
3


### Code:
---
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        
    }
};


*/
// Solution: --------------------------------------

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count = 0;
        int sum = 0;
        
        // Create a hash table to store the frequency of prefix sums
        unordered_map<int, int> prefix_sum_freq;
        prefix_sum_freq[0] = 1; // Initialize with 0 sum
        
        // Iterate through the array
        for (int num : nums) {
            // Calculate the current prefix sum
            sum += num;
            
            // Check if there exists a prefix sum such that sum - k = prefix_sum
            if (prefix_sum_freq.find(sum - k) != prefix_sum_freq.end()) {
                // If found, increment the count by the frequency of that prefix sum
                count += prefix_sum_freq[sum - k];
            }
            
            // Increment the frequency of the current prefix sum
            prefix_sum_freq[sum]++;
        }
        
        return count;
    }
};

// Description: ===================================
/*
The task is to find the total number of subarrays in an array of integers whose sum equals a given value k.

To solve this problem efficiently, we can use the concept of prefix sums along with a hash table to store the frequency of encountered prefix sums.

The algorithm iterates through the array, maintaining a running sum of elements encountered so far. For each element, it calculates the current prefix sum by adding the current element to the running sum.

At each step, the algorithm checks if there exists a prefix sum such that the difference between the current prefix sum and k equals a previously encountered prefix sum. This indicates the presence of a subarray with the desired sum.

If such a prefix sum is found, the algorithm increments a count variable by the frequency of the prefix sum. This accounts for all possible subarrays with the desired sum ending at the current position.

The algorithm updates the frequency of the current prefix sum in the hash table to account for future occurrences.

After processing all elements in the array, the algorithm returns the total count of subarrays with the desired sum.

By utilizing prefix sums and a hash table to store prefix sum frequencies, the algorithm achieves a time complexity of O(n), where n is the number of elements in the input array.

*/
