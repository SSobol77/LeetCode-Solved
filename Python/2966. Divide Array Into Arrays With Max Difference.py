# 2966. Divide Array Into Arrays With Max Difference.


# Topic: Array, Greedy, Sorting

"""
### Task:
---
You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following conditions:

Each element of nums should be in exactly one array.
The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. 
And if there are multiple answers, return any of them.

Example 1:
Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
Output: [[1,1,3],[3,4,5],[7,8,9]]
Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
The difference between any two elements in each array is less than or equal to 2.
Note that the order of elements is not important.

Example 2:
Input: nums = [1,3,3,2,7,3], k = 3
Output: []
Explanation: It is not possible to divide the array satisfying all the conditions.
 
Constraints:
n == nums.length
1 <= n <= 10^5
n is a multiple of 3.
1 <= nums[i] <= 10^5
1 <= k <= 10^5

Hint 1:
Try to use a greedy approach.
Hint 2:
Sort the array and try to group each 3 consecutive elements.


### Testcase:
---
[1,3,4,8,7,9,3,5,1]
2
[1,3,3,2,7,3]
3


### Code:
---
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        


"""
### Solution: --------------------------------------

from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Step 1: Sort the array
        nums.sort()
        
        result = []
        for i in range(0, len(nums), 3):
            # Step 2: Divide the sorted array into chunks of size 3
            chunk = nums[i:i+3]
            
            # Step 3: Check the difference condition for the current chunk
            if max(chunk) - min(chunk) > k:
                # If the condition is not met, return an empty array
                return []
            
            # Add the valid chunk to the result
            result.append(chunk)
        
        # Step 4: Return the result
        return result

# Test cases
solution = Solution()
print(solution.divideArray([1,3,4,8,7,9,3,5,1], 2))  # Expected: [[1, 1, 3], [3, 4, 5], [7, 8, 9]] or any other valid division
print(solution.divideArray([1,3,3,2,7,3], 3))  # Expected: []


### Description: ===================================
'''
To solve this task, we can follow a greedy approach as hinted. The key idea is to sort the array first, which allows us 
to easily check if we can form arrays of size 3 with elements whose differences are less than or equal to `k`. 
By sorting, we ensure that elements that are close to each other in value are also close in position, making it easier to 
group them while satisfying the condition on the maximum difference.

Here's a step-by-step breakdown of the approach:

1. **Sort the array:** This will group elements closer in value together.
2. **Divide the array into chunks of size 3:** Starting from the beginning of the sorted array, create sub-arrays of size 3.
3. **Check the difference condition:** For each sub-array, check if the maximum difference between any two elements is less 
     than or equal to `k`. If this condition is not met for any sub-array, it means it's impossible to divide the array as required, so we return an empty array.
4. **Return the result:** If all sub-arrays meet the condition, return the list of these sub-arrays.



This code defines the `divideArray` method within the `Solution` class, which takes a list of integers `nums` and an integer `k`, 
and returns a 2D list according to the specified conditions. Remember, the output can have multiple correct answers due to the 
nature of the problem (the order of elements in sub-arrays or the order of sub-arrays themselves is not strictly defined), so your 
actual output might vary as long as it satisfies the problem's conditions.

'''
