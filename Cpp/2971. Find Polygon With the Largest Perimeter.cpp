// 2971. Find Polygon With the Largest Perimeter.


// Topic: Array, Greedy, Sorting, Prefix Sum.


/*
### Task:
---
You are given an array of positive integers nums of length n.

A polygon is a closed plane figure that has at least 3 sides. The longest side of a polygon is smaller than the sum of its other sides.

Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.

The perimeter of a polygon is the sum of lengths of its sides.

Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.

Example 1:
Input: nums = [5,5,5]
Output: 15
Explanation: The only possible polygon that can be made from nums has 3 sides: 5, 5, and 5. The perimeter is 5 + 5 + 5 = 15.

Example 2:
Input: nums = [1,12,1,2,5,50,3]
Output: 12
Explanation: The polygon with the largest perimeter which can be made from nums has 5 sides: 1, 1, 2, 3, and 5. The perimeter is 1 + 1 + 2 + 3 + 5 = 12.
We cannot have a polygon with either 12 or 50 as the longest side because it is not possible to include 2 or more smaller sides that have a greater sum than either of them.
It can be shown that the largest possible perimeter is 12.

Example 3:
Input: nums = [5,5,50]
Output: -1
Explanation: There is no possible way to form a polygon from nums, as a polygon has at least 3 sides and 50 > 5 + 5.
 
Constraints:
3 <= n <= 10^5
1 <= nums[i] <= 10^9

Hint 1:
Sort the array.
Hint 2:
Use greedy algorithm. If we select an edge as the longest side, it is always better to pick up all the edges with length no longer than this longest edge.
Hint 3:
Note that the number of edges should not be less than 3.


### Testcase:
---
[5,5,5]
[1,12,1,2,5,50,3]
[5,5,50]


### Code:
---
class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
  long long largestPerimeter(vector<int>& n) {
    // Calculate the sum of all elements in the array
    long long prefix = accumulate(n.begin(), n.end(), 0LL);

    // Sort the array in non-decreasing order
    ranges::sort(n);

    // Iterate from the end to find a valid set of sides for the polygon
    for (int i = n.size() - 1; i >= 2; --i) {
      // Subtract the current side from the prefix sum to get the sum of all smaller sides
      prefix -= n[i];

      // Check if the sum of all smaller sides is greater than the current side
      if (prefix > n[i])
        // If so, return the sum of the current side and all smaller sides as the largest perimeter
        return prefix + n[i];
    }

    // If no valid set of sides is found, return -1
    return -1;
  }
};


// Description: ===================================
/*
The provided code snippet is a solution to the problem of finding the largest perimeter of a polygon that can be formed from a given set of side lengths, represented by the array `n`. The solution employs a greedy algorithm combined with sorting and a prefix sum calculation to efficiently determine the maximum possible perimeter. Here's a detailed description of how the solution works:

### Step 1: Calculate Prefix Sum
- The solution starts by calculating the sum of all elements in the array `n` using the `accumulate` function. This sum is stored in the `prefix` variable and represents the total length of all sides available for forming a polygon.

### Step 2: Sort the Array
- The array `n` is then sorted in non-decreasing order using the `ranges::sort` function. Sorting is crucial because it allows the algorithm to start checking for possible polygons from the largest side lengths, maximizing the potential perimeter.

### Step 3: Iterate and Check Conditions
- The solution iterates through the sorted array from the largest side length to the smallest, checking at each step whether a valid polygon can be formed with the current side length and all smaller side lengths.
- During each iteration, the current side length (`n[i]`) is subtracted from the `prefix` sum. After subtraction, `prefix` represents the sum of all smaller side lengths.
- The key condition checked is whether the sum of all smaller side lengths (`prefix`) is greater than the current side length (`n[i]`). This condition is derived from the polygon inequality principle, which states that for any polygon, the sum of the lengths of any two sides must be greater than the length of the remaining side. In this context, it's adapted to ensure that the sum of all smaller sides is greater than the largest side, allowing the polygon to close.

### Step 4: Return the Largest Perimeter
- If the condition is met, the function returns the sum of the current side length and all smaller side lengths (`prefix + n[i]`), which represents the largest possible perimeter that can be formed with the given set of side lengths.
- If the loop completes without finding any set of side lengths that satisfy the condition, the function returns `-1`, indicating that it's not possible to form a polygon with the given side lengths.

### Efficiency and Correctness
- The solution is efficient because it sorts the side lengths only once and then iterates through them, performing constant-time checks at each step. The use of a prefix sum eliminates the need for recalculating the sum of smaller side lengths in each iteration, further improving efficiency.
- The solution is correct because it adheres to the polygon inequality principle and starts checking from the largest possible side lengths, ensuring that if a polygon can be formed, it will have the largest possible perimeter.

This approach is a clever application of sorting, prefix sums, and the polygon inequality principle to solve the problem in an efficient and effective manner.



*/