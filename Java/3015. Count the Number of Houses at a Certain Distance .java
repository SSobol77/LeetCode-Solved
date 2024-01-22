// 3015. Count the Number of Houses at a Certain Distance I.

/*
### Task:
--------
You are given three positive integers n, x, and y.

In a city, there exist houses numbered 1 to n connected by n streets. There is a street connecting the house numbered i with the house numbered i + 1 for all 1 <= i <= n - 1 . An additional street connects the house numbered x with the house numbered y.

For each k, such that 1 <= k <= n, you need to find the number of pairs of houses (house1, house2) such that the minimum number of streets that need to be traveled to reach house2 from house1 is k.

Return a 1-indexed array result of length n where result[k] represents the total number of pairs of houses such that the minimum streets required to reach one house from the other is k.

Note that x and y can be equal.

Example 1:
Input: n = 3, x = 1, y = 3
Output: [6,0,0]
Explanation: Let's look at each pair of houses:
- For the pair (1, 2), we can go from house 1 to house 2 directly.
- For the pair (2, 1), we can go from house 2 to house 1 directly.
- For the pair (1, 3), we can go from house 1 to house 3 directly.
- For the pair (3, 1), we can go from house 3 to house 1 directly.
- For the pair (2, 3), we can go from house 2 to house 3 directly.
- For the pair (3, 2), we can go from house 3 to house 2 directly.

Example 2:
Input: n = 5, x = 2, y = 4
Output: [10,8,2,0,0]
Explanation: For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (2, 4), (4, 2), (3, 4), (4, 3), (4, 5), and (5, 4).
- For k == 2, the pairs are (1, 3), (3, 1), (1, 4), (4, 1), (2, 5), (5, 2), (3, 5), and (5, 3).
- For k == 3, the pairs are (1, 5), and (5, 1).
- For k == 4 and k == 5, there are no pairs.

Example 3:
Input: n = 4, x = 1, y = 1
Output: [6,4,2,0]
Explanation: For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (3, 4), and (4, 3).
- For k == 2, the pairs are (1, 3), (3, 1), (2, 4), and (4, 2).
- For k == 3, the pairs are (1, 4), and (4, 1).
- For k == 4, there are no pairs.

Constraints:
2 <= n <= 100
1 <= x, y <= n

### Testcase:
---
3
1
3
5
2
4
4
1
1

### Code:
---
class Solution {
    public int[] countOfPairs(int n, int x, int y) {

    }
}

*/
// Solution:  ----------------------------------------------

import java.util.Arrays;

public class Solution {
    public int[] countOfPairs(int n, int x, int y) {
        int[] result = new int[n]; // Initialize the result array

        // Iterate over all possible pairs of houses
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                // Calculate direct distance between houses i and j
                int directDist = j - i;

                // Calculate distance if traveling via the additional street between x and y
                int viaXyDist = Math.min(Math.abs(x - i), Math.abs(y - i)) + 1 + Math.min(Math.abs(x - j), Math.abs(y - j));

                // Determine the minimum of the two distances
                int minDist = Math.min(directDist, viaXyDist);

                // Update the count for this minimum distance in the result array
                result[minDist - 1] += 2;
            }
        }

        return result;
    }

    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();

        // Test examples
        System.out.println(Arrays.toString(sol.countOfPairs(3, 1, 3))); // Output: [6,0,0]
        System.out.println(Arrays.toString(sol.countOfPairs(5, 2, 4))); // Output: [10,8,2,0,0]
        System.out.println(Arrays.toString(sol.countOfPairs(4, 1, 1))); // Output: [6,4,2,0]
    }
}

// Description: -------------------------------------------
/*

In this code:
- We iterate over all pairs of houses using nested loops.
- For each pair, we calculate two distances: the direct distance and the distance via the additional street.
- We then find the minimum of these two distances, as this is the shortest path between the houses.
- The count of pairs for each minimum distance is updated in the `result` array.
- Finally, the `result` array is returned, which contains the total number of pairs for each minimum street distance.

The `main` method includes test cases to demonstrate the functionality of the `countOfPairs` method.


To solve this problem in Java, we can follow the same logic as the Python solution you provided. The key idea is to iterate through all pairs of houses and calculate the minimum distance between them, either directly or via the additional street. Then, for each pair, increment the count of pairs that correspond to this minimum distance. The result is a 1-indexed array where each element represents the total number of pairs of houses such that the minimum number of streets required to reach one house from the other is the index of that element.

Here's how to implement this in Java:

1. **Initialize the Result Array**: Create an array `result` of length `n`, initialized with zeros.

2. **Iterate Over All House Pairs**: Use nested loops to iterate over every pair of houses `(i, j)` where `i` is less than `j`.

3. **Calculate the Minimum Distance**:
   - Compute the direct distance between `i` and `j`.
   - Compute the distance if traveling via the additional street between `x` and `y`.
   - Determine the minimum of these two distances.

4. **Update the Result Array**: For each pair, increment the count in the `result` array at the index corresponding to the minimum distance.

5. **Return the Result**: The `result` array now contains the count of pairs for each minimum distance.


*/
