// 152. Maximum Product Subarray.


// Topic: Array, Dynamic Programming.


/*
### Task:
---
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 10^4
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

### Testcase:
---
[2,3,-2,4]
[-2,0,-1]


### Code:
---
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.empty()) return 0;

        int maxProduct = nums[0];
        int minProduct = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.size(); ++i) {
            // When the current element is negative, maxProduct and minProduct will swap values.
            if (nums[i] < 0) std::swap(maxProduct, minProduct);

            // maxProduct and minProduct are updated by considering the current element and
            // the product of the current element with the previous maxProduct and minProduct.
            maxProduct = std::max(nums[i], maxProduct * nums[i]);
            minProduct = std::min(nums[i], minProduct * nums[i]);

            // Update the result with the maximum product found so far.
            result = std::max(result, maxProduct);
        }

        return result;
    }
};

// Description: ===================================
/*
To solve the "Maximum Product Subarray" problem, we need to keep track of the maximum and minimum products at each 
position in the array, because a negative number can turn a minimum product into a maximum product and vice versa. 
We iterate through the array while updating the maximum and minimum products using the current number, the product 
of the current number and the maximum product so far, and the product of the current number and the minimum product 
so far. The maximum product found during the iteration is the result.

Here's a step-by-step approach:

1. **Initialize Variables**: Start with `maxProduct`, `minProduct`, and `result` initialized to the first element of the array. `maxProduct` and `minProduct` represent the maximum and minimum product subarrays ending at the current position, and `result` is the maximum product of any subarray found so far.
2. **Iterate Through the Array**: For each element in the array starting from the second element, update `maxProduct` and `minProduct` by considering the current element, the product of the current element and the previous `maxProduct`, and the product of the current element and the previous `minProduct`.
3. **Handle Negative Numbers**: Since a negative number can change the maximum product to minimum and vice versa, compare both the product of the current element with the previous `maxProduct` and `minProduct`.
4. **Update Result**: After updating `maxProduct` and `minProduct` for the current element, update the `result` if `maxProduct` is greater than the current `result`.

### Description of the Solution:

This solution employs dynamic programming where `maxProduct` and `minProduct` are used to keep track of the maximum and minimum product subarrays ending at the current position. This is necessary because multiplying a negative number by the smallest product could result in the largest product. By iterating through the array and updating these values while considering the current element, we can find the maximum product subarray. The `result` variable keeps track of the maximum product encountered during the iteration, which is ultimately returned as the solution. This approach efficiently solves the problem by considering all possible subarrays and handling the impact of negative numbers on the product.

*/
