# 525. Contiguous Array.

# Topics: Array, Hash Table, Prefix Sum.

"""
## Task:
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.

## Testcase:
[0,1]
[0,1,0]

## Code:
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
"""
## Solution:

from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        # Initialize defaultdict without a lambda for simplicity
        count_index_map = defaultdict()
        count_index_map[0] = -1  # Initialize base case

        for i, num in enumerate(nums):
            # Adjust count based on whether num is 1 or 0 more explicitly
            count += 1 if num == 1 else -1
            
            # Check if count has been seen before
            if count in count_index_map:
                # Update max_length based on the first occurrence of this count
                max_length = max(max_length, i - count_index_map[count])
            else:
                # Record the first occurrence of this count
                count_index_map[count] = i
        
        return max_length


## Description:
'''
This solution is designed to find the maximum length of a contiguous subarray within a binary array where the number of 0s 
and 1s is equal. It employs a `defaultdict` from the `collections` module for efficient count tracking and a single pass through 
the array to achieve linear time complexity. Here's a breakdown of how the solution works:

1. **Initialization**:
    - `max_length`: A variable set to 0 to keep track of the maximum length of any subarray found that meets the criteria.
    - `count`: A counter initialized at 0 to maintain the net difference between the number of 1s and 0s encountered as we iterate through the array. A positive count indicates more 1s than 0s, a negative count indicates more 0s than 1s, and a count of 0 indicates an equal number of each.
    - `count_index_map`: A `defaultdict` that maps each unique count value to the earliest index at which this count was observed. The dictionary is initialized with the key-value pair `(0, -1)` to represent the count before the start of the array.

2. **Iteration**:
    - The solution iterates through the `nums` array, adjusting the `count` for each element. The count is incremented for a 1 and decremented for a 0.
    - For each new count value, the solution checks if this count has been seen before:
        - If the count is found in `count_index_map`, it means a subarray with an equal number of 0s and 1s has been closed at the current index `i`. The length of this subarray is computed as `i - count_index_map[count]`. If this length is greater than the current `max_length`, `max_length` is updated.
        - If the count has not been seen before, the current index `i` is added to `count_index_map` with the current count as the key. This marks the first occurrence of this count.

3. **Result**:
    - After completing the iteration through the array, the solution returns `max_length`, which now holds the length of the longest contiguous subarray with an equal number of 0s and 1s.

This approach ensures that the solution is both time-efficient, with a complexity of \(O(n)\), where \(n\) is the length of the 
input array, and space-efficient, using a hash table to keep track of count occurrences with a worst-case space complexity of \(O(n)\) for storing each unique count value encountered during iteration.

'''
