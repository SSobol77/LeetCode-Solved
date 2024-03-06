// 42. Trapping Rain Water.     - HARD -


// Topic: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack.

/*
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
class Solution {
public:
    int trap(vector<int>& height) {
        
    }
};


*/
// Solution: --------------------------------------

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = height.size() - 1; // Initialize two pointers.
        int result = 0; // Initialize the result variable.
        int leftMax = 0, rightMax = 0; // Variables to keep track of the max heights to the left and right.

        // Loop until the two pointers meet.
        while (left < right) {
            if (height[left] < height[right]) {
                // If the current left height is smaller than the right height, work on the left side.
                if (height[left] >= leftMax) {
                    // Update leftMax if the current height is greater or equal.
                    leftMax = height[left];
                } else {
                    // Otherwise, add to the result the difference between leftMax and the current height.
                    result += leftMax - height[left];
                }
                left++; // Move the left pointer to the right.
            } else {
                // If the current right height is smaller or equal, work on the right side.
                if (height[right] >= rightMax) {
                    // Update rightMax if the current height is greater or equal.
                    rightMax = height[right];
                } else {
                    // Otherwise, add to the result the difference between rightMax and the current height.
                    result += rightMax - height[right];
                }
                right--; // Move the right pointer to the left.
            }
        }

        return result; // Return the total water trapped.
    }
};


// Description: ===================================
/*
The "Trapping Rain Water" problem is a classic problem that can be solved using various approaches, including two pointers, dynamic programming, and using a stack. The essence of the problem is to find the total amount of water trapped between the bars of an elevation map, where each bar's height is given by an array.

One effective approach to solve this problem is using the two pointers method, which is both intuitive and efficient. The main idea is to iterate over the elevation map from both ends towards the center, keeping track of the maximum height seen so far from both ends. The water trapped at any point depends on the height of the taller bars on its left and right; it will be the difference between the height of the current bar and the minimum of the maximum heights to its left and right.

Here's a step-by-step guide to implementing this solution:

1. **Initialize two pointers**: One at the beginning (`left`) and one at the end of the array (`right`).
2. **Initialize variables to track the maximum heights**: `leftMax` and `rightMax`, for the left and right sides, respectively.
3. **Iterate over the array**: Move the `left` and `right` pointers towards each other.
   - If `height[left]` is less than `height[right]`, we move the `left` pointer to the right.
     - Update `leftMax` to the maximum of `leftMax` and `height[left]`.
     - Add `leftMax - height[left]` to the total water trapped (`result`), if `leftMax` is greater than `height[left]`.
   - Otherwise, move the `right` pointer to the left.
     - Update `rightMax` to the maximum of `rightMax` and `height[right]`.
     - Add `rightMax - height[right]` to `result`, if `rightMax` is greater than `height[right]`.
4. **Continue** until the `left` and `right` pointers meet.

### Description:

This solution uses a two-pointer technique to iterate over the array of heights from both ends. It keeps track of the maximum height seen so far from both ends and calculates the water trapped at each step based on the minimum of these maximum heights and the current height. The pointers are moved inward based on the comparison of the heights at their current positions. This method ensures that we consider the elevation map's contour and effectively compute the total water trapped without needing any additional data structures. The time complexity of this approach is O(n), where n is the number of elements in the `height` array, making it an efficient solution.

*/
