# 2971. Find Polygon With the Largest Perimeter.


# Topic: Array, Greedy, Sorting, Prefix Sum.


"""
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
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
    

"""
# Solution: --------------------------------------

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Calculate the total sum of all elements in the array
        total_sum = sum(nums)
        
        # Sort the array in descending order
        nums.sort(reverse=True)
        
        # Initialize index for iteration
        i = 0
        
        # Iterate through the sorted array
        while i < len(nums):
            # Get the current longest side
            longest_side = nums[i]
            
            # Subtract the current longest side from the total sum
            total_sum -= longest_side
            
            # Check if the sum of all remaining edges is greater than the current longest side
            if total_sum > longest_side:
                # If so, return the perimeter of the polygon
                return total_sum + longest_side
            
            # Move to the next element in the array
            i += 1

        # If no valid polygon can be formed, return -1
        return -1


# Description: ===================================
'''
The task is to find the largest possible perimeter of a polygon whose sides can be formed from a given array of positive integers. 
A polygon is defined as a closed plane figure with at least three sides, and the longest side of a polygon must be smaller than 
the sum of its other sides.

To solve this problem, we can employ a greedy approach by first sorting the array in descending order. This allows us to prioritize 
the longest sides of the potential polygons. We then iterate through the sorted array, considering each element as the longest side 
of a potential polygon.

For each element in the sorted array, we calculate the sum of all elements excluding the current longest side. If this sum is greater 
than the current longest side, it indicates that the remaining sides can form a valid polygon. In this case, we return the sum of the 
remaining sides plus the current longest side as the largest possible perimeter.

If no valid polygon can be formed with the current longest side, we move to the next element in the sorted array and repeat the 
process. If all elements have been considered without finding a valid polygon, we return -1 to indicate that it is not possible 
to create a polygon from the given array.

The solution prioritizes the longest sides while ensuring that the remaining sides can form a valid polygon. 
By following this approach, we efficiently determine the largest possible perimeter of a polygon that can be formed from the given 
array of positive integers.

'''
