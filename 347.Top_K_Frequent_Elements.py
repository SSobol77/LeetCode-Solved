"""
# 347. Top K Frequent Elements.

# Topic: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect.


# Task:
---------
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


# Testcase:
-------------
[1,1,1,2,2,3]
2
[1]
1


# Code:
----------
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

         
"""

# Solution:
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        # Count the frequency of each element in 'nums'
        # Counter returns a dictionary where keys are elements of 'nums' and values are their frequencies
        freq_map = Counter(nums)

        # Initialize a min-heap to keep track of the top 'k' frequent elements
        min_heap = []

        # Iterate through the frequency map
        for num, freq in freq_map.items():
            # Push a tuple of (frequency, element) onto the heap
            # Heap is ordered by the first element of the tuple, i.e., frequency
            heapq.heappush(min_heap, (freq, num))

            # If heap size exceeds 'k', pop the smallest element
            # This ensures only the 'k' most frequent elements remain in the heap
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Extract the elements from the heap and construct the result list
        # Since the heap contains tuples of (frequency, element), we extract the second element (the number)
        top_k = [num for freq, num in min_heap]

        # Return the list of top 'k' frequent elements
        return top_k


# Description:
'''
The problem you've presented is a classic one in data structures and algorithms, particularly involving hash tables,
heaps, and sorting. The goal is to find the k most frequent elements in an array. A Python solution to this problem 
should efficiently handle large inputs, as the constraints allow for a sizeable array.

To solve this, we can use a hash table (in Python, a dictionary) to count the frequency of each element in the array. 
Then, we can use a heap (priority queue in Python) to keep track of the k most frequent elements. The Python heapq 
module provides a convenient way to use a min-heap. We can also optimize the solution by using a bucket sort approach,
but let's focus on the heap solution for now, considering its simplicity and efficiency.


Detailed Explanation:
---------------------------
1. Count Frequencies (Line 6-7): We create a frequency map (freq_map) of the elements in nums using Counter. This map 
   associates each unique element with its count in the array.

2. Initialize Min-Heap (Line 10): A min-heap (min_heap) is initialized to store the elements and their frequencies.

3. Heap Operations (Lines 12-20): For each element in the frequency map, we push a tuple (freq, num) onto the heap. 
   The heap is ordered by frequency. If the heap's size exceeds k, we remove the element with the lowest frequency, 
   ensuring that only the k most frequent elements remain.

4. Construct Result (Line 23-24): We extract the num part from each (freq, num) tuple in the heap to form the 
   list top_k, which contains the k most frequent elements.

5. Return Result (Line 26): The top_k list is returned as the final result.


Explanation:
-------------
- Count Frequencies: We use Counter from the collections module to count the frequency of each element in the array.

- Heap for Top K Elements: We use a min-heap to keep track of the top k elements. We push each element and its frequency 
  onto the heap. If the heap size exceeds k, we pop the smallest element (which is the least frequent so far).

- Extract Elements: Finally, we extract the elements from the heap. These are the k most frequent elements.

This solution should work efficiently for the problem's constraints and meets the requirement of having a better time 
complexity than O(n log n). The actual time complexity of this solution is O(n + k log n) due to the frequency counting 
and heap operations.

'''
