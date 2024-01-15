// 4. Median of Two Sorted Arrays

/*
###Task:
-----
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6


### Testcase:
---
[1,3]
[2]
[1,2]
[3,4]

###Code:
--- 
impl Solution {
    
}

*/
// Solution:

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        // Determine the smaller array to perform binary search on it.
        // This reduces the search space and ensures we don't miss any elements in the larger array.
        let (nums1, nums2) = if nums1.len() > nums2.len() {
            (nums2, nums1)
        } else {
            (nums1, nums2)
        };

        // Calculate the total number of elements and the middle index.
        let total = nums1.len() + nums2.len();
        let half = total / 2;

        // Initialize binary search bounds.
        let (mut left, mut right) = (0, nums1.len());

        while left <= right {
            let mid1 = (left + right) / 2; // Middle index for nums1
            let mid2 = half - mid1;        // Complementary index for nums2

            // Edge cases: when the partition is at the start or end of nums1
            let max_left1 = if mid1 == 0 { i32::MIN } else { nums1[mid1 - 1] };
            let min_right1 = if mid1 == nums1.len() { i32::MAX } else { nums1[mid1] };

            // Edge cases: when the partition is at the start or end of nums2
            let max_left2 = if mid2 == 0 { i32::MIN } else { nums2[mid2 - 1] };
            let min_right2 = if mid2 == nums2.len() { i32::MAX } else { nums2[mid2] };

            // Check if we have found the correct partition
            if max_left1 <= min_right2 && max_left2 <= min_right1 {
                // If the total number of elements is even, the median is the average of the two middle values.
                // If odd, the median is the middle value from the right half.
                if total % 2 == 0 {
                    return (max(max_left1, max_left2) as f64 + min(min_right1, min_right2) as f64) / 2.0;
                } else {
                    return min(min_right1, min_right2) as f64;
                }
            } else if max_left1 > min_right2 {
                // Adjust binary search bounds
                right = mid1 - 1;
            } else {
                left = mid1 + 1;
            }
        }

        // Fallback value, should never be reached if inputs are valid
        0.0
    }
}

use std::cmp::{max, min};


// Description:---------------------------------------------
/*
To solve the problem of finding the median of two sorted arrays with a time complexity of O(log(m+n)), 
we need to use a binary search algorithm. The idea is to partition both arrays into two halves such that 
the left half contains an equal (or one less) number of elements as the right half. The median will then 
be calculated based on the largest element on the left and the smallest element on the right.

Here's a step-by-step approach in Rust:

1. Identify the smaller array to apply the binary search.
2. Apply binary search on the smaller array.
3. Find the partition index in both arrays such that `left_part <= right_part`.
4. Handle edge cases where the partition is at the start or end of the array.
5. Calculate the median based on the maximum of left elements and minimum of right elements, considering odd 
   and even total length.

In this implementation, we first determine the smaller of the two arrays and perform binary search on it. 
We then calculate the partition indices in both arrays and adjust them to find the correct partition where 
elements on the left are less than or equal to elements on the right. The median is computed based on these 
partitions, accounting for both odd and even total lengths of the arrays.

*/