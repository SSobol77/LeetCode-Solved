// 215. Kth Largest Element in an Array.


// Topic: Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect.


/*
### Task:
---
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4


### Testcase:
---
[3,2,1,5,6,4]
2
[3,2,3,1,2,4,5,5,6]
4


### Code:
---
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Use std::nth_element to rearrange the elements in nums
        // such that the element at the (n-k)th position is the one that
        // would be in that position if the array were sorted.
        // This means that all elements before this position are not greater
        // than the element at the (n-k)th position and all elements after
        // this position are not less than the element at the (n-k)th position.
        std::nth_element(nums.begin(), nums.begin() + nums.size() - k, nums.end());

        // Since std::nth_element rearranges the array in a way that the
        // kth largest element (which is the (n-k)th element in a sorted array
        // of size n) is placed at its correct position in the sorted order,
        // we can directly return the element at the (n-k)th position.
        return nums[nums.size() - k];
    }
};

// Description: ===================================
/*
### Explanation:

- `std::nth_element` is a powerful STL algorithm that partially sorts a range such that the element at the specified position (`nums.begin() + nums.size() - k` in this case) is placed in the position it would be in a fully sorted array. All elements before this position are less than or equal to the element, and all elements after are greater or equal, although they may not be sorted among themselves.
- The `kth` largest element in an array corresponds to the `(n-k)th` element in a sorted version of that array, where `n` is the total number of elements in the array. This is why we use `nums.size() - k` to find the correct position.
- After rearranging the elements using `std::nth_element`, the function returns the element at position `nums.size() - k`, which is now the `kth` largest element in the array.

The provided C++ solution employs the `std::nth_element` function from the C++ Standard Library to efficiently find the kth largest element in an unsorted array. Here's a detailed description of how the solution works:

### Understanding `std::nth_element`:
`std::nth_element` is a partial sorting algorithm that rearranges elements in a given range `[first, last)` such that:
- The element at the nth position (`first + n`) is the same as the one that would be in that position in a fully sorted array.
- All elements before this nth position are less than or equal to the elements after this nth position.
- The elements before and after the nth position are not necessarily sorted among themselves.

### Solution Strategy:
The goal is to find the kth largest element in an unsorted array. In a sorted array, this element would be at the `(n-k)`th position, where `n` is the size of the array. The solution leverages this fact and uses `std::nth_element` to partially sort the array such that the kth largest element is moved to its correct position as if the array were fully sorted.

### Step-by-Step Process:
1. **Partial Sorting with `std::nth_element`:**
   - The function is called with the beginning of the array (`nums.begin()`), the position where we want the kth largest element to be (`nums.begin() + nums.size() - k`), and the end of the array (`nums.end()`).
   - This rearranges the array so that the kth largest element is placed at the `(n-k)`th position, and all elements before this position are not greater than this element, while all elements after this position are not less than this element.

2. **Retrieving the kth Largest Element:**
   - After the partial sorting, the kth largest element is now correctly positioned at `nums.size() - k` in the array. The solution simply returns the value of the element at this position.

### Key Advantages:
- **Efficiency:** The `std::nth_element` function is more efficient for this task than fully sorting the array, especially for large arrays, because it only partially sorts the array to place the kth largest element in its correct position.
- **Simplicity:** The solution is concise and leverages the powerful STL algorithm, making the code easy to understand and maintain.

### Example:
Consider an array `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`. The function partially sorts `nums` to `[3, 2, 4, 5, 6, 1]`, where `5` is the 2nd largest element and is now at the 4th position (`nums.size() - 2`). The function then returns `5` as the 2nd largest element.

This solution is particularly useful in scenarios where finding a specific order statistic in an unsorted collection is required without the overhead of fully sorting the data.

*/
