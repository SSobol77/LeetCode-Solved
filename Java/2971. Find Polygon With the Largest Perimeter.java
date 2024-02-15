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
    public long largestPerimeter(int[] nums) {
        
    }
}


*/
// Solution: --------------------------------------

import java.util.Arrays;

class Solution {
  
  // Method to find the largest perimeter among three integers
  public long largestPerimeter(int[] n) {
    // Calculate the sum of all elements in the array
    long sol = Arrays.stream(n).asLongStream().sum();
    
    // Sort the array in ascending order
    Arrays.sort(n);
    
    // Iterate through the sorted array from the end
    for (int i = n.length - 1; i >= 2; --i) {
      // Subtract the current element from the sum
      sol -= n[i];
      
      // Check if the remaining sum is greater than the current element
      if (sol > n[i])
        // If so, return the sum plus the current element, as it forms the largest perimeter
        return sol + n[i];
    }
    
    // If no valid perimeter is found, return -1
    return -1;
  }
  
}

// Description:
/*
In this solution offers an efficient approach to solving the problem of finding the polygon with the largest 
perimeter using an array of positive integers representing potential side lengths. It employs a combination of 
array manipulation, sorting, and a greedy algorithm to maximize the perimeter under the given constraints.

The core idea of the solution is to sort the array in ascending order to easily access the longest sides and then 
iteratively check from the largest potential side if a valid polygon can be formed. The algorithm starts by 
calculating the sum of all elements in the array, assuming initially that all elements could contribute to the 
perimeter. It then iterates from the largest element downwards, subtracting each element from the total sum and 
checking if the remaining sum (representing the sum of all other sides) is greater than the current largest side. 
If this condition is met, a valid polygon can be formed, and the current sum, including the largest side, represents 
the largest possible perimeter.

The `largestPerimeter` method iterates from the end of the sorted array towards the beginning, ensuring that each 
potential longest side is tested with the maximum possible sum of remaining sides. This greedy approach ensures 
that the algorithm always tries to use the longest sides available while still satisfying the polygon inequality 
theorem, which states that the sum of the lengths of any two sides of a polygon must be greater than the length 
of the remaining side.

This solution is efficient and straightforward, leveraging the properties of sorted arrays and the characteristics 
of polygons to find the maximum possible perimeter. The use of sorting makes it easier to handle the sides in 
descending order of length, and the greedy approach of checking the sum of the remaining sides against the current 
longest side ensures that the solution is both correct and optimized for performance.

*/