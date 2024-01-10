"""
# 275. H-Index II

# Topic:Array, Binary Search.

# Task:
----------------------
Given an array of integers citations where citations[i] is the number of citations a researcher 
received for their ith paper and citations is sorted in ascending order, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value 
of h such that the given researcher has published at least h papers that have each been cited at
least h times.

You must write an algorithm that runs in logarithmic time.

Example 1:
Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,2,100]
Output: 2

Constraints:
n == citations.length
1 <= n <= 10^5
0 <= citations[i] <= 1000
citations is sorted in ascending order.

Hint 1:
Expected runtime complexity is in O(log n) and the input is sorted.

# Testcase:
---------------
[0,1,3,5,6]
[1,2,100]


# Code:
---------------
class Solution:
    def hIndex(self, citations: List[int]) -> int:

"""

# Solution:
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # n is the total number of papers
        n = len(citations)
        # Initialize the low and high pointers for binary search
        low, high = 0, n - 1

        # Binary search loop
        while low <= high:
            # Find the middle index
            mid = (low + high) // 2

            # Check if citations at the mid index is equal to n - mid
            # n - mid is the number of papers with citations more than or equal to citations[mid]
            if citations[mid] == n - mid:
                # If it's a match, return citations[mid] as the h-index
                return citations[mid]
            elif citations[mid] < n - mid:
                # If citations[mid] is less, move the search to the right half
                low = mid + 1
            else:
                # If citations[mid] is more, move the search to the left half
                high = mid - 1

        # Return the h-index, which is n - low after exiting the loop
        # This accounts for the case where we don't find an exact match
        return n - low


# Description:
'''
To solve the "H-Index II" problem, we can use a binary search approach, given that 
the array citations is sorted in ascending order and the goal is to achieve logarithmic 
time complexity. The h-index is defined as the maximum value of h such that the researcher 
has published at least h papers that have each been cited at least h times.

Here are the steps for the binary search algorithm:
---------------------------------------------------
    Initialize Search Space: Set the low (low) to 0 and high (high) to the length of the citations array minus one.

    Binary Search: While low is less than or equal to high, do the following:
        Find the middle index (mid) of the current search space.
        Calculate the number of papers that have citations greater than or equal to citations[mid]. This can be done as n - mid, where n is the total number of papers.
        If citations[mid] is equal to n - mid, return citations[mid] as the h-index.
        If citations[mid] is less than n - mid, narrow the search to the right half by setting low to mid + 1.
        Otherwise, narrow the search to the left half by setting high to mid - 1.

    Return Result: The h-index is n - low after the loop finishes.

Testing the Solution:
-----------------------
    Test Case 1: citations = [0,1,3,5,6]
        The researcher has 3 papers with at least 3 citations each, so the h-index is 3.

    Test Case 2: citations = [1,2,100]
        The researcher has 2 papers with at least 2 citations each, so the h-index is 2.

This solution efficiently calculates the h-index using a binary search approach, which is suitable for large datasets due to its logarithmic time complexity.

    
'''
