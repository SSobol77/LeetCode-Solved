# 1637. Widest Vertical Area Between Two Points Containing No Points

# Topics: Array, Sorting

'''
# Task:
-----
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no 
points are inside the area.
A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest 
vertical area is the one with the maximum width.

Note: that points on the edge of a vertical area are not considered included in the area.

Example 1:
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.

Example 2:
Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3
 

Constraints:

n == points.length
2 <= n <= 10^5
points[i].length == 2
0 <= xi, yi <= 10^9


# Testcase:
-----------
[[8,7],[9,9],[7,4],[9,7]]
[[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]


# Code:
-------
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
     

'''
# Solution:
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Extract x-coordinates and sort them
        x_coords = sorted([x for x, y in points])

        # Initialize the maximum width
        max_width = 0

        # Iterate through the sorted x-coordinates
        for i in range(1, len(x_coords)):
            # Calculate the width of the current vertical area
            width = x_coords[i] - x_coords[i - 1]

            # Update the maximum width if necessary
            max_width = max(max_width, width)

        return max_width

# Test cases
points1 = [[8,7],[9,9],[7,4],[9,7]]
points2 = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]

sol = Solution()
print(sol.maxWidthOfVerticalArea(points1))  # Expected output: 1
print(sol.maxWidthOfVerticalArea(points2))  # Expected output: 3



# Description:
'''
To solve this problem efficiently, we can follow these steps:
1. Extract the x-coordinates from each point since we are only concerned with the horizontal (x-axis) distances.
2. Sort these x-coordinates.
3. Iterate through the sorted x-coordinates, calculating the difference between each pair of adjacent x-coordinates. 
   This difference represents the width of the vertical area between these points.
4. Keep track of the maximum width found during this iteration.

This solution first sorts the x-coordinates, which takes O(n log n) time, where n is the number of points. Then, 
it iterates through the sorted list once, taking O(n) time. Thus, the overall time complexity is O(n log n), which 
is efficient for the given constraints.

'''