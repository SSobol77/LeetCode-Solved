// 231. Power of Two.


// Topic: Math, Bit Manipulation, Recursion.


/*
### Task:
---
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false

Constraints:
-2^31 <= n <= 2^31 - 1


### Testcase:
---
1
16
3


### Code:
---
class Solution {
public:
    bool isPowerOfTwo(int n) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    bool isPowerOfTwo(int n) {
        // Check if n is positive and if n & (n-1) is 0
        return n > 0 && (n & (n - 1)) == 0;
    }
};


// Description: ===================================
/*
To solve the "Power of Two" problem, we need to determine if the given integer `n` is a power of two. This means we need to check if there exists an integer `x` such that `n == 2^x`. There are several ways to approach this problem, including mathematical, bit manipulation, and recursion methods. Here, I'll provide a solution using bit manipulation, which is efficient and concise.

### Bit Manipulation Approach:
A number `n` is a power of two if it has exactly one bit set in its binary representation. For example, `2` (`10` in binary), `4` (`100` in binary), and `8` (`1000` in binary) are powers of two. We can use this property to determine if a number is a power of two.

One characteristic of a power of two in binary form is that it is a single `1` bit followed by `0` bits. If we subtract `1` from such a number, we flip all the bits after the `1` bit, including the `1` bit itself, resulting in a binary number with all `1`s up to the position of the original `1` bit. For example, `4` (`100` in binary) minus `1` equals `3` (`011` in binary).

If we `AND` a power of two and the number one less than it, we should get `0`. This is because there are no bits in common. For example, `4 & 3` (`100 & 011`) equals `0`.

However, we need to be careful with the case when `n` is non-positive. Powers of two are always positive, so we should return `false` for non-positive numbers.

### Explanation:
- `n > 0` ensures that `n` is positive, as powers of two cannot be zero or negative.
- `(n & (n - 1)) == 0` checks if `n` has exactly one `1` bit in its binary representation, indicating it is a power of two.

This solution is efficient because it performs a constant number of operations regardless of the size of `n`.

*/
