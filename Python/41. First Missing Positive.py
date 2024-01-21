# 41. First Missing Positive.

# Topic: Array, Hash Table

"""
### Task:
---
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:
1 <= nums.length <= 105
-2^31 <= nums[i] <= 2^31 - 1


### Tstcase:
---
[1,2,0]
[3,4,-1,1]
[7,8,9,11,12]


### Code:
---
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

"""
###Solution: ------------------------------------------------

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Iterate through each number in the array
        for i in range(n):
            # Check if the current number belongs in this array (is in the range 1 to n)
            # and is not already in its correct position
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap the number with the number at its 'correct' position
                # nums[i] - 1 is the index where nums[i] should be placed
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # After rearranging, we iterate through the array again
        for i in range(n):
            # The first position where the number is not i + 1,
            # i.e., the number at index i is not equal to i + 1, is our missing number
            if nums[i] != i + 1:
                return i + 1

        # If all numbers are in their correct positions and no number is missing in the sequence,
        # then the smallest missing positive is just beyond the end of the array
        return n + 1


### Description: =============================================
'''
To solve the "First Missing Positive" problem, we need to find the smallest missing positive integer in an unsorted array `nums`. 
The constraints are to implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

We can achieve this by re-arranging the numbers in the array such that each positive integer `i` is placed in the `i-1` index position, 
if possible. This way, we ensure that if an integer is in the array, it will be in its 'correct' position. After rearranging, we can 
simply traverse the array to find the first position where the number is not `i + 1`, indicating the missing positive integer.

Here's a step-by-step approach:

1. Iterate through the array.
2. For each number `nums[i]`, if it is a positive integer and within the range of the array length, swap it with the number 
   at its 'correct' position (`nums[nums[i] - 1]`).
3. Take care to handle duplicates and avoid infinite loops during swapping.
4. After rearranging, iterate through the array again.
5. The first position where `nums[i]` is not equal to `i + 1` is the missing number.
6. If all positions are correct, then the missing number is `len(nums) + 1`.

This code works as follows:

- It first rearranges the elements in the array such that if an element `x` is present in the array and `1 <= x <= n`, then 
  it puts `x` at index `x - 1`.
- Then it scans the array again. The first index `i` for which `nums[i] != i + 1` is the smallest missing positive integer. 
  If all numbers are in their correct positions, the smallest missing positive integer is `n + 1`.

In this code:
- The first `for` loop rearranges the elements. It places each positive integer `x` in the array such that `x` is at index `x - 1`. This is done by swapping elements. The `while` loop is used to keep swapping until all elements are either in their correct positions or are out of range (less than 1 or greater than `n`).
- The second `for` loop checks each position in the array. If an element is not in its 'correct' position (i.e., `nums[i]` is not `i + 1`), it means that `i + 1` is the smallest missing positive integer.
- If all elements are in their correct positions, the smallest missing positive integer is `len(nums) + 1` (i.e., one more than the length of the array), as all integers from `1` to `n` are present.


'''