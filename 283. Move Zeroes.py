# 283. Move Zeroes.         -Easy-

# Topic: Array, Two Pointers.


"""
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
1 <= nums.length <= 104
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you minimize the total number of operations done?

Hint 1:
In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array.
However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, 
first apply the idea discussed using an additional array and the in-place solution will pop up eventually.
Hint 2:
A two-pointer approach could be helpful here. The idea would be to have one pointer for iterating the array and another 
pointer that just works on the non-zero elements of the array.


### Testcase:
---
[0,1,0,3,12]
[0]


### Code:
---
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        Do not return anything, modify nums in-place instead.
        '''

"""
### Solution: -------------------------------------------------

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Pointer to the next position where a non-zero element should be placed
        left = 0

        # Iterate through the array
        for i in range(len(nums)):
            # When a non-zero element is found
            if nums[i] != 0:
                # Swap the element with the one at the 'left' pointer
                nums[i], nums[left] = nums[left], nums[i]
                # Move the 'left' pointer to the next position
                left += 1



### Description: ==============================================
'''
The "Move Zeroes" problem is a classic example of using the two-pointer technique to solve array manipulation problems efficiently.

### Problem Analysis:
The task is to move all the zeros in the given array to the end while maintaining the order of non-zero elements. The operation should be done in-place, meaning without using any extra space.

### Approach:
- **Two-Pointer Technique**: 
  - One pointer (`left`) is used to keep track of the position where the next non-zero element should be placed.
  - The other pointer (`i`) iterates through the array.
  - When a non-zero element is encountered, it is swapped with the element at the `left` pointer, and the `left` pointer is incremented.

### Explanation:
- **Initialization**: The `left` pointer starts at the beginning of the array.
- **Iterating the Array**: The loop iterates through each element.
- **Non-Zero Check**: If a non-zero element is found, it's swapped with the element at the `left` pointer. This ensures that all non-zero elements are moved to the start of the array.
- **Incrementing the Pointer**: After swapping, the `left` pointer is incremented to the next position.
- **Result**: By the end of the loop, all zeros are moved to the end of the array, and the order of non-zero elements is maintained.

### Time Complexity:
- The time complexity of this algorithm is O(n), where n is the length of the array. Each element is checked once.

### Test Cases:
1. `nums = [0,1,0,3,12]` should be modified to `[1,3,12,0,0]`.
2. `nums = [0]` remains `[0]`.

This solution effectively addresses the problem requirements and optimizes operations by minimizing the number of swaps necessary to move all zeroes to the end.

'''