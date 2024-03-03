// 977. Squares of a Sorted Array.


// Topic: Array, Two Pointers, Sorting.


/*
### Task:
---
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?


### Testcase:
---
[-4,-1,0,3,10]
[-7,-3,2,3,11]


### Code:
---
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        // 'n' holds the size of the input array 'nums'
        int n = nums.size();
        // Initialize a new vector 'result' to store the squared values
        vector<int> result(n);

        // Initialize two pointers:
        // 'left' starts at the beginning of 'nums'
        // 'right' starts at the end of 'nums'
        int left = 0, right = n - 1;
        
        // Iterate over the 'result' array from end to start
        for (int i = n - 1; i >= 0; --i) {
            // Compare the absolute values of the elements at 'left' and 'right' pointers
            if (abs(nums[left]) > abs(nums[right])) {
                // If the element at 'left' is greater, square it and assign to 'result[i]'
                result[i] = nums[left] * nums[left];
                // Move the 'left' pointer to the right, to the next element
                ++left;
            } else {
                // If the element at 'right' is greater or equal, square it and assign to 'result[i]'
                result[i] = nums[right] * nums[right];
                // Move the 'right' pointer to the left, to the previous element
                --right;
            }
        }
        
        // Return the 'result' array with squared and sorted values
        return result;
    }
};



// Description: ===================================
/*
To solve the task of squaring each element of a sorted array and returning a new array with the squares sorted in non-decreasing 
order, we can use a two-pointer approach which is efficient and meets the requirement of finding an O(n) solution.

The key insight is that the largest squared values can come from either the beginning or the end of the original array, due to 
the presence of negative numbers. By comparing the absolute values of the elements pointed to by the two pointers, we can decide 
which squared value should be placed next in the output array.

Here's a step-by-step approach:

1. Initialize two pointers: one at the start (`left`) and one at the end (`right`) of the input array.
2. Create a new array (`result`) of the same length as the input array to store the squared values.
3. Iterate from the end of the `result` array backwards, filling it with the squared values.
   - Compare the absolute values of the elements at `left` and `right` in the input array.
   - Square the larger absolute value and place it in the current position of the `result` array.
   - Move the pointer (`left` or `right`) inward, depending on which had the larger absolute value.
4. Continue until all positions in the `result` array are filled.
5. Return the `result` array.

### Description:

This solution leverages the two-pointer technique to efficiently solve the problem in O(n) time complexity, which is linear in 
relation to the size of the input array. The algorithm starts by comparing the absolute values of the elements at the two ends of 
the sorted array. It squares the larger of the two values and places this value in the correct position in the result array, starting 
from the end. This ensures that the result array is filled in non-decreasing order of squared values. The pointer corresponding to 
the chosen value then moves inward, and the process repeats until all positions in the result array are filled. This approach does 
not require an explicit sorting step after squaring the elements, thereby achieving the desired time complexity.

*/
