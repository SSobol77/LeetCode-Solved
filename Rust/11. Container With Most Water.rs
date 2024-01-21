// 11. Container With Most Water.            - Medium -

// Topic:  Array, Two Pointers, Greedy.

/*
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
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        
    }
}

*/
// Solution: ----------------------------------------------------------------------
impl Solution {
    // Define the public function `max_area` within the struct `Solution`.
    // The function takes a vector of i32, named `height`, as its argument.
    pub fn max_area(height: Vec<i32>) -> i32 {
        // Initialize `left` as the start index (0) of the `height` vector.
        let mut left = 0usize;

        // Initialize `right` as the end index (length - 1) of the `height` vector.
        let mut right = height.len() - 1;

        // Initialize `max_area` to store the maximum area found, starting at 0.
        let mut max_area = 0i32;

        // Use a `while` loop to iterate as long as `left` index is less than `right` index.
        while left < right {
            // Calculate the width between the current `left` and `right` pointers.
            let width = (right - left) as i32;

            // Determine the smaller height and its corresponding index.
            // Use a tuple to hold the height and index, and an if-else block to assign values.
            let (smaller_height, smaller_index) = if height[left] < height[right] {
                (height[left], left)
            } else {
                (height[right], right)
            };
            
            // Calculate the area formed by the smaller height and the current width.
            let current_area = smaller_height * width;

            // Update `max_area` to the larger of the two: current `max_area` or `current_area`.
            max_area = max_area.max(current_area);

            // Move the pointer (`left` or `right`) based on which side had the smaller height.
            if smaller_index == left {
                left += 1;  // Increment `left` if the smaller height was at `left`.
            } else {
                right -= 1; // Decrement `right` if the smaller height was at `right`.
            }
        }

        // Return the maximum area found.
        max_area
    }
}



// Description: ----------------------------------------------------------------------------
/*
### Solution Description

The "Container With Most Water" problem is solved using an optimized two-pointer approach. 
The solution is implemented in Rust and is designed to efficiently compute the maximum amount 
of water that can be trapped between pairs of vertical lines, represented by an array of integers.

### Algorithm Explanation

1. **Initialization:**
   - Two pointers, `left` and `right`, are initialized to point at the start (0) and end (length - 1) of the input array, 
     respectively.
   - A variable `max_area` is initialized to 0 to keep track of the maximum area found.

2. **Iterating Over the Array:**
   - The algorithm uses a `while` loop to iterate as long as `left` is less than `right`.
   - Within each iteration, the algorithm performs the following steps:

3. **Calculating Width and Determining Smaller Height:**
   - The width between the `left` and `right` pointers is calculated.
   - The heights at `left` and `right` indices are compared, and the smaller of the two is identified along with its index.

4. **Area Calculation:**
   - The area is calculated as the product of the smaller height (determined in the previous step) and the current width.
   - The `max_area` variable is updated if the newly calculated area is greater than the current `max_area`.

5. **Pointer Movement:**
   - The pointer (`left` or `right`) corresponding to the smaller height is moved one step towards the other pointer. 
     This step is crucial as moving the pointer at the smaller height might lead to a larger area.

6. **Completion:**
   - The loop continues until the two pointers meet, ensuring that every possible pair of lines is evaluated.
   - The function finally returns the `max_area` as the maximum water container area that can be formed.

### Key Aspects of the Solution

- **Two-Pointer Approach:** This technique reduces the time complexity to O(n) by effectively narrowing down the search space in each iteration.
- **Efficient Area Calculation:** By always moving the pointer at the smaller height, the algorithm efficiently finds the maximum possible area.
- **Optimal Space Usage:** The solution only uses a constant amount of extra space, making its space complexity O(1).

### Performance

- **Time Complexity:** O(n), where n is the number of elements in the input array. Each element is accessed once.
- **Space Complexity:** O(1), as the solution uses a

fixed amount of space regardless of the input size.

### Practical Considerations

- **Robustness:** The solution is robust and works for any input conforming to the problem's constraints.
- **Maintainability:** The code is structured and commented for clarity, making it easy to understand and maintain.
- **Scalability:** The algorithm scales linearly with the size of the input, ensuring efficient performance even for large arrays.

### Conclusion

The provided solution effectively balances computational efficiency with code clarity, making it an ideal approach for 
solving the "Container With Most Water" problem in Rust. By leveraging a two-pointer strategy, it achieves optimal
performance in both runtime and memory usage, suitable for large datasets and real-world applications.

*/