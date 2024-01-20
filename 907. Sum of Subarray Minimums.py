# 907. Sum of Subarray Minimums.

# Topic: Array, Dynamic Programming, Stack, Monotonic Stack.

"""
### Task:
---
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. 
Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444

Constraints:
1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4


### Testcases:
[3,1,2,4]
[11,81,94,43,3]


### Code:
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        
"""
### Solution:  -----------------------------------------------------------------

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7  # Define the modulo value
        n = len(arr)  # Get the length of the array
        PLE = [0] * n  # Initialize Previous Less Element array
        NLE = [0] * n  # Initialize Next Less Element array

        stack = []
        # Iterate over the array to find PLE for each element
        for i in range(n):
            # Pop elements from the stack while they are greater than the current element
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            # The PLE index is the index at the top of the stack or -1 if the stack is empty
            PLE[i] = stack[-1] if stack else -1
            stack.append(i)  # Push the current index onto the stack

        stack = []
        # Reverse iterate over the array to find NLE for each element
        for i in range(n-1, -1, -1):
            # Pop elements from the stack while they are greater or equal to the current element
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            # The NLE index is the index at the top of the stack or n if the stack is empty
            NLE[i] = stack[-1] if stack else n
            stack.append(i)  # Push the current index onto the stack

        # Calculate the sum of subarray minimums
        result = sum((i - PLE[i]) * (NLE[i] - i) * arr[i] for i in range(n)) % MOD

        return result




### Description: ===============================================================
'''
### Explanation:

- **MOD**: This is used for taking modulo 10^9 + 7 as per the problem statement to handle large numbers.
- **n**: Stores the length of the input array.
- **PLE and NLE Arrays**: These arrays are used to store the indices of the previous and next lesser elements for each element in the array.
- **Stack**: A stack is used to efficiently find the PLE and NLE for each element. We maintain the stack such that elements in `arr` corresponding to indices in the stack are in increasing order.
- **Calculating PLE and NLE**: We iterate over the array, updating the PLE and NLE arrays. This involves comparing each element with the elements represented in the stack and updating the stack accordingly.
- **Calculating the Result**: Finally, the sum is calculated using the formula `(i - PLE[i]) * (NLE[i] - i) * arr[i]`, which gives the number of subarrays where `arr[i]` is the minimum, multiplied by the value of `arr[i]`. We take the sum modulo MOD to avoid overflow.


To solve the "Sum of Subarray Minimums" problem, we can utilize a technique called "Monotonic Stack". This approach is 
efficient for finding the next smaller (or greater) elements in an array. The idea is to maintain a stack of indices of 
elements, ensuring that the elements in the array corresponding to these indices are in increasing order.

Here's how the algorithm works for this specific problem:

1. **Initialization**: We create a stack to keep track of indices of array elements. Also, we need two additional arrays 
to store the distance to the previous lesser element (PLE) and the next lesser element (NLE) for each element in the array.

2. **Finding PLE and NLE**: We iterate over the array, and for each element, we pop from the stack until the top of the 
stack is less than the current element. The distance to PLE is the difference between the current index and the index on 
the top of the stack after popping. We do a similar process to find NLE but in a reverse iteration.

3. **Calculate the Sum**: For each element, the number of subarrays where it is the minimum can be calculated 
as `(i - PLE_index) * (NLE_index - i)`. We multiply this with the element value and add it to the sum.

4. **Return the Result**: Since the problem asks for the result modulo 10^9 + 7, we take the modulo at each step to 
avoid overflow.


This solution has a time complexity of O(n) and a space complexity of O(n), as we iterate over the array once and use additional 
arrays and a stack for computation.

'''