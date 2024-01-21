# 45. Jump Game II.

# Topic: Array, Dynamic Programming, Greedy.

"""
## Task:
---------
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], 
you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to 
the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

## Testcase:
-------------
[2,3,1,1,4]
[2,3,0,1,4]

## Code:
----------
class Solution:
    def jump(self, nums: List[int]) -> int:  

"""
# Solution

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0  # Initialize the number of jumps
        max_reach = 0  # Initialize the maximum index that can be reached with the current number of jumps
        current_end = 0  # Initialize the end index of the current jump
        
        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])  # Update the maximum index that can be reached
            
            if i == current_end:
                jumps += 1  # Increment jumps because we reached the end of the current jump
                current_end = max_reach  # Set the end index of the next jump as the updated max_reach
            
            if current_end >= n - 1:
                break  # If we can reach the last index, no need to continue
        
        return jumps


# Description
'''
To solve this problem, we can use a greedy approach to determine the minimum number of jumps needed to reach the last index.
We can use this jump method of the Solution class to find the minimum number of jumps needed to reach the last index. 
The greedy approach is used to determine the optimal jump strategy, and the function returns the required number of jumps.

'''