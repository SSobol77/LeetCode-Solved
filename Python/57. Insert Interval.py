# 57. Insert Interval.

# Topic: Array.

"""
### Task:
---

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5


### Testcase:
---
[[1,3],[6,9]]
[2,5]
[[1,2],[3,5],[6,7],[8,10],[12,16]]
[4,8]


### Code:
---
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
  

"""
### Solution: --------------------------------------

class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        
        # Add all intervals ending before newInterval starts
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Merge all overlapping intervals to one considering newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)  # Add the union of intervals
        
        # Add all the rest
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        
        return result


### Description: ===================================
'''
To insert a new interval into a list of non-overlapping, sorted intervals and merge overlapping intervals if necessary, you can follow these steps:

1. **Initialize variables:** Create a result list to store the final set of intervals after the insertion and merging.

2. **Add non-overlapping intervals before the new interval:** Iterate through the list of intervals. For each interval, if the end of the current interval is less than the start of the new interval, it means there's no overlap. Add such intervals to the result list directly.

3. **Merge overlapping intervals:** For intervals that overlap with the new interval (the start of the current interval is less than or equal to the end of the new interval, and the end of the current interval is greater than or equal to the start of the new interval), merge them by updating the start of the new interval to the minimum of the current interval's start and the new interval's start, and the end of the new interval to the maximum of the current interval's end and the new interval's end.

4. **Add the merged new interval:** After processing all potential overlaps, add the updated new interval to the result list.

5. **Add remaining intervals:** Finally, add any remaining intervals that come after the new interval to the result list.

6. **Return the result list.**


### Explanation:

- The first `while` loop adds all intervals that end before the new interval starts to the result list. These intervals don't overlap with the new interval.
- The second `while` loop merges all overlapping intervals, including the new interval, into a single interval. It updates the start of the new interval to the minimum start between the current and new interval, and the end to the maximum end.
- The merged new interval is then added to the result list.
- The final `while` loop adds any remaining intervals that start after the new interval ends to the result list.
- The result list, which now contains the original intervals with the new interval inserted and any necessary merges performed, is returned.

'''
