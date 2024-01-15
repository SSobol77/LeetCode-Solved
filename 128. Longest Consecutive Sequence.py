# 128. Longest Consecutive Sequence.

# Topic: Array, Hash Table, Union Find.

"""
### Task:
---
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

#Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

#Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

#Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9


### Testcase:
---
[100,4,200,1,3,2]
[0,3,7,2,5,8,4,6,0,1]

### Code:
---
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
"""
### Solution:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Create a set to store unique elements in nums
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Check if num is the start of a sequence (i.e., num-1 is not in the set)
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Traverse the sequence to find its length
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the longest streak if needed
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak


### Description:
'''
To find the length of the longest consecutive sequence in an unsorted array of integers nums in O(n) time, you can 
use a hash set to store the unique elements in the array and then traverse the array to find consecutive sequences.

This code first creates a set num_set to store the unique elements from the input array nums. It then iterates through 
each element in num_set and checks if it is the start of a sequence. If it is, it starts counting the length of the 
sequence by incrementing current_streak while checking for consecutive numbers.

The variable longest_streak keeps track of the longest consecutive sequence found so far, and it is updated whenever 
a longer sequence is encountered. Finally, the function returns longest_streak, which represents the length of the 
longest consecutive sequence in the input array.

This solution has a time complexity of O(n) because it iterates through the array once and uses constant time operations 
 set operations and sequence traversal.
 
'''