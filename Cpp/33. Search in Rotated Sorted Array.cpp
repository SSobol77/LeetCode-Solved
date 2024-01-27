// 33. Search in Rotated Sorted Array.


// Topic: Array, Binary Search.


/*
### Task:
---
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that 
the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, 
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
 
Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4


### Testcase:
---
[4,5,6,7,0,1,2]
0
[4,5,6,7,0,1,2]
3
[1]
0


### Code:
---
class Solution {
public:
    int search(vector<int>& nums, int target) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        // Initialize start and end to the first and last index of the array
        int start = 0, end = nums.size() - 1;

        // Continue searching while the start index is less than or equal to the end index
        while (start <= end) {
            // Calculate mid index to divide the array into two halves
            int mid = start + (end - start) / 2; // This prevents potential overflow

            // If the target is found at the mid index, return mid
            if (nums[mid] == target) {
                return mid;
            }

            // Check if the left side of the array is sorted
            // This is determined by comparing the start element with the mid element
            if (nums[start] <= nums[mid]) {
                // If the target is within the range of the sorted left side
                // This means the target must be between start and mid
                if (target >= nums[start] && target < nums[mid]) {
                    // Narrow the search to the left side
                    end = mid - 1;
                } else {
                    // If the target is not in the sorted left side, it must be in the right side
                    // Shift the search to the right side by adjusting the start index
                    start = mid + 1;
                }
            } else {
                // If the left side is not sorted, the right side must be sorted
                // Check if the target is within the range of the sorted right side
                if (target > nums[mid] && target <= nums[end]) {
                    // If the target is within the sorted right side, narrow the search to this side
                    start = mid + 1;
                } else {
                    // If the target is not in the sorted right side, it must be in the left side
                    // Shift the search to the left side by adjusting the end index
                    end = mid - 1;
                }
            }
        }

        // If the search completes without finding the target, return -1 to indicate failure
        return -1;
    }
};



// Description: ===================================
/*
To solve the problem of searching in a rotated sorted array with a time complexity of O(log n), we can utilize a modified binary search. 
The array is divided into two portions at the pivot point: one sub-array is sorted in ascending order, and the other might contain the 
pivot point but is also sorted in its own range. The key to solving this problem is to determine which part of the array the target is 
likely to be in and then apply binary search to that part.


### Here's a step-by-step guide to the algorithm:

1. Initialize the start and end pointers to the beginning and end of the array, respectively.
2. Perform a binary search. In each iteration, calculate the middle point.
3. Determine if the middle element is the target. If so, return the index.
4. Check if the left part of the array is sorted by comparing the start element with the middle element.
   - If the left part is sorted, check if the target is within this range. If so, adjust the end pointer to narrow the search to the left part. Otherwise, search in the right part.
   - If the left part is not sorted, then the right part must be sorted. Check if the target is within the range of the right part. If so, adjust the start pointer to narrow the search to the right part. Otherwise, search in the left part.
5. Repeat the process until the target is found or the search space is exhausted.



### Detailed Explanation:

- The algorithm starts by initializing two pointers, `start` and `end`, to delineate the search boundaries.
- A binary search loop is initiated, with the condition `start <= end` ensuring the search continues as long as there is a potential search space.
- Inside the loop, the middle index `mid` is calculated. If `nums[mid]` is equal to `target`, the index `mid` is immediately returned.
- The algorithm then checks if the left half of the array (from `start` to `mid`) is sorted by comparing `nums[start]` and `nums[mid]`.
  - If the left half is sorted and the `target` lies within the range of `nums[start]` and `nums[mid]`, the search space is narrowed to this left half by updating `end` to `mid - 1`.
  - If the left half is sorted but the `target` does not lie within its range, the search space is shifted to the right half by updating `start` to `mid + 1`.
- If the left half is not sorted, the right half must be sorted. The same logic is applied to determine if the search should continue in the right half or shift back to the left half.
- The loop continues until the target is found or the search space is exhausted (`start` exceeds `end`), at which point `-1` is returned to indicate that the `target` is not present in the array.

*/
