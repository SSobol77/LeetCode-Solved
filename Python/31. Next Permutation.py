# 31. Next Permutation.             -Medium-

# Topic:Array, Two Pointers.

"""
### Task:
---
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, 
the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100


### Tstcase:
---
[1,2,3]
[3,2,1]
[1,1,5]


### Code:
---
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        '''
        Do not return anything, modify nums in-place instead.
        '''
        

"""
### Solution: ------------------------------------------------

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # Step 1: Find the first decreasing element
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:  # If the array is not entirely in descending order
            # Step 2: Find the element to swap with
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the sub-array from nums[i+1] to the end
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


### Descripton: =================================================
'''
To solve the "Next Permutation" problem, the goal is to rearrange the numbers in the given array to form the next lexicographically greater permutation. The steps to achieve this are as follows:

1. **Find the first decreasing element**: Traverse the array from the end and find the first element `nums[i]` which is smaller than the element to its right `nums[i+1]`. If there is no such element, it means the entire array is in descending order, and we just need to reverse it to get the lowest possible order (ascending).

2. **Find the element to swap with**: If such an element is found in step 1, traverse again from the end and find the first element `nums[j]` which is larger than `nums[i]`.

3. **Swap and reverse**: Swap `nums[i]` and `nums[j]`, then reverse the sub-array from `nums[i+1]` to the end to get it in ascending order.

This code modifies the given array in-place to form the next permutation, adhering to the problem's constraint of using only constant extra memory.

For the given test cases:

- `nums = [1,2,3]` will output `[1,3,2]`
- `nums = [3,2,1]` will output `[1,2,3]`
- `nums = [1,1,5]` will output `[1,5,1]`


'''