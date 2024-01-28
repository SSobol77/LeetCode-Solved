// 1359. Count All Valid Pickup and Delivery Options.

// Topics: Math, Dynamic Programming, Combinatorics.

/*
# Task:
Given n orders, each order consists of a pickup and a delivery service.
Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

Example 2:
Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

Example 3:
Input: n = 3
Output: 90

Constraints:
1 <= n <= 500

Hint 1
Use the permutation and combination theory to add one (P, D) pair each time until n pairs.

# Testcase:
1
2
3

# Code:
class Solution {
public:
    int countOrders(int n) {
        
    }
};

*/
// Solution:
class Solution {
public:
    int countOrders(int n) {
        const int MOD = 1000000007; // Define the modulo constant
        
        long long result = 1; // Initialize the result variable to 1
        
        // Iterate from n=1 to n
        for (int i = 1; i <= n; i++) {
            // Calculate the number of valid pickup and delivery options for n using a formula
            // Formula: result = result * (2 * i - 1) * i
            // This formula is based on permutation and combination theory
            // It counts the valid sequences for the current n by multiplying with (2n-1) and n
            result = (result * (2 * i - 1) * i) % MOD; // Use modular arithmetic to prevent overflow
        }
        
        return static_cast<int>(result); // Convert and return the result as an integer
    }
};


// Description:
/*
Certainly! Here's a detailed algorithm description for the corrected solution to the "Count All Valid Pickup and Delivery Options" problem:

**Algorithm Description:**

1. Define a constant `MOD` with a value of 1000000007 to represent the modulo operation.

2. Initialize a variable `result` to 1. This variable will be used to keep track of the total number of valid pickup and delivery sequences.

3. Loop from `i = 1` to `n`, where `n` represents the number of orders:

   - For each `i`, calculate the number of valid pickup and delivery sequences for the current `i` using the following formula:
   
     ```
     result = result * (2 * i - 1) * i
     ```
     
     This formula is based on the principles of permutation and combination. It calculates the number of valid sequences for the current `i` by multiplying the previous result by `(2 * i - 1)` and `i`.
   
   - Use modular arithmetic by taking the result modulo `MOD` to prevent potential integer overflow.

4. After the loop completes, the `result` variable contains the total number of valid pickup and delivery sequences for `n` orders.

5. Return the `result` as an integer.

**Complexity Analysis:**

- Time Complexity: The algorithm has a time complexity of O(n) since it loops through the values from 1 to `n`.
- Space Complexity: The algorithm has a space complexity of O(1) as it uses a constant amount of memory.

This algorithm efficiently counts all valid pickup and delivery sequences for the given number of orders `n` and provides the result modulo 10^9 + 7, as required by the problem statement.
*/