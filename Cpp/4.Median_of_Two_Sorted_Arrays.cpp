// 4. Median of Two Sorted Arrays

/*
### Task:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

#Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

#Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

#Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6

### Testcase:
--------------
[1,3]
[2]
[1,2]
[3,4]


### Code:
----------
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
*/

// Solution:
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Ensure nums1 is the shorter array to minimize binary search iterations
        if (nums1.size() > nums2.size()) {
            swap(nums1, nums2);
        }
        
        int m = nums1.size();
        int n = nums2.size();
        int left = 0, right = m;
        
        while (left <= right) {
            // Partition the smaller array to find potential median indices
            int partitionX = (left + right) / 2;
            int partitionY = (m + n + 1) / 2 - partitionX;
            
            // Calculate maximum and minimum elements on both sides of partitions
            int maxX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            int maxY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            int minX = (partitionX == m) ? INT_MAX : nums1[partitionX];
            int minY = (partitionY == n) ? INT_MAX : nums2[partitionY];
            
            // Check if partitions are correct for finding the median
            if (maxX <= minY && maxY <= minX) {
                // Median found
                if ((m + n) % 2 == 0) {
                    // If even total elements, return average of two middle elements
                    return (max(maxX, maxY) + min(minX, minY)) / 2.0;
                } else {
                    // If odd total elements, return the larger of the two middle elements
                    return max(maxX, maxY);
                }
            } else if (maxX > minY) {
                // Adjust partitionX to move towards the left side of nums1
                right = partitionX - 1;
            } else {
                // Adjust partitionX to move towards the right side of nums1
                left = partitionX + 1;
            }
        }
        
        // This should not happen if input arrays are sorted
        throw invalid_argument("Input arrays are not sorted.");
    }
};

// Description:
/*
The code uses a binary search approach to efficiently find the median in logarithmic time while maintaining 
a minimal amount of memory usage. There isn't a more efficient algorithm in terms of time complexity for 
finding the median of two sorted arrays.

This code uses the same efficient binary search approach as before. There isn't much more room for 
optimization in terms of time complexity, as O(log(min(m, n))) is already the best achievable complexity 
for this problem.

*/
