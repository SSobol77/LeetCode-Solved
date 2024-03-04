# 40. Combination Sum II.

# Topic: Array, Backtracking.

"""
### Task:
---
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates 
where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 
Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30


### Testcase:
---
[10,1,2,7,6,1,5]
8
[2,5,2,1,2]
5

### Code:
---
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
 
"""
### Solution: --------------------------------------

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort the candidates
        res = []
        
        def backtrack(start, target, path):
            if target == 0:  # Found a valid combination
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:  # Skip duplicates
                    continue
                if candidates[i] > target:  # No need to continue if the candidate exceeds the target
                    break
                # Include the candidate and move to the next
                backtrack(i+1, target-candidates[i], path+[candidates[i]])
        
        backtrack(0, target, [])  # Start the backtracking process
        return res

# Test cases
solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))  # Output: [[1,1,6], [1,2,5], [1,7], [2,6]]
print(solution.combinationSum2([2,5,2,1,2], 5))  # Output: [[1,2,2], [5]]



### Description: ===================================
'''
To solve the "Combination Sum II" problem, we'll use a backtracking approach to explore all possible combinations of the candidate 
numbers that add up to the target. We'll also take care to avoid duplicates by sorting the candidates and skipping over duplicate 
values during our recursion. Here's a step-by-step breakdown of the solution:

1. **Sort the Candidates**: First, we sort the `candidates` array. Sorting helps in easily skipping duplicate numbers and also in 
making the combination process efficient.

2. **Backtracking Function**: We define a recursive backtracking function that takes the current combination being constructed, 
the current sum of the combination, the current index in the `candidates` array, and the `target` sum we're aiming for. The base 
cases for this function are when the current sum equals the target (we've found a valid combination) or exceeds it (we need to backtrack).

3. **Avoiding Duplicates**: As we iterate through the candidates starting from the current index, if we encounter the same number 
as the previous (and it's not the first index we're looking at), we skip it. This step is crucial to avoid adding duplicate combinations 
to the result.

4. **Recursive Exploration**: For each candidate number, we explore two possibilities - either include the number in the current 
combination or skip it and move to the next. When including a number, we call the backtracking function recursively with the updated 
combination and sum. After exploring the inclusion path, we backtrack by removing the last number added to the combination before 
moving to the next candidate.

5. **Result Collection**: Whenever the base case of the current sum equaling the target is met, we add the current combination to 
our result list.


This code defines a `Solution` class with the `combinationSum2` method. The method sorts the input candidates, defines a `backtrack` 
function for exploring combinations, and initializes the backtracking process. The `backtrack` function explores all possible combinations, 
avoiding duplicates and exceeding target sums, and adds valid combinations to the result list.

'''
