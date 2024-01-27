// 4. Median of Two Sorted Arrays.

// Topic: Array, Binary Search, Divide and Conquer.

/*
### Task:
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


### Testcase:
---------------------
Case 1
nums1 = [1,3]
nums2 = [2]

Case 2
nums1 = [1,2]
nums2 = [3,4]


### Code:
------------------------
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
    }
};

*/
// Solution:  --------------------------------------------------------------

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Ensure nums1 is the smaller array to optimize the binary search process
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int x = nums1.size();
        int y = nums2.size();

        // Set initial binary search boundaries
        int low = 0, high = x;

        // Binary search begins on the smaller array (nums1)
        while (low <= high) {
            // Partition nums1 such that left half of the combined array is considered
            int partitionX = (low + high) / 2;

            // Calculate partitionY using the median formula, ensuring total left half size equals total right half
            int partitionY = (x + y + 1) / 2 - partitionX;

            // Handling edge cases: if partitionX is 0 or x, maxLeftX or minRightX could be out of bounds
            int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            int minRightX = (partitionX == x) ? INT_MAX : nums1[partitionX];

            // Similar handling for partitionY in nums2
            int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            int minRightY = (partitionY == y) ? INT_MAX : nums2[partitionY];

            // Check if we have found the correct partition
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // If total length is even, median is average of max of left elements and min of right elements
                if ((x + y) % 2 == 0) {
                    return (double)(max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2;
                } else {
                    // If total length is odd, median is max of left elements
                    return (double)max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) {
                // If left part of nums1 is too big, move towards left in nums1
                high = partitionX - 1;
            } else {
                // If left part of nums1 is too small, move towards right in nums1
                low = partitionX + 1;
            }
        }

        // If the loop exits without returning, input arrays were not sorted or had invalid sizes
        throw invalid_argument("Input arrays are not sorted or have invalid sizes.");
    }
};



// Description: =============================================================
/*
To solve the "Median of Two Sorted Arrays" problem with a time complexity of O(log(m+n)), where `m` and `n` are the sizes 
of the two arrays, we can use a binary search algorithm. The key idea is to find the correct partition in each array such 
that the left half of the combined array contains elements less than or equal to the elements in the right half. 
This approach does not require merging the arrays, which keeps the algorithm efficient.

Here's an outline of the steps involved:
1. Ensure `nums1` is the shorter array to minimize the binary search range.
2. Use binary search on the shorter array (`nums1`) to find the partition.
3. Calculate the partition for `nums2` based on the partition of `nums1` to ensure the left half of the combined array is 
   equal to or one more than the right half.
4. Find the max of the left elements and the min of the right elements from both arrays around the partition to calculate 
   the median.


### Detailed Comments:

- The algorithm starts by ensuring `nums1` is the smaller array to optimize the binary search process. This is crucial for achieving the desired time complexity.
- The binary search is conducted on `nums1`, with `low` and `high` defining the current search boundaries.
- Within the loop, `partitionX` and `partitionY` are calculated to divide the arrays into left and right halves. The goal is to ensure the left half of the combined array is equal to or one element more than the right half.
- `maxLeftX` and `minRightX` are the edge values around the partition in `nums1`. If `partitionX` is at the start or end, these values are set to `INT_MIN` and `INT_MAX` respectively to simulate infinity. This prevents out-of-bounds errors and correctly handles edge cases where the median might be at the edge of one array.
- A similar approach is used for `maxLeftY` and `minRightY` in `nums2`, adjusting for `partitionY`.
- The core condition (`maxLeftX <= minRightY && maxLeftY <= minRightX`) checks if the current partition is correct. If true, the median is calculated based on whether the total length of combined arrays is odd or even.
- If the partition is not correct, the binary search boundaries (`low` and `high`) are adjusted to explore a new partition in `nums1`.
- The loop continues until the correct partition is found, ensuring that the algorithm adheres to the O(log(min(m,n))) complexity requirement.


### Explanation:

- The binary search is performed on the smaller array (`nums1`) to minimize the search space.
- `partitionX` and `partitionY` determine the split in `nums1` and `nums2`, respectively, such that the left halves of both arrays combined is equal to or one more than the right halves combined.
- `maxLeftX`, `minRightX`, `maxLeftY`, and `minRightY` are used to find the maximum element on the left side of the partition and the minimum element on the right side.
- If the correct partition is found (i.e., `maxLeftX <= minRightY` and `maxLeftY <= minRightX`), the median is calculated based on the parity of the total length of the combined arrays.
- The algorithm ensures O(log(min(m,n))) complexity by performing the binary search on the smaller array.


*/