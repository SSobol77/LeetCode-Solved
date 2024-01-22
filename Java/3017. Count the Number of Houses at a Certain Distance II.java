// 3017. Count the Number of Houses at a Certain Distance II.            - HARD -

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
    public long[] countOfPairs(int n, int x, int y) {

    }
}

*/

// Solution:

class Solution {
    public long[] countOfPairs(int n, int x, int y) {
        // Ensure x is less than y for consistency
        if (x > y) {
            int t = x;
            x = y;
            y = t;
        }

        long[] ans = new long[n];  // Array to store the final answer
        long[] diff = new long[n + 2];  // Array for maintaining differences for efficient computation

        for (int i = 1; i <= n; i++) {
            // Initial calculation of pairs for each distance i
            ans[i - 1] += (n - i) * 2;

            // Special case handling when x equals y or x is adjacent to y
            if (x == y || x == y - 1) {
                continue;
            }

            // Calculate adjustments for pairs that have a shorter distance due to the extra street
            // Case 1: When the path includes a portion of the houses before x
            long max = (long) Math.min(x - 1, i - 1);
            long min = (long) Math.max(0, (i - 1 - (n - y)));
            if (max >= min) {
                ans[i - 1] += (max - min + 1L) * 2L;
                if (i + (y - x - 1) <= n - 1) {
                    ans[i + (y - x - 1) - 1] -= (max - min + 1L) * 2L;
                }
            }

            // Case 2: When the path goes through the extra street and involves houses closer to x
            max = (long) Math.min(x - 1, i - 2);
            min = (long) Math.max(0, i - 1 - (y - (y + x + 1) / 2 - 1));
            if (max >= min) {
                ans[i - 1] += (max - min + 1L) * 2L;
                int start = y - (i - 1 - (int) min) - (x - (int) min);
                int end = y - (i - 1 - (int) max) - (x - (int) max);
                diff[start - 1] -= 2L;
                diff[end + 1] += 2L;
            }

            // Case 3: Similar to Case 2 but for houses closer to y
            max = (long) Math.min(n - y, i - 2);
            min = (long) Math.max(0, i - 1 - ((y + x - 2) / 2 - x));
            if (max >= min) {
                ans[i - 1] += (max - min + 1L) * 2L;
                int start = y + (int) min - (x + (i - 1 - (int) min));
                int end = y + (int) max - (x + (i - 1 - (int) max));
                diff[start - 1] -= 2L;
                diff[end + 1] += 2L;
            }

            // Adjusting for cases where the extra street creates a shorter path
            if (2 * i < y - x + 1) {
                ans[i - 1] += (long) Math.max(0, i - 2) * 2L;
                ans[(y - x + 1 - i) - 1] -= (long) Math.max(0, i - 2) * 2L;
            }
        }

        // Applying the differences using the diff array to get the final count of pairs
        for (int i = 0; i < n; i++) {
            diff[i] += i >= 2 ? diff[i - 2] : 0L;
            ans[i] += diff[i];
        }

        return ans;  // Return the final result
    }
}


// Description:
/*
The strategy employed in this code to solve the "Count the Number of Houses at a Certain Distance II" problem revolves around a combination of initial count adjustments and differential updates using prefix sums. Here's a detailed breakdown of the algorithm and the underlying logic:

### Algorithm and Logic:

1. **Sorting `x` and `y`**:
   - The code starts by ensuring that `x` is always less than or equal to `y`. This simplifies the calculations as it ensures consistency in handling the additional street.

2. **Initial Pair Counts**:
   - The code then iterates through each possible distance `i` (from 1 to `n`) and initially counts the number of pairs at each distance as if there were no additional street. This is done by realizing that for each distance `i`, there are `2 * (n - i)` pairs because each pair can be traversed in both directions.

3. **Handling the Additional Street**:
   - The code incorporates the effect of the additional street by adjusting the counts. This adjustment is made in several steps, depending on the position of the houses in relation to `x` and `y`:
     - **When `x` Equals `y` or Adjacent**: In this scenario, the additional street doesn't create a shortcut, so no adjustment is needed.
     - **Adjustments for Shortcuts Involving Houses Before `x` and After `y`**: The code calculates how many pairs are affected by the additional street creating a shortcut. This involves calculating the maximum and minimum number of affected pairs and then adjusting the counts for these distances.
     - **Differential Updates**: The code uses a `diff` array to store differential values, which are used to efficiently update the counts for longer distances where the additional street affects the count. This step is crucial as it allows updating many values in the `ans` array in a single pass at the end.

4. **Applying Differential Updates**:
   - Finally, the code iterates through the `diff` array, applying the differential updates to the `ans` array. This is where the prefix sum technique is used – the differential values in `diff` are added to the running total, and these totals are used to update the counts in the `ans` array.

### Summary of the Logic:

- The algorithm efficiently calculates the initial number of pairs for each distance, assuming a linear arrangement of houses.
- It then adjusts these counts to account for the additional street, which can provide shortcuts for certain pairs of houses.
- The use of the `diff` array for differential updates and the prefix sum technique for applying these updates ensures efficient handling of the problem, especially for large values of `n`.
- The final `ans` array contains the total count of pairs of houses for each distance, considering the additional street.

*/
