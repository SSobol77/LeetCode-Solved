# 204. Count Primes.

# Topic: Array, Math, Enumeration, Number Theory.

"""
### Task:
---
Given an integer n, return the number of prime numbers that are strictly less than n. 

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 10^6

Hint 1:
Checking all the integers in the range [1, n - 1] is not efficient. Think about a better approach.
Hint 2:
Since most of the numbers are not primes, we need a fast approach to exclude the non-prime integers.
Hint 3:
Use Sieve of Eratosthenes.

### Testcases:
---
10
0
1

### Code:
---
class Solution:
    def countPrimes(self, n: int) -> int:
        
"""
### Solution: 

class Solution:
    def countPrimes(self, n: int) -> int:
        # Handle edge cases where n is 0 or 1, in which case there are no primes
        if n <= 2:
            return 0

        # Initialize a list to keep track of whether each number is prime.
        # Initially, assume all numbers (except 0 and 1) are prime.
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False  # 0 and 1 are not prime numbers

        # Use Sieve of Eratosthenes to eliminate non-prime numbers
        # Only need to check numbers up to the square root of n
        for i in range(2, int(n**0.5) + 1):
            if isPrime[i]:  # If i is prime
                # Mark all multiples of i as non-prime
                for j in range(i*i, n, i):
                    isPrime[j] = False

        # Count the number of primes by summing the boolean values in isPrime
        # True values (indicating prime numbers) contribute 1 to the sum
        return sum(isPrime)
    

### Description:
'''
In this detailed explanation:
-----------------------------
- We start by handling the edge cases where `n` is 0 or 1. Since there are no prime numbers less than 2, we return 0 in these cases.
- We then initialize a list `isPrime` where each index represents a number, and the value at each index is a boolean indicating whether that number is prime. By default, all numbers are assumed to be prime except for 0 and 1.
- The core of the algorithm is the Sieve of Eratosthenes. We iterate over the numbers starting from 2 up to the square root of `n`. The reason for stopping at the square root is that any non-prime number larger than the square root of `n` will have been marked as non-prime by one of its smaller factors.
- For each prime number `i` we find, we mark all of its multiples (starting from `i*i` to avoid redundant work) as non-prime.
- Finally, we count the prime numbers by summing the boolean values in `isPrime`. In Python, `True` is treated as 1 and `False` as 0 in arithmetic operations, so summing the list gives the count of prime numbers.

This solution efficiently counts the number of primes less than `n` and is particularly effective for large values of `n` within the given constraints.

### Solution Description for "Count Primes"

#### Problem Overview:
The "Count Primes" problem asks for the count of prime numbers that are strictly less than a given integer `n`.

#### Solution Approach:
**Sieve of Eratosthenes Algorithm**: This classic algorithm is an efficient way to find all primes smaller than a given number `n`.

1. **Initialization**:
   - Create a list of boolean values, `isPrime`, indexed from `0` to `n-1`, initially set to `True` for all indices except `0` and `1`, 
     which are set to `False`.

2. **Sieve Process**:
   - Iterate over the numbers starting from `2` to `sqrt(n)`.
   - For each number `i`, if `isPrime[i]` is `True`:
     - Iterate over multiples of `i` (from `i*i` to `n`, incrementing by `i`) and set `isPrime[j]` to `False`. This step marks the 
       multiples of `i` as non-prime.

3. **Count Primes**:
   - Count and return the number of `True` values in the `isPrime` list. This count represents the number of prime numbers less than `n`.


#### Explanation:
- We start by setting all numbers as prime (True). `0` and `1` are explicitly set as non-prime.
- We then iterate through the list, starting from `2`. If a number `i` is prime, we mark all of its multiples as non-prime.
- The outer loop runs only up to the square root of `n` because any non-prime number `n` must have a factor less than or equal to `sqrt(n)`.
- Finally, we count the number of prime numbers by summing the boolean values in `isPrime`.

#### Complexity Analysis:
- **Time Complexity**: O(n log log n) - The sieve algorithm runs in nearly linear time.
- **Space Complexity**: O(n) - We use an additional list of size `n` to keep track of prime numbers.

#### Conclusion:
This solution efficiently counts the number of prime numbers less than `n` using the Sieve of Eratosthenes algorithm. 
It is well-suited for handling large inputs up to `5 * 10^6` as specified in the constraints.

'''