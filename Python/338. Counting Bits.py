# 338. Counting Bits.

# Topic: Dynamic Programming, Bit Manipulation.


"""
### Task:
---
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is
the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
0 <= n <= 10^5

Follow up:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n)
and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

Hint 1:
You should make use of what you have produced already.
Hint 2:
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
Hint 3:
Or does the odd/even status of the number help you in calculating the number of 1s?


### Testcase:
---
2
5


### Code:
---
class Solution:
    def countBits(self, n: int) -> List[int]:

"""
### Solution: --------------------------------------

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)  # Initialize the array with zeros
        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + (i % 2)  # Use previous results to compute ans[i]
        return ans


### Description: ===================================
'''
To solve the "Counting Bits" problem, we can use dynamic programming. The idea is to build up an
array `ans` where each `ans[i]` contains the number of 1's in the binary representation of `i`.
We can do this efficiently by realizing that the number of 1's in a number's binary representation
is related to numbers that have already been processed.

Here's a step-by-step approach:

1. **Initialize**: Create an array `ans` of size `n + 1` and initialize `ans[0]` to 0 because 0 has no 1's in
   its binary representation.

2. **Utilize Previous Results**: For each number `i` from 1 to `n`, determine the number of 1's in its binary
   representation. We use the fact that `ans[i] = ans[i // 2] + i % 2`. This works because:

   - `i // 2` is the number `i` shifted right by one bit (essentially `i / 2` if `i` is even, or `(i - 1) / 2` if `i` is odd).
   - `i % 2` is 1 if `i` is odd (which means an extra 1 bit compared to `i // 2`), and 0 if `i` is even.

3. **Return Result**: After filling the `ans` array, return it as the result.

This solution is efficient because it computes the result in a single pass through the numbers from 1 to `n`,
and each computation of `ans[i]` takes constant time. Therefore, the overall time complexity is O(n).

The key to the efficiency is the observation that the number of 1 bits in a binary number is closely related
to the number of 1 bits in half that number, with an adjustment for whether the original number is odd or even.
This allows us to build up the solution iteratively using already computed values, which is a hallmark of
dynamic programming.

'''
