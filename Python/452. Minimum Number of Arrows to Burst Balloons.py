# 452. Minimum Number of Arrows to Burst Balloons.


# Topic: Array, Greedy, Sorting.

"""
### Task:
---
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Constraints:
1 <= points.length <= 10^5
points[i].length == 2
-2^31 <= xstart < xend <= 2^31 - 1

### Testcase:
---
[[10,16],[2,8],[1,6],[7,12]]
[[1,2],[3,4],[5,6],[7,8]]
[[1,2],[2,3],[3,4],[4,5]]


### Code:
---
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
    

"""
### Solution: --------------------------------------

class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        # Sort the points based on the end coordinate
        points.sort(key=lambda x: x[1])

        # Initialize the first end position and the arrow count
        arrows = 1
        first_end = points[0][1]

        for x_start, x_end in points:
            # If the current balloon starts after the last end position,
            # we need another arrow and update the end position
            if x_start > first_end:
                arrows += 1
                first_end = x_end

        return arrows

### Description: ===================================
'''
To solve this problem, we can follow a greedy approach. The main idea is to sort the balloons by their ending coordinates and then try to burst as many balloons as possible with one arrow. Here's a step-by-step breakdown:

1. **Sort the balloons:** First, we sort the array of points based on the ending coordinates of the balloons (i.e., the `xend` values). This allows us to easily find the earliest point at which we can shoot an arrow to burst the most balloons.

2. **Initialize variables:** We need a variable to keep track of the position where we will shoot the arrow. Initially, this can be set to the end of the first balloon in the sorted list. We also need a counter for the minimum number of arrows required, which is initially set to 1 since we'll definitely need at least one arrow.

3. **Iterate through the balloons:** We iterate through the sorted list of balloons. For each balloon, we check if the start of the current balloon (`xstart`) is less than or equal to the position where we plan to shoot the arrow. If it is, it means we can burst this balloon with the current arrow, and we don't need to do anything. If the start of the current balloon is greater than the arrow position, it means we need a new arrow for this balloon and potentially others that follow. So, we increment our arrow counter and update the arrow position to the end of the current balloon.

By the end of the iteration, the arrow counter will represent the minimum number of arrows needed to burst all balloons.


### Explanation:

- The `points.sort(key=lambda x: x[1])` line sorts the `points` list based on the second element of each sub-list, which is the end coordinate of the balloons.
- The `for x_start, x_end in points:` loop iterates through each balloon.
- If `x_start > first_end`, it means the current balloon cannot be burst by an arrow shot at `first_end`, so we need a new arrow. We increment `arrows` and update `first_end` to the end of the current balloon (`x_end`).
- Finally, we return the total count of arrows needed.



'''
