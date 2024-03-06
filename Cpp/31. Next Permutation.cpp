// 31. Next Permutation.


// Topic: Array, Two Pointers.


/*
### Task:
---
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

    - For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

    - For example, the next permutation of arr = [1,2,3] is [1,3,2].
    - Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    - While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100

### Testcase:
---
[1,2,3]
[3,2,1]
[1,1,5]


### Code:
---
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        
    }
};


*/
// Solution: --------------------------------------

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i = nums.size() - 2;

        // Step 1: Find the first decreasing element from the end
        while (i >= 0 && nums[i + 1] <= nums[i]) {
            i--;
        }

        if (i >= 0) {  // If such element was found
            int j = nums.size() - 1;
            // Step 2: Find the element just larger than nums[i]
            while (nums[j] <= nums[i]) {
                j--;
            }
            // Step 3: Swap nums[i] and nums[j]
            swap(nums[i], nums[j]);
        }

        // Step 4: Reverse the suffix starting at nums[i + 1]
        reverse(nums.begin() + i + 1, nums.end());
    }
};


// Description: ===================================
/*
To implement the "Next Permutation" function, we follow a specific algorithm to rearrange the array into its next lexicographically greater permutation. If no such permutation exists (the array is in descending order), we must transform the array into its lowest possible order (ascending order). This problem can be solved efficiently in-place with a few steps that involve scanning and swapping elements in the array.

Here is the step-by-step algorithm:

1. **Find the first decreasing element**: Traverse the array from the end and find the first element `nums[i]` such that `nums[i] < nums[i + 1]`. This element is the one we need to swap to increase the permutation. If no such element exists, the array is in its highest permutation, so we simply reverse the entire array to get the lowest permutation.

2. **Find the element just larger than `nums[i]`**: Again traverse the array from the end and find the first element `nums[j]` that is greater than `nums[i]`. This element will be swapped with `nums[i]` to ensure we get the next permutation just larger than the current one.

3. **Swap `nums[i]` and `nums[j]`**: Swap these two elements to form a new permutation that is greater than the current one.

4. **Reverse the suffix starting at `nums[i + 1]`**: Finally, reverse the array from `nums[i + 1]` to the end. This step is crucial because after the swap, the suffix (the part of the array after `i`) is in descending order, and we need the lowest possible order (ascending) for the suffix to ensure the permutation is the next one lexicographically.

### Description:

This solution follows the algorithm described to find the next lexicographically greater permutation of an array in place. The key is to identify the first decreasing element from the end, which indicates the "increasable" part of the array. Swapping this element with the just larger element found later in the array, and then reversing the suffix starting just after the swapped element, ensures the next permutation is achieved with minimal increase. If no decreasing element is found, reversing the entire array gives the lowest permutation, effectively rolling over to the start in the sorted list of permutations.

*/
