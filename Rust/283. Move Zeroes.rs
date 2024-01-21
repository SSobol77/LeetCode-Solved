// 283. Move Zeroes         -Easy-


// Topic:  Array, Two Pointers.

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
impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        
    }
}
*/
// Solution: -------------------------------------------------

impl Solution {
    // Define the public function `move_zeroes` that takes a mutable reference to a vector of i32.
    // The function will rearrange the elements in the vector, moving all zeros to the end.
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        // Initialize `non_zero_index` to keep track of where the next non-zero element should be placed.
        let mut non_zero_index = 0;

        // Iterate over the array using the variable `current` to index each element.
        for current in 0..nums.len() {
            // Check if the current element is non-zero.
            if nums[current] != 0 {
                // If it's non-zero, swap the current element with the element at `non_zero_index`.
                // This operation moves the non-zero element to the front part of the array.
                nums.swap(current, non_zero_index);

                // Increment `non_zero_index` so that it now points to the next position
                // where the following non-zero element should be placed.
                non_zero_index += 1;
            }
            // If the current element is zero, simply proceed to the next element.
            // The `non_zero_index` remains unchanged, effectively leaving a space for future non-zero elements.
        }
        // By the end of the loop, all non-zero elements are moved to the front of the array,
        // and all zeros are shifted to the end, maintaining the relative order of non-zero elements.
    }
}


// Description: ==============================================
/*
To solve the "Move Zeroes" problem, we will implement the `move_zeroes` function in Rust. 
The goal is to move all zeroes in the given array to the end while maintaining the relative 
order of the non-zero elements. This must be done in-place to minimize space usage.

### Algorithm:

1. **Two-Pointer Approach:**
   - Initialize two pointers, `non_zero_index` and `current`. Both start from the beginning of the array.
   - `non_zero_index` is used to keep track of the position where the next non-zero element should be placed.
   - `current` iterates through the array.

2. **Iterating Through the Array:**
   - Iterate through the array using the `current` pointer.
   - When a non-zero element is encountered:
     - Swap the elements at `current` and `non_zero_index`.
     - Increment `non_zero_index`.

3. **Move Zeroes to the End:**
   - By swapping non-zero elements to the front, zeroes are automatically moved to the end.
   - The relative order of non-zero elements is maintained.

4. **End of Iteration:**
   - Once the `current` pointer has iterated over the entire array, all zeroes will be at the end, and 
     non-zero elements will retain their original order.


### Description:

- The function `move_zeroes` is designed to reorder the elements of the given array in such a way that all 
  zeroes are moved to the end.
- It employs a two-pointer approach where one pointer (`non_zero_index`) marks the position for the next
  non-zero element, and the other (`current`) iterates through the array.
- Each non-zero element is swapped with the element at `non_zero_index`, effectively moving all zeroes 
  towards the end.
- This process is done in-place,

 ensuring no additional space is allocated, adhering to the in-place requirement of the problem.
- The relative order of the non-zero elements is preserved through this swapping mechanism.

### Complexity Analysis:

- **Time Complexity:** O(n), where n is the number of elements in the input array. The algorithm makes a 
    single pass through the array.
- **Space Complexity:** O(1), as the rearrangement is done in-place without using any extra space beyond 
    temporary variables.

### Performance Considerations:

- The solution is efficient and straightforward, minimizing both the time and space complexity.
- It follows the two-pointer technique, a common and effective approach in array manipulation problems.
- The in-place operation ensures optimal space usage, an important aspect for large datasets or 
  memory-constrained environments.

### Conclusion:

This implementation of the "Move Zeroes" problem in Rust provides an efficient and space-optimized 
solution, effectively handling arrays of varying sizes while maintaining the order of non-zero elements. 
The two-pointer approach ensures a minimal number of operations, making it a practical solution for 
real-world applications.

*/
