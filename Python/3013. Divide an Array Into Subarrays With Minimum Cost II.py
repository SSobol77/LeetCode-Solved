# 3013. Divide an Array Into Subarrays With Minimum Cost II.   - HARD -

# Topic: Array, Hash Table, Sliding Window, Heap (Priority Queue)

"""
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
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
  
"""
### Solution: --------------------------------------

from sortedcontainers import SortedList
import bisect

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)  # Determine the length of the nums array

        # Initialize a SortedList to maintain elements in sorted order efficiently
        sl = SortedList()
        y = nums[0]  # The cost of the first subarray is fixed as the first element
        ans = float("inf")  # Initialize answer to infinity to find the minimum sum later
        i = 1  # Start of the sliding window, excluding the first fixed element
        running_sum = 0  # Running sum of elements contributing to the subarray costs

        # Iterate through the array starting from the second element
        for j in range(1, n):
            # Find the position where the current element should be inserted in the sorted list
            pos = bisect.bisect_left(sl, nums[j])
            sl.add(nums[j])  # Add the current element to the sorted list

            # If the inserted element's position affects the first k-1 elements,
            # update the running sum accordingly
            if pos < k - 1:
                running_sum += nums[j]
                # If the sorted list size exceeds k-1, remove the contribution of the k-1th element
                if len(sl) > k - 1:
                    running_sum -= sl[k - 1]

            # Ensure the size of the sliding window does not exceed 'dist'
            while j - i > dist:
                # Find the position and value of the element to be removed from the window
                removed_pos = sl.index(nums[i])
                removed_element = nums[i]
                sl.remove(removed_element)  # Remove the element from the sorted list

                # Adjust the running sum if the removed element was among the first k-1
                if removed_pos < k - 1:
                    running_sum -= removed_element
                    # Add the contribution of the new k-1th element if the list still has enough elements
                    if len(sl) >= k - 1:
                        running_sum += sl[k - 2]
                i += 1  # Move the start of the window forward

            # Update the minimum sum (ans) if the current window can form k-1 subarrays
            if j - i + 1 >= k - 1:
                ans = min(ans, running_sum)

        # Return the total minimum cost including the cost of the first subarray
        return ans + y


### Description: ===================================
"""
Your Python solution employs a `SortedList` from the `sortedcontainers` module to efficiently manage a sliding window of elements from the `nums` array while calculating the minimum possible sum of the costs of dividing the array into `k` disjoint contiguous subarrays, considering the `dist` constraint. Here's a detailed description of how the algorithm works:

1. **Initialization**:
    - `n` is determined as the length of the `nums` array.
    - A `SortedList` instance `sl` is initialized to maintain a sorted order of elements within the sliding window.
    - `y` is set to `nums[0]`, representing the cost of the first subarray.
    - `ans` is initialized to `float("inf")` to track the minimum sum of the costs of the remaining `k-1` subarrays.
    - `i` is set to `1`, indicating the start of the sliding window (excluding the first element which is always part of the first subarray).
    - `running_sum` is initialized to `0` to keep track of the sum of the first elements of the subarrays within the sliding window.

2. **Iterating through the array**:
    - The algorithm iterates from the second element (`j = 1`) to the end of the `nums` array.
    - For each element `nums[j]`, its position in the sorted list (`pos`) is determined using binary search (`bisect_left`), and the element is added to `sl`.
    - If the position of the newly added element is among the first `k-1` elements in the sorted list, it potentially affects the `running_sum`. The element is added to `running_sum`, and if the sorted list size exceeds `k-1`, the element at the `k-1`th position (now the least significant towards the sum) is subtracted from `running_sum`.

3. **Maintaining the sliding window**:
    - The algorithm ensures that the size of the sliding window does not exceed `dist` by incrementing `i` (the start of the window) and adjusting the sorted list and `running_sum` accordingly.
    - When an element is removed (because it's outside the window), its position in the sorted list is found. If the removed element was contributing to `running_sum` (i.e., its position was among the first `k-1`), it's subtracted from `running_sum`. If the sorted list still has at least `k-1` elements, the new `k-1`th element's value is added to `running_sum`.

4. **Calculating the minimum sum**:
    - After each iteration, if the current window size (from `i` to `j`) is at least `k-1`, `ans` is updated to the minimum of its current value and `running_sum`, which represents the sum of the first elements of the `k-1` subarrays within the window.

5. **Final result**:
    - The final minimum sum is the sum of `ans` (the minimum sum of the costs of `k-1` subarrays) and `y` (the cost of the first subarray).

This algorithm efficiently handles the sliding window of elements, maintaining a sorted order and dynamically updating the sum of the first elements of potential subarrays, to find the minimum cost of dividing the array into `k` subarrays while respecting the `dist` constraint.
"""