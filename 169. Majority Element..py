# 169. Majority Element.          -Easy-

# Topic: Array, Hash Table, Divide and Conquer, Sorting, Counting.

"""
### Task:
---
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority 
element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9

Follow-up: Could you solve the problem in linear time and in O(1) space?


### Testcase:
---
[3,2,3]
[2,2,1,1,1,2,2]


### Code:
---
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

"""
### Solution: -------------------------------------

class Solution:
    def majorityElement(self, nums):
        # Initialize the candidate for the majority element and a counter
        candidate, count = None, 0

        for num in nums:
            # If the count is zero, we select the current element as our new candidate
            if count == 0:
                candidate = num
            # If the current element is the candidate, increment the count
            # Otherwise, decrement the count
            count += (1 if num == candidate else -1)

        # The candidate at the end is the majority element
        return candidate

# Testing the function
sol = Solution()
test_case_1 = [3, 2, 3]
test_case_2 = [2, 2, 1, 1, 1, 2, 2]

output_1 = sol.majorityElement(test_case_1)
output_2 = sol.majorityElement(test_case_2)

output_1, output_2


### Description: ===================================
'''

The "Majority Element" problem asks to find the element in an array that appears more than ⌊n / 2⌋ times, 
where n is the size of the array. A popular and efficient way to solve this problem in linear time and with 
constant space is using the Boyer-Moore Voting Algorithm.

### Boyer-Moore Voting Algorithm:
1. **Initialization**: Start with an initial candidate and a counter set to 0.
2. **Iterate Through the Array**:
   - If the counter is 0, choose the current element as the new candidate.
   - If the current element is the same as the candidate, increment the counter.
   - Otherwise, decrement the counter.
3. **Result**: The candidate at the end of the array is the majority element. This works because the majority element 
   is guaranteed to have more occurrences than all other elements combined.


### Explanation:
- The algorithm maintains a candidate for the majority element and a counter.
- Each time it finds an element equal to the candidate, it increments the counter.
- If it finds an element different from the candidate, it decrements the counter.
- When the counter reaches 0, it picks a new candidate from the current position in the array.
- Since the majority element appears more than ⌊n / 2⌋ times, it will always be the final candidate.

This approach has a time complexity of O(n) and a space complexity of O(1), fulfilling the follow-up challenge.

Let's execute the code to test the provided examples.

The implemented solution correctly identifies the majority element for the given test cases:

1. For the input `[3, 2, 3]`, the output is `3`. This is correct as `3` appears more than ⌊3 / 2⌋ = 1 times in the array.

2. For the input `[2, 2, 1, 1, 1, 2, 2]`, the output is `2`. This is also correct as `2` appears more than ⌊7 / 2⌋ = 3 times in the array.


### Explanation of Comments:
- **Initialization**: We start with no candidate and a counter set to 0.
- **Choosing a New Candidate**: When the count becomes zero, it means the previous candidate is not the majority. 
    Hence, we choose the current element as the new candidate.
- **Updating the Count**: If the current element is the same as our candidate, we increase the count as it's likely 
    to be the majority. If it's different, we decrease the count.
- **Final Candidate**: The algorithm ensures that the final candidate is the majority element due to its frequency in the array. 

This approach ensures that the majority element, which appears more than half the time in the array, is always selected as the 
final candidate. The comments added provide clarity on how the Boyer-Moore Voting Algorithm works in this context.

The Boyer-Moore Voting Algorithm efficiently finds the majority element in O(n) time and O(1) space, satisfying 
the problem's constraints and the follow-up challenge.

'''
