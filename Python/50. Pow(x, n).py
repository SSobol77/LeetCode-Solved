# 50. Pow(x, n)

# Topic:

'''
# Task:
-------
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:

-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
n is an integer.
Either x is not zero or n > 0.
-10^4 <= xn <= 10^4


# Testcase:
-----------
2.00000
10
2.10000
3
2.00000
-2


# Code:
-------
class Solution:
    def myPow(self, x: float, n: int) -> float:

'''
# Solution:
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Function to efficiently compute power
        def fastPow(value, power):
            if power == 0:
                return 1
            half = fastPow(value, power // 2)
            if power % 2 == 0:
                return half * half  # When power is even
            else:
                return half * half * value  # When power is odd

        # Handling negative powers
        result = fastPow(x, abs(n))
        return result if n >= 0 else 1 / result

# Test cases
solution = Solution()
print(solution.myPow(2.00000, 10))  # Expected output: 1024.00000
print(solution.myPow(2.10000, 3))   # Expected output: 9.26100
print(solution.myPow(2.00000, -2))  # Expected output: 0.25000


'''
Description:
To implement the pow(x, n) function efficiently, we can use the fast exponentiation algorithm, 
also known as binary exponentiation. This method reduces the number of multiplications needed 
by exploiting the property

'''