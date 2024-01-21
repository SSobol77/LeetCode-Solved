# 213. House Robber II.     --Medium--

# Topic: Array, Dynamic Programming.

"""
### Task:
---------
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, 
adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were 
broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob 
tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
 
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000

Hint 1
Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to 
rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. Now the 
problem has degenerated to the House Robber, which is already been solved.


### Testcase:
[2,3,2]
[1,2,3,1]
[1,2,3]

### Code:
class Solution:
    def rob(self, nums: List[int]) -> int:

"""
### Solution: ---------------------------------------------

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_line(houses):
            rob1, rob2 = 0, 0
            for house in houses:
                new_rob = max(house + rob1, rob2)
                rob1 = rob2
                rob2 = new_rob
            return rob2

        n = len(nums)
        if n == 1:
            return nums[0]
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))

# Test cases
sol = Solution()
print(sol.rob([2,3,2]))  # Output: 3
print(sol.rob([1,2,3,1]))  # Output: 4
print(sol.rob([1,2,3]))  # Output: 3


### Description: ===========================================
'''
The problem you've described is a variation of the classic dynamic programming problem "House Robber". In this case, the houses are arranged in a circle, which means we cannot rob the first and last houses simultaneously. We can solve this problem by breaking it into two sub-problems:

1. Rob houses from 0 to n-2 (excluding the last house).
2. Rob houses from 1 to n-1 (excluding the first house).

The maximum of these two cases will be the answer. We can use dynamic programming to solve each sub-problem.

Explanation:

- `rob_line` function is a helper function to solve the classic house robber problem for a line of houses. It uses two variables, `rob1` and `rob2`, to keep track of the maximum amount robbed so far.
- For the given `nums`, we first check if there is only one house. If so, we simply return its value.
- If there are more houses, we calculate the maximum money that can be robbed by either excluding the first house (`nums[1:]`) or excluding the last house (`nums[:-1]`).
- Finally, we return the maximum of these two values. 

This solution effectively handles the circular arrangement of houses by considering two separate cases and applying dynamic programming to each.

'''