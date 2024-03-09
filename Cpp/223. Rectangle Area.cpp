// 223. Rectangle Area.

// Topic: Math, Geometry.


/*
### Task:
---
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

Example 1:
Rectangle Area
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45

Example 2:
Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16
 
Constraints:
-10^4 <= ax1 <= ax2 <= 10^4
-10^4 <= ay1 <= ay2 <= 10^4
-10^4 <= bx1 <= bx2 <= 10^4
-10^4 <= by1 <= by2 <= 10^4


### Testcase:
---
-3
0
3
4
0
-1
9
2
-2
-2
2
2
-2
-2
2
2


### Code:
---
class Solution {
public:
    int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        int area1 = (ax2 - ax1) * (ay2 - ay1); // Area of the first rectangle
        int area2 = (bx2 - bx1) * (by2 - by1); // Area of the second rectangle

        // Check for overlap
        int overlapWidth = max(0, min(ax2, bx2) - max(ax1, bx1));
        int overlapHeight = max(0, min(ay2, by2) - max(ay1, by1));

        int overlapArea = overlapWidth * overlapHeight; // Area of the overlap

        return area1 + area2 - overlapArea; // Total covered area
    }
};


// Description: ===================================
/*
To compute the total area covered by two rectilinear rectangles, we first calculate the area of each rectangle independently, 
and then subtract the area of their overlap (if any). The overlap area is only considered if the rectangles actually overlap.

### Steps to Solve:
1. Calculate the area of the first rectangle as `(ax2 - ax1) * (ay2 - ay1)`.
2. Calculate the area of the second rectangle as `(bx2 - bx1) * (by2 - by1)`.
3. Determine if there is an overlap:
   - The overlap happens if the right side of one rectangle is greater than the left side of the other and the top side of one 
     rectangle is greater than the bottom side of the other. This can be checked with `max(ax1, bx1) < min(ax2, bx2)` and 
     `max(ay1, by1) < min(ay2, by2)`.
4. If there is an overlap, calculate the area of the overlapping rectangle as `(min(ax2, bx2) - max(ax1, bx1)) * (min(ay2, by2) 
    - max(ay1, by1))`.
5. Subtract the area of the overlap from the sum of the areas of the two rectangles to get the total area covered by them.

### Description:
This solution efficiently calculates the total area covered by two rectangles by first finding the area of each rectangle and 
then subtracting the area of their overlap. The overlap is determined by comparing the coordinates of the rectangles to see if 
they intersect. If they do, the dimensions of the overlapping area are calculated and its area is found. The final total covered 
area is obtained by subtracting the overlap area from the sum of the individual rectangle areas. This method is effective and 
straightforward, using simple mathematical and geometric principles to solve the problem.

*/
