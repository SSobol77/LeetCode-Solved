# 41. First Missing Positive.       - HARD -

# Topics: Array, Hash Table.

'''
# Task:
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1

Hint 1:
Think about how you would solve the problem in non-constant space. Can you apply that logic to the existing space?
Hint 2:
We don't care about duplicates or non-positive integers
Hint 3:
Remember that O(2n) = O(n)

# Testcase:
[1,2,0]
[3,4,-1,1]
[7,8,9,11,12]

# Code:
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
     
'''
## Solution:

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Place each number in its right place
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Find the first place where nums[i] != i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If no place found, the missing number is n + 1
        return n + 1


## Description:
'''
To solve the problem "First Missing Positive" in O(n) time and O(1) space, we can employ the strategy of placing each number in 
its corresponding position if possible, and then iterating through the array to find the first place where the number doesn't 
match its index. This approach leverages the given array itself for storage to achieve the constant space requirement.

Here's a detailed step-by-step description of the algorithm:

1. **Ignore Non-Positive and Large Values**: First, we ignore any non-positive numbers and numbers larger than the length of 
     the array, as the first missing positive cannot be outside the range `[1, len(nums) + 1]`. This is because in the best-case 
     scenario, the array contains all positive numbers from 1 to `n`.

2. **Place Numbers in Their Correct Positions**: Iterate through the array and for each number `nums[i]`, if it is in the 
     range `[1, len(nums)]` and it is not in its correct position (`nums[i] != nums[nums[i] - 1]`), swap it with the number 
     in its correct position (`nums[nums[i] - 1]`). Repeat this process until every number is either out of range or in its 
     correct position.

3. **Find the First Missing Positive**: After rearranging, iterate through the array again. The first index `i` 
     where `nums[i] != i + 1` gives us the smallest missing positive number, which is `i + 1`. If all numbers are 
     in their correct positions, then the smallest missing positive is `len(nums) + 1`.

4. **Return Result**: Return the first missing positive number found in step 3.


This code respects the constraints of running in O(n) time and using O(1) extra space, as it performs in-place swaps and 
iterates through the array a constant number of times.

'''
