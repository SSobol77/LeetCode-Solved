// 128. Longest Consecutive Sequence.


// Topic: Array, Hash Table, Union Find.


/*
### Task:
---
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9


### Testcase:
---
[100,4,200,1,3,2]
[0,3,7,2,5,8,4,6,0,1]


### Code:
---
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
    }
};


*/
// Solution: --------------------------------------

#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty())
            return 0;
        
        // Convert the vector to an unordered_set for O(1) lookup
        unordered_set<int> num_set(nums.begin(), nums.end());
        
        int max_length = 0;
        
        // Iterate through each number in the set
        for (int num : num_set) {
            // Check if num - 1 is not in the set, indicating the start of a sequence
            if (num_set.find(num - 1) == num_set.end()) {
                int current_num = num;
                int current_length = 1;
                
                // Increment current_num and current_length until the sequence ends
                while (num_set.find(current_num + 1) != num_set.end()) {
                    current_num++;
                    current_length++;
                }
                
                // Update max_length if current_length is greater
                max_length = max(max_length, current_length);
            }
        }
        
        return max_length;
    }
};


// Description: ===================================
/*
The task is to find the length of the longest consecutive sequence of elements in an unsorted array of integers. The algorithm must run in O(n) time complexity.

To solve this problem efficiently, we can use an unordered set to store the elements of the array. This allows us to perform O(1) average-case lookup operations.

The algorithm iterates through each element in the array and checks if it is the start of a consecutive sequence. This is done by verifying if the element one less than the current element is present in the unordered set.

If the current element is the start of a sequence, the algorithm incrementally counts the consecutive elements starting from the current element. It does this by repeatedly checking if the next consecutive element is present in the unordered set.

During this process, the algorithm keeps track of the maximum length of consecutive elements encountered so far.

Once the iteration is complete, the algorithm returns the maximum length of consecutive elements found.

By utilizing the unordered set for efficient lookup operations and traversing the array only once, the algorithm achieves a time complexity of O(n), where n is the number of elements in the input array.

*/
