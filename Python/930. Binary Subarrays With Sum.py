# 930. Binary Subarrays With Sum.

# Topic: Array, Hash Table, Sliding Window, Prefix Sum.

"""
### Task:
---
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

Constraints:
1 <= nums.length <= 3 * 10^4
nums[i] is either 0 or 1.
0 <= goal <= nums.length


### Testcase:
---
[1,0,1,0,1]
2
[0,0,0,0,0]
0


### Code:
---
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    
"""
### Solution: --------------------------------------

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Initialize a hash table to keep track of the frequencies of prefix sums
        prefix_sum_freq = {0: 1}
        # Initialize variables for the current sum and the count of valid subarrays
        current_sum = 0
        count = 0

        # Iterate through each number in the array
        for num in nums:
            # Update the current sum with the value of the current element
            current_sum += num
            # If the difference between the current sum and the goal is in the prefix sum frequencies,
            # it means there are subarrays ending at the current index that meet the goal sum
            if current_sum - goal in prefix_sum_freq:
                # Add the frequency of (current_sum - goal) to the count, as this represents the number of
                # valid subarrays ending at the current index
                count += prefix_sum_freq[current_sum - goal]
            # Update the frequency of the current sum in the hash table. If the current sum is not present,
            # it gets added with a default frequency of 1. If it is present, its frequency is incremented.
            prefix_sum_freq[current_sum] = prefix_sum_freq.get(current_sum, 0) + 1

        # After iterating through the array, return the total count of valid subarrays
        return count


### Description: ===================================
'''
To solve the "Binary Subarrays With Sum" task, we can use a combination of Prefix Sum and Hash Table techniques. This approach works 
well because we're dealing with binary arrays and a specific goal sum for subarrays.

### Solution:

1. **Initialize Variables:** Create a hash table (or a dictionary in Python) to store the frequency of prefix sums encountered so far. 
     Also, initialize a variable to keep track of the current sum of elements and a variable to store the count of subarrays meeting 
     the goal sum.

2. **Iterate Through the Array:** Go through each element in the array. Update the current sum by adding the current element to it. 
     The current sum represents the sum of all elements from the start of the array to the current element.

3. **Find Subarrays Meeting the Goal:** Check if `(current sum - goal)` exists in the hash table. If it does, it means there are 
     subarrays ending at the current element whose sum equals the goal. Add the frequency of `(current sum - goal)` from the hash 
     table to the count of valid subarrays.

4. **Update Hash Table:** Increase the frequency of the current sum in the hash table by 1. If the current sum has not been encountered 
     before, add it to the hash table with a frequency of 1.

5. **Return Count:** After iterating through the entire array, return the count of subarrays that meet the goal sum.


### Description:

- The hash table `prefix_sum_freq` tracks how many times a particular sum has been seen. It starts with `{0: 1}` to account for the 
  case when a subarray starts from the beginning of the array.

- `current_sum` keeps track of the sum from the start of the array to the current element.

- For each element, we check if `current_sum - goal` is in `prefix_sum_freq`. If it is, it means there are subarrays ending at the 
  current element that meet the goal, so we add the frequency of `current_sum - goal` to `count`.

- We then update `prefix_sum_freq` with the new `current_sum`.

- The final `count` represents the total number of subarrays whose sum equals the goal.

This method efficiently solves the problem with a single pass through the array and has a time complexity of O(N), where N is the length 
of the array.

'''
