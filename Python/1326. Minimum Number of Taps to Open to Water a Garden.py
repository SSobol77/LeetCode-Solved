# 1326. Minimum Number of Taps to Open to Water a Garden.        - HARD -

# Topic: Array, Dynamic Programming, Greedy.

"""
### Task:
---
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at t
he point n. (i.e., the length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means
the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden
cannot be watered return -1.

Example 1:
Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]

Example 2:
Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.

Constraints:
1 <= n <= 10^4
ranges.length == n + 1
0 <= ranges[i] <= 100

Hint 1:
Create intervals of the area covered by each tap, sort intervals by the left end.
Hint 2:
We need to cover the interval [0, n]. we can start with the first interval and out of all intervals
that intersect with it we choose the one that covers the farthest point to the right.
Hint 3:
What if there is a gap between intervals that is not covered ? we should stop and return -1 as there
is some interval that cannot be covered.

### Testcase:
---
5
[3,4,1,1,0,0]
3
[0,0,0,0]


### Code:
---
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

"""
### Solution: --------------------------------------

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Convert tap ranges to intervals. Each tap i can water the range [i - ranges[i], i + ranges[i]]
        intervals = []
        for i, r in enumerate(ranges):
            intervals.append((max(0, i - r), min(n, i + r)))

        # Sort the intervals based on their start position
        intervals.sort()

        # Initialize variables to track the number of taps used and the farthest point watered so far
        taps = 0
        farthest = 0
        i = 0

        # Iterate through the garden (0 to n)
        while farthest < n:
            # Track the maximum reach within the current overlapping intervals
            max_reach = farthest
            # Find the interval that reaches the farthest within the current range
            while i < len(intervals) and intervals[i][0] <= farthest:
                max_reach = max(max_reach, intervals[i][1])
                i += 1

            # If no progress is made, a gap exists and the garden cannot be fully watered
            if max_reach == farthest:
                return -1

            # Update the farthest point watered and increment the tap count
            taps += 1
            farthest = max_reach

        # Return the minimum number of taps required
        return taps



### Description: ===================================
'''
In this code:

- We first convert the tap ranges into intervals where each interval `[start, end]` represents the part of the garden that a tap can water.
- We then sort these intervals by their starting points.
- The main loop iterates over these intervals to find the minimum number of taps needed. We always choose the interval that extends our current reach the farthest.
- If we encounter a situation where we cannot extend our current reach (`max_reach == farthest`), it means there's a part of the garden that cannot be watered, and we return -1.
- Finally, we return the total number of taps needed to water the entire garden.


To solve the problem "Minimum Number of Taps to Open to Water a Garden," we can use a greedy algorithm. The problem is essentially about choosing the minimum number of intervals (formed by the ranges of the taps) that can cover the entire garden.

Here's a step-by-step approach:

1. **Convert Taps to Intervals**: Convert each tap's range into an interval. For tap `i` with range `ranges[i]`, the interval is `[i - ranges[i], i + ranges[i]]`. This interval represents the part of the garden that the tap can water.

2. **Sort Intervals**: Sort these intervals by their starting points. This sorting helps in efficiently finding overlapping intervals.

3. **Find Overlapping Intervals**: Start with the first interval and find all intervals that overlap with it. Among these overlapping intervals, choose the one that extends the farthest to the right. This step ensures that we cover the maximum possible area with the minimum number of taps.

4. **Check for Gaps**: If there is a gap between intervals that is not covered, return -1. This means it's impossible to water the entire garden.

5. **Count Taps**: Keep track of the number of taps required to cover the entire garden.


In this code, we first convert the ranges of taps into intervals. Then, we sort these intervals and use a greedy approach to find the minimum number of taps needed to cover the entire garden. If at any point we find that a portion of the garden cannot be covered (indicated by no progress in the `farthest` variable), we return -1. Otherwise, we return the total number of taps required.

'''
