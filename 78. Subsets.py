# 78. Subsets.

# Topic: Array, Backtracking, Bit Manipulation.


'''
# Task:
----------
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.


# Testcase:
-------------
[1,2,3]
[0]

# Code:
-------------
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
 
'''
# Solution:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Function to backtrack and generate subsets
        def backtrack(start, subset):
            # Add the current subset to the result
            result.append(subset[:])

            # Iterate over the array to build subsets
            for i in range(start, len(nums)):
                # Include current number and backtrack
                subset.append(nums[i])
                backtrack(i + 1, subset)
                # Backtrack - remove the number and try next
                subset.pop()

        result = []
        backtrack(0, [])
        return result

# The Solution class and subsets method are now defined. 
# Below are the test cases to validate the implementation.

# Test cases
sol = Solution()

# Test case 1: nums = [1, 2, 3]
print(sol.subsets([1, 2, 3]))  # Expected output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Test case 2: nums = [0]
print(sol.subsets([0]))  # Expected output: [[],[0]]

# Description:
'''
To generate all possible subsets of a given set of unique integers, we can use a backtracking approach. 
This problem is simpler than generating subsets with duplicates because we don't need to worry about 
avoiding duplicate subsets.

The algorithm works as follows:
1.  Start with an Empty Subset: Begin with an empty subset and add elements to it one by one.
2.  Recursive Backtracking: For each element, we have two choices: either include the element in the current subset or not.
    We explore both these options recursively.
3.  Add Subsets to the Result: Each time we reach the end of the array, we add the current subset to our list of subsets.

In this code:
- The subsets method generates all subsets of an array with unique elements.
- The backtrack function is used to recursively build subsets.
- The test cases validate the implementation for the given examples. The order of the subsets in the output may vary
  as the problem statement allows returning the solution in any order.

'''
