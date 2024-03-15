# 238. Product of Array Except Self.      -Medium-

# Topic: Array, Prefix Sum.

"""
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
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
"""
# Solution: -------------------------------------

class Solution:
    def productExceptSelf(self, nums):
        # Get the number of elements in nums
        n = len(nums)
        
        # Initialize the result list with 1s for each element
        result = [1] * n

        # Initialize left_product as 1 before the start of the loop
        left_product = 1
        # Calculate the product of all elements to the left of each element
        for i in range(1, n):
            left_product *= nums[i - 1]  # Multiply the current left_product with the element to the left of i
            result[i] = left_product  # Store the current left_product in result[i]

        # Initialize right_product as 1 before the start of the loop
        right_product = 1
        # Calculate the product of all elements to the right of each element
        for i in range(n - 1, -1, -1):  # Start from the end of the list and move backwards
            result[i] *= right_product  # Multiply the current value in result[i] by the right_product
            right_product *= nums[i]  # Update right_product to include the current element

        # Return the result list containing the product of all elements except self
        return result

# Test the function with the provided test cases
sol = Solution()
test_case_1 = [1, 2, 3, 4]
test_case_2 = [-1, 1, 0, -3, 3]

output_1 = sol.productExceptSelf(test_case_1)
output_2 = sol.productExceptSelf(test_case_2)

output_1, output_2



# Description: ==================================
'''
This code uses two passes to compute the result:
1. The first pass (forward) computes the running product of all elements to the left of each index and stores it in the `result` array.
2. The second pass (backward) multiplies the running product of all elements to the right of each index by the value already stored in `result` from the first pass, giving the final answer.

'''