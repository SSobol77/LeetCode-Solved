# 90. Subsets II.

# Topic: Array, Backtracking, Bit Manipulation.

'''
# Task:
--------
Given an integer array nums that may contain duplicates, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10

# Testcase:
--------------
[1,2,2]
[0]


# Code: 
--------------
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
'''
# Solution:
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to ensure duplicates are adjacent
        nums.sort()

        # Function to backtrack and generate subsets
        def backtrack(start, subset):
            # Add the current subset to the result
            result.append(subset[:])

            # Iterate over the array to build subsets
            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # Include current number and backtrack
                subset.append(nums[i])
                backtrack(i + 1, subset)
                # Backtrack - remove the number and try next
                subset.pop()

        result = []
        backtrack(0, [])
        return result

# The Solution class and subsetsWithDup method are now defined. 
# Below are the test cases to validate the implementation.

# Test cases
sol = Solution()

# Test case 1: nums = [1,2,2]
print(sol.subsetsWithDup([1, 2, 2]))  # Expected output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Test case 2: nums = [0]
print(sol.subsetsWithDup([0]))  # Expected output: [[],[0]]


# Description:
'''
To generate all possible subsets of an array with duplicates, ensuring no duplicate subsets, we can use
a backtracking approach. The algorithm involves sorting the array first to ensure duplicates are adjacent,
and then recursively generating subsets. When building these subsets, we need to be careful to skip over duplicates.

Here's a step-by-step approach:
* Sort the Array: Sorting the array ensures that duplicates are adjacent, making it easier to avoid adding duplicate subsets.
* Backtracking Function: Define a function that takes the current subset, the starting index, and the original array. This 
  function will be used recursively to add elements to the subset or skip them.
* Avoiding Duplicates: When adding elements to the current subset, if an element is the same as the previous one and the
  previous one was not added, skip adding this element to avoid duplicates.

In this code:
- The subsetsWithDup method generates all unique subsets of an array with duplicates.
- The backtrack function is used to recursively build subsets, ensuring no duplicates are added.
- The test cases validate the implementation for the given examples. The order of the subsets in the output may vary as 
  the problem statement allows returning the solution in any order.

'''
