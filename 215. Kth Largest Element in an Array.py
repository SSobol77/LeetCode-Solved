# 215. Kth Largest Element in an Array

# Topic: Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect.

'''
# Task:
-------
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4


# Testcase:
-----------
[3,2,1,5,6,4]
2
[3,2,3,1,2,4,5,5,6]
4

'''
# Solution:
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize a min-heap
        heap = []

        # Keep adding elements to the heap. If the heap size exceeds k,
        # remove the smallest element (heap root).
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        # The root of the heap is the kth largest element
        return heap[0]

# Test cases
solution = Solution()
print(solution.findKthLargest([3,2,1,5,6,4], 2))  # Output: 5
print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # Output: 4

'''
Effective algorithm implementation is to use a min-heap. This approach maintains a heap of size k. By iterating 
through the array and keeping the heap size fixed at k, we ensure that the heap always contains the 'k'
largest elements. At the end, the root of the heap (the smallest in the k largest elements) will be the 
kth largest element in the array.

In this solution:

A min-heap is used to efficiently track the k largest elements.
The heapq module in Python provides a simple way to use a list as a min-heap.
Whenever the heap size exceeds k, the smallest element in the heap (which is the root of the heap) is popped out, 
ensuring that only the k largest elements remain.
This approach has a time complexity of O(n log k), which is efficient, especially when k is much smaller than n.

'''
