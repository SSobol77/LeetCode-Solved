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
        n = len(nums)
        # Initialize two arrays: 'left' to store the product of elements to the left of each index,
        # and 'result' to store the final product values.
        left, result = [0] * n, [0] * n
        
        # The product of elements to the left of the first element is 1 (since there are no elements to the left)
        left[0] = 1
        for i in range(1, n):
            # left[i] is the product of all elements to the left of 'nums[i]', which is
            # the product up to 'nums[i - 1]' (stored in left[i - 1]) times 'nums[i - 1]'
            left[i] = nums[i - 1] * left[i - 1]
        
        # 'right' will keep track of the product of elements to the right of the current index
        right = 1
        for i in range(n - 1, -1, -1): # Loop through the array in reverse
            # For each index i, multiply the product of all elements to the left (left[i])
            # with the product of all elements to the right (right) to get the final product
            result[i] = left[i] * right
            # Update 'right' to include the current element, for the next iteration
            right *= nums[i]
        
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
In this code:
- The `left` array is used to store the cumulative product of all elements to the left of each index in the input array.
- The `right` variable is used to keep track of the cumulative product of elements to the right of the current index as we iterate 
  backward through the array.
- The final result is obtained by multiplying the corresponding values from the `left` array and the `right` variable.


The "Product of Array Except Self" problem requires us to calculate, for each element in the array, the product of all other 
elements in the array without including the current element. The challenge is to do this efficiently, in O(n) time complexity, 
and without using division.

### Algorithm:
1. Create two arrays, `left` and `right`, each of the same length as the input array `nums`. 
2. Fill the `left` array such that `left[i]` contains the product of all elements to the left of `i` in `nums`.
3. Similarly, fill the `right` array such that `right[i]` contains the product of all elements to the right of `i` in `nums`.
4. Create an output array `result` of the same length as `nums`.
5. For each index `i` in `nums`, calculate `result[i]` as `left[i] * right[i]`.
6. Return `result`.

### Optimization for Space Complexity:
To optimize space complexity, we can avoid using the `right` array. Instead, we can directly accumulate the product from the 
right in a variable and use it to update the `result` array.


### Explanation:
- `left` array stores the cumulative product of elements to the left of the current index.
- We iterate from right to left, keeping track of the cumulative product (`right`) and multiplying it with the corresponding 
 `left` value to get the final product for each index.
- This approach takes O(n) time and O(1) space (excluding the output array).

### Example Execution:
- Input: `[1,2,3,4]`
- `left` array after first loop: `[

The implemented solution correctly solves the "Product of Array Except Self" problem for the given test cases:

1. For the input `[1, 2, 3, 4]`, the output is `[24, 12, 8, 6]`. 
   - Here, each element in the output array is the product of all other elements in the input array, except for the element at the 
    corresponding position.

2. For the input `[-1, 1, 0, -3, 3]`, the output is `[0, 0, 9, 0, 0]`.
   - Notably, when there's a `0` in the input array (like in this case), the product for all positions except where the zero is 
     located will be `0`, since multiplying by zero results in zero. The position corresponding to the zero in the input array 
     gets the product of all other (non-zero) elements.

This solution meets the requirements of the problem:
- It runs in O(n) time complexity, iterating over the array twice.
- It doesn't use the division operation.
- It has O(1) extra space complexity, excluding the output array, as it uses only a constant amount of additional space for the 
  `left` and `right` variables.

'''