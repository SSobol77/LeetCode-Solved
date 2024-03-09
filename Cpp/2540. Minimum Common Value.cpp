// 2540. Minimum Common Value.


// Topic: Array, Hash Table, Two Pointers, Binary Search.


/*
### Task:
---
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.

Example 2:
Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
 
Constraints:
1 <= nums1.length, nums2.length <= 10^5
1 <= nums1[i], nums2[j] <= 10^9
Both nums1 and nums2 are sorted in non-decreasing order.

Hint 1:
Try to use a set.
Hint 2:
Otherwise, try to use a two-pointer approach.

### Testcase:
---
[1,2,3]
[2,4]
[1,2,3,6]
[2,3,4,5]


### Code:
---
class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int i = 0, j = 0; // Initialize two pointers
        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] == nums2[j]) {
                return nums1[i]; // Common element found, return it
            } else if (nums1[i] < nums2[j]) {
                i++; // Move to the next element in nums1
            } else {
                j++; // Move to the next element in nums2
            }
        }
        return -1; // No common element found
    }
};

// Description: ===================================
/*
To solve the "Minimum Common Value" task, we can utilize both hints provided. The first hint suggests using a set, which 
is suitable for quickly identifying common elements between the two arrays. However, since the arrays are sorted in 
non-decreasing order, the two-pointer approach hinted at second would be more efficient in terms of both time and space 
complexity. We will go with the two-pointer approach for this solution.

### Two-Pointer Approach Explanation:

1. Initialize two pointers, `i` and `j`, at the beginning of `nums1` and `nums2`, respectively.
2. Iterate through both arrays simultaneously until one of them is fully traversed. 
3. At each step, compare the elements pointed to by `i` and `j`.
   - If `nums1[i]` is equal to `nums2[j]`, we have found a common element. Return this element as it is the minimum common 
     value due to the sorted order of the arrays.
   - If `nums1[i]` is less than `nums2[j]`, increment `i` to move to the next element in `nums1`.
   - If `nums1[i]` is greater than `nums2[j]`, increment `j` to move to the next element in `nums2`.
4. If no common element is found by the end of the iteration, return -1.


### Description:

The two-pointer approach efficiently finds the minimum common value by taking advantage of the sorted order of the input arrays. 
This method avoids the need for extra space that would be required if using a set and is more efficient than binary search for this 
specific problem since we are leveraging the sorted property of the arrays. The time complexity is `O(n + m)`, where `n` and `m` 
are the lengths of `nums1` and `nums2`, respectively, making this solution highly efficient for large datasets.

*/
