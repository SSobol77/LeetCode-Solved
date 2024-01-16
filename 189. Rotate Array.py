# 189. Rotate Array.           -Medium-

# Topic: Array, Math, Two Pointers.

"""
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
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        '''
        Do not return anything, modify nums in-place instead.
        '''
          
"""
# Solution: -------------------------------------

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n  # Normalize k

        # Function to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        # Reverse the whole array
        reverse(0, n - 1)
        # Reverse the first k elements
        reverse(0, k - 1)
        # Reverse the rest
        reverse(k, n - 1)

# Testing the function
sol = Solution()
test_case_1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
sol.rotate(test_case_1, k1)

test_case_2 = [-1, -100, 3, 99]
k2 = 2
sol.rotate(test_case_2, k2)

test_case_1, test_case_2


# Description: ==================================
'''
The "Rotate Array" problem requires rotating an array to the right by `k` steps. There are multiple ways to approach this problem, 
including using extra space or doing it in-place. The in-place approach is more challenging but more efficient in terms of 
space complexity.

### Algorithm (In-Place Solution):
1. **Normalize the Rotation**: If `k` is larger than the length of the array, it effectively means rotating the array multiple times, 
   which can be simplified. We only need to rotate `k % len(nums)` times.

2. **Reverse the Whole Array**: First, reverse the entire array. This action places the last `k` elements at the front of the array 
    but in reverse order.

3. **Reverse the First k Elements**: Reverse the first `k` elements to correct their order.

4. **Reverse the Rest of the Array**: Finally, reverse the remaining part of the array (from `k` to the end).


### Explanation:
- This solution is in-place, so it doesn't use additional arrays.
- By reversing the array in parts, we effectively rotate it.
- The time complexity is O(n) as each element is moved once.
- The space complexity is O(1) as it only uses a constant amount of extra space.

Let's run this code to test the provided examples.

The implemented solution successfully rotates the arrays as per the given examples:

1. For the input `[1, 2, 3, 4, 5, 6, 7]` with `k = 3`, the output is `[5, 6, 7, 1, 2, 3, 4]`. This matches the expected result, 
demonstrating that the array has been correctly rotated 3 steps to the right.

2. For the input `[-1, -100, 3, 99]` with `k = 2`, the output is `[3, 99, -1, -100]`. This too matches the expected result, 
confirming the correct 2-step rotation.

This in-place solution with a space complexity of O(1) and a time complexity of O(n) effectively solves the "Rotate Array" problem 
by using array reversal.

'''