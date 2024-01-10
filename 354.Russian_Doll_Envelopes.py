"""
# 354. Russian Doll Envelopes.


# Topic: Array, Binary Search, Dynamic Programming, Sorting.



# Task:
-----------
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the 
height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater 
than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1

Constraints:
1 <= envelopes.length <= 10^5
envelopes[i].length == 2
1 <= wi, hi <= 10^5



# Testcase:
------------
[[5,4],[6,4],[6,7],[2,3]]
[[1,1],[1,1],[1,1]]


# Code:
-----------
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
  

"""
# Solution:
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort the envelopes by width in ascending order and by height in descending order
        # This sorting ensures that when applying LIS, only increasing widths are considered
        # and for the same width, the envelope with smaller height is considered first
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Function to apply Binary Search
        def binary_search(lst, x):
            low, high = 0, len(lst) - 1
            while low <= high:
                mid = (low + high) // 2
                if lst[mid] < x:
                    low = mid + 1  # Move to the right half if x is greater
                else:
                    high = mid - 1  # Move to the left half if x is less or equal
            return low  # Return the position where x should be inserted

        # Apply LIS (Longest Increasing Subsequence) on the heights of the envelopes
        lis = []  # List to store the LIS
        for _, h in envelopes:
            idx = binary_search(lis, h)  # Find the position of the height in the LIS
            if idx == len(lis):
                lis.append(h)  # If it's greater than all elements in LIS, append it
            else:
                lis[idx] = h  # Otherwise, replace the element at the found position

        return len(lis)  # The length of the LIS is the maximum number of envelopes that can be nested






# Description:
'''
To solve the "Russian Doll Envelopes" problem, we need to find the maximum number of envelopes 
that can be nested inside each other. This problem is essentially a variation of the Longest 
Increasing Subsequence (LIS) problem, with an additional sorting step.

Here's the approach:
---------------------
    Sort the Envelopes:
        First, sort the envelopes array. Sort by width in ascending order and, if widths are the 
        same, sort by height in descending order. This sorting ensures that when we apply LIS on 
        heights, envelopes with the same width are not considered in sequence.

    Apply Longest Increasing Subsequence (LIS):
        Apply the LIS algorithm on the heights of the sorted envelopes. Since envelopes with the 
        same width are not increasing in height due to the sorting, they won't be counted together 
        in the sequence.

Explanation:
-------------
* Sorting: The sorting step ensures that for envelopes with the same width, only the envelope with 
  the smallest height is considered valid for nesting.
* LIS on Heights: The LIS algorithm is applied to the heights of the envelopes. We use binary search 
  for efficiency, as the traditional LIS has a higher time complexity.
* Result: The length of the LIS corresponds to the maximum number of envelopes that can be nested.

Testing the Solution:
---------------------
    Test Case 1: envelopes = [[5,4],[6,4],[6,7],[2,3]]
        The maximum number of envelopes that can be Russian dolled is 3 ([2,3] => [5,4] => [6,7]).

    Test Case 2: envelopes = [[1,1],[1,1],[1,1]]
        Only one envelope can be used since all others are of the same size. Hence, the maximum number is 1.

        
In this code:
----------------
-   Envelopes are first sorted by width (ascending) and height (descending). This sorting strategy is crucial 
    as it allows us to apply the LIS algorithm on the heights of the envelopes, ensuring that envelopes with 
    the same width aren't counted in the sequence.
-   The LIS algorithm is then applied using a binary search approach. For each height in the sorted envelopes, 
    we find its position in the current LIS sequence. If the height is larger than all elements in the LIS, 
    it's appended to the LIS. Otherwise, it replaces the first element in the LIS that is equal to or larger 
    than it.
-   The length of the LIS represents the maximum number of envelopes that can be nested inside each other.

This solution efficiently solves the problem using sorting and a modified version of the LIS algorithm, 
suitable for large datasets.     


'''    