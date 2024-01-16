// 56. Merge Intervals.

// Topic: Array, Sorting.

/*
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
impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
*/
// Solution: ------------------------------------------------

impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        // Sort the intervals based on the starting time.
        // This is essential because it allows us to consider merging intervals in a linear pass.
        intervals.sort_by(|a, b| a[0].cmp(&b[0]));

        // Initialize the result vector to store the merged intervals.
        let mut merged: Vec<Vec<i32>> = Vec::new();

        // Iterate through each interval in the sorted intervals vector.
        for interval in intervals {
            // Check if the merged vector is empty, which is true for the first iteration,
            // or if the current interval does not overlap with the last interval in the merged vector.
            // Two intervals [a, b] and [c, d] do not overlap if b < c.
            if merged.is_empty() || merged.last().unwrap()[1] < interval[0] {
                // Since there's no overlap, we can safely add the current interval to the merged vector.
                merged.push(interval);
            } else {
                // There is an overlap with the last interval in the merged vector.
                // In this case, we need to merge the current interval with the last interval in the merged vector.
                // The start of the merged interval is already correctly set (as the intervals are sorted),
                // so we only need to update the end of the interval.
                // We set the end of the merged interval to the maximum of the ends of the current and last intervals.
                let last = merged.last_mut().unwrap();
                last[1] = last[1].max(interval[1]);
            }
        }

        // After processing all intervals, the merged vector contains the merged intervals.
        // Return the merged intervals as the result.
        merged
    }
}


// Description: =============================================
/*
To solve the "Merge Intervals" problem in Rust, we'll follow these steps:

1. **Sort the Intervals**: First, we sort the `intervals` vector based on the starting times. This makes it easier to find 
   overlapping intervals.

2. **Merge Intervals**: We then iterate through the sorted intervals. For each interval, we check if it overlaps with the 
   previously added interval in our result vector. If it does, we merge them by updating the end time of the last interval in our result vector. If it doesn't overlap, we simply add the current interval to our result vector.

This implementation efficiently merges the intervals by first sorting them and then merging the overlapping intervals in a single pass. 
The time complexity is O(n log n) due to the sorting step, and the space complexity is O(1) if we ignore the space used for the output.

*/
