// 34. Find First and Last Position of Element in Sorted Array.


// Topic: Array, Binary Search.


/*
### Task:
---
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9


### Testcase:
---
[5,7,7,8,8,10]
8
[5,7,7,8,8,10]
6
[]
0


### Code:
---
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> result{-1, -1};  // Initialize the result with default values [-1, -1]

        // Perform binary search to find the first occurrence of the target
        int leftIndex = findFirstOrLast(nums, target, true);

        // If target is not found (leftIndex is out of bounds or does not point to target), return default result
        if (leftIndex == nums.size() || nums[leftIndex] != target) {
            return result;  // Target not found
        }

        // Perform binary search to find the last occurrence of the target
        // Subtracting 1 because the function returns the insertion point for the target, which is one index past the last occurrence
        int rightIndex = findFirstOrLast(nums, target, false) - 1;

        // Update result with the indices of the first and last occurrence
        result[0] = leftIndex;  // First position where target is found
        result[1] = rightIndex; // Last position where target is found

        return result;  // Return the updated result
    }

private:
    // Helper function to perform binary search
    // findFirst controls whether to find the first occurrence (true) or the insertion point for the last occurrence (false)
    int findFirstOrLast(vector<int>& nums, int target, bool findFirst) {
        int start = 0, end = nums.size();  // Initialize binary search bounds
        int mid;

        while (start < end) {  // Continue until search space is exhausted
            mid = start + (end - start) / 2;  // Prevent potential overflow

            // When finding the first occurrence, move end if target is found to continue searching left
            // When finding the last occurrence, only move end if target is strictly greater
            if (nums[mid] > target || (findFirst && nums[mid] == target)) {
                end = mid;  // Narrow search to the left half
            } else {
                start = mid + 1;  // Narrow search to the right half
            }
        }

        // For the first occurrence, start will point to the first target instance
        // For the last occurrence, start will point to the insertion point, which is one index past the last target instance
        return start;
    }
};



// Description: ===================================
/*
To solve the problem of finding the first and last position of an element in a sorted array with O(log n) runtime complexity, 
we can use a binary search algorithm. Since the array is sorted, binary search is an efficient way to find the target elements. 
However, instead of stopping at the first occurrence of the target, we need to find the first and last positions where this 
target appears.

The approach involves performing binary search twice with slight modifications:

1. First binary search to find the first (leftmost) occurrence of the target.
2. Second binary search to find the last (rightmost) occurrence of the target.


### Detailed Explanation:

- The function `searchRange` initializes the result vector with `[-1, -1]`, which will be returned if the target is not found.
- `findFirstOrLast` is a helper function that performs a binary search to find the first or last occurrence of the target. It takes 
   a boolean parameter `findFirst` to indicate whether to find the first or last occurrence.

- In the first call to `findFirstOrLast`, it searches for the first occurrence by setting `findFirst` to `true`. If the target is 
  not found (i.e., `leftIndex` is equal to the size of the array or the value at `leftIndex` is not the target), the function 
  returns `[-1, -1]`.

- If the first occurrence is found, the function calls `findFirstOrLast` again with `findFirst` set to `false` to find the last 
  occurrence. The last occurrence's index is one less than the returned value because `findFirstOrLast` returns the index where 
  the target could be inserted to maintain the order, which is one position after the last occurrence of the target.

- The result vector is then updated with the first and last positions of the target and returned.

*/
