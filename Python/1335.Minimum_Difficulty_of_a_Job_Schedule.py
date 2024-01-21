# 1335. Minimum Difficulty of a Job Schedule

# Topic: Array, Dynamic Programming.

'''
# Task:
-------
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish 
all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each 
day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Example 1:
Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 

Example 2:
Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.

Example 3:
Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.

Constraints:
1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10

Hint 1:
Use DP. Try to cut the array into d non-empty sub-arrays. Try all possible cuts for the array.
Hint 2:
Use dp[i][j] where DP states are i the index of the last cut and j the number of remaining cuts. 
Complexity is O(n * n * d).


# Testcase:
------------
[6,5,4,3,2,1]
2
[9,9,9]
4
[1,1,1]
3


# Code:
------------
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    
'''
# Solution:

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        # If the number of jobs is less than the number of days, it's impossible to schedule.
        if n < d:
            return -1

        # Initialize a 2D DP array with 'infinity' values. The dimensions are (n + 1) x (d + 1).
        # dp[i][j] represents the minimum difficulty to schedule the first i jobs in j days.
        dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
        
        # Base case: No jobs and no days requires 0 difficulty.
        dp[0][0] = 0

        # Iterate over the range of jobs.
        for i in range(1, n + 1):
            # Iterate over the range of days, but not more than the current number of jobs.
            for j in range(1, min(i, d) + 1):
                # Variable to keep track of the maximum difficulty job for the current day.
                max_diff = 0

                # Iterate backwards to find where to split the job schedule.
                # k represents the job index where the previous day ends.
                for k in range(i - 1, j - 2, -1):
                    # Update the maximum difficulty job for the current day.
                    max_diff = max(max_diff, jobDifficulty[k])

                    # Update the DP table with the minimum difficulty found so far.
                    # It is the sum of the minimum difficulty of scheduling the first k jobs in j - 1 days
                    # and the maximum difficulty job on the jth day.
                    dp[i][j] = min(dp[i][j], dp[k][j - 1] + max_diff)

        # Return the result. If dp[n][d] is still infinity, return -1, indicating it's not possible.
        return dp[n][d] if dp[n][d] != float('inf') else -1


# Tests:
sol = Solution()
print(sol.minDifficulty([6, 5, 4, 3, 2, 1], 2))  # Output: 7
print(sol.minDifficulty([9, 9, 9], 4))           # Output: -1
print(sol.minDifficulty([1, 1, 1], 3))           # Output: 3


# Description:
'''
Code Explanation
Dynamic Programming Approach: The code uses a dynamic programming (DP) approach to solve the problem of scheduling jobs 
across days while minimizing the total difficulty.

DP Array Initialization: A 2D DP array dp is initialized with float('inf') to represent the minimum difficulty of 
scheduling jobs. The size is (n + 1) x (d + 1) to accommodate all jobs and days, including the base case of zero jobs
and zero days.

Base Case: The base case dp[0][0] is set to 0, as no difficulty is needed for scheduling zero jobs in zero days.

Iterating Over Jobs and Days: The code iterates through each job (i) and each possible day (j). It considers all 
potential splits where the jobs could be divided between the days.

Max Difficulty Calculation: For each split (represented by k), the maximum job difficulty for the current day is
determined. This is essential because the difficulty of a day is defined by the most difficult job done on that day.

DP Table Update: The DP table is updated with the minimum cumulative difficulty found so far, considering the difficulty 
of previous days and the maximum difficulty of the current day.

Result Computation: The final result is obtained from dp[n][d]. If it's infinity, it means scheduling is not possible, 
and -1 is returned.

This algorithm efficiently computes the minimum difficulty of a job schedule over d days, considering the dependencies
and constraints of the jobs.

'''
