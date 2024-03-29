# 137. Single Number II

'''
Task:
-----
Given an integer array nums where every element appears three times except for one, which appears exactly once. 
Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
 
Constraints:
1 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each element in nums appears exactly three times except for one element which appears once.


# Testcase:
-----------
[2,2,3,2]
[0,1,0,1,0,1,99]


# Code:
-------
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    

'''
# Solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos, threes = 0, 0, 0
        
        for num in nums:
            # Update twos by adding the bits that appear twice
            twos |= ones & num
            
            # XOR ones with the current number. 
            # If a bit in num is set, it will be unset in ones if it was set, or set if it was unset
            ones ^= num
            
            # If a bit is set in both ones and twos, it means it has appeared three times
            threes = ones & twos
            
            # Remove the bits that have appeared three times from ones and twos
            ones &= ~threes
            twos &= ~threes

        return ones
