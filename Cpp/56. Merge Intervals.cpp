// 56. Merge Intervals.


// Topic: Array, Sorting.


/*
### Task:
---
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of 
the non-overlapping intervals that cover all the intervals in the input.

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
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // Check if the input is empty
        if (intervals.empty()) return {};

        // Sort the intervals based on the start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        // Initialize the result vector with the first interval
        vector<vector<int>> mergedIntervals;
        mergedIntervals.push_back(intervals[0]);

        for (int i = 1; i < intervals.size(); i++) {
            // Get the last interval from the mergedIntervals
            vector<int>& lastInterval = mergedIntervals.back();

            // If the current interval overlaps with the last interval in mergedIntervals, merge them
            if (intervals[i][0] <= lastInterval[1]) {
                lastInterval[1] = max(lastInterval[1], intervals[i][1]);
            } else {
                // If not overlapping, simply add the current interval to mergedIntervals
                mergedIntervals.push_back(intervals[i]);
            }
        }

        return mergedIntervals;
    }
};


// Description: ===================================
/*
To merge overlapping intervals in an array, the primary steps involve sorting the intervals based on their start times and then iterating through the sorted intervals to find and merge the overlapping ones. Here's a detailed breakdown of the process:

1. **Sort the Intervals**: First, sort the `intervals` array based on the start times of the intervals. This ordering ensures that any potential overlapping intervals are positioned next to each other.

2. **Iterate and Merge**: Initialize an empty array `mergedIntervals` to store the result. Then, iterate through the sorted `intervals`. For each interval:
   - If `mergedIntervals` is empty or if the current interval does not overlap with the last interval in `mergedIntervals`, simply add the current interval to `mergedIntervals`.
   - If the current interval does overlap with the last interval in `mergedIntervals`, merge the two intervals by updating the end time of the last interval in `mergedIntervals` to be the maximum of the end times of the two overlapping intervals.

### Description:
This C++ code defines a function `merge` that takes an array of intervals and returns an array of merged intervals. It starts by sorting the `intervals` based on their start times. Then, it initializes a result vector `mergedIntervals` and iterates through the sorted intervals. During the iteration, it checks if the current interval overlaps with the last interval in `mergedIntervals`. If they overlap, it merges them by updating the end time of the last interval in `mergedIntervals`. If they don't overlap, it adds the current interval to `mergedIntervals`. The function finally returns `mergedIntervals`, containing the merged intervals.

*/
