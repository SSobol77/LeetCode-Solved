# 4. Median of Two Sorted Arrays

# Topic: Array, Binary Search, Divide and Conquer.

'''
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
---------------------
Case 1
nums1 = [1,3]
nums2 = [2]

Case 2
nums1 = [1,2]
nums2 = [3,4]



# Code:
------------------------
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

'''
# Solution Optimize 1:
class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure that nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        
        # Perform binary search on nums1
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            
            # Check if i is too small
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            
            # Check if i is too big
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            
            # i is perfect
            else:
                # Calculate the maximum element of the left half
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])
                
                # If the total length of the arrays is odd, return the max of the left half
                if (m + n) % 2 == 1:
                    return max_of_left
                
                # Calculate the minimum element of the right half
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                
                # If the total length of the arrays is even, return the average of the max of the left half and the min of the right half
                return (max_of_left + min_of_right) / 2




#---------------------------------------------------------------------------------------------------------------------
# Solution2:

class Solution2:
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge the two sorted arrays nums1 and nums2 into a single sorted array
        # The '+' operator concatenates the two arrays, and 'sorted()' sorts the merged array
        merged = sorted(nums1 + nums2)
        
        # Calculate the median of the merged array
        # The median is the middle element in a sorted array if the array length is odd,
        # or the average of the two middle elements if the array length is even
        mid = len(merged) // 2  # '//' is the integer division operator

        # Check if the length of the merged array is even
        if len(merged) % 2 == 0:
            # If even, the median is the average of the two middle elements
            # 'merged[mid - 1]' is the first middle element and 'merged[mid]' is the second
            return (merged[mid - 1] + merged[mid]) / 2
        else:
            # If odd, the median is the middle element of the merged array
            return merged[mid]

# Test cases
sol = Solution()

# Example 1: Median of arrays [1, 3] and [2]
nums1_1 = [1, 3]
nums2_1 = [2]
result1 = sol.findMedianSortedArrays(nums1_1, nums2_1)  # Expected Output: 2

# Example 2: Median of arrays [1, 2] and [3, 4]
nums1_2 = [1, 2]
nums2_2 = [3, 4]
result2 = sol.findMedianSortedArrays(nums1_2, nums2_2)  # Expected Output: 2.5

result1, result2

# Description:
'''
This code is an implementation of a function that finds the median of two sorted arrays. It first 
merges the two arrays into one and sorts it, then calculates the median based on the combined array's 
length. The median is either the middle element (for odd-length arrays) or the average of the two 
middle elements (for even-length arrays). The code includes test cases to validate its functionality.
'''
