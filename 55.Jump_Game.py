# 55. Jump Game.

# Topic: Array, Dynamic Programming, Greedy.

"""
## Task:
---------
You are given an integer array nums. You are initially positioned at the array's first index, and each element in 
the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

#Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

#Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible 
to reach the last index.
 
#Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5

## Testcase:
-------------
[2,3,1,1,4]
[3,2,1,0,4]

## Code:
----------
class Solution:
    def canJump(self, nums: List[int]) -> bool:

"""
# Solution

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0  # Initialize the maximum index that can be reached
        
        for i in range(n):
            if i > max_reach:
                return False  # If the current index is not reachable, return False
            
            max_reach = max(max_reach, i + nums[i])  # Update the maximum index that can be reached
        
        return True  # If we can reach the end of the array, return True


# Description
'''
To determine if you can reach the last index, you can use a greedy approach or dynamic programming.

We can use this canJump method of the Solution class to check if it's possible to reach the last index. 
The greedy approach is used to determine if we can keep moving forward, and the function returns True 
if it's possible to reach the last index and False otherwise.

For the given test cases, it will return True for [2,3,1,1,4] and False for [3,2,1,0,4].

'''
