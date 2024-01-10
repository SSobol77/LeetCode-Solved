"""
# 1498. Number of Subsequences That Satisfy the Given Sum Condition

# Topic: Array, Two Pointers, Binary Search, Sorting.


# Task:
---------------
You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum 
element on it is less or equal to target. Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

Example 2:
Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

Example 3:
Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= target <= 10^6


Hint 1:
Sort the array nums.

Hint 2:
Use two pointers approach: Given an index i (choose it as the minimum in a subsequence) find 
the maximum j where j ≥ i and nums[i] +nums[j] ≤ target.

Hint 3:
Count the number of subsequences.



# Testcase:
-----------------
[3,5,6,7]
9
[3,3,6,8]
10
[2,3,3,4,6,7]
12


# Code:
-----------------
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
     
"""
# Solution:
class Solution:
    MOD = 10**9 + 7  # Modulo constant for large numbers

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array for two pointers approach
        left, right = 0, len(nums) - 1
        result = 0
        pow2 = [1] * (len(nums))  # Array to store powers of 2 for efficiency

        # Precompute powers of 2 up to len(nums)
        for i in range(1, len(nums)):
            pow2[i] = pow2[i - 1] * 2 % self.MOD

        # Iterate using two pointers
        while left <= right:
            if nums[left] + nums[right] <= target:
                # If sum of min and max in current subsequence is less than or equal to target
                # Add the number of subsequences that can be formed
                # Count is 2^(right - left), which is the number of ways to choose elements between left and right
                result += pow2[right - left]
                result %= self.MOD  # Apply modulo to handle large numbers
                left += 1  # Move left pointer to consider the next subsequence
            else:
                right -= 1  # Move right pointer to reduce the sum

        return result

# Description:
'''
To solve the problem "Number of Subsequences That Satisfy the Given Sum Condition," we need 
to count the number of non-empty subsequences in an array nums such that the sum of the minimum 
and maximum elements in each subsequence is less than or equal to a given target. The key here 
is to use sorting and a two-pointers approach.

Here's the step-by-step approach:
------------------------------------------
    Sort the Array: Sort nums in non-decreasing order.

    Use Two Pointers:
        Initialize two pointers: left at the start and right at the end of the array.
        For each left, find the maximum right such that nums[left] + nums[right] <= target.

    Count Subsequences:
        For each valid pair of left and right, count the number of subsequences that can be formed.
        The number of subsequences formed by elements between left and right is 2^(right - left), as 
        each element can either be included or excluded.

    Return the Result:
        Return the total count modulo 10^9 + 7, as the answer might be large.

Testing the Solution:
-----------------------
    Test Case 1: nums = [3,5,6,7], target = 9
        The valid subsequences are [3], [3,5], [3,5,6], and [3,6]. Hence, the output is 4.

    Test Case 2: nums = [3,3,6,8], target = 10
        The valid subsequences include [3], [3,3], [3,6], etc. The output is 6.

    Test Case 3: nums = [2,3,3,4,6,7], target = 12
        There are multiple valid subsequences. The output is 61.

This code first sorts the array nums and then applies a two-pointers approach. For each pair of left 
and right pointers, where nums[left] is the minimum and nums[right] is the maximum of the subsequence, 
it calculates the number of valid subsequences if their sum is less than or equal to target. The number 
of subsequences between two pointers is given by 2^(right - left), representing the binary choice 
(include or exclude) for each element in the range. The use of modulo (10^9 + 7) ensures that the result 
stays within integer limits even for large numbers. Precomputing powers of 2 improves the efficiency of 
the solution, especially for large arrays.

This solution efficiently calculates the number of valid subsequences using a sorted array, a two-pointers 
approach, and precomputed powers of 2, ensuring optimal performance for large datasets.

'''
