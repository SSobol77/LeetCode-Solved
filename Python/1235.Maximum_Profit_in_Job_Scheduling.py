# 1235. Maximum Profit in Job Scheduling.

# Topic: Array, Binary Search, Dynamic Programming, Sorting.

"""
# Task:
----------------
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining 
a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such 
that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 
Constraints:
1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4

Hint 1:
Think on DP.
Hint 2:
Sort the elements by starting time, then define the dp[i] as the maximum profit taking elements from the suffix starting at i.
Hint 3:
Use binarySearch (lower_bound/upper_bound on C++) to get the next index for the DP transition.


# Testcase:
--------------------
[1,2,3,3]
[3,4,5,6]
[50,10,40,70]
[1,2,3,4,6]
[3,5,10,6,9]
[20,20,100,70,60]
[1,1,1]
[2,3,4]
[5,6,4]


# Code:
---------------------
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

"""

# Solution:
from typing import List
from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine start time, end time, and profit into a single list and sort by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        # Initialize a DP list with a tuple (end time, max profit until this time)
        dp = [(0, 0)]
        max_profit = 0

        for start, end, p in jobs:
            # Find the index of the last job that ends before the current job starts
            # bisect_right is used to find the insertion point which would maintain the sorted order
            i = bisect_right(dp, (start, float('inf'))) - 1

            # Calculate total profit if the current job is included
            total_profit = dp[i][1] + p

            # If the total profit is greater than the current max profit, update it
            if total_profit > max_profit:
                max_profit = total_profit
                # Add the new end time and updated max profit to the DP list
                dp.append((end, max_profit))

        # Return the maximum profit achieved
        return max_profit

# Test cases
sol = Solution()
print(sol.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))  # Expected: 120
print(sol.jobScheduling([4,2,4,8,2], [5,5,5,10,8], [1,2,8,10,4]))  # Expected: 18



# Description:
'''
The key is to correctly handle overlapping jobs and efficiently find the most profitable combination
 of non-overlapping jobs:

1. Sort Jobs by End Time: We will sort the jobs by their end times. This ordering ensures that when we 
   process a job, all potential previous non-overlapping jobs have already been considered.

2. Dynamic Programming with Efficient Job Selection: For each job, we need to decide whether to include 
   it in our schedule. This decision will be based on the maximum profit achieved by including this job 
   versus the maximum profit without it.

3. Binary Search for Non-Overlapping Jobs: For each job, we will use binary search to find the latest 
   job that ends before the current job starts. This will allow us to efficiently find the maximum profit 
   up to that point.

In this code, we first sort the jobs by their end times. For each job, we use binary search (bisect_right) 
to efficiently find the last job that ends before the current job starts. This approach helps us build up 
the maximum profit by considering each job and deciding whether to include it or not, based on the profits 
of previous non-overlapping jobs. The dynamic programming list dp keeps track of the maximum profit at each 
point, allowing us to avoid recalculating for overlapping time ranges.

'''
