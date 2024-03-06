// 15. 3Sum.


// Topic: Array, Two Pointers, Sorting.


/*
### Task:
---
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

Hint 1:
So, we essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!
Hint 2:
For the two-sum problem, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y, which is value - x where value is the input parameter. Can we change our array somehow so that this search becomes faster?
Hint 3:
The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?


### Testcase:
---
[-1,0,1,2,-1,-4]
[0,1,1]
[0,0,0]


### Code:
---
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // Initialize the result vector that will store all unique triplets.
        vector<vector<int>> result;

        // Sort the input array to make it easier to navigate and avoid duplicates.
        sort(nums.begin(), nums.end());

        // Iterate through the array, considering each element as the first element of a potential triplet.
        for (int i = 0; i < nums.size(); ++i) {
            // Skip duplicate elements to ensure each triplet is unique.
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            // Initialize two pointers: 'left' just after the current element and 'right' at the end of the array.
            int left = i + 1, right = nums.size() - 1;

            // Use a while loop to move 'left' and 'right' pointers towards each other.
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right]; // Calculate the sum of the triplet.

                // If the sum is less than zero, move the 'left' pointer to the right to increase the sum.
                if (sum < 0) {
                    ++left;
                }
                // If the sum is greater than zero, move the 'right' pointer to the left to decrease the sum.
                else if (sum > 0) {
                    --right;
                }
                // If the sum is zero, we've found a valid triplet.
                else {
                    // Add the valid triplet to the result vector.
                    result.push_back({nums[i], nums[left], nums[right]});

                    // Skip over any duplicate elements for the second and third elements of the triplet.
                    while (left < right && nums[left] == nums[left + 1]) ++left;
                    while (left < right && nums[right] == nums[right - 1]) --right;

                    // Move both pointers towards each other after finding a valid triplet.
                    ++left;
                    --right;
                }
            }
        }

        // Return the result vector containing all unique triplets that sum to zero.
        return result;
    }
};



// Description: ===================================
/*
To solve the 3Sum problem efficiently, we can utilize a combination of sorting and two-pointer technique. The main idea is to sort the array first to make it easier to navigate and avoid duplicates. Then, for each element in the array, we can use the two-pointer approach to find the other two elements that sum up to the negative value of the current element, which effectively solves the two-sum problem for the remaining part of the array.

Here's a step-by-step approach:
1. **Sort the array**: This will allow us to use two pointers effectively and handle duplicates.
2. **Iterate through the array**: For each element `nums[i]`, we'll treat it as the first element of a potential triplet.
3. **Two-pointer approach**: For the remaining part of the array, use two pointers, one starting just after the current element (`left = i + 1`) and the other at the end of the array (`right = nums.size() - 1`). Move these pointers towards each other to find pairs that sum up to `-nums[i]`.
4. **Skip duplicates**: Be careful to skip over duplicate elements to ensure unique triplets.
5. **Store valid triplets**: When a valid triplet is found, add it to the result.

### Description:

This code defines a `Solution` class with a `threeSum` function that takes a vector of integers `nums` and returns a vector of vectors of integers representing the triplets that sum up to 0.

1. **Sort the `nums` array**: This allows for an easier two-pointer approach and handling of duplicates.
2. **Iterate over each element in `nums`**: Each element is considered as a potential first element of a triplet.
3. **Two-pointer approach**: For each element, use two pointers starting just after the current element and at the end of the array to find pairs that sum up to the negative of the current element.
4. **Skip duplicates**: Ensure that we skip over duplicates for the first, second, and third elements of the triplet to avoid duplicate triplets in the result.
5. **Store valid triplets**: When a valid triplet is found, it's added to the `result`.

This solution has a time complexity of O(n^2), where n is the number of elements in `nums`, due to the nested loop (the outer loop and the two-pointer inner loop). The sorting operation outside the loops has a time complexity of O(n log n), which is overshadowed by the O(n^2) complexity of the loop operations.

*/
