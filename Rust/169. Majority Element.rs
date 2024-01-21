// 169. Majority Element.          -Easy-

// Topic: Array, Hash Table, Divide and Conquer, Sorting, Counting.

/*
### Task:
---
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority 
element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9

Follow-up: Could you solve the problem in linear time and in O(1) space?


### Testcase:
---
[3,2,3]
[2,2,1,1,1,2,2]


### Code:
---
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        
    }
}

*/
//Solution: -------------------------------------

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut count = 0;  // Counter for the majority element
        let mut candidate = 0;  // To store the potential majority element

        for &num in &nums {
            if count == 0 {
                // When count is 0, we choose the current element as the new candidate.
                candidate = num;
            }
            // If the current element is the same as the candidate, increase the count,
            // otherwise decrease it.
            count += if num == candidate { 1 } else { -1 };
        }

        // The candidate is the majority element
        candidate
    }
}

// Description: ---------------------------------
/*
To solve the "Majority Element" problem, an efficient approach is to use the Boyer-Moore Voting Algorithm. 
This algorithm offers a solution with linear time complexity (O(n)) and constant space complexity (O(1)), satisfying 
the follow-up challenge. 


### Precision Description:

The Boyer-Moore Voting Algorithm works by maintaining a count of a potential majority element (candidate). 

It iterates through the array, and for each element:

- If the count is zero, the algorithm picks the current element as a new candidate.
- Then, it increments the count if the current element is the same as the candidate, or decrements the count otherwise.

Since the majority element appears more than ⌊n / 2⌋ times, the candidate at the end of the array traversal is guaranteed 
to be the majority element. This method effectively "votes" elements in and out based on their frequency, ensuring that the 
one with a frequency greater than half the array's length survives.

This approach is highly efficient as it only requires a single pass through the array (O(n) time complexity) and uses only 
two additional variables, thus achieving O(1) space complexity.

*/
