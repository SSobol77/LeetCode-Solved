# 217. Contains Duplicate.                  - Easy -

# Topic: Array, Hash Table, Sorting.

"""
### Task:
---
Given an integer array nums, return true if any value appears at least twice in the array, and return 
false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

### Testcase:
---
[1,2,3,1]
[1,2,3,4]
[1,1,1,3,3,4,3,2,4,2]


### Code:
---
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
"""
### Solution:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty set to keep track of seen numbers
        seen = set()

        # Iterate over each number in the input array
        for num in nums:
            # Check if the current number is already in the set
            if num in seen:
                # If the number is found in the set, a duplicate exists
                return True
            # Add the current number to the set
            seen.add(num)

        # If no duplicates were found in the entire array, return False
        return False

# Test cases
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))  # Output: true (since 1 is a duplicate)
print(sol.containsDuplicate([1,2,3,4]))  # Output: false (no duplicates)
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # Output: true (multiple duplicates)



### Description:
'''
To solve the "Contains Duplicate" problem, we need to check if there are any duplicate elements in the given array `nums`. 
There are several ways to approach this problem, including using a hash table or sorting the array. The hash table approach 
is generally more efficient as it can provide a solution in linear time.

### Approach Using a Hash Table
We can use a set to keep track of the elements we've seen so far. As we iterate through the array, we check if the current 
element is already in the set. If it is, we return `true` because it means we've found a duplicate. If we finish iterating 
through the array without finding any duplicates, we return `false`.

### Explanation

- We initialize an empty set named `seen`.
- We iterate over each element in `nums`.
- If an element is already in the `seen` set, we return `true` as a duplicate is found.
- If the element is not in the set, we add it to the `seen` set.
- If the loop completes without returning `true`, it means no duplicates were found, so we return `false`.

This solution is efficient and has a time complexity of O(n), where n is the number of elements in the array, because set 
operations (checking if an element is in the set and adding an element to the set) are generally O(1) in Python.

'''
