# 218. The Skyline Problem

# Topics: Array, Divide and Conquer, Binary Indexed Tree, Segment Tree, Line Sweep, Heap (Priority Queue), Ordered Set.

'''
Tasks:
--------------
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when 
viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed 
by these buildings collectively.

The geometric information of each building is given in the array buildings where 
buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the 
form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline 
except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's 
termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should
be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. 
For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 
should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

Example 1:
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.

Example 2:
Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]

Constraints:
1 <= buildings.length <= 10^4
0 <= lefti < righti <= 2^31 - 1
1 <= heighti <= 2^31 - 1
buildings is sorted by lefti in non-decreasing order.


# Testcase:
-------------
[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
[[0,2,3],[2,5,3]]


# Code:
--------------
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    


'''

# Solution:
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create events for both the start and end of each building.
        # For start, use negative height to distinguish it from end.
        # For end, height is 0 as it signifies the building is no longer part of the skyline.
        events = [(L, -H, R) for L, R, H in buildings]
        events += [(R, 0, None) for _, R, _ in buildings]
        # Sort the events by their x-coordinate (pos). In case of a tie, sort by height.
        events.sort()

        # Initialize the result list with a ground-level point.
        res = [[0, 0]]
        # Initialize a max-heap with an initial ground level (height 0, infinitely extending).
        heap = [(0, float("inf"))]
        # Dictionary to keep track of active buildings (those that have started but not ended).
        active_buildings = defaultdict(int)

        for pos, negH, R in events:
            # Remove buildings from the heap that are no longer part of the skyline at current position.
            while heap and heap[0][1] <= pos:
                _, end = heapq.heappop(heap)
                # Continue removing from heap if the top of the heap is also past.
                while heap and heap[0][1] <= end:
                    heapq.heappop(heap)

            # If it's the start of a building, add it to the heap.
            if negH:
                heapq.heappush(heap, (negH, R))
                active_buildings[negH] += 1

            # If the highest building at this point is different from the last recorded height in result,
            # it means the skyline has changed, and we add this point to the result.
            if res[-1][1] != -heap[0][0]:
                res.append([pos, -heap[0][0]])

        # Exclude the initial ground level from the result and return.
        return res[1:]

# Test cases
solution = Solution()
print(solution.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))  # Expected Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
print(solution.getSkyline([[0,2,3],[2,5,3]]))  # Expected Output: [[0,3],[5,0]]


# Description:
'''
This commented code provides a detailed explanation of how the solution processes the buildings to form 
the skyline, taking into account the height and x-coordinates of the buildings. The max-heap is used to 
keep track of the currently 'active' buildings, and the skyline points are updated whenever the highest 
building at a certain position changes.

'''
