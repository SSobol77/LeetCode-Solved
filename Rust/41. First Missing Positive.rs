// 41. First Missing Positive.

// Topic: Array, Hash Table

/*
### Task:
---
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:
1 <= nums.length <= 105
-2^31 <= nums[i] <= 2^31 - 1

### Testcase:
---
[1,2,0]
[3,4,-1,1]
[7,8,9,11,12]


### Code:
---
impl Solution {
    pub fn first_missing_positive(nums: Vec<i32>) -> i32 {
        
    }
}
*/
// Solution: ------------------------------------------------
impl Solution {
    pub fn first_missing_positive(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();

        // Iterate over the array
        for i in 0..n {
            // While the number is in the range [1, n] and not in its correct position,
            // swap it to its correct position.
            // Correct position for a number `x` is `x - 1` (since array indices start at 0).
            while nums[i] > 0 && nums[i] <= n as i32 && nums[nums[i] as usize - 1] != nums[i] {
                let correct_pos = nums[i] as usize - 1;
                nums.swap(i, correct_pos);
            }
        }

        // After rearranging, iterate through the array again
        for (i, &num) in nums.iter().enumerate() {
            // The first index `i` where `nums[i] != i + 1` indicates that `i + 1` is missing.
            // This is because in a correctly arranged array, the number at index `i` should be `i + 1`.
            if num != i as i32 + 1 {
                return i as i32 + 1;
            }
        }

        // If all numbers from 1 to n are present, the missing number is `n + 1`.
        n as i32 + 1
    }
}


// Description: =============================================
/*
To solve the "First Missing Positive" problem in Rust, we need to adhere to the constraints of O(n) time complexity and O(1) auxiliary space. This problem can be solved using an algorithm that essentially places each number in its correct position if it lies within the range of 1 to the length of the array (`n`). 

Here's the step-by-step algorithm:

1. **Cyclic Sort**: Iterate over the array, and for each number, if it is in the range `[1, n]` (where `n` is the length of the array), and it's not in its correct position (i.e., `nums[i] != i + 1`), swap it with the number in its correct position. 

2. **Find the Missing Positive**: After the cyclic sort, iterate through the array again. The first position where `nums[i] != i + 1` indicates that `i + 1` is the missing positive number. If all numbers are in their correct positions, the missing number is `n + 1`.

This implementation efficiently finds the first missing positive integer in the given array `nums`. It utilizes cyclic sort to place 
each number in its correct position and then identifies the missing positive number. This approach ensures that the time complexity 
remains O(n) and no additional space is used beyond constant variables, thus satisfying the problem's constraints.

This code uses the cyclic sort pattern, which is particularly effective for problems where elements need to be rearranged based on their 
value to fit into a specific position within the array. The primary loop handles the sorting, ensuring that each positive integer less 
than or equal to the length of the array is placed in its correct position. The subsequent loop checks for the first instance where the 
numbers do not match the index plus one, indicating the first missing positive integer. If all numbers are in place, the missing number 
is n + 1, where n is the length of the array. This solution adheres to the constraints of O(n) time complexity and O(1) space complexity.

*/