# 442. Find All Duplicates in an Array.

# Topic: Array, Hash Table.


# Task:
'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.

# Testcase:
[4,3,2,7,8,2,3,1]
[1,1,2]
[1]


# Code:

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
'''
# Solution
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []  # This will store the result
        
        for num in nums:
            index = abs(num) - 1  # Convert the value to an index
            
            # If the number at this index is negative, it means we've seen this number before
            if nums[index] < 0:
                duplicates.append(index + 1)  # Add the original number to the result
            else:
                # Mark this number as seen by negating the number at its corresponding index
                nums[index] = -nums[index]
        
        return duplicates
    

# Description:
'''
To solve this problem within the specified constraints (O(n) time complexity and O(1) extra space), we can use 
the input array itself to keep track of the numbers that we've seen. The idea is to navigate through the array 
and for each value we encounter, we use its absolute value as an index and negate the number at that index in 
the array. If a number at a particular index is already negative, it means we have encountered the index (or the 
value) before, so we add the index (or the value) to our result list. This approach works because the problem 
statement guarantees that all integers are in the range `[1, n]`, which means they can be directly mapped to 
indices in the array.

Explanation:

- We iterate through each number in the array.
- We use the absolute value of each number as an index (since the numbers are in the range `[1, n]`, they can directly 
  map to an index by subtracting 1).
- If the number at the calculated index is already negative, it means the number corresponding to this index has been 
  seen before, so we add it to the result list.
- If the number at the calculated index is positive, we negate it to mark it as seen.
- This way, we use the sign of the numbers in the array as a marker to identify duplicates without needing extra space, 
  thereby meeting the space complexity constraint.

Note that this approach modifies the input array, which is a common trade-off when optimizing for space complexity. If 
modifying the input array is not permissible, a different approach would be required, which might not meet the O(1) space 
complexity constraint.

'''
