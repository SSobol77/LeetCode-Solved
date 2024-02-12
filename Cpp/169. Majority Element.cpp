// 169. Majority Element.


// Topic: Array, Hash Table, Divide and Conquer, Sorting, Counting.


/*
### Task:
---
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-10^9 <= nums[i] <= 10^9
 
Follow-up: Could you solve the problem in linear time and in O(1) space?


### Testcase:
---
[3,2,3]
[2,2,1,1,1,2,2]


### Code:
---
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // Initialize count and candidate for majority element
        int count = 0;
        int major;

        // Iterate through the array
        for (int num : nums) {
            // If count is 0, we choose the current element as the new candidate
            if (count == 0) {
                major = num;
            }

            // If the current element is the same as our current candidate, increase the count
            // This means the current candidate is gaining support
            if (num == major) {
                count++;
            } else {
                // If the current element is different, decrease the count
                // This means the current candidate is losing support
                count--;
            }
        }

        // The candidate remaining after the entire array traversal is the majority element
        return major;
    }
};




// Description: ===================================
/*

To solve the "Majority Element" problem, we can use the Boyer-Moore Voting Algorithm, which is efficient in terms of time 
(linear time complexity) and space (constant space complexity). The essence of this algorithm is to find a candidate for 
the majority element and then verify if it is indeed the majority element.

Here's how the Boyer-Moore Voting Algorithm works:
1. Initialize a candidate element `major` and a count `count` to 0.
2. Traverse through the array `nums`.
   - If `count` is 0, set `major` to the current element.
   - If the current element is the same as `major`, increment `count`.
   - Otherwise, decrement `count`.
3. Since the majority element appears more than ⌊n / 2⌋ times, the remaining element in `major` after the entire array is traversed 
   is the majority element.

### Description:
- We initialize `count` to 0 and `major` to an undefined value.
- As we iterate through `nums`, we set `major` to the current element `num` if `count` is 0. This is like saying, "Let's consider this new element as a candidate for the majority element."
- If the current element `num` is the same as our candidate `major`, we increment `count`, indicating that we've found another instance of our candidate.
- If `num` is different from `major`, we decrement `count`, indicating that there's a conflict, and our candidate might not be the majority element.
- By the end of the array, `major` holds the element that has survived these conflicts, which must be the majority element due to the problem's constraints.

This solution is efficient because it only requires a single pass through the array (`O(n)` time complexity) and uses only constant 
extra space (`O(1)` space complexity), meeting the follow-up challenge of solving the problem in linear time and constant space.

*/