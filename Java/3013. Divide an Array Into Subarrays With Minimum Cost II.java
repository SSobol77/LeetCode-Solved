// 3013. Divide an Array Into Subarrays With Minimum Cost II.

// Topic: Array, Hash Table, Sliding Window, Heap (Priority Queue)

/*
### Task:
---
You are given a 0-indexed array of integers nums of length n, and two positive integers k and dist.
The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.
You need to divide nums into k disjoint contiguous subarrays, such that the difference between the starting index of the second 
subarray and the starting index of the kth subarray should be less than or equal to dist. In other words, if you divide nums into 
the subarrays nums[0..(i1 - 1)], nums[i1..(i2 - 1)], ..., nums[ik-1..(n - 1)], then ik-1 - i1 <= dist.

Return the minimum possible sum of the cost of these subarrays.

Example 1:
Input: nums = [1,3,2,6,4,2], k = 3, dist = 3
Output: 5
Explanation: The best possible way to divide nums into 3 subarrays is: [1,3], [2,6,4], and [2]. This choice is valid because ik-1 - i1 is 5 - 2 = 3 which is equal to dist. The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.

Example 2:
Input: nums = [10,1,2,2,2,1], k = 4, dist = 3
Output: 15
Explanation: The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because ik-1 - i1 is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
The division [10], [1], [2,2,2], and [1] is not valid, because the difference between ik-1 and i1 is 5 - 1 = 4, which is greater than dist.
It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.

Example 3:
Input: nums = [10,8,18,9], k = 3, dist = 1
Output: 36
Explanation: The best possible way to divide nums into 4 subarrays is: [10], [8], and [18,9]. This choice is valid because ik-1 - i1 is 2 - 1 = 1 which is equal to dist.The total cost is nums[0] + nums[1] + nums[2] which is 10 + 8 + 18 = 36.
The division [10], [8,18], and [9] is not valid, because the difference between ik-1 and i1 is 3 - 1 = 2, which is greater than dist.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 36.
 
Constraints:
3 <= n <= 10^5
1 <= nums[i] <= 10^9
3 <= k <= n
k - 2 <= dist <= n - 2

Hint 1
For each i > 0, try each nums[i] as the first element of the second subarray. We need to find the sum of k - 2 smallest values in the index range [i + 1, min(i + dist, n - 1)].
Hint 2
Typically, we use a max heap to maintain the top k - 2 smallest values dynamically. Here we also have a sliding window, which is the index range [i + 1, min(i + dist, n - 1)]. We can use another min heap to put unselected values for future use.
Hint 3
Update the two heaps when iteration over i. Ordered/Tree sets are also a good choice since we have to delete elements.
Hint 4
If the max heap’s size is less than k - 2, use the min heap’s value to fill it. If the maximum value in the max heap is larger than the smallest value in the min heap, swap them in the two heaps.


### Testcase:
---
[1,3,2,6,4,2]
3
3
[10,1,2,2,2,1]
4
3
[10,8,18,9]
3
1


### Code:
---
class Solution {
    public long minimumCost(int[] nums, int k, int dist) {
        
    }
}

*/
// Solution: --------------------------------------

