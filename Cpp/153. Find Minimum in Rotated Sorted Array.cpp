// 153. Find Minimum in Rotated Sorted Array.

// Topic:


/*
### Task:
---
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the 
array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

Hint 1:
Array was originally in ascending order. Now that the array is rotated, there would be a point in the array where there is a small deflection from the increasing sequence. eg. The array would be something like [4, 5, 6, 7, 0, 1, 2].
Hint 2:
You can divide the search space into two and see which direction to go. Can you think of an algorithm which has O(logN) search complexity?
Hint 3:
- All the elements to the left of inflection point > first element of the array.
- All the elements to the right of inflection point < first element of the array.


### Testcase:
---
[3,4,5,1,2]
[4,5,6,7,0,1,2]
[11,13,15,17]


### Code:
---
class Solution {
public:
    int findMin(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    int findMin(vector<int>& nums) {
        int start = 0; // Start of the search range
        int end = nums.size() - 1; // End of the search range

        // Binary search for the inflection point
        while (start < end) {
            int mid = start + (end - start) / 2; // Calculate mid index to avoid potential overflow

            if (nums[mid] > nums[end]) {
                // Minimum element must be to the right of mid
                start = mid + 1;
            } else {
                // Minimum element is to the left of mid, including mid
                end = mid;
            }
        }

        // When start == end, we have found the smallest element
        return nums[start];
    }
};


// Description: ===================================
/*
To find the minimum element in a rotated sorted array, we can leverage the binary search algorithm due to the unique 
properties of the array. The array is originally sorted in ascending order, then rotated, which means there's an inflection
point where the smallest number exists. This inflection point divides the array into two subarrays that are individually
sorted. The challenge is to identify the correct half of the array to continue the binary search process, aiming for O(log n) 
time complexity.


### Algorithm Description:

1. **Initialize Start and End Pointers:** Start by setting two pointers, `start` and `end`, to the first and last index of the array, 
     respectively.

2. **Binary Search Loop:** While the `start` pointer is less than the `end` pointer, calculate the `mid` index. If the element at `mid` 
     is greater than the element at `end`, the smallest element must be to the right of `mid`, so move the `start` pointer to `mid + 1`. 
     Otherwise, the smallest element is on the left side, including `mid`, so move the `end` pointer to `mid`.

3. **Termination:** When the `start` equals `end`, the smallest element of the array is found.


### Detailed Explanation:

- **Initialization:** The algorithm starts with the entire array as the search range.
- **Binary Search:** It uses a binary search loop to narrow down the search range. The `mid` element is compared to the `end` element 
    to determine which half of the array contains the inflection point. This is based on the fact that in a rotated sorted array, one half 
    of the array will always be in sorted order from the inflection point.
- **Decision Making:** If `nums[mid]` is greater than `nums[end]`, the inflection point and the minimum element must be to the right 
    of `mid`. If not, the inflection point could be at `mid` or to the left of `mid`.
- **Loop Invariant:** The condition `start < end` ensures that the loop continues until the search range is narrowed down to a single
    element, which is the minimum element.
- **Result:** The loop exits when `start` equals `end`, which is the index of the minimum element in the rotated sorted array.

*/