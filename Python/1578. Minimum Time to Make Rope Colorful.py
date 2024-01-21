# 1578. Minimum Time to Make Rope Colorful

# Topic:

'''
# Task:
-------
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the 
color of the ith balloon.
Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color,
so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given 
a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove 
the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

Example 1:
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.

Example 2:
Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.

Example 3:
Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
 
Constraints:
n == colors.length == neededTime.length
1 <= n <= 10^5
1 <= neededTime[i] <= 10^4
colors contains only lowercase English letters.

Hint 1
Maintain the running sum and max value for repeated letters.



# Testcase:
-----------
"abaac"
[1,2,3,4,5]
"abc"
[1,2,3]
"aabaa"
[1,2,3,4,1]



# Code:
--------
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
 
'''
# Solution:
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        # Initialize the total time required to remove balloons
        totalTime = 0

        # Initialize the maximum time needed to remove a balloon in a sequence of the same color
        maxTime = 0

        # Iterate through each balloon
        for i in range(len(colors)):
            # If the current and previous balloons are the same color
            if i > 0 and colors[i] == colors[i - 1]:
                # Add the minimum of the current or previous balloon's removal time to the total
                totalTime += min(maxTime, neededTime[i])
                # Update maxTime to the maximum removal time of the current sequence
                maxTime = max(maxTime, neededTime[i])
            else:
                # Reset maxTime for a new color sequence
                maxTime = neededTime[i]

        return totalTime

# Example tests
sol = Solution()
print(sol.minCost("abaac", [1,2,3,4,5]))  # Expected Output: 3
print(sol.minCost("abc", [1,2,3]))        # Expected Output: 0
print(sol.minCost("aabaa", [1,2,3,4,1]))  # Expected Output: 2

'''
Description:
-------------
In this code, we use a greedy approach to minimize the total time it takes to remove the balls. 
The key point is to maintain the maximum removal time for each sequence of identical colors and 
add to the total time the minimum time of two adjacent balls of the same color. This method 
provides an effective and optimal solution to the problem.

'''
