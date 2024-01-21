# 216. Combination Sum III.     -Medium-

# Topic: Array, Backtracking.

"""
### Task:
---
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

  -  Only numbers 1 through 9 are used.
  -  Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and 
the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 
Constraints:
2 <= k <= 9
1 <= n <= 60

### Testcase:
---
3
7
3
9
4
1


### Code:
---
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
   

"""
### Solution: --------------------------------------------------------


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Helper function for backtracking
        def backtrack(start, comb, remaining):
            # Check if the combination is valid
            if len(comb) == k and remaining == 0:
                result.append(list(comb))
                return
            # Explore further combinations
            for i in range(start, 10):
                comb.append(i)  # Add the current number to the combination
                backtrack(i + 1, comb, remaining - i)  # Recurse with updated parameters
                comb.pop()  # Backtrack: remove the last added number

        result = []
        backtrack(1, [], n)  # Initial call to the helper function
        return result

# Test cases
sol = Solution()
print(sol.combinationSum3(3, 7))  # Output: [[1,2,4]]
print(sol.combinationSum3(3, 9))  # Output: [[1,2,6], [1,3,5], [2,3,4]]
print(sol.combinationSum3(4, 1))  # Output: []


### Description: =============================================================
'''
In this code, the `backtrack` function is a recursive function used for generating all possible combinations. 
It explores each number from `start` to 9, checks if adding the number to the current combination (`comb`) will 
contribute to a valid solution, and then recursively calls itself to explore further possibilities. If a valid 
combination is found (i.e., the combination length equals `k` and the sum equals `n`), it's added to the result list. 
The use of `.pop()` ensures that the function backtracks correctly, removing the last added number before trying 
the next one in the loop.

To solve the "Combination Sum III" problem, we can use backtracking, which is an efficient way to explore all possible 
combinations of numbers. The goal is to find all unique combinations of `k` numbers that add up to `n`, using numbers 
from 1 to 9. Each number can be used at most once, and the combinations should be unique.

Here's a step-by-step approach to solve this problem:

1. **Define a Helper Function**: Create a helper function for the backtracking process. It should keep track of the current 
combination of numbers, the current sum, and the starting number for the next step.

2. **Backtracking Logic**: In each step, iterate through the numbers starting from the last used number up to 9. For each number, 
add it to the current combination and recursively call the helper function with the updated combination and sum. If the length 
of the current combination reaches `k` and the sum equals `n`, add the current combination to the result.

3. **Avoiding Duplicates**: To ensure that combinations are not repeated, always start the next step of iteration from the last 
added number + 1.

This solution will find all valid combinations that meet the conditions. The `backtrack` function is the key part of the solution, 
where the backtracking algorithm is implemented to explore all possible combinations.

'''
