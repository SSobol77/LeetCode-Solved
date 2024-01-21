// 189. Rotate Array.           -Medium-

// Topic: Array, Math, Two Pointers.

/*
### Task:
---
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5
 
Follow up:
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Hint 1:
The easiest solution would use additional memory and that is perfectly fine.
Hint 2:
The actual trick comes when trying to solve this problem without using any additional memory. This means you need to use 
the original array somehow to move the elements around. Now, we can place each element in its original location and shift 
all the elements around it to adjust as that would be too costly and most likely will time out on larger input arrays.
Hint 3:
One line of thought is based on reversing the array (or parts of it) to obtain the desired result. Think about how reversal 
might potentially help us out by using an example.
Hint 4:
The other line of thought is a tad bit complicated but essentially it builds on the idea of placing each element in its 
original position while keeping track of the element originally in that position. Basically, at every step, we place an 
element in its rightful position and keep track of the element already there or the one being overwritten in an additional 
variable. We can't do this in one linear pass and the idea here is based on cyclic-dependencies between elements.


### Testcase:
---
[1,2,3,4,5,6,7]
3
[-1,-100,3,99]
2


### Code:
---
impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        
    }
}

*/
//Solution: -------------------------------------

impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        let n = nums.len();
        let k = (k as usize) % n; // Ensure k is within the bounds of the array length

        // Reverse the entire array
        nums.reverse();

        // Reverse the first k elements
        nums[0..k].reverse();

        // Reverse the remaining n-k elements
        nums[k..n].reverse();
    }
}


// Description: ---------------------------------
/*
To solve the "Rotate Array" problem, we can implement the `rotate` function in Rust using array manipulation. 
The key idea is to rotate the array in place to avoid extra space usage. The rotation involves three steps:

1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the remaining `n-k` elements.

This `k` is the number of steps for the rotation, and `n` is the length of the array. We need to adjust `k` to 
be within the bounds of the array length, as rotating the array by its length or a multiple of it results in the same array.



Explanation:
- First, we reverse the entire array. This step brings the last `k` elements to the front but in reverse order.
- Next, we reverse the first `k` elements to correct their order.
- Finally, we reverse the remaining `n-k` elements to restore their original order.

This approach has a time complexity of O(n) and does not use any extra space (O(1) space complexity), meeting the problem's 
constraints and follow-up requirement. The use of in

-place modifications on the array ensures that no additional memory is allocated beyond the input array itself. 
This method is efficient and elegant, leveraging the power of array reversals to achieve the desired rotation.

*/
