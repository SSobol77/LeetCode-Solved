# 3017. Count the Number of Houses at a Certain Distance II.

"""
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
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:



"""
### Solution Python:


from itertools import accumulate

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y = y, x
        ans = [0] * (n + 2)
        x -= 1
        y -= 1

        for i in range(n):
            # Initialize binary search bounds for finding the furthest house
            l, r = i + 1, n - 1
            while l <= r:
                # Midpoint of the current segment
                m = (l + r) // 2

                # Check if the direct distance (m - i) is shorter than the distance via the additional street
                if m - i < abs(i - x) + abs(m - y) + 1:
                    # If the direct path is shorter, move the left boundary to search further
                    l = m + 1
                else:
                    # Otherwise, move the right boundary to search closer
                    r = m - 1

            # Adjust the counts for pairs closer than distance m
            # Increment the count for distance 1 and decrement for distance (r + 1 - i)
            ans[1] += 1
            ans[r+1-i] -= 1

            # Skip if all pairs are closer in the direct path
            if l == n:
                continue

            # Calculate the adjustments for pairs that are exactly at certain distances using the additional street
            end = y
            val = abs(i - x) + 1

            # Adjust the counts for pairs at distances using the additional street
            if l < y:
                ans[val + 1] += 1
                ans[val + y - l + 1] -= 1

            ans[val] += 1
            ans[val + n - y] -= 1

        # Convert the difference array to actual counts using prefix sum
        ans = list(accumulate(ans))
        return [x * 2 for x in ans[1:-1]]

# Example usage
sol = Solution()
print(sol.countOfPairs(3, 1, 3)) # Output: [6,0,0]
print(sol.countOfPairs(5, 2, 4)) # Output: [10,8,2,0,0]
print(sol.countOfPairs(4, 1, 1)) # Output: [6,4,2,0]


### Description:
'''

### Explanation of the Binary Search Loop:

- **Binary Search Logic**: The binary search is used to find the farthest house `r` from the house `i` such that
    the direct distance is shorter than the distance when traveling via the additional street connecting houses
    `x` and `y`. This loop effectively divides the houses into two categories based on their distances from house
    `i`: those closer than the additional street path and those farther or equal.

- **Adjusting Counts with Binary Search Results**: After determining `r`, the code adjusts the `ans` array, which
    is essentially a difference array used to calculate the number of pairs for each distance. It increments the
    count for distance 1 and decrements for the distance `r + 1 - i`. This adjustment accounts for pairs that are
    directly reachable and those that are not due to the additional street.

- **Handling the Additional Street**: After completing the binary search, the code checks if there are pairs of
    houses that can be exactly `k` streets apart using the additional street. If the left boundary `l` of the
    binary search has not reached `n`, it indicates that there are such pairs, and the counts are adjusted accordingly.

- **Final Count Calculation**: At the end of the function, a prefix sum is applied to the `ans` array to convert it
    from a difference array to an actual count array. This array is then processed to return the final counts for each
    distance `k`, adjusted for 1-indexing.

This implementation should correctly reflect the count of house pairs for each distance, considering both the direct
paths and the additional street.


### Strategy:

1. **Preprocess x and y**: Ensure `x` is less than `y` for consistency, and adjust their values for 0-based indexing.

2. **Initialize Answer Array**: Create an array `ans` of size `n + 2` to store the count of pairs at each distance.

3. **Iterate Over Each House**: For each house `i`, calculate the number of pairs at each distance considering both
     the direct path and the path via the additional street.

4. **Calculate Distances Using Binary Search**:
   - Use binary search to find the furthest house `r` from house `i` such that the direct distance is still shorter
     than the distance using the additional street. Adjust the counts accordingly.
   - If `l` (the left pointer in binary search) doesn't reach `n`, it means some pairs are at an exact distance using
     the additional street. Adjust counts for these pairs.

5. **Post-process Answer Array**:
   - Use a prefix sum (`accumulate`) to convert the difference array into the actual counts of pairs at each distance.
   - Multiply each element by 2 as each pair can be traveled in both directions.

6. **Return Result**:
   - Return the result array, excluding the first and last elements to adjust for 1-indexed output and extra padding in
     the answer array.

### Solution Description:

- The solution efficiently calculates the number of pairs of houses at each minimum distance considering both the direct
  path and the path via the additional street.
- Binary search is used to optimize the process of finding the longest direct path between pairs of houses that is shorter
  than the path using the additional street.
- The solution also handles the edge cases, such as when `x` and `y` are equal or when all pairs are closer in the direct
  path.
- Prefix sums (`accumulate`) are used to convert the difference array into actual counts, making the solution more
  efficient and elegant.

'''
