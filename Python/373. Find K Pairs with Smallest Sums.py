# 373. Find K Pairs with Smallest Sums

# Topic: Array, Heap (Priority Queue).

'''
# Task:
----------
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
 
Constraints:
1 <= nums1.length, nums2.length <= 10^5
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 10^4
k <= nums1.length * nums2.length

# Testcase:
-----------
[1,7,11]
[2,4,6]
3
[1,1,2]
[1,2,3]
2
[1,2,4,5,6]
[3,5,7,9]
3

'''
# Solution:
from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Check for empty input arrays
        if not nums1 or not nums2:
            return []

        # Initialize a min-heap with the first pair (smallest sum pair)
        # The heap elements are tuples: (sum of pair, index in nums1, index in nums2)
        min_heap = [(nums1[0] + nums2[0], 0, 0)]
        result = []

        # Extract up to k smallest pairs
        while k > 0 and min_heap:
            # Pop the smallest pair from the heap
            current_sum, i, j = heapq.heappop(min_heap)
            # Add the corresponding pair from nums1 and nums2 to the result
            result.append([nums1[i], nums2[j]])
            k -= 1

            # If it's the first pair with nums1[i], add the next pair in the sequence (with nums1[i + 1])
            if j == 0 and i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))

            # Add the next pair in the sequence (with nums2[j + 1])
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result

# Test cases
solution = Solution()
print(solution.kSmallestPairs([1,7,11], [2,4,6], 3))  # Output: [[1,2],[1,4],[1,6]]
print(solution.kSmallestPairs([1,1,2], [1,2,3], 2))  # Output: [[1,1],[1,1]]
print(solution.kSmallestPairs([1,2,4,5,6], [3,5,7,9], 3))  # Output: [[1,3],[2,3],[4,3]]
 

'''
This solution uses a min-heap to maintain the smallest sums at each step. It ensures that at each iteration, 
the next pair with the smallest sum is added to the result. The heap starts with the smallest possible sum 
pair and gradually adds new pairs that potentially have the next smallest sums, thereby optimizing the number
of operations and reducing the likelihood of a runtime error due to excessive processing.
In this code:

A min-heap is used to efficiently find the smallest pairs by sum. It stores tuples containing the sum of the pairs and the corresponding indices in nums1 and nums2.
The heap is initialized with the first pair (the smallest sum pair), formed by the first elements of nums1 and nums2.
The algorithm repeatedly extracts the smallest pair from the heap and adds the next potential smallest pairs until k pairs are found or the heap is exhausted.
The check if j == 0 and i + 1 < len(nums1) ensures that for each element in nums1, we only add the pair with the first element of nums2 once. This helps in systematically exploring all pairs without repetition.
For each extracted pair, the next pair in the sequence (with the next element of nums2) is added to the heap. This step ensures that we explore all possible pairs while maintaining the heap size to be minimal.
The result is a list of k pairs with the smallest sums, based on the given input arrays.
'''