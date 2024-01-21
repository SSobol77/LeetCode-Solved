// 238. Product of Array Except Self.      -Medium-

// Topic: Array, Prefix Sum.

/*
### Task:
---
Given an integer array nums, return an array answer such that answer[i] is equal to the product of 
all the elements of nums except nums[i].

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
 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count 
           as extra space for space complexity analysis.)

### Testcase:
---
[1,2,3,4]
[-1,1,0,-3,3]

### Code:
---
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
*/
//Solution: -------------------------------------

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len(); // Get the length of the input array
        let mut answer = vec![1; n]; // Initialize the answer array with 1s. This array will eventually contain the product of all elements except the one at the current index.

        // Calculate left products for each element
        let mut left_product = 1; // Initialize left_product which will hold the product of all elements to the left of the current index
        for i in 0..n {
            // For each element in the array:
            answer[i] = left_product; // Set the current index of answer to left_product. Initially, for the first element, it will be 1 (as there are no elements to the left).
            left_product *= nums[i]; // Update left_product by multiplying it with the current element. This prepares left_product for the next index in the array.
        }

        // Calculate right products for each element and finalize the answer
        let mut right_product = 1; // Initialize right_product which will hold the product of all elements to the right of the current index
        for i in (0..n).rev() {
            // Traverse the array in reverse order:
            answer[i] *= right_product; // Multiply the current index of answer with right_product. This combines the product of all elements to the left and right of the current index.
            right_product *= nums[i]; // Update right_product by multiplying it with the current element. This prepares right_product for the next index (to the left) in the array.
        }

        answer // Return the final answer array
    }
}


// Description: ---------------------------------
/*
To solve the problem presented, we'll implement the `product_except_self` function in Rust. The function must compute the product of all elements in the `nums` array except the current element, without using division and ensuring a time complexity of O(n).

The key strategy here is to use two arrays (or one array with two passes if optimizing for space): 
1. `left_products`: At each index `i`, it stores the product of all elements to the left of `i`.
2. `right_products`: At each index `i`, it stores the product of all elements to the right of `i`.

Finally, we calculate the output array where each element is the product of its corresponding values in `left_products` and `right_products`.

Explanation:
- We initialize `answer` as a vector of 1's, since the product of zero numbers is 1.
- We first traverse the array from left to right, updating `left_product` with the cumulative product at each step, and setting `answer[i]` to `left_product`.
- Then, we traverse from right to left. We update `right_product` with the cumulative product and multiply `answer[i]` by `right_product`. This step combines the left and right products for each element.

This solution has a time complexity of O(n) as it traverses the array twice, and a space complexity of O(1) (not counting the output array, as per the problem's follow-up requirement).

*/