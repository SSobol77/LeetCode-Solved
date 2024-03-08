// 136. Single Number.


// Topic: Array, Bit Manipulation.


/*
### Task:
---
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
Each element in the array appears twice except for one element which appears only once.


### Testcase:
---
[2,2,1]
[4,1,2,1,2]
[1]


### Code:
---
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>

class Solution {
public:
    int singleNumber(std::vector<int>& nums) {
        int result = 0; // Initialize result to 0.

        // Iterate over all the elements in the array.
        for (int num : nums) {
            // XOR the result with each element. Identical numbers will cancel each other out.
            result ^= num;
        }

        // After the entire array has been XORed, the result will be the single number.
        return result;
    }
};


// Description: ===================================
/*
To solve the "Single Number" problem, we can use bit manipulation, specifically the XOR operation, which is an excellent tool 
for this task due to its properties. The XOR of two identical numbers is 0 (e.g., `a XOR a = 0`), and the XOR of any number 
with 0 is the number itself (e.g., `a XOR 0 = a`). Moreover, XOR is commutative and associative, which means the order of 
operations does not affect the result.

Given the problem statement, every element in the array `nums` appears exactly twice except for one element that appears only once. 
By XORing all the elements in the array, the pairs of identical numbers will cancel each other out (become 0), and we will be left 
with the unique number, as `a XOR a XOR b = 0 XOR b = b`, where `b` is the unique number.

### Description:
---
This solution iterates through the array `nums` and applies the XOR operation between `result` and each element in the array. 
Since XOR of two identical numbers is 0 and XOR of any number with 0 is the number itself, and given that all elements except 
one appear twice in the array, all paired elements will cancel each other out, leaving `result` with the value of the single 
element by the end of the loop. This approach satisfies the constraints of linear runtime complexity and constant extra space, 
making it an efficient solution to the problem.

*/
