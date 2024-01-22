# 645. Set Mismatch.

# Topic: Array, Hash Table, Bit Manipulation, Sorting.

"""
### Task:
---
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, 
one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss 
of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]
 
Constraints:
2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4


### Testcase:
---
[1,2,2,4]
[1,1]


### Code:
---
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
"""
### Solution: --------------------------------------------

class Solution:
    def findErrorNums(self, nums):
        # Initialize a dictionary to store the frequency of each number
        freq_dict = {}

        # Initialize variables to store the duplicated and missing numbers
        dup = -1
        missing = 1

        # Count the frequency of each number in the nums array
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        # Iterate through the range from 1 to n
        for i in range(1, len(nums) + 1):
            if i in freq_dict:
                # If the frequency is 2, we found the duplicated number
                if freq_dict[i] == 2:
                    dup = i
            else:
                # If the number is not in the dictionary, it's the missing number
                missing = i

        return [dup, missing]

# Test cases
sol = Solution()
print(sol.findErrorNums([1,2,2,4]))  # Output: [2,3]
print(sol.findErrorNums([1,1]))      # Output: [1,2]




### Desription: =========================================================================================
'''
To solve this problem, we can use a hash table to keep track of the frequency of each number in the array. 
The number that appears twice will have a frequency of 2, and the missing number will be the one that doesn't 
appear in the hash table. Since the original set contains all the numbers from 1 to n, we can iterate through 
this range to find the missing number.

This solution iterates through the list once to build the frequency dictionary and then iterates through the 
range from 1 to n, resulting in a time complexity of O(n) and a space complexity of O(n), where n is the length 
of the input array.
'''
