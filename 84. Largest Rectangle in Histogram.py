# 84. Largest Rectangle in Histogram.      HARD

# Topic: Array, Stack, Monotonic Stack.

"""
### Task:
---
Given an array of integers heights representing the histogram's bar height where the width 
of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4


### Testcase:
---
[2,1,5,6,2,3]
[2,4]

### Code:
---
class Solution(object):
    def largestRectangleArea(self, heights):
        '''
        :type heights: List[int]
        :rtype: int
        '''
"""
### Solution:-------------------------------------------------------------------

class Solution(object):
    def largestRectangleArea(self, heights):
        '''
        :type heights: List[int]
        :rtype: int
        '''
        # Initialize an empty stack to store indices of bars
        stack = []
        # Initialize max_area to keep track of the largest rectangle area found
        max_area = 0
        # Append a sentinel bar of height 0 to handle remaining bars after the loop
        heights.append(0)

        # Iterate over each bar in the histogram
        for i in range(len(heights)):
            # While stack is not empty and current bar's height is less than the top bar in the stack
            while stack and heights[i] < heights[stack[-1]]:
                # Pop the top bar from the stack and calculate its height
                h = heights[stack.pop()]
                # Calculate the width of the rectangle with the popped bar as height
                w = i if not stack else i - stack[-1] - 1
                # Update max_area if the calculated area is larger
                max_area = max(max_area, h * w)
            # Push the current index onto the stack
            stack.append(i)

        # Return the maximum area found
        return max_area


### Description:
'''
The "Largest Rectangle in Histogram" problem can be efficiently solved using a stack, specifically a monotonic stack. The idea is to maintain a stack of indices of the bars, and calculate the area of rectangles with the stack bars as heights. When a smaller bar is encountered, it triggers the calculation of the area for bars in the stack that are taller than the current one.

Here's a detailed approach:

1. **Initialize Variables**: Create a stack to store indices. Initialize a variable to keep track of the maximum area found.

2. **Iterate Over the Heights**: Go through each bar in the histogram:
   - While the stack is not empty and the current bar's height is less than the height of the bar at the top of the stack, pop from the stack and calculate the area formed by the popped bar. The width of the area is the difference between the current index and the index just below the top of the stack (after popping), minus one.
   - Push the current index onto the stack.

3. **Handle Remaining Bars**: After the loop, some bars may remain in the stack. These bars were never smaller than any bar to their right. For each of these, calculate the area considering the width extends to the end of the histogram.

4. **Return the Maximum Area**.

### Explanation:
- We append a sentinel bar of height 0 to handle any remaining bars in the stack after iterating through the list.
- The `while` loop inside the `for` loop calculates the area for each bar popped from the stack.
- The width calculation changes depending on whether the stack is empty or not after popping. If the stack is empty, the width is the current index `i`; otherwise, it's the distance between the current index and the index below the top of the stack.

This algorithm has a time complexity of O(n), as each bar is pushed and popped from the stack exactly once. The space complexity is also O(n) for the stack in the worst case.

### Breakdown of the Code:

1. **Stack Initialization**: An empty stack is used to store the indices of bars. This stack helps to keep track of bars that might form part of a larger rectangle.

2. **Max Area Initialization**: `max_area` is used to record the largest rectangle area found during the iteration.

3. **Append Sentinel Bar**: Adding a bar of height 0 at the end ensures that any remaining bars in the stack are processed, as they will all be greater than 0.

4. **Iterating Over the Heights**: The loop goes through each bar in the histogram.

5. **Processing the Stack**: If the current bar is lower than the bar at the top of the stack, we pop from the stack, calculate the area with the popped bar as height, and update `max_area` if this area is larger than the current `max_area`.

6. **Pushing to the Stack**: If the current bar is taller than the bar at the top of the stack (or the stack is empty), we push the current index onto the stack.

7. **Returning the Result**: After processing all bars, the largest rectangle area found is returned.

'''
