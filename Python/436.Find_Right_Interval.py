"""
# 436. Find Right Interval.

#

# Topic: Array, Binary Search, Sorting.


# Task:
-----------------
You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. 
Note that i may equal j.

Return an array of right interval indices for each interval i. If no right interval exists for interval i,
then put -1 at index i.

Example 1:
Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:
Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.

Example 3:
Input: intervals = [[1,4],[2,3],[3,4]]
Output: [-1,2,-1]
Explanation: There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.

Constraints:

1 <= intervals.length <= 2 * 10^4
intervals[i].length == 2
-10^6 <= starti <= endi <= 10^6
The start point of each interval is unique.


# Testcase:
-----------------
[[1,2]]
[[3,4],[2,3],[1,2]]
[[1,4],[2,3],[3,4]]


# Code:
-----------------
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
    
"""
# Solution:
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Create a sorted list of start points with their original indices
        sorted_starts = sorted((interval[0], i) for i, interval in enumerate(intervals))

        # Function to find the right interval using binary search
        def find_min_start_greater_than_end(end):
            left, right = 0, len(sorted_starts) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if sorted_starts[mid][0] < end:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if left < len(sorted_starts) else -1

        # Find the right interval for each interval
        return [sorted_starts[find_min_start_greater_than_end(interval[1])][1] if find_min_start_greater_than_end(interval[1]) != -1 else -1 for interval in intervals]


# Description:
'''
To solve the "Find Right Interval" problem, we can approach it in the following way:
Approach:

1.Create a Sorted List of Intervals: We first create a list of the start points of each interval along 
  with their original indices and sort this list. This helps in efficiently finding the smallest start 
  point greater than or equal to a given end point.

2.Binary Search for Right Interval: For each interval, we perform a binary search on the sorted list of
  start points to find the smallest start point that is greater than or equal to the end point of the 
  current interval.

3.Handle No Right Interval Case: If no such start point is found, we return -1 for that interval.

4.Return Results: Finally, we return an array of the indices of the right intervals found for each interval.

Explanation:

- We store each start point along with its index in the sorted_starts list.
- The find_min_start_greater_than_end function performs a binary search to find the index of the smallest 
  start point that is greater than or equal to the given end point.
- We iterate over each interval, using this function to find the right interval or return -1 if no such 
  interval exists.

This solution efficiently handles the problem by leveraging sorting and binary search, resulting in a time
complexity that is better than a brute-force approach.

'''
