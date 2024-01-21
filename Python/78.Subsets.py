"""
# 78. Subsets.

# Topic: Array, Backtracking, Bit Manipulation,

# Task:
---------
Given an integer array nums of unique elements, return all possible
subsets (the power set).

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
-----------
[1,2,3]
[0]


# Code:
------------
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
   
"""
# Solution:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Adding the current subset to the result
            result.append(path.copy())

            # Considering each element starting from 'start'
            for i in range(start, len(nums)):
                # Include the element nums[i]
                path.append(nums[i])
                # Recurse with the next element
                backtrack(i + 1, path)
                # Backtrack: exclude the last element
                path.pop()

        result = []
        backtrack(0, [])
        return result

# Description:
'''
To solve the subsets problem, we can use backtracking, a method that allows us to generate all possible 
combinations of the given set. We can also solve this using bit manipulation, but let's focus on the 
backtracking approach for clarity.

The idea is to generate all subsets by including or excluding each element. For each element in the input 
list, we have two choices: either include the element in the current subset or exclude it. By exploring 
both these choices for every element, we can generate all possible subsets.

Here's a step-by-step approach:
------------------------------------
    Start with an Empty Subset: Begin with an empty subset and consider each element one by one.

    Include or Exclude Elements: For each element, make two recursive calls: one including the element in 
                                 the current subset and another excluding it.

    Base Case: When we have considered all elements, add the current subset to the list of subsets.

    Avoiding Duplicates: Since the input guarantees unique elements, we don't need to worry about duplicate 
                         subsets.

    Returning the Result: After considering all elements, return the list of subsets.


In this implementation:
------------------------
-    backtrack is a recursive function that takes the current index (start) and the current subset (path) as 
     arguments.
-    We start with an empty path and for each element, we include it in path, recurse for the next elements, 
     and then exclude it (backtrack) to consider subsets without this element.
-    The result list accumulates all the subsets generated.

This solution effectively generates all subsets of the given set through backtracking.

'''
