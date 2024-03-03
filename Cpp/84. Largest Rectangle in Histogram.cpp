// 84. Largest Rectangle in Histogram.       - HARD -

// Topic: Array, Stack, Monotonic Stack.


/*
### Task:
---
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the
area of the largest rectangle in the histogram.

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
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        // Initialize a stack to keep indices of bars
        stack<int> stk;
        // Variable to keep track of the maximum area found
        int maxArea = 0;
        // Get the number of bars in the histogram
        int n = heights.size();

        // Iterate through each bar in the histogram
        for (int i = 0; i <= n; ++i) {
            // While the stack is not empty and the current bar's height is less than
            // the height of the bar at the top of the stack
            while (!stk.empty() && (i == n || heights[stk.top()] > heights[i])) {
                // Get the height of the bar at the top of the stack
                int height = heights[stk.top()];
                // Pop the top element from the stack
                stk.pop();
                // Calculate the width of the rectangle with the popped bar as the shortest bar
                // If the stack is empty, the width is 'i'
                // Otherwise, the width is the difference between 'i' and the new top of the stack - 1
                int width = stk.empty() ? i : i - stk.top() - 1;
                // Update the maximum area found
                maxArea = max(maxArea, height * width);
            }
            // Push the current index onto the stack
            stk.push(i);
        }

        // Return the maximum area found
        return maxArea;
    }
};




// Description: ===================================
/*
To solve the "Largest Rectangle in Histogram" problem, we can use a stack to efficiently track the indices of bars in the histogram. 
The stack helps us determine the boundaries of rectangles with the current bar as the shortest bar. We use a monotonic stack approach, 
which keeps the indices of the bars in the stack in increasing order of their heights.

Here's a step-by-step approach:

1. **Initialize**: Create an empty stack to store indices of bars. Initialize `maxArea` as 0 to keep track of the maximum area found.

2. **Iterate through Each Bar**: For each bar in the histogram, do the following:
   - While the stack is not empty and the current bar's height is less than the height of the bar at the top of the stack, it means we've 
   found a right boundary for the rectangle containing the bar at the top of the stack. Pop the top of the stack, calculate the area of 
   the rectangle using the height of the popped bar, and update `maxArea` if this area is larger.
   - Push the current index onto the stack.

3. **Handle Remaining Bars**: After iterating through all bars, some bars might not have been popped from the stack. These bars don't 
have a right boundary smaller than themselves. For each remaining bar in the stack, calculate the area of the rectangle with the bar as 
the shortest one and update `maxArea` if necessary.

4. **Return Result**: After processing all bars, `maxArea` will contain the area of the largest rectangle.

### Description:

This solution leverages a monotonic stack to find the largest rectangle in a histogram efficiently. By maintaining a stack of indices 
of bars in increasing order of heights, the algorithm can quickly determine the left and right boundaries for the largest rectangle 
that can be formed with each bar as the shortest bar in that rectangle. When a bar is encountered that is shorter than the bar at the 
top of the stack, it signifies a right boundary for rectangles involving bars in the stack, allowing for the calculation of areas and 
updating the maximum area found. This approach ensures that each bar is pushed and popped from the stack exactly once, leading to a time 
complexity of O(n), making it highly efficient for large histograms.

*/
