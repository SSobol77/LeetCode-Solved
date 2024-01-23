# 2366. Minimum Replacements to Sort the Array.         - HARD -


# Topic: Array, Math, Greedy.

"""
### Task:
---
You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any
two elements that sum to it.

For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
Return the minimum number of operations to make an array that is sorted in non-decreasing order.

Example 1:
Input: nums = [3,9,3]
Output: 2
Explanation: Here are the steps to sort the array in non-decreasing order:
- From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
- From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 0
Explanation: The array is already in non-decreasing order. Therefore, we return 0.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9

Hint 1:
It is optimal to never make an operation to the last element of the array.
Hint 2:
You can iterate from the second last element to the first. If the current value is greater than the previous bound,
we want to break it into pieces so that the smaller one is as large as possible but not larger than the previous one.


### Testcase:
---
[3,9,3]
[1,2,3,4,5]


### Code:
---
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

"""
### Solution: --------------------------------------

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        # Start with the last element as the initial upper bound
        upper_bound = nums[-1]

        # Iterate from the second last element to the first
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > upper_bound:
                # Calculate how many pieces we can break nums[i] into
                # The pieces should be as large as possible but not larger than upper_bound
                pieces = (nums[i] + upper_bound - 1) // upper_bound
                operations += (pieces - 1)  # Minus 1 as the element itself counts as one piece
                upper_bound = nums[i] // pieces
            else:
                # Update the upper bound if the current element is smaller
                upper_bound = nums[i]

        return operations

# Test cases
sol = Solution()
print(sol.minimumReplacement([3,9,3]))  # Output: 2
print(sol.minimumReplacement([1,2,3,4,5]))  # Output: 0


### Description: ===================================
'''
To solve this problem, we can use a greedy algorithm. The goal is to minimize the number of operations needed to make the array non-decreasing. The key insight is that we should try to make the larger numbers in the array as close as possible to the smaller numbers preceding them without exceeding them. This is because each operation can break a number into two parts, and we want to minimize how many times we need to do this.

Given the hints, we can iterate from the second last element to the first (in reverse order) and adjust each number if it's greater than the one following it.

### Steps:

1. Start from the second last element of the array and move backwards.
2. For each element, if it is greater than the next element (which acts as a current upper bound), we need to break it down.
3. To minimize operations, we want to break it into the largest possible pieces that do not exceed the upper bound.
4. The number of operations needed for each element is determined by how many times you can fit the upper bound into it (with some adjustments to handle remainders).
5. Update the total number of operations and adjust the upper bound for the next iteration.

### Explanation:
- The algorithm starts from the end of the array and moves backwards.
- For each element, if it is greater than the current upper bound (the next element in the original array), it is divided into the maximum number of pieces that do not exceed the upper bound.
- The number of operations for each element is the number of pieces minus one.
- Finally, the total number of operations is returned.



'''
