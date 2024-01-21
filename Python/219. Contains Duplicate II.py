# 219. Contains Duplicate II.       - Easy -

# Topic: Array, Hash Table, Sliding Window.

"""
### Task:
---
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the 
array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 
Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5


### Testcase:
---
[1,2,3,1]
3
[1,0,1,1]
1
[1,2,3,1,2,3]
2


### Code:
---
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
"""
### Solution: --------------------------------------------------------------------

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the last seen index of each number
        last_seen = {}

        # Iterate over the array
        for i, num in enumerate(nums):
            # Check if the number is in the dictionary and the indices are within k distance
            if num in last_seen and i - last_seen[num] <= k:
                return True
            # Update the dictionary with the current index
            last_seen[num] = i

        # No nearby duplicates were found
        return False


# Test cases
sol = Solution()
print(sol.containsNearbyDuplicate([1,2,3,1], 3))  # Output: true
print(sol.containsNearbyDuplicate([1,0,1,1], 1))  # Output: true
print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))  # Output: false



### Description: =====================================================================
'''
To solve the "Contains Duplicate II" problem, we can use a hash table to keep track of the numbers and their indices in the array. 
The goal is to find out if there are any two indices `i` and `j` such that `nums[i] == nums[j]` and `abs(i - j) <= k`. A hash table 
(or dictionary in Python) is an efficient way to store and retrieve the last seen index of each number.

Here's the step-by-step approach:

1. **Create a Dictionary**: Initialize an empty dictionary to store the last seen index of each number.

2. **Iterate Through the Array**: Loop through each element in the array. For each element, check if it is already in the dictionary 
   and also if the current index and the stored index in the dictionary are within `k` distance.

3. **Update the Dictionary**: After the check, update the dictionary with the current index for each number.


This solution efficiently checks for nearby duplicates within `k` distance by maintaining a running record of the last seen indices of
each number. The time complexity is O(n), where n is the number of elements in the array, because we only traverse the list once.

'''