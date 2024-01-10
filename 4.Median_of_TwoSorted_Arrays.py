"""
# 4. Median of Two Sorted Arrays.

# Topic: Array, Binary Search, Divide and Conquer.

# Task:
------------
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the 
two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6


# Testcase:
------------
[1,3]
[2]
[1,2]
[3,4]


# Code:
------------
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
"""
# Solution:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize the binary search space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Get the lengths of the arrays
        m, n = len(nums1), len(nums2)
        # Calculate the total number of elements and the half point
        total = m + n
        half = total // 2

        # Initialize binary search boundaries on the smaller array
        left, right = 0, m
        while left <= right:
            # Find the partition index for the smaller array
            partition1 = (left + right) // 2
            # Calculate the corresponding partition index for the larger array
            partition2 = half - partition1

            # Find the max element on the left and min element on the right for the first array
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            # Find the max element on the left and min element on the right for the second array
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Check if we have found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If the total number of elements is even
                if total % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                # If the total number of elements is odd
                else:
                    return min(minRight1, minRight2)
            # Adjust the binary search boundaries
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1

        # If no valid partition is found, raise an error
        raise ValueError("Input arrays are not sorted or not valid")



# Description:
'''
Explanation of the Comments:

1. Array Size Comparison: The code begins by ensuring that nums1 is the smaller array, as this minimizes 
   the search space for the binary search, thus optimizing the algorithm.

2. Length and Half Calculation: The lengths of both arrays are stored, and the half-way point of the total
   number of elements is calculated. This half-way point is crucial for determining the median.

3. Binary Search Initialization: A binary search is set up on the smaller array (nums1). The left and right 
   pointers are used to navigate through nums1.

4. Binary Search Process: The binary search involves finding a partition in nums1 and calculating the 
   corresponding partition in nums2. This partitioning aims to split all elements of both arrays into two 
   halves such that elements in the left half are less than or equal to elements in the right half.

5. Finding Median:
   * Correct Partition Check: The code checks if the partitions are valid, i.e., the max on the left sides 
     of both arrays is less than or equal to the min on the right sides.
   * Even Total Number of Elements: If the total length is even, the median is the average of the max of 
     the left halves and the min of the right halves.
   * Odd Total Number of Elements: If the total length is odd, the median is the min of the right halves.

6. Adjusting Search on Mismatch: If the current partition is not correct, the binary search boundaries are 
   adjusted accordingly.

7. Error Handling: If a valid partition is not found, indicating that the input arrays are not sorted or 
   valid, an error is raised.

This code efficiently finds the median of two sorted arrays in O(log(min(m, n))) time complexity, adhering 
to the constraints and requirements of the problem.

'''
