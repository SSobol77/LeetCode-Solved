"""
46. Permutations

# Topic: Array, Backtracking.


# Task:
---------
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

# Testcase:
-------------
[1,2,3]
[0,1]
[1]


# Code:
----------
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
       

"""
# Solution:
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Define a helper function for backtracking
        def backtrack(path):
            # If the path has the same length as nums, we have a valid permutation
            if len(path) == len(nums):
                result.append(path[:])  # Add the current permutation to the result
                return
            # Iterate through the elements in nums
            for num in nums:
                if num not in path:  # If num is not in the current path, consider it
                    path.append(num)  # Add num to the current path
                    backtrack(path)  # Recursively explore with the updated path
                    path.pop()  # Backtrack by removing the last element from the path
        
        result = []  # Initialize a list to store the permutations
        backtrack([])  # Start the backtracking process with an empty path
        return result  # Return the list containing all possible permutations


# Description:
'''
In this code:

1. We define a helper function backtrack that takes a single parameter path, which represents the current 
   permutation being constructed.

2. If the length of path becomes equal to the length of nums, we have found a valid permutation, so we 
   add it to the result list.

3. We iterate through the elements of nums. If an element is not already in the path, we add it to the 
   path and recursively call backtrack.

4. After the recursive call, we backtrack by removing the last element from the path to explore other 
   possibilities.

5. We initialize an empty list result to store the permutations.

6. We call the backtrack function initially with an empty path.

7. Finally, we return the result list containing all the possible permutations.

You can use this Solution class to call the permute method and pass in the nums array as an argument to 
find the desired permutations.

'''



