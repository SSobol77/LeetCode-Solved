# 42. Trapping Rain Water       -HARD-

# Topic: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack.

"""
### Task:
---
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5


### Testcase:
---
[0,1,0,2,1,0,1,3,2,1,2,1]
[4,2,0,3,2,5]


### Code:
---
class Solution:
    def trap(self, height: List[int]) -> int:
        

"""
### Solution: ----------------------------------------------------

class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: if the array is empty, no water can be trapped.
        if not height:
            return 0

        n = len(height)
        # Initialize arrays to store the maximum height to the left and right of each bar.
        left_max, right_max = [0] * n, [0] * n
        water_trapped = 0

        # Fill the left_max array: for each bar, store the maximum height seen so far from the left.
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        # Fill the right_max array: for each bar, store the maximum height seen so far from the right.
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        # Calculate the trapped water for each bar.
        for i in range(n):
            # The water trapped on top of the current bar is the minimum of the max heights
            # on its left and right sides, minus the height of the bar itself.
            water_trapped += min(left_max[i], right_max[i]) - height[i]

        # Return the total amount of water trapped.
        return water_trapped


### Description: ===================================================
'''
### Comments Explanation:
- **Edge Case Handling**: Initially, the function checks if the input array is empty. If it is, the function returns 0, as no water can be trapped.
- **Initialization**: Two arrays, `left_max` and `right_max`, are created to store the maximum height to the left and right of each bar in the `height` array.
- **Computing Left Max Heights**: The `left_max` array is filled from left to right. Each element in `left_max` represents the highest bar up to that point from the left.
- **Computing Right Max Heights**: The `right_max` array is filled in the opposite direction, from right to left. Each element in `right_max` represents the highest bar up to that point from the right.
- **Calculating Water Trapped**: The function iterates through each bar and calculates the amount of water that can be trapped on top of it. This is done by taking the minimum of the two maximum heights from `left_max` and `right_max` for that bar and subtracting the bar's height.
- **Total Water Calculation**: The water trapped on each bar is added to `water_trapped`, which accumulates the total amount of water trapped.
- **Return Statement**: Finally, the function returns `water_trapped`, which holds the total amount of water that can be trapped according to the elevation map represented by the `height` array.

!These comments in the code provide a clear, step-by-step explanation of the logic behind each operation, making the dynamic programming approach to solving the "Trapping Rain Water" problem more understandable.


The "Trapping Rain Water" problem is a more challenging array manipulation problem, often involving concepts like dynamic programming, two pointers, or stacks. Let's dive into the problem and its solution.

### Problem Analysis:
You are given an array representing an elevation map, where each element represents the height of a bar. The task is to calculate how much water can be trapped between these bars after it rains.

### Approach:
1. **Dynamic Programming Approach**: 
   - Precompute the maximum height to the left and right of every bar.
   - The amount of water that can be trapped on top of each bar is the minimum of the maximum heights to its left and right, minus its own height.

2. **Two Pointers Approach**:
   - Initialize two pointers, one at the start and one at the end of the array.
   - Move the pointers towards each other, updating the maximum height seen so far from both ends.
   - The water trapped at each step is determined by the minimum of the two maximum heights minus the current height.

3. **Stack Approach** (Monotonic Stack):
   - Use a stack to keep track of the bars.
   - Iterate over each bar and pop from the stack when you find a bar that is taller than the one at the top of the stack.
   - Calculate the trapped water using the height difference and the width.

### Explanation:
- **Dynamic Programming**: The `left_max` and `right_max` arrays store the maximum heights to the left and right of each bar, respectively.
- **Calculating Water**: For each bar, the trapped water is the minimum of `left_max[i]` and `right_max[i]` minus the height of the current bar. This is because water can only

 be trapped up to the height of the shorter boundary and the bar itself displaces some water.
- **Total Water**: The `water_trapped` variable accumulates the water trapped over each bar.

### Time Complexity:
- The time complexity of this approach is O(n) as it requires three passes through the array: one to fill `left_max`, one for `right_max`, and one to calculate the trapped water.

### Test Cases:
1. `height = [0,1,0,2,1,0,1,3,2,1,2,1]` should return `6`.
   - The function calculates the maximum height to the left and right of each bar and then determines the trapped water.

2. `height = [4,2,0,3,2,5]` should return `9`.
   - Similarly, the function computes trapped water using the precomputed maximum heights.

This dynamic programming solution is efficient and elegantly handles the problem of calculating trapped rainwater in a given elevation map.

'''
