// 70. Climbing Stairs.


// Topic: Math, Dynamic Programming, Memoization.


/*
### Task:
---
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:
1 <= n <= 45

Hint 1:
To reach nth step, what could have been your previous steps? (Think about the step sizes)

### Testcase:
---
2
3


### Code:
---
class Solution {
public:
    int climbStairs(int n) {
        
    }
};

*/

// Solution: --------------------------------------

class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n; // Base cases directly returned

        // Initialize the DP array with the base cases
        vector<int> dp(n + 1);
        dp[0] = 1; // Not used but initialized for completeness
        dp[1] = 1;
        dp[2] = 2;

        // Fill the DP array based on the recurrence relation
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        // The nth entry contains the total number of distinct ways to reach the nth step
        return dp[n];
    }
};


// Description: ===================================
/*
The "Climbing Stairs" problem is a classic example of a dynamic programming question. The intuition behind the solution is that to reach the \(n\)-th step, you could have either come from the \((n-1)\)-th step by taking one step, or from the \((n-2)\)-th step by taking two steps. Therefore, the total number of ways to reach the \(n\)-th step is the sum of the ways to reach the \((n-1)\)-th step and the ways to reach the \((n-2)\)-th step.

This leads to a recursive formula similar to the Fibonacci sequence, where the base cases are:
- 1 way to climb 1 step (just one step),
- 2 ways to climb 2 steps (one step + one step, or just two steps).

### Dynamic Programming Approach:
1. Initialize an array `dp` of size `n + 1` to store the number of ways to reach each step, with `dp[0] = 1` and `dp[1] = 1` for the base cases.
2. Iterate from the 2nd step to the \(n\)-th step, and for each step \(i\), set `dp[i] = dp[i - 1] + dp[i - 2]`, which represents the sum of the ways to get to the current step from the two previous steps.
3. The value at `dp[n]` will give the total number of distinct ways to reach the \(n\)-th step.

### Description:
- **Line 3:** Directly return `n` for the base cases where `n` is 1 or 2, as there are `n` ways to climb `n` steps in these cases (either one step at a time or a single two-step move).
- **Lines 6-8:** Initialize the dynamic programming (DP) array with the base cases. `dp[0]` is set to 1 for mathematical completeness (think of it as the number of ways to stay on the ground).
- **Lines 11-14:** Iterate through the DP array starting from index 3, calculating the number of ways to reach each step based on the sum of the ways to reach the two previous steps.
- **Line 17:** Return the value stored at `dp[n]`, which represents the total number of distinct ways to climb to the \(n\)-th step.

*/
