// 42. Trapping Rain Water          -HARD-

// Topic: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack.

/*
### Task:
---
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water 
it can trap after raining.

#Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

#Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

#Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5

### Testcase:
---
[0,1,0,2,1,0,1,3,2,1,2,1]
[4,2,0,3,2,5]


### Code:
---
impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        
    }
}
*/
// Solution: ---------------------------------------------------------------

impl Solution {
    // Define the public function `trap` that takes a vector of i32 as an argument 
    // and returns the total amount of trapped rainwater as i32.
    pub fn trap(height: Vec<i32>) -> i32 {
        // Initialize two pointers: `left` starting from the beginning of the array,
        // and `right` starting from the end.
        let (mut left, mut right) = (0, height.len() - 1);

        // Initialize variables to keep track of the maximum height encountered
        // so far from the left

and right sides.
        let (mut left_max, mut right_max) = (0, 0);

        // Initialize a variable to accumulate the total amount of water trapped.
        let mut water_trapped = 0;

        // Iterate over the array until the two pointers meet.
        while left < right {
            // If the height at the `left` pointer is less than or equal to the height at the `right` pointer.
            if height[left] <= height[right] {
                // Update `left_max` to be the maximum of itself and the current height at `left`.
                left_max = left_max.max(height[left]);

                // Accumulate water trapped at the current position. It's the difference between
                // `left_max` and the current height since `left_max` is the potential water level.
                water_trapped += left_max - height[left];

                // Move the `left` pointer to the right.
                left += 1;
            } else {
                // If the height at `right` is less than the height at `left`.
                // Update `right_max` similarly, keeping track of the maximum height from the right.
                right_max = right_max.max(height[right]);

                // Accumulate water trapped at the current position from the right side.
                water_trapped += right_max - height[right];

                // Move the `right` pointer to the left.
                right -= 1;
            }
        }

        // Return the total amount of water trapped.
        water_trapped
    }
}

/*
### Commentary:

- The function `trap` calculates the total rainwater that can be trapped within a given elevation map represented by an array.
- It efficiently uses a two-pointer approach to scan the elevation map from both ends towards the center.
- The `left_max` and `right_max` variables are crucial in determining the maximum possible water level from the left and right sides at any point.
- The water trapped at each position is computed based on the difference between the water level (either `left_max` or `right_max`) and the height of the current bar.
- The choice of pointer movement (left or right) is determined by comparing the heights at the current left and right pointers, ensuring the correctness of the trapped water calculation.
- The algorithm is designed to be efficient both in terms of time and space complexity, making it suitable for handling large elevation maps.
*/


// Description: ============================================================
/*
To solve the "Trapping Rain Water" problem, we will implement the `trap` function in Rust. This function aims to compute the total amount of rainwater that can be trapped between the bars, given an array representing an elevation map. The challenge is to calculate the water that can be accumulated in the valleys of this elevation map.

### Algorithm:

1. **Two-Pointer Approach:**
   - Initialize two pointers, `left` and `right`, at the start and end of the array respectively.
   - Also, initialize two variables, `left_max` and `right_max`, to keep track of the maximum heights encountered so far from the left and right ends.

2. **Iterating Through the Array:**
   - While `left` is less than `right`, iterate through the array.
   - If `height[left]` is less than or equal to `height[right]`:
     - Update `left_max` to the maximum of `left_max` and `height[left]`.
     - Add `left_max - height[left]` to the total water trapped. This is because the water trapped at the current position is the difference between the height of the water level (determined by `left_max`) and the height of the bar (`height[left]`).
     - Increment `left`.
   - Else:
     - Update `right_max` to the maximum of `right_max` and `height[right]`.
     - Add `right_max - height[right]` to the total water trapped.
     - Decrement `right`.

3. **Return Total Water Trapped:**
   - After the loop completes, return the total amount of water trapped.

### Description:

- The `trap` function is designed to calculate the amount of rainwater that can be trapped in an elevation map represented by an array of integers.
- It uses a two-pointer approach, moving from both ends of the array towards the center.
- The `left_max` and `right_max` variables keep track of the maximum heights encountered so far from the left and right sides. These variables help in determining the potential water level at any point.
- Water trapped at each position is calculated by subtracting the bar height from the water level (determined by either `left_max` or `right_max`, whichever is relevant).
- The algorithm ensures that water trapping is calculated based on the lower of the two ends (left or right) at each step, as the water level is limited by the shorter end.
- The total amount of trapped water is accumulated and returned.

### Complexity Analysis:

- **Time Complexity:** O(n), where n is the number of elements in the input array. The algorithm iterates through the array only once.
- **Space Complexity:** O(1), as the solution uses a constant amount of space regardless of the input size.

### Performance Considerations:

- This approach is efficient and optimized for large datasets due to its linear time complexity and constant space usage.
- It avoids the need for additional data structures like stacks or dynamic programming arrays, making it a straightforward and efficient solution for the given problem.
*/