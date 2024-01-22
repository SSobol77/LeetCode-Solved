# 646. Maximum Length of Pair Chain.   -Medium-

# Topic: Array, Dynamic Programming, Greedy, Sorting.

"""
### Task:
---
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

Example 1:
Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].

Example 2:
Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].

Constraints:
n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000


### Testcase:
[[1,2],[2,3],[3,4]]
[[1,2],[7,8],[4,5]]


### Code:
---
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

"""
### Solution:   -------------------------------------------------------

class Solution:
    def findLongestChain(self, pairs):
        # Sort the pairs based on their second elements
        pairs.sort(key=lambda x: x[1])

        # Initialize the current end to a very small number
        curr_end = float('-inf')
        count = 0

        # Iterate through the pairs
        for pair in pairs:
            # If the current pair can be chained
            if pair[0] > curr_end:
                # Update the end to the second element of the current pair
                curr_end = pair[1]
                count += 1

        return count

# Test cases
sol = Solution()
print(sol.findLongestChain([[1,2],[2,3],[3,4]]))  # Output: 2
print(sol.findLongestChain([[1,2],[7,8],[4,5]]))  # Output: 3


### Description: ======================================================
'''
To solve the problem of finding the maximum length of a pair chain, we can apply a greedy approach. The key
idea is to sort the pairs based on their second elements (righti) in ascending order. After sorting, we iterate
through the pairs and select the next pair in the sequence if its left element is greater than the right element
of the previously selected pair. This approach ensures that we can form the longest possible chain.

### Explanation:
- **Sorting**: The pairs are sorted based on their second elements. This ensures that we always have the pair
               with the smallest end next, which gives us more options to extend the chain later.

- **Greedy Selection**: We iterate through the sorted pairs and select a pair if and only if its left element
                        is greater than the end of the last pair in the chain. This ensures that the chain is valid.

- **Counting**: We maintain a count of the number of pairs in the longest chain.

This solution has a time complexity of O(n log n) due to the sorting step, and a space complexity of O(1) as we
only use a few variables for tracking purposes.

'''
