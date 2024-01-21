# 15. 3Sum.            - Medium -

# Topic: Array, Two Pointers, Sorting.

"""
### Task:
---
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

Hint 1
So, we essentially need to find three numbers x, y, and z such that they add up to the given value. 
If we fix one of the numbers say x, we are left with the two-sum problem at hand!
Hint 2
For the two-sum problem, if we fix one of the numbers, say x, we have to scan the entire array to find 
the next number y, which is value - x where value is the input parameter. Can we change our array somehow 
so that this search becomes faster?
Hint 3
The second train of thought for two-sum is, without changing the array, can we use additional space somehow? 
Like maybe a hash map to speed up the search?


### Testcase:
---
[-1,0,1,2,-1,-4]
[0,1,1]
[0,0,0]

### Code:
---
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
"""
### Solution: -----------------------------------------------------
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # First, sort the array to make two-pointer scanning efficient.
        nums.sort()
        result = []

        # Iterate through the array, fixing one element at a time.
        for i in range(len(nums) - 2):
            # Skip over duplicate values to avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers: one just after the current element, and the other at the end of the array.
            left, right = i + 1, len(nums) - 1
            while left < right:
                # Calculate the sum of the current triplet.
                total = nums[i] + nums[left] + nums[right]

                # If the sum is less than zero, move the left pointer to the right to increase the sum.
                if total < 0:
                    left += 1
                # If the sum is greater than zero, move the right pointer to the left to decrease the sum.
                elif total > 0:
                    right -= 1
                # If the sum is zero, add the triplet to the result list.
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip over duplicate values to the right of the left pointer.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip over duplicate values to the left of the right pointer.
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # Move both pointers for the next potential pair.
                    left += 1
                    right -= 1

        # Return the list of triplets that sum up to zero.
        return result


### Description: --------------------------------------------------
'''
The "3Sum" problem is a popular one in algorithmic interviews, often testing one's ability to manipulate arrays and use 
two-pointers efficiently. Let's break down the problem and then provide a solution.

### Problem Analysis:
The goal is to find all unique triplets in an array that add up to zero. The key challenges are:
1. **Avoiding Duplicates**: Ensuring that the solution set does not contain duplicate triplets.
2. **Efficiency**: The solution must be efficient enough to handle arrays with up to 3000 elements.

### Approach:
1. **Sort the Array**: First, sort the array. This makes it easier to avoid duplicates and use the two-pointer technique.
2. **Iterate with a Fixed Element**: Use a loop to fix one element at a time. For each fixed element, use the two-pointer
     approach to find pairs that sum up to the negative of the fixed element.
3. **Two-Pointer Technique**: For the remaining part of the array, use two pointers - one starting just after the fixed 
     element and the other at the end of the array. Move these pointers to find pairs that sum up to the required value.
4. **Avoid Duplicates**: Skip over duplicate values to avoid duplicate triplets in the result.

### Explanation:
- **Sorting**: Sorting the array allows for efficient two-pointer scanning.
- **Fixed Element**: By fixing one element, the problem is reduced to a two-sum problem.
- **Two-Pointer**: The two-pointer method is used to find pairs that sum up to the negative of the fixed element.
- **Avoiding Duplicates**: Skip over elements that are the same as the previous one to avoid considering the same triplet again.

### Time Complexity:
- The sorting of the array takes O(n log n) time.
- The outer loop runs in O(n), and the inner two-pointer scan in O(n)

 in the worst case. So, the overall time complexity is O(n^2), which is acceptable given the problem constraints.

### Examples:
1. `nums = [-1, 0, 1, 2, -1, -4]`
   - Sorted array: `[-4, -1, -1, 0, 1, 2]`
   - The algorithm finds triplets `[-1, -1, 2]` and `[-1, 0, 1]`.

2. `nums = [0, 1, 1]`
   - Sorted array: `[0, 1, 1]`
   - No triplet adds up to 0.

3. `nums = [0, 0, 0]`
   - Sorted array: `[0, 0, 0]`
   - The only triplet `[0, 0, 0]` adds up to 0.

This solution effectively handles the requirements of the problem, providing a way to find all unique triplets that sum up to 
zero in an efficient manner.

'''