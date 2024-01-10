# 300. Longest Increasing Subsequence.

# Topic: Array, Binary Search,Dynamic Programming.


'''
# Task:
-------
Given an integer array nums, return the length of the longest strictly increasing
subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4


# Testcase:
-----------
[10,9,2,5,3,7,101,18]
[0,1,0,3,2,3]
[7,7,7,7,7,7,7]


# Code:
-------
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

'''
# Solution:

from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []  # This array will store the smallest tail of all increasing subsequences

        for num in nums:
            # Find the index of the first element in tails that is greater than or equal to num
            index = bisect.bisect_left(tails, num)

            # If num is larger than all elements in tails, append it
            if index == len(tails):
                tails.append(num)
            else:
                # Otherwise, replace the first element that is greater than or equal to num
                tails[index] = num

        # The length of tails array is the length of the longest increasing subsequence
        return len(tails)

# Test cases
solution = Solution()
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Expected output: 4
print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))            # Expected output: 4
print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))         # Expected output: 1


'''
Description:
To find the length of the longest strictly increasing subsequence in an array, a very efficient 
algorithm combines dynamic programming with binary search. The method involves maintaining an 
array that stores the smallest possible tail for all increasing subsequences with different lengths.

Explanation:
- Tails Array: tails is an array that stores the smallest possible tail for all increasing subsequences 
with different lengths.
- Iterating Through Nums: For each number num in the input array nums, find the position where this number 
would fit in the tails array. This is done using binary search, which makes the algorithm efficient.
- Updating Tails: If num is larger than all elements in tails, it is appended, indicating a new subsequence 
with a larger length is found. If num is smaller, it replaces the first element in tails that is greater 
than or equal to num. This step ensures that tails always contains the smallest possible tails.
- Length of LIS: The length of the tails array at the end of the iteration represents the length of the 
longest strictly increasing subsequence.

This approach is efficient with a time complexity of O(n log n), where n is the number of elements in the 
input array nums. This is due to the use of binary search (log n) within a loop through the elements (n).

'''
