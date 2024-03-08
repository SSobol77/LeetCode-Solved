// 238. Product of Array Except Self.

// Topic: Array, Prefix Sum.


/*
### Task:
---
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

### Testcase:
---
[1,2,3,4]
[-1,1,0,-3,3]


### Code:
---
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
    }
};


*/
// Solution: --------------------------------------

#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int length = nums.size();
        // Initialize the answer array with 1s, as the product of no elements is 1.
        std::vector<int> answer(length, 1);

        // First pass: Calculate prefix products for each element.
        // Prefix product of an element at index i is the product of all elements to the left of i.
        int prefix = 1;
        for (int i = 0; i < length; ++i) {
            // Store the current prefix product at the current index.
            answer[i] = prefix;
            // Update the prefix product for the next iteration.
            prefix *= nums[i];
        }

        // Second pass: Calculate suffix products and multiply with prefix products.
        // Suffix product of an element at index i is the product of all elements to the right of i.
        int suffix = 1;
        for (int i = length - 1; i >= 0; --i) {
            // Multiply the current suffix product with the value in the answer array (which currently holds the prefix product).
            answer[i] *= suffix;
            // Update the suffix product for the next iteration.
            suffix *= nums[i];
        }

        // The answer array now contains the product of all elements except self for each element.
        return answer;
    }
};




// Description: ===================================
/*
To solve the "Product of Array Except Self" problem within the constraints specified (O(n) time complexity and without using division), 
a common approach involves using two arrays to store the prefix and suffix products of each element. However, to achieve O(1) extra 
space complexity (excluding the output array), we can modify the output array in-place to store the prefix products and use a single 
variable to keep track of the suffix products during a second pass through the array.

Here's the step-by-step approach:

1. Initialize the answer array with the same size as `nums`, setting all elements to 1. This array will hold the final results.
2. Calculate the prefix product for each element and store it in the answer array. The prefix product of an element at index `i` is 
   the product of all elements to the left of `i`.
3. Use a variable to keep track of the suffix product (product of all elements to the right of the current element). Traverse the 
   array in reverse, and for each element, multiply the current suffix product with the corresponding element in the answer array to 
   get the final product for that element.
4. Update the suffix product variable by multiplying it with the current element in `nums`.


### Description:
---
This solution first initializes the answer array with 1s, then calculates the prefix product for each element and stores it in the 
answer array. It then iterates through the array in reverse to calculate the suffix product for each element and multiplies it with 
the corresponding prefix product already stored in the answer array. This approach efficiently computes the product of all elements 
except the current one for each position in the array, adhering to the O(n) time complexity constraint and achieving O(1) space 
complexity if we exclude the space required for the output array.

*/
