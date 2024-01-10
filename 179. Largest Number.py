# 179. Largest Number

# Topic:

'''
# Task:
-------------------
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 10^9


# Testcase:
--------------
[10,2]
[3,30,34,5,9]

# Code:
--------------
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        

'''
# Solution:
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert integers to strings for comparison
        nums = [str(num) for num in nums]

        # Custom sort function to decide which combination is larger
        nums.sort(key=lambda x: x*10, reverse=True)

        # Join the numbers to form the largest number
        largest_num = ''.join(nums)

        # Check if the result is all zeros (to avoid returning '00...0')
        if largest_num[0] == '0':
            return '0'

        return largest_num

# Test cases
sol = Solution()
test1 = [10, 2]
test2 = [3, 30, 34, 5, 9]

output1 = sol.largestNumber(test1)
output2 = sol.largestNumber(test2)

output1, output2

# Description:
'''
To solve this problem correctly, you need to sort the numbers such that when they are concatenated,
they form the largest possible number.

A key insight is to compare the numbers after converting them to strings and concatenating them in
different orders. For example, when comparing '3' and '30', we need to compare '330' and '303' to 
see which should come first.

'''
