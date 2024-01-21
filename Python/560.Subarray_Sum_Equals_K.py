"""
# 560. Subarray Sum Equals K.

# Topic: Array, Hash Table, Prefix Sum.

# Task:
--------
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7

Hint 1:
Will Brute force work here? Try to optimize it.

Hint 2:
Can we optimize it by using some extra space?

Hint 3:
What about storing sum frequencies in a hash table? Will it be useful?

Hint 4:
sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.


# Testcase:
------------
[1,1,1]
2
[1,2,3]
3

# Code:
-------------
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       
"""
# Solution:
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Hash table to store frequency of cumulative sums
        sum_frequency = {0: 1}
        cumulative_sum = 0
        count = 0

        # Iterate over the array
        for num in nums:
            # Update the cumulative sum
            cumulative_sum += num

            # If (cumulative sum - k) is in the hash table, it contributes to the count
            count += sum_frequency.get(cumulative_sum - k, 0)

            # Update the frequency of the cumulative sum in the hash table
            sum_frequency[cumulative_sum] = sum_frequency.get(cumulative_sum, 0) + 1

        return count


# Description:
'''
To solve the "Subarray Sum Equals K" problem, we can use the concept of prefix sum along with a hash table. 
The key idea is to keep track of the cumulative sum of the elements of the array and the frequency of each 
sum encountered. This method leverages the fact that the sum of a subarray (i, j] can be calculated 
as prefixSum[j] - prefixSum[i].

Here's a step-by-step approach:
----------------------------------
1. Initialize Variables: Create a hash table to store the frequency of cumulative sums. Initialize it with {0: 1} to 
   handle the case where the cumulative sum equals k itself. Also, initialize a variable to keep track of the cumulative 
   sum and a counter for the number of subarrays that sum up to k.

2. Iterate Over the Array:
   - For each element in the array, add it to the cumulative sum.
   - Check if (cumulative sum - k) is in the hash table. If it is, it means there are subarrays ending at the current 
     index which sum up to k. Add the frequency of (cumulative sum - k) from the hash table to the count.
   - Update the hash table with the new cumulative sum.

3. Return the Count: The count variable will have the total number of subarrays whose sum equals k.

    
In this solution:
-------------------

*    We maintain a hash table sum_frequency to store the frequency of each cumulative sum encountered.

*    As we iterate through the array, we update the cumulative sum and check how many times we have seen 
     a cumulative sum that is k less than the current sum. Each occurrence indicates a subarray summing up to k.

*    Finally, count will hold the total number of such subarrays. This approach efficiently solves the problem
     with a time complexity of O(n) and a space complexity of O(n).

'''