class Solution {
    public long minimumCost(int[] nums, int k, int dist) {
        // Initialize result with the maximum possible value to track the minimum sum
        long result = Long.MAX_VALUE, sum = 0L;
        int n = nums.length;
        
        // TreeSet to maintain indices of elements, sorted by their values in nums
        // In case of equal values, indices are used for sorting to maintain uniqueness
        TreeSet<Integer> set1 = new TreeSet<>((a, b) -> nums[a] == nums[b] ? a - b : nums[a] - nums[b]);
        TreeSet<Integer> set2 = new TreeSet<>((a, b) -> nums[a] == nums[b] ? a - b : nums[a] - nums[b]);

        // Start iterating from the second element since the first element's cost is fixed
        for (int i = 1; i < n; i++) {
            // Add current index to set1 and update sum with the element's value
            set1.add(i);
            sum += nums[i];

            // If set1 size exceeds k-1, move the largest element to set2 and adjust sum
            if (set1.size() >= k) {
                int x = set1.pollLast(); // Retrieve and remove the last element in set1
                sum -= nums[x]; // Subtract its value from sum
                set2.add(x); // Add the removed index to set2
            }

            // Once the sliding window exceeds 'dist', start evaluating the result
            if (i - dist > 0) {
                // Update result with the minimum sum of the current window
                result = Math.min(result, sum);

                // Determine the index to be removed based on the sliding window constraint
                int temp = i - dist;

                // If the removed index is in set1, adjust set1 and sum accordingly
                if (set1.contains(temp)) {
                    set1.remove(temp); // Remove the index from set1
                    sum -= nums[temp]; // Subtract its value from sum

                    // If set2 is not empty, move its smallest element to set1 and adjust sum
                    if (set2.size() > 0) {
                        int y = set2.pollFirst(); // Retrieve and remove the first element in set2
                        sum += nums[y]; // Add its value to sum
                        set1.add(y); // Add the removed index to set1
                    }
                } else {
                    // If the removed index is in set2, simply remove it from set2
                    set2.remove(temp);
                }
            }
        }

        // Return the minimum sum found plus the cost of the first subarray (nums[0])
        return result + nums[0];
    }
}


// Description: ===================================
/*
This Java solution for the problem uses two `TreeSet` instances to manage indices of elements in the `nums` array, ensuring an 
efficient way to keep track of and update the minimum cost to divide the array into `k` disjoint contiguous subarrays, considering 
the `dist` constraint. Here's a detailed description of how the algorithm works:

1. **Initialization**:
    - Initialize `result` with `Long.MAX_VALUE` to track the minimum sum of the first elements of the subarrays.
    - Initialize `sum` with `0L` to maintain the cumulative sum of the elements considered for inclusion in the subarrays.
    - Define `n` as the length of the `nums` array.
    - Initialize two `TreeSet` instances, `set1` and `set2`, with custom comparators that prioritize by value at the indices in 
      the `nums` array, and in case of ties, by the indices themselves. This ensures uniqueness and order based on the array 
      values and their indices.

2. **Iterating through the array**:
    - Start iterating from index `1` through the end of the `nums` array.
    - Add each index to `set1` and update `sum` by adding the corresponding element from `nums`.
    - If `set1`'s size reaches `k`, remove the last (highest) element from it, subtract its value from `sum`, and add its 
      index to `set2`. This step effectively maintains the `k-1` smallest elements within the considered range in `set1`.

3. **Adjusting for the distance constraint**:
    - After the initial setup, for each new index `i` starting from the point where `i - dist > 0`, perform the following:
        - Update `result` with the minimum of its current value and `sum`. This accounts for the possibility that the current set of elements forms an optimal subarray grouping.
        - Calculate `temp` as `i - dist`, which represents the index of the element that needs to be removed from the current consideration due to the distance constraint.
        - If `temp` is in `set1`, remove it and adjust `sum` by subtracting the value at `temp` in `nums`. Then, if `set2` is not empty, transfer the smallest element from `set2` to `set1` and adjust `sum` accordingly. This step ensures that `set1` always contains the `k-1` smallest elements within the valid range.
        - If `temp` is not in `set1`, simply remove it from `set2`. This handles the case where the element to be removed had been previously transferred to `set2`.

4. **Final computation**:
    - The final result is obtained by adding `nums[0]` (the cost of the first subarray) to the minimum sum calculated (`result`). 
      This sum represents the minimum cost to divide the array into `k` subarrays while adhering to the `dist` constraint.

This algorithm effectively manages the sliding window of elements and their indices, ensuring that at each step, the subarrays 
formed comply with the problem's constraints and that the minimum possible sum of the costs of these subarrays is calculated.

*/
