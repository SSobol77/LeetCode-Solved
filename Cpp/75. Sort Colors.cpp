// 75. Sort Colors.


// Topic: Array, Two Pointers, Sorting.


/*
### Task:
---
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 
Follow up: Could you come up with a one-pass algorithm using only constant extra space?

Hint 1:
A rather straight forward solution is a two-pass algorithm using counting sort.
Hint 2:
Iterate the array counting number of 0's, 1's, and 2's.
Hint 3:
Overwrite array with the total number of 0's, then 1's and followed by 2's.


### Testcase:
---
[2,0,2,1,1,0]
[2,0,1]


### Code:
---
class Solution {
public:
    void sortColors(vector<int>& nums) {
        
    }
};


*/
// Solution: --------------------------------------

#include <vector>

class Solution {
public:
    void sortColors(std::vector<int>& nums) {
        // Initialize pointers for the current element (mid),
        // the boundary for 0s (low), and the boundary for 2s (high).
        int low = 0, mid = 0, high = nums.size() - 1;

        // Traverse through the array.
        while (mid <= high) {
            switch (nums[mid]) {
                case 0:
                    // If the element is 0, swap it with the element at low boundary.
                    std::swap(nums[low++], nums[mid++]);
                    break;
                case 1:
                    // If the element is 1, just move to the next element.
                    mid++;
                    break;
                case 2:
                    // If the element is 2, swap it with the element at high boundary.
                    std::swap(nums[mid], nums[high--]);
                    break;
            }
        }
    }
};


// Description: ===================================
/*
To solve the "Sort Colors" problem, we'll implement the `sortColors` function, which aims to sort the input array `nums` 
containing 0s, 1s, and 2s, representing the colors red, white, and blue respectively. The sorting should be done in-place, 
and the order of colors should be red, white, and blue corresponding to 0, 1, and 2.

Following the hints provided, a straightforward two-pass solution would involve counting the number of 0s, 1s, and 2s first 
and then overwriting the array with these counts. However, the challenge encourages a one-pass algorithm with constant space 
complexity. For this, we can use the Dutch National Flag algorithm by Edsger W. Dijkstra, which uses three pointers to sort 
the elements in a single pass.

Here's how the algorithm works:

1. Maintain three pointers `low`, `mid`, and `high` representing the boundaries of 0s, 1s, and unknown region respectively.
2. Initially, `low` and `mid` are set to the start of the array, and `high` is set to the end of the array.
3. Traverse the array with `mid` and swap elements to ensure 0s go to the beginning, 1s stay in the middle, and 2s move to the 
   end of the array.
4. The iteration continues until `mid` exceeds `high`.

### Description:
---
This solution applies the Dutch National Flag algorithm to sort the colors in a single pass with constant space complexity. 
It maintains three pointers: `low` for the next position of 0, `mid` for the current element, and `high` for the next position of 2. 
It iterates through the array, swapping elements as necessary to ensure all 0s are before `low`, all 2s are after `high`, and all 
1s are between `low` and `high`. This in-place sorting algorithm efficiently sorts the elements with minimal space usage and without 
the need for a library sort function.

*/
