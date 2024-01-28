// 3021. Alice and Bob Playing Flower Game.

/*
### Task:
---
Alice and Bob are playing a turn-based game on a circular field surrounded by flowers. The circle represents the field, and there are x flowers in the clockwise direction between Alice and Bob, and y flowers in the anti-clockwise direction between them.

The game proceeds as follows:

Alice takes the first turn.
In each turn, a player must choose either the clockwise or anti-clockwise direction and pick one flower from that side.
At the end of the turn, if there are no flowers left at all, the current player captures their opponent and wins the game.
Given two integers, n and m, the task is to compute the number of possible pairs (x, y) that satisfy the conditions:

Alice must win the game according to the described rules.
The number of flowers x in the clockwise direction must be in the range [1,n].
The number of flowers y in the anti-clockwise direction must be in the range [1,m].
Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.

Example 1:
Input: n = 3, m = 2
Output: 3
Explanation: The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).

Example 2:
Input: n = 1, m = 1
Output: 0
Explanation: No pairs satisfy the conditions described in the statement.

Constraints:
1 <= n, m <= 10^5

Hint 1:
(x, y) is valid if and only if they have different parities.


### Testcase:
---
3
2
1
1


### Code:
---
class Solution {
public:
    long long flowerGame(int n, int m) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    long long flowerGame(int n, int m) {
        // Count of odd numbers in [1, n] and even numbers in [1, m]
        long long odd_n = (n + 1) / 2;
        long long even_m = m / 2;

        // Count of even numbers in [1, n] and odd numbers in [1, m]
        long long even_n = n / 2;
        long long odd_m = (m + 1) / 2;

        // Total valid pairs = (odd in n * even in m) + (even in n * odd in m)
        return (odd_n * even_m) + (even_n * odd_m);
    }
};


// Description: ===================================
/*
For the described flower game between Alice and Bob, the key to determining the number of valid `(x, y)` pairs where Alice always wins lies in understanding the parity of `x` and `y`. As hinted, Alice can only ensure a win if `x` and `y` have different parities. This means one must be odd, and the other must be even.

### Analyzing the Conditions:

1. **Alice's Winning Condition**: Alice wins if she takes the last flower. Since Alice starts, for her to ensure victory, the total number of turns (including both players' turns) must be odd. This implies that the sum of `x` and `y` must be odd, leading to the conclusion that one of `x` or `y` must be odd, and the other must be even.

2. **Counting Valid Pairs**: To count the valid `(x, y)` pairs:
   - Count the number of odd numbers in the range `[1, n]` for `x`.
   - Count the number of even numbers in the range `[1, m]` for `y`.
   - Since Alice can also start picking flowers in the anti-clockwise direction, also count the even numbers in `[1, n]` and odd numbers in `[1, m]`.

3. **Computing the Counts**:
   - The number of odd numbers in a range `[1, k]` can be calculated as `(k + 1) / 2`.
   - The number of even numbers in the same range is `k / 2`.

### Explanation:

- `odd_n` and `even_m` represent the cases where Alice picks the first flower in the clockwise direction, and `even_n` and `odd_m` cover the cases where she starts anti-clockwise.
- The total number of valid pairs is the sum of the products of these counts, representing all combinations where Alice can ensure a win by picking the last flower.



*/
