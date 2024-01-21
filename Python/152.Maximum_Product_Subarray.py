# 152. Maximum Product Subarray.

# Topic: Array, Dynamic Programming.

"""
## Task:
---------
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


## Testcase:
-------------
[2,3,-2,4]
[-2,0,-1]


## Code:
----------
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

"""
# Solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:  # Check if the nums list is empty
            return 0

        # Initialize max_product and min_product to the first element.
        # max_product is the maximum product up to the current element.
        # min_product is the minimum product (which might become maximum if multiplied by a negative number).
        # result stores the maximum product found so far.
        max_product = min_product = result = nums[0]

        # Iterate through the nums array starting from the second element.
        for i in range(1, len(nums)):
            # If the current element is negative, swap max_product and min_product.
            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            # Update max_product. It is the maximum of the current element and the product of the current element and the previous max_product.
            # This accounts for the possibility that the maximum product ends at the current element.
            max_product = max(nums[i], max_product * nums[i])

            # Similarly, update min_product. It is the minimum of the current element and the product of the current element and the previous min_product.
            min_product = min(nums[i], min_product * nums[i])

            # Update the result with the maximum value between the current result and the new max_product.
            result = max(result, max_product)

        # Return the final result, which is the maximum product of any subarray in nums.
        return result


# Description
'''
The Maximum Product Subarray problem is a classic example that can be efficiently solved using dynamic programming. 
The goal is to find the subarray within an array that has the largest product.

## Algorithm:
1. **Initialization**: 
     Set two variables, `max_product` and `min_product`, equal to `nums[0]`. Also, initialize `result` 
     as `nums[0]`. Here, `max_product` tracks the maximum product up to the current element, and `min_product` tracks the 
     minimum (which could become maximum if the next element is negative).

2. **Iterate Through the Array**: For each element in `nums` (except the first one), do the following:

   - **Handle Negative Numbers**: If the current element is negative, swap `max_product` and `min_product` because a 
       negative number times a minimum negative product could turn into a maximum.
   - **Update Max and Min Products**: Update `max_product` by taking the maximum of the current element and the product 
       of the current element and `max_product`. Similarly, update `min_product`.

3. **Update Result**: After each iteration, update `result` to be the maximum of `result` and `max_product`.

4. **Return Result**: After the loop ends, `result` contains the maximum product of any subarray.

## Complexity:
- Time Complexity: O(n), where n is the number of elements in the array. This is because we only need to iterate through 
  the array once.
- Space Complexity: O(1), as we are using only a constant amount of extra space.

## Explanation of Examples:
- **Example 1**: `nums = [2,3,-2,4]`. The subarray `[2,3]` gives the largest product, which is 6.
- **Example 2**: `nums = [-2,0,-1]`. The largest product is 0, as the subarray cannot extend across the 0 (which resets the product).

This solution efficiently handles the variations in the product due to the presence of negative numbers and zeroes in the array.

'''
