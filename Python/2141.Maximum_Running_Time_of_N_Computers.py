# 2141. Maximum Running Time of N Computers

# Topic: Array, Binary Search, Greedy, Sorting.

'''
# Task:
-------
You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a 
computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove 
a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery 
or a battery from another computer. You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.

Example 1:
Input: n = 2, batteries = [3,3,3]
Output: 4
Explanation: 
Initially, insert battery 0 into the first computer and battery 1 into the second computer.
After two minutes, remove battery 1 from the second computer and insert battery 2 instead. Note that battery 1 can still run for one minute.
At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer and insert battery 1 instead.
By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.
We can run the two computers simultaneously for at most 4 minutes, so we return 4.

Example 2:
Input: n = 2, batteries = [1,1,1,1]
Output: 2
Explanation: 
Initially, insert battery 0 into the first computer and battery 2 into the second computer. 
After one minute, battery 0 and battery 2 are drained so you need to remove them and insert battery 1 into the first computer and battery 3 into the second computer. 
After another minute, battery 1 and battery 3 are also drained so the first and second computers are no longer running.
We can run the two computers simultaneously for at most 2 minutes, so we return 2.
 
Constraints:
1 <= n <= batteries.length <= 10^5
1 <= batteries[i] <= 10^9

Hint 1
For a given running time, can you determine if it is possible to run all n computers simultaneously?

Hint 2
Try to use Binary Search to find the maximal running time



# Testcase:
-----------
2
[3,3,3]
2
[1,1,1,1]


# Code:
-------
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
     

'''
# Solution:
from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # Sort the batteries to easily identify the ones with the most charge.
        batteries.sort()

        # Select the 'n' batteries with the most charge for the 'n' computers.
        comps = batteries[-n:]

        # Calculate the total reserve power from the remaining batteries.
        reserve = sum(batteries[:-n])

        # Iterate through the batteries in 'comps' (except the first one).
        for i in range(1, len(comps)):
            # Calculate the amount of power needed to equalize the charge of the current
            # battery with the next higher-charged battery, multiplied by the number of
            # batteries that have been equalized so far.
            needed = (comps[i] - comps[i-1]) * i

            # If the reserve power is not enough to equalize the charge of the current battery
            # with the next, distribute the remaining reserve power equally among the
            # batteries equalized so far and return the total runtime.
            if reserve <= needed:
                return comps[i-1] + reserve // i
            
            # If the reserve power is sufficient, subtract the used power from the reserve.
            reserve -= needed
        
        # If all batteries in 'comps' are equalized, distribute the remaining reserve power
        # equally among all 'n' computers and return the total runtime.
        return comps[-1] + reserve // n


# Description:
'''
This code essentially sorts the batteries and then tries to equalize the charge among the n most
charged batteries, utilizing the reserve from the lesser-charged ones. If the reserve runs out 
before equalizing all n batteries, it calculates the maximum runtime with the available power. 
If it manages to equalize all n batteries, it distributes the remaining reserve power equally among them.

'''
