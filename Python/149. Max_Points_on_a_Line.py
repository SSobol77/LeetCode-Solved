# 149. Max Points on a Line.

# Topic: Array, Hash Table, Math, Geometry.


'''
# Task:
--------------------------
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 
Constraints:
1 <= points.length <= 300
points[i].length == 2
-10^4 <= xi, yi <= 10^4
All the points are unique.


# Testcase:
----------------------------
Case 1
points = [[1,1],[2,2],[3,3]]
Case 2
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]


# Code:
---------------------------
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
 

'''
# Solution:

from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        def gcd(a, b):
            """
            Calculate the greatest common divisor (GCD) of a and b using Euclid's algorithm.
            This is essential for reducing fractions to their simplest form.
            """
            while b:
                a, b = b, a % b
            return a

        def calculate_slope(p1, p2):
            """
            Calculate the slope between two points (p1 and p2) as a fraction.
            This fraction is reduced to the simplest form using GCD.
            Special cases:
            - Vertical line (dx == 0): return 'inf' (infinity).
            - Horizontal line (dy == 0): return 0.
            """
            dy = p2[1] - p1[1]  # Difference in y-coordinates
            dx = p2[0] - p1[0]  # Difference in x-coordinates
            if dx == 0: 
                return 'inf'  # Vertical line
            if dy == 0: 
                return 0  # Horizontal line
            divisor = gcd(dy, dx)  # Simplifying the slope
            return (dy // divisor, dx // divisor)

        def max_points_on_line_through_point(i):
            """
            Calculate the maximum number of points on a line that passes through points[i].
            It uses a dictionary to map each unique slope to the number of points with that slope.
            It also counts duplicate points (points with the same coordinates).
            """
            lines = defaultdict(int)
            duplicate = 0  # Counter for duplicate points
            cur_max = 0  # Tracks the maximum number of points for the current point

            for j in range(len(points)):
                if i != j:
                    if points[i] == points[j]:
                        duplicate += 1  # Increment duplicate count
                    else:
                        slope = calculate_slope(points[i], points[j])
                        lines[slope] += 1
                        cur_max = max(cur_max, lines[slope])  # Update the current max

            return cur_max + duplicate + 1  # Add 1 to include the point itself

        if len(points) <= 2:
            return len(points)  # With 2 or fewer points, all points are on a line

        max_points = 0  # Initialize max_points
        for i in range(len(points) - 1):
            # Update max_points for each point in the array
            max_points = max(max_points, max_points_on_line_through_point(i))

        return max_points

# Test cases
sol = Solution()

# Case 1
points1 = [[1,1],[2,2],[3,3]]
result1 = sol.maxPoints(points1)  # Expected output: 3

# Case 2
points2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
result2 = sol.maxPoints(points2)  # Expected output: 4

result1, result2


# Description:
'''
Description of the solution:

- GCD Function: 
The gcd function is used to compute the greatest common divisor of two numbers, which is essential 
for simplifying the slope between two points.

- Calculate Slope: 
calculate_slope function calculates the slope between two points. Slopes are stored as a tuple (dy, dx) 
representing the ratio of the difference in y-coordinates to the difference in x-coordinates, simplified 
to the lowest terms.

- Max Points on Line Through a Point: 
The max_points_on_line_through_point function calculates the maximum number of points on a line that 
includes a specific point. It uses a dictionary (lines) to map slopes to the number of points with that 
slope relative to the current point. This function also accounts for duplicate points.

- Overall Logic: 
The maxPoints method iterates over each point and calculates the maximum number of points that can be 
on the same line through that point. It returns the maximum of these values.

This solution efficiently handles the problem of finding the maximum number of points on a line by using 
a combination of slope calculation and a dictionary to count occurrences of each unique slope.

'''
