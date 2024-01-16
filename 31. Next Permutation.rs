// 31. Next Permutation.             -Medium-

// Topic:Array, Two Pointers.

/*
### Task:
---
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, 
the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100


### Tstcase:
---
[1,2,3]
[3,2,1]
[1,1,5]


### Code:
---
impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        
    }
}
*/
// Solution: ------------------------------------------------

impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        let n = nums.len();
        if n <= 1 {
            return;
        }

        // Step 1: Identify the pivot
        let mut i = n - 2;
        while i != usize::MAX && nums[i] >= nums[i + 1] {
            i -= 1;
        }

        // If the entire array is in descending order
        if i == usize::MAX {
            nums.reverse();
            return;
        }

        // Step 2: Find the successor to the pivot
        let mut j = n - 1;
        while nums[j] <= nums[i] {
            j -= 1;
        }

        // Step 3: Swap the pivot and its successor
        nums.swap(i, j);

        // Step 4: Reverse the suffix
        nums[i + 1..].reverse();
    }
}


// Description: =============================================
/*
To implement the `next_permutation` function in Rust, we need to follow these steps:

1. **Identify the pivot**: Find the largest index `i` where `nums[i] < nums[i + 1]`. If no such index exists, the entire array is in descending order, and we simply reverse it to get the lowest possible order.

2. **Find the successor to the pivot**: If such an `i` exists, find the largest index `j` where `j > i` and `nums[i] < nums[j]`.

3. **Swap the pivot and its successor**: Swap the elements at indices `i` and `j`.

4. **Reverse the suffix**: Reverse the elements from index `i + 1` to the end of the array.

This implementation efficiently finds the next lexicographical permutation of the given array `nums` in place, as per the constraints of the problem. It handles the edge cases and follows the algorithmic steps required to solve the "Next Permutation" problem.

*/