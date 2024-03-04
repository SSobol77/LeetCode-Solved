// 11. Container With Most Water.


// Topic: Array, Two Pointers, Greedy.


/*
### Task:
---
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4

Hint 1:
If you simulate the problem, it will be O(n^2) which is not efficient.
Hint 2:
Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.
Hint 3:
How can you calculate the amount of water at each step?


### Testcase:
---
[1,8,6,2,5,4,8,3,7]
[1,1]


### Code:
---
class Solution {
public:
    int maxArea(vector<int>& height) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = 0; // Step 1: Initialize max area
        int left = 0, right = height.size() - 1; // Start with two pointers at both ends of the array

        while (left < right) { // Step 5: Continue until the two pointers meet
            // Step 2: Calculate the area between left and right pointers
            int currentArea = min(height[left], height[right]) * (right - left);

            // Step 3: Update maxArea if currentArea is larger
            maxArea = max(maxArea, currentArea);

            // Step 4: Move the pointer pointing to the shorter line
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        // Step 6: Return the maximum area found
        return maxArea;
    }
};


// Description: ===================================
/*
To solve the "Container With Most Water" problem, we can use a two-pointer approach which is both intuitive and efficient. 
The idea is to start with two pointers, one at the beginning and one at the end of the `height` array, and gradually move 
them closer to find the maximum area.

Here is a step-by-step guide to the algorithm:

1. **Initialize Variables**: Start with two pointers, `left` at 0 and `right` at `height.length - 1`. Also, initialize a 
   variable `maxArea` to keep track of the maximum area found.

2. **Calculate Area**: At each step, calculate the area formed between the lines at the `left` and `right` pointers. The 
   area is calculated as `min(height[left], height[right]) * (right - left)` because the height of the water is limited by 
   the shorter line and the width is the distance between the two lines.

3. **Update Maximum Area**: Compare the calculated area with `maxArea` and update `maxArea` if the calculated area is larger.

4. **Move Pointers**: Move the pointer pointing to the shorter line towards the other pointer by one step. This is because 
    moving the shorter line might lead to a higher area, while moving the taller line cannot increase the area.

5. **Repeat**: Repeat steps 2-4 until the `left` and `right` pointers meet.

6. **Return Result**: Once the pointers meet, the loop ends and `maxArea` is returned as the maximum area found.


This solution efficiently finds the maximum area with a time complexity of O(n), where n is the number of elements in the `height` 
array, by only needing to pass through the array once.

*/
