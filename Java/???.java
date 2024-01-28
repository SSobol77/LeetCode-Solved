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
public:
    long long minimumCost(vector<int>& nums, int k, int dist) {
        
    }
};

*/
// Solution: --------------------------------------


// Description: ===================================
/*
Your solution uses an interesting approach involving two multisets to manage the elements within a sliding window of 
size `dist + 1` while maintaining the `k - 1` smallest elements in one multiset (`sml`) and the larger elements in 
another (`big`). The algorithm aims to find the minimum possible sum of the costs of dividing the array into `k` disjoint 
contiguous subarrays with the constraints given. Here's a description of the algorithm based on your solution:

1. **Initialization**: 
    - Create two multisets: `sml` for the smallest elements and `big` for the larger elements.
    - Set the size of the sliding window as `sz = dist + 1`.
    - Initialize `sum` to 0 to hold the sum of elements in `sml`, and `ans` to 0 to hold the final answer.

2. **First Window Setup**: 
    - Populate `sml` with the first `sz` elements from `nums`, starting from index 1, and update `sum` accordingly.
    - If `sml` has more than `k - 1` elements, move the largest elements to `big` and adjust `sum` to reflect the sum of 
      the `k - 1` smallest elements.

3. **Sliding Window Iteration**: 
    - Iterate through the rest of the array starting from index `sz + 1`.
    - For each new element, add it to `sum` and `sml`. If the element that falls out of the window (`nums[i - sz]`) is 
      in `big`, remove it from `big`; otherwise, remove it from `sml` and adjust `sum`.
    - Ensure `sml` contains exactly `k - 1` smallest elements by moving elements between `sml` and `big` as necessary.
    - If the largest element in `sml` is greater than the smallest element in `big`, swap them to maintain the order, 
      and adjust `sum` accordingly.
    - Update `ans` with the minimum of `ans` and the current `sum`.

4. **Final Answer**: 
    - The final answer is the sum of the smallest element (`nums[0]`, as the first subarray's cost) and the minimum sum (`ans`) 
      calculated for the subarrays starting from the second element.

This algorithm efficiently maintains a balance between the smallest `k - 1` elements within a sliding window of size `dist + 1`, 
ensuring that the division of the array respects the given constraints. The use of multisets allows for easy insertion, deletion, 
and retrieval of the smallest and largest elements, facilitating the dynamic adjustment of the window and the selection of subarray 
costs.

*/
