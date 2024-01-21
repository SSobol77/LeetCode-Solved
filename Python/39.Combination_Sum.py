"""
# 39. Combination Sum.


# Topic: Array, Backtracking.

# Task:
-----------------
Given an array of distinct integers candidates and a target integer target, return a list of all 
unique combinations of candidates where the chosen numbers sum to target. You may return the combinations 
in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if 
the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less 
than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40


# Testcase:
--------------
[2,3,6,7]
7
[2,3,5]
8
[2]
1


# Code:
-------------
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
   
"""
# Solution:

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remain, path, start):
            # If the target becomes zero, add the current path to the result
            if remain == 0:
                result.append(path[:])
                return
            # If the target becomes negative or we have exhausted the candidates, return
            if remain < 0 or start == len(candidates):
                return
            
            # Try adding each candidate to the path and recurse
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(remain - candidates[i], path, i)
                path.pop()  # Backtrack by removing the last element from the path
        
        result = []  # Initialize a list to store the combinations
        backtrack(target, [], 0)  # Start the backtracking process
        return result

# Description:
'''
In this code:

1. We define a helper function backtrack that takes three parameters:
   - remain: the remaining target value.
   - path: the current combination being constructed.
   - start: the index to start considering candidates.

2. If remain becomes zero, we have found a valid combination, so we add it to the result list.

3. If remain becomes negative or we have exhausted the candidates, we return without doing anything.

4. We iterate through the candidates, trying each candidate by adding it to the path and recursively 
   calling backtrack.

5. After the recursive call, we backtrack by removing the last element from the path to explore other 
   possibilities.

6. We initialize an empty list result to store the unique combinations.

7. We call the backtrack function initially with the target, an empty path, and a start index of 0.

8. Finally, we return the result list containing all the unique combinations.

You can use this Solution class to call the combinationSum method and pass in the candidates and target 
as arguments to find the desired combinations.

'''
