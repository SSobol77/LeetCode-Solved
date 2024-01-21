// 15. 3Sum.            - Medium -

// Topic: Array, Two Pointers, Sorting.

/*
### Task:
---
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

#Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

#Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
#Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

Hint 1
So, we essentially need to find three numbers x, y, and z such that they add up to the given value. 
If we fix one of the numbers say x, we are left with the two-sum problem at hand!
Hint 2
For the two-sum problem, if we fix one of the numbers, say x, we have to scan the entire array to find 
the next number y, which is value - x where value is the input parameter. Can we change our array somehow so that this search becomes faster?
Hint 3
The second train of thought for two-sum is, without changing the array, can we use additional space somehow? 
Like maybe a hash map to speed up the search?


### Testcase:
---
[-1,0,1,2,-1,-4]
[0,1,1]
[0,0,0]


### Code:
---
impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        
    }
}

*/
// Solution: ----------------------------------------------------------

impl Solution {
    // Define the public function `three_sum` that takes a vector of i32 as an argument 
    // and returns a vector of vectors of i32.
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        // Initialize a vector to store the result.
        let mut result = Vec::new();

        // Sort the input array in-place.
        nums.sort_unstable();

        // Iterate over the array with `i`. The length is checked to avoid overflow.
        for i in 0..nums.len() {
            // Skip duplicate elements to avoid duplicate triplets.
            if i > 0 && nums[i] == nums[i - 1] {
                continue;
            }

            // Initialize two pointers, `left` and `right`.
            let mut left = i + 1;
            let mut right = nums.len() - 1;

            // Iterate as long as `left` is less than `right`.
            while left < right {
                // Calculate the sum of the values at indices `i`, `left`, and `right`.
                let sum = nums[i] + nums[left] + nums[right];

                // Check if the sum equals zero.
                if sum == 0 {
                    // If sum is zero, add the triplet to the result.
                    result.push(vec![nums[i], nums[left], nums[right]]);

                    // Skip duplicates for `left`.
                    while left < right && nums[left] == nums[left + 1] {
                        left += 1;
                    }

                    // Skip duplicates for `right`.
                    while left < right && nums[right] == nums

[right - 1] {
                        right -= 1;
                    }

                    // Move both pointers towards the center after finding a valid triplet.
                    left += 1;
                    right -= 1;
                } else if sum < 0 {
                    // If sum is less than zero, increment `left` to increase the sum.
                    left += 1;
                } else {
                    // If sum is more than zero, decrement `right` to decrease the sum.
                    right -= 1;
                }
            }
        }

        // Return the vector containing all unique triplets that sum up to zero.
        result
    }
}

/*
### Commentary:

- The function `three_sum` is designed to handle the challenge of finding all unique triplets in an array that sum up to zero.
- It begins by sorting the array, which is a crucial step for the two-pointer approach and for efficiently skipping duplicate values.
- The function uses a for loop to iterate through the array, with additional nested while loops for the two-pointer implementation.
- Careful handling of duplicates is critical in this algorithm to ensure that only unique triplets are added to the result.
- The two-pointer technique is effectively used to find pairs that, along with the current element, sum up to zero.
- This implementation is efficient in terms of both time and space complexity, adhering to the constraints and requirements of the problem.
*/


// Description: =======================================================

/*
To solve the "3Sum" problem in Rust, we'll implement a function `three_sum` within a struct `Solution`. 
The goal is to find all unique triplets in the array which give the sum of zero. The solution involves sorting 
the array and using a two-pointer technique to find pairs that, together with the current element, sum up to zero.

### Algorithm:

1. **Sort the Array:** 
   - First, sort the array. This helps in skipping duplicates and also in using a two-pointer approach.

2. **Iterate Over the Array:**
   - Iterate over the array with an index `i`. 
     For each `i`, we'll try to find pairs `j, k` such that `nums[i] + nums[j] + nums[k] == 0`.
   - Skip duplicate values for `i` to avoid duplicate triplets.

3. **Two-Pointer Approach for Pair Finding:**
   - For each `i`, set two pointers: `left = i + 1` and `right = length of array - 1`.
   - While `left < right`, check the sum `nums[i] + nums[left] + nums[right]`.
     - If the sum is zero, add the triplet to the result and move both pointers, skipping any duplicate values.
     - If the sum is less than zero, increment `left`.
     - If the sum is more than zero, decrement `right`.

4. **Return the Result:**
   - After iterating through the array, return the collected triplets.

### Notes:

- The array is sorted using `sort_unstable()` which is typically faster than `sort()` but does not preserve the order 
  of equal elements.
- The implementation efficiently skips over duplicates to ensure unique triplets.
- The time complexity is O(n^2), primarily due to the nested loop structure (the outer loop and the two-pointer inner loop). 
  Sorting the array adds O(n log n), but the overall complexity remains dominated by the O(n^2) part.
- The space complexity is O(1) in terms of extra space, not considering the space required for the output. The sorting is done 
  in-place, and no additional data structures are used for computation.

### Performance Considerations:

- **Sorting:** Sorting the array upfront is a critical step as it allows efficient skipping of duplicates and simplifies 
    the two-pointer search.
- **Duplicate Skipping:** Careful handling of duplicates is essential to avoid repeating the same triplets in the output, 
    which is a requirement of the problem.
- **Two-Pointer Technique:** This approach effectively reduces the problem to a two-sum problem for each element, 
    significantly cutting down the search space and time.

### Conclusion:

This solution provides an efficient way to solve the 3Sum problem in Rust, balancing performance and code clarity. 
It's well-suited for scenarios where a combination of sorting and the two-pointer method can be applied to reduce complexity
in array-based problems.

*/