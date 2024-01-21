# 2870. Minimum Number of Operations to Make Array Empty.

# Topic: Array, Hash Table, Greedy, Counting.

"""
# Task:
---------
You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

*  Choose two elements with equal values and delete them from the array.
*  Choose three elements with equal values and delete them from the array.

Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

Example 1:
Input: nums = [2,3,3,2,2,4,2,3,4]
Output: 4
Explanation: We can apply the following operations to make the array empty:
- Apply the first operation on the elements at indices 0 and 3. The resulting array is nums = [3,3,2,4,2,3,4].
- Apply the first operation on the elements at indices 2 and 4. The resulting array is nums = [3,3,4,3,4].
- Apply the second operation on the elements at indices 0, 1, and 3. The resulting array is nums = [4,4].
- Apply the first operation on the elements at indices 0 and 1. The resulting array is nums = [].
It can be shown that we cannot make the array empty in less than 4 operations.

Example 2:
Input: nums = [2,1,2,2,3,3]
Output: -1
Explanation: It is impossible to empty the array.

Constraints:
2 <= nums.length <= 10^5
1 <= nums[i] <= 10^6


# Testcase:
-----------
[2,3,3,2,2,4,2,3,4]
[2,1,2,2,3,3]


# Code:
------------
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
"""
# Solution:
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import Counter

        # Count the frequency of each number in the array
        freq = Counter(nums)
        total_operations = 0

        # Iterate through each unique number's frequency
        for count in freq.values():
            # Initialize the minimum operations for this frequency as infinity
            min_operations = float('inf')

            # Try all possible numbers of triple operations (from 0 to the maximum possible)
            for triples in range((count // 3) + 1):
                # Calculate the remaining count after triple operations
                remaining = count - triples * 3

                # Check if the remaining count can be completely removed by pair operations
                if remaining % 2 == 0:
                    pairs = remaining // 2
                    # Update the minimum operations if this combination is better
                    min_operations = min(min_operations, triples + pairs)

            # If no valid combination of pairs and triples found, return -1
            if min_operations == float('inf'):
                return -1

            # Add the minimum operations for this number to the total operations
            total_operations += min_operations

        # Return the total number of operations required for all numbers
        return total_operations





# Description:
'''
To solve this problem, we need to efficiently utilize both types of operations (pair and triplet deletions) 
to minimize the total number of operations. The key challenge is to determine the optimal mix of these 
operations for different counts of the same number.

Given the nature of the problem, a greedy approach might not always yield the correct solution, as it may 
not consider the optimal sequence of operations for each number. Instead, we should explore a more analytical 
approach that carefully evaluates the combination of operations based on the counts of each number.

Let's re-evaluate the approach with these considerations:

1.Count Frequencies: Continue using a hash table to count the occurrences of each number.

2.Analyze Each Number's Frequency:
  - If the frequency is divisible by 2, we can pair all occurrences.
  - If the frequency is divisible by 3, we can triple all occurrences.
  - If the frequency is not divisible by 2 or 3, we need to find the optimal combination of pair and 
    triple operations.

3.Calculate Operations for Each Frequency:
  For each frequency, calculate the minimum number of operations by considering all possible combinations 
  of pair and triple operations that sum up to that frequency.

4.Aggregate Total Operations:
  Sum the calculated operations for each frequency to get the total number of operations.

5.Handle Impossible Cases:
  If there are any frequencies for which no combination of operations can make them zero, return -1.


This commented code outlines the logic for calculating the minimum number of operations needed to empty 
the array using the given rules. It iteratively calculates the optimal mix of pair and triple deletions 
for each unique number in the array. If it finds a number that cannot be entirely removed by the allowed 
operations, it returns -1, indicating that emptying the array is impossible.

'''
