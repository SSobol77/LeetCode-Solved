// 3017. Count the Number of Houses at a Certain Distance II.             - HARD -

/*
### Task:
---------
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
2 <= n <= 10^5
1 <= x, y <= n

Hint 1:
If there were no additional street connecting house x to house y, there would be 2 * (n - i) pairs of houses at distance i.
Hint 2:
The shortest distance between house i and house j (j < i) is along one of these paths: - i -> j - i -> y---x -> j
Hint 3:
Try to change the distances calculated by path i ->j to the other path.
Hint 4:
Can we use prefix sums to compute the answer?


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
public:
    vector<long long> countOfPairs(int n, int x, int y) {

    }
};

*/
// Solution:

class Solution {
public:
    vector<long long> countOfPairs(int n, int x, int y) {
        vector<long long> psa(n+5); // Initialize a prefix sum array (psa) with a size slightly larger than n for safety

        // Ensure x is always less than y for consistent processing
        if (x > y) swap(x, y);

        // Handle the special case when x is equal to y
        if (x == y) {
            for (int i = 1; i <= n; i++) {
                // When x equals y, the problem reduces to a simple linear arrangement of houses
                psa[1]++; psa[i]--;
                psa[1]++; psa[n+1-i]--;
            }
        } else {
            // Main loop for handling the case when x is not equal to y
            for (int i = 1; i <= n; i++) {
                // If current house is before x
                if (i <= x) {
                    // Update prefix sum array for direct paths and paths going through the additional street
                    psa[1]++; psa[i]--;
                    psa[1]++; psa[x-i+1]--;

                    // Calculate midpoints between x and y
                    int rq = y - x;
                    int h = rq / 2;
                    int h2 = rq - h;

                    // Update psa for paths using the additional street with different split points
                    psa[x-i+1]++; psa[h+1+x-i]--;
                    psa[x-i+1]++; psa[h2+1+x-i]--;
                    psa[x-i+2]++; psa[n+1-y+1+x-i]--;
                }
                // If current house is after y
                else if (i >= y) {
                    // Similar updates as above but for houses after y
                    psa[1]++; psa[n-i+1]--;
                    psa[1]++; psa[i-y+1]--;

                    // Calculate and use midpoints between x and y for updates
                    int rq = y - x;
                    int h = rq / 2;
                    int h2 = rq - h;

                    psa[i-y+1]++; psa[i-y+h+1]--;
                    psa[i-y+1]++; psa[i-y+h2+1]--;
                    psa[i-y+2]++; psa[x+1+i-y]--;
                }
                // If current house is between x and y
                else {
                    // Calculate midpoints and update psa accordingly
                    int rq = y - x;
                    int h = rq / 2;
                    int h2 = rq - h;

                    psa[1]++; psa[h+1]--;
                    psa[1]++; psa[h2+1]--;

                    // Determine closest distances to either x or y
                    int distX = min(i-x, y-i+1);
                    int distY = min(y-i, i-x+1);

                    // Update psa based on these distances
                    psa[distX+1]++;
                    psa[distX+x]--;
                    psa[distY+1]++;
                    psa[distY+n-y+1]--;
                }
            }
        }

        vector<long long> pairs; // Initialize the result vector
        // Convert the prefix sum array to the actual count of pairs
        for (int i = 1; i <= n; i++) {
            psa[i] += psa[i-1];
            pairs.push_back(psa[i]);
        }
        return pairs; // Return the final result
    }
};


// Description:
/*
The strategy used in your code to solve the problem of counting the number of pairs of houses at certain distances involves the use of a prefix sum array (`psa`) for efficient computation. Here's a detailed description of the algorithm and the logic behind the solution:

### Algorithm and Logic:

1. **Prefix Sum Array Initialization**:
   - A prefix sum array (`psa`) is initialized with a size slightly larger than `n`. This array is used to efficiently calculate the cumulative counts of pairs at various distances.

2. **Handling `x` and `y` Order**:
   - The code ensures that `x` is always less than or equal to `y` by swapping them if necessary. This simplification allows for consistent processing in subsequent steps.

3. **Special Case - `x` Equals `y`**:
   - When `x` is equal to `y`, the additional street does not affect the distance between any houses. The problem simplifies to a linear arrangement of houses. The code updates `psa` to reflect the count of pairs at each distance considering only direct paths.

4. **General Case - `x` Not Equal to `y`**:
   - The code then iterates over each house position `i` from 1 to `n`.
   - It handles three main scenarios based on the position of `i` relative to `x` and `y`:
     - **Before `x`**: Updates `psa` for direct paths and paths going through the additional street, considering distances to `x` and the midpoint between `x` and `y`.
     - **After `y`**: Similar to the case of before `x`, but considering distances from `y`.
     - **Between `x` and `y`**: Updates `psa` considering paths that use the additional street and the closest distances to either `x` or `y`.

5. **Prefix Sum Computation**:
   - The code computes the prefix sums in `psa` to transform it into the actual count of pairs for each possible distance.

6. **Final Result Construction**:
   - Finally, the code constructs the result vector `pairs` from `psa`, where each element represents the total number of pairs of houses such that the minimum number of streets required to reach one house from the other is a specific distance.

### Summary of the Logic:

- The code cleverly uses the prefix sum technique to accumulate the number of pairs of houses at each distance, considering both direct paths and paths that may include the additional street.
- It efficiently handles different relative positions of houses to `x` and `y`, ensuring that the additional street's impact on distances is correctly accounted for in the counts.
- The final transformation of the prefix sums into the actual counts provides the solution to the problem.

*/
