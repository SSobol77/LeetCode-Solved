# 3015. Count the Number of Houses at a Certain Distance I.

"""
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
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:



"""
### Solution:

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        result = [0] * n  # Initialize the result array

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                # Calculate the direct distance
                direct_dist = j - i

                # Calculate the distance via the additional street
                via_xy_dist = min(abs(x - i), abs(y - i)) + 1 + min(abs(x - j), abs(y - j))

                # Find the minimum of the two distances
                min_dist = min(direct_dist, via_xy_dist)

                # Update the count for this minimum distance
                result[min_dist - 1] += 2

        return result


### Description:
'''
My solution employs a brute-force approach to count the pairs of houses for each possible minimum distance.

### Strategy:

1. **Iterate Over All House Pairs**:
   - Loop through all possible pairs of houses `(i, j)` where `i` is less than `j`. This ensures that every
     unique pair of houses is considered exactly once.

2. **Calculate Direct Distance**:
   - For each pair `(i, j)`, calculate the direct distance as `direct_dist = j - i`. This is the number of
     streets between the two houses without considering the additional street between `x` and `y`.

3. **Calculate Distance Via Additional Street**:
   - For the same pair, calculate the distance if traveling via the additional street. This is done in two parts:
     - Calculate the distance from house `i` to the closer of the two houses `x` or `y`.
     - Calculate the distance from house `j` to the closer of the two houses `x` or `y`.
     - Add 1 to this sum to include the additional street itself.

4. **Determine the Minimum Distance**:
   - Determine the minimum distance `min_dist` between `direct_dist` and `via_xy_dist` for each pair.

5. **Count the Pairs for Each Distance**:
   - Increment the count in the `result` array for the index corresponding to `min_dist - 1` by 2. The subtraction
     of 1 is to adjust for the 1-indexing of the `result` array.

6. **Return the Result**:
   - Return the `result` array, which now contains the count of pairs for each minimum distance.


In this code, nested loops are used to iterate over every pair of houses. For each pair, both the direct distance and
the distance via the additional street are calculated, and the minimum of these two is determined. The result array is
then updated accordingly for each minimum distance. This method effectively accounts for every possible pair and the
shortest path between them, whether it's the direct route or via the additional street.

'''
