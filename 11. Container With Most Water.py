# 11. Container With Most Water.            - Medium -

# Topic: Array, Two Pointers, Greedy.

"""
### Task:
---
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

#Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of 
water (blue section) the container can contain is 49.

#Example 2:
Input: height = [1,1]
Output: 1

#Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4

Hint 1
If you simulate the problem, it will be O(n^2) which is not efficient.
Hint 2
Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.
Hint 3
How can you calculate the amount of water at each step?


### Testcase:
---
[1,8,6,2,5,4,8,3,7]
[1,1]


### Code:
---
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
"""
### Solution:

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            # Calculate area
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)

            # Move pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


### Description:
'''
The problem you've presented, known as the "Container With Most Water" problem, is a classic example in algorithmic problem solving, particularly involving arrays and the two-pointer technique. Let's first analyze the problem and then move on to a solution.

### Problem Analysis:
You are given an array of integers where each integer represents the height of a vertical line on a graph. The goal is to find two lines, along with the x-axis, that together will form a container capable of holding the maximum amount of water.

The area of water contained by two lines is determined by the shorter of the two lines (as water would overflow from the shorter side) and the distance between these two lines.

### Approach:
1. **Initialize two pointers**: One at the beginning (left) and one at the end (right) of the array. This way, we start with the maximum width.
2. **Calculate the area**: The area is the minimum of the two heights multiplied by the distance (width) between the pointers.
3. **Move the pointers**: We move the pointer pointing to the shorter line inwards, as moving the longer line would not increase the area.
4. **Repeat**: Continue the process, always keeping track of the maximum area found so far.
5. **Termination**: The process continues until the two pointers meet.

### Explanation:
- The algorithm starts with the widest possible container and iteratively reduces the width.
- By always moving the shorter line, we ensure that there is a possibility (though not guaranteed) of finding a taller line that can potentially hold more water.
- This algorithm is efficient as it only requires one pass through the array, making it O(n) in time complexity, where n is the number of elements in the array.

### Example:
Let's consider the first example:
- `height = [1,8,6,2,5,4,8,3,7]`
- The function starts by considering the distance between the first and the last line (width = 8) and the shorter of these two lines (height = 1).
- As it progresses, it considers different pairs of lines and finds that the pair of lines at positions 2 and 9 (1-indexed, corresponding to heights 8 and 7) give the maximum area of 49.

This solution is optimal and solves the problem as per the given constraints.

'''