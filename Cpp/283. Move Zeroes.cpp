// 283. Move Zeroes.


// Topic: Array, Two Pointers.


/*
### Task:
---
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
 
Follow up: Could you minimize the total number of operations done?

Hint 1:
In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.
Hint 2:
A two-pointer approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.


### Testcase:
---
[0,1,0,3,12]
[0]


### Code:
---
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int lastNonZeroFoundAt = 0; // Pointer to place the next non-zero element.
        
        // Move all non-zero elements to the beginning of the array.
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                swap(nums[lastNonZeroFoundAt++], nums[i]);
            }
        }
        // After the loop, all non-zero elements are in front, and zeros are in the back.
    }
};


// Description: ===================================
/*
To solve the "Move Zeroes" problem efficiently, you can indeed use a two-pointer approach. This approach ensures that the operation is done in-place, maintaining the relative order of the non-zero elements and minimizing the total number of operations. Here's a step-by-step guide:

1. **Initialize two pointers**: 
   - `i`: Iterates through the array.
   - `lastNonZeroFoundAt`: Keeps track of the last non-zero element's position.
2. **Iterate through `nums`**: Use the pointer `i` to go through each element in the array.
3. **Process non-zero elements**:
   - When you encounter a non-zero element, swap it with the element at `lastNonZeroFoundAt`.
   - Increment `lastNonZeroFoundAt`.
4. **Keep zeros at the end**: By swapping non-zero elements towards the beginning, zeros automatically move towards the end.

### Description:

This code defines a `Solution` class with a `moveZeroes` function that takes a reference to a vector of integers `nums`. It iterates through the `nums` array with a pointer `i`, identifying non-zero elements. Each non-zero element encountered is swapped with the element at the position `lastNonZeroFoundAt`, effectively moving the non-zero elements towards the beginning of the array and the zeros towards the end. The `lastNonZeroFoundAt` pointer is incremented each time a swap occurs to ensure that non-zero elements are placed in their correct relative order. This approach is in-place, as it does not use any additional space for another array, and it minimizes the number of operations by only swapping when necessary.

*/
