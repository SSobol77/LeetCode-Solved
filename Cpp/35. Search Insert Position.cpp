// 35. Search Insert Position.


// Topic:


/*
### Task:
---
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 
Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4


### Testcase:
---
[1,3,5,6]
5
[1,3,5,6]
2
[1,3,5,6]
7


### Code:
---
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0;  // Start of the search range
        int right = nums.size();  // End of the search range, set to nums.size() for potential insertion at the end

        while (left < right) {  // Continue searching until the range is narrowed down to a single element
            int mid = left + (right - left) / 2;  // Calculate mid to prevent overflow

            if (nums[mid] < target) {  // Target is in the upper half
                left = mid + 1;  // Move left up, narrowing the search range to the upper half
            } else {  // Target is in the lower half or at mid
                right = mid;  // Move right down, narrowing the search range to the lower half or keeping it at mid
            }
        }

        // At this point, left is the position where target fits in the sorted order
        return left;
    }
};


// Description: ===================================
/*
To solve the "Search Insert Position" problem with O(log n) runtime complexity, a binary search algorithm can be employed. 
The task is to find the index of a target value in a sorted array of distinct integers or the index where the target should
be inserted to maintain the sorted order. Binary search is perfectly suited for this because it efficiently narrows down 
the search range by half with each iteration.

### Detailed Explanation:

- **Initialization:** The `left` pointer is set to the beginning of the array, and `right` is set to the size of the array, which 
    accounts for the possibility that the target might need to be inserted at the end of the array.
- **Binary Search Loop:** The loop continues until `left` and `right` converge, meaning the search range has been narrowed down to 
    the point where the target value either is found or would be inserted.
- **Mid Calculation:** The midpoint `mid` is calculated in a way that avoids integer overflow, using `left + (right - left) / 2`.
- **Search Logic:**
  - If `nums[mid]` is less than the target, the target must be in the upper half of the current search range, so `left` is moved up 
    to `mid + 1`.
  - Otherwise, the target is either at `mid` or in the lower half, so `right` is moved down to `mid`.
- **Result:** When the loop exits, `left` will be at the position where the target is found or should be inserted to maintain the 
    sorted order of the array. This is because when the target is not found, `left` and `right` converge at the smallest element 
    greater than the target, which is precisely where the target should be inserted.

*/
