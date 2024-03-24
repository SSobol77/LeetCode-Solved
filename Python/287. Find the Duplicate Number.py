# 287. Find the Duplicate Number.

# Topics: Array, Two Pointers, Binary Search, Bit Manipulation.

'''
## Task:
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3
 
Constraints:
1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?

## Testcase:
[1,3,4,2,2]
[3,1,3,4,2]
[3,3,3,3,3]

## Code:
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
'''
## Solution:
from typing import List  # Import List from the typing module

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Finding the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]  # Moves by 1 step
            hare = nums[nums[hare]]    # Moves by 2 steps
            if tortoise == hare:
                break  # A cycle has been detected

        # Phase 2: Finding the "entrance" to the cycle.
        tortoise = nums[0]  # Reset tortoise to the start
        while tortoise != hare:
            tortoise = nums[tortoise]  # Moves by 1 step
            hare = nums[hare]          # Also moves by 1 step

        # The point where they meet is the entrance to the cycle, which is the duplicate number.
        return hare


## Description:
'''
To solve the problem of finding the duplicate number in an array with certain constraints (without modifying the array and using constant extra space), we can apply the Floyd's Tortoise and Hare (Cycle Detection) algorithm. This approach is particularly efficient as it adheres to the constraints and achieves linear runtime complexity.

### Floyd's Tortoise and Hare (Cycle Detection):

The key insight is to treat the array like a linked list where each element points to the next element's index. Given the constraints, there's a cycle in this "list" because of the duplicate number. We use two pointers, a slow one (tortoise) moving one step at a time, and a fast one (hare) moving two steps at a time. The duplicate number is the entry point of the cycle.

1. **Initialization**: Start both the tortoise and hare at the first element of the array.
2. **Phase 1 - Detecting the Cycle**: Move the tortoise by one step and the hare by two steps until they meet inside the cycle, which guarantees that a cycle exists.
3. **Phase 2 - Finding the Entrance to the Cycle**: Reset the tortoise to the beginning of the list. Keep the hare at the meeting point and change its step size to one. Move both tortoise and hare one step at a time until they meet again; the meeting point is the duplicate number (entrance to the cycle).

### Explanation:
- **Phase 1**: We use a slow pointer (tortoise) and a fast pointer (hare) to find a point inside the cycle. The cycle exists because there's a duplicate number, causing at least one number to point to an index already pointed to by another number.
- **Phase 2**: To find the duplicate number, we reset one pointer to the start and keep the other at the meeting point from phase 1. We then move both one step at a time; the point where they meet again is the duplicate number.

### Follow Up Answers:
- **Proving the Existence of a Duplicate**: The pigeonhole principle guarantees a duplicate because there are `n + 1` numbers (the pigeons) and `n` distinct possible values (the pigeonholes). Therefore, at least one value must be duplicated.
- **Linear Runtime Complexity**: The Floyd's Tortoise and Hare algorithm runs in O(n) time, which meets the requirement for linear runtime complexity. The space complexity is O(1) since we only use two pointers regardless of the input size.

'''
