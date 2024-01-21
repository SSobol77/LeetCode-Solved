"""
# 287. Find the Duplicate Number.

# Topic: Array, Two Pointers, Binary Search, Bit Manipulation.

# Task:
--------
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Constraints:
1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 
Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?


# Testcase:
-----------
[1,3,4,2,2]
[3,1,3,4,2]


# Code:
----------
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

"""
# Solution:
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize the tortoise and hare pointers at the first element
        tortoise = hare = nums[0]
        
        # Phase 1: Finding the intersection point of the two runners in the cycle.
        # Tortoise moves one step, hare moves two steps.
        while True:
            tortoise = nums[tortoise]  # Move tortoise by one step
            hare = nums[nums[hare]]    # Move hare by two steps
            if tortoise == hare:       # Check if they meet
                break

        # Phase 2: Finding the entrance to the cycle, which is the duplicate number.
        # Reset tortoise to the start of the array.
        tortoise = nums[0]
        # Move both pointers one step at a time until they meet.
        # The meeting point is the duplicate number.
        while tortoise != hare:
            tortoise = nums[tortoise]  # Move tortoise by one step
            hare = nums[hare]          # Move hare by one step

        # The duplicate number is found where tortoise and hare meet.
        return hare


# Description:
'''
To solve this problem, we can use Floyd's Tortoise and Hare (Cycle Detection) algorithm. This approach is based on the fact 
that duplicate numbers in the array create a cycle. We can think of the array values as pointers to the next index. 
For example, if nums[0] = 3, it points to index 3.

The algorithm involves two pointers, the slow pointer (tortoise) and the fast pointer (hare). Initially, both pointers start 
at the first index of the array. In each step, the tortoise moves one step (i.e., tortoise = nums[tortoise]), and the hare 
moves two steps (i.e., hare = nums[nums[hare]]). If there is a cycle, the hare and tortoise will meet at some point inside 
the cycle.

Once they meet, we keep the hare at the meeting point and move the tortoise back to the start. Then, we move both the hare 
and the tortoise one step at a time. The point at which they meet again is the start of the cycle, which in this case, is 
the duplicate number.

Here's the step-by-step implementation:

1. Initialize two pointers, tortoise and hare, both at the first index.
2. Move tortoise by one step and hare by two steps until they meet.
3. Once they meet, reset tortoise to the first index.
4. Move both tortoise and hare one step at a time until they meet again.
5. The meeting point now is the duplicate number.

In this code:

* We first find the intersection point within the cycle. Since a duplicate number exists, a cycle must exist in the sequence 
  formed by following the indices as pointed out by the array's values.
* The while loop continues until the tortoise and hare meet, which is guaranteed to happen within the cycle.
* After finding the intersection point, we reset one of the pointers to the start of the array.
* We then move both pointers one step at a time. The point at which they meet again is the start of the cycle and hence the 
  duplicate number.
* This solution leverages Floyd's Tortoise and Hare algorithm for cycle detection, commonly used in linked lists but applied 
  here in the array context.

This solution is efficient with time complexity O(n) and space complexity O(1), adhering to the constraints of the problem.

'''