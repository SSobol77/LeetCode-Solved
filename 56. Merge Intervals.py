# 56. Merge Intervals

# Topic: Array, Sorting.

"""
### Task:
---
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and 
return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4

### Testcase:
---
[[1,3],[2,6],[8,10],[15,18]]
[[1,4],[4,5]]


### Code:
---
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
"""
###Solution: ------------------------------------------------
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # If the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Otherwise, there is an overlap, so we merge the current and previous intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

## Test Cases:
sol = Solution()
# Test case 1
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))  # Expected output: [[1,6],[8,10],[15,18]]
# Test case 2
print(sol.merge([[1,4],[4,5]]))  # Expected output: [[1,5]]


### Description: =============================================
'''
To solve the "Merge Intervals" problem, the idea is to first sort the intervals based on the starting time of each interval. 
Once sorted, we can then iterate through the intervals and merge them if they overlap. Overlapping is determined if the end 
time of the current interval is greater than or equal to the start time of the next interval. 

Here's the step-by-step algorithm:

1. Sort the intervals based on the start time.
2. Initialize a list, say `merged`, to hold the merged intervals.
3. For each interval in the sorted list:
    - If the `merged` list is empty or if the current interval does not overlap with the last interval in `merged`, append it to `merged`.
    - Otherwise, there is an overlap, so we merge the current interval with the last interval in `merged` by updating the end time of t
      he last interval in `merged` to be the maximum of the end times of both overlapping intervals.

This code will correctly merge the intervals as per the problem statement.

'''
