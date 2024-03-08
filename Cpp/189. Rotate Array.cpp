// 189. Rotate Array.


// Topic: Array, Math, Two Pointers.


/*
### Task:
---
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 
Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5

Follow up:
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Hint 1:
The easiest solution would use additional memory and that is perfectly fine.
Hint 2:
The actual trick comes when trying to solve this problem without using any additional memory. This means you need to use the 
original array somehow to move the elements around. Now, we can place each element in its original location and shift all the 
elements around it to adjust as that would be too costly and most likely will time out on larger input arrays.
Hint 3:
One line of thought is based on reversing the array (or parts of it) to obtain the desired result. Think about how reversal 
might potentially help us out by using an example.
Hint 4:
The other line of thought is a tad bit complicated but essentially it builds on the idea of placing each element in its original 
position while keeping track of the element originally in that position. Basically, at every step, we place an element in its 
rightful position and keep track of the element already there or the one being overwritten in an additional variable. We can't do 
this in one linear pass and the idea here is based on cyclic-dependencies between elements.

### Testcase:
---
[1,2,3,4,5,6,7]
3
[-1,-100,3,99]
2


### Code:
---
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        
    }
};


*/
// Solution: --------------------------------------

#include <vector>
#include <algorithm> // For std::reverse

class Solution {
public:
    void rotate(std::vector<int>& nums, int k) {
        // Normalize k to ensure it's within the bounds of the array length.
        k %= nums.size();

        // Step 1: Reverse the entire array.
        std::reverse(nums.begin(), nums.end());

        // Step 2: Reverse the first k elements to correct their order.
        std::reverse(nums.begin(), nums.begin() + k);

        // Step 3: Reverse the remaining n-k elements.
        std::reverse(nums.begin() + k, nums.end());
    }
};


// Description: ===================================
/*
To solve the "Rotate Array" task, we can employ a method that is both efficient and in-place. This approach involves reversing 
segments of the array to achieve the desired rotation without using extra space for another array.

The steps for this method are as follows:

1. Normalize `k` to ensure it is within the bounds of the array length (since rotating the array by its length brings it back to 
   the original position). We do this by taking `k % nums.size()`.
2. Reverse the entire array. This brings the elements that should be at the beginning of the rotated array towards the front, but 
   in the wrong order.
3. Reverse the first `k` elements, which corrects the order of the elements that were moved to the front.
4. Reverse the remaining `n-k` elements to correct their order as well.

### Description:
---
This solution employs a clever use of array reversal to achieve the desired rotation in-place, with `O(1)` extra space and `O(n)` time 
complexity, where `n` is the length of the array. The normalization of `k` ensures that the number of rotations is within the array 
bounds, preventing unnecessary rotations. By reversing the entire array, we bring the last `k` elements to the front but in reverse order. 
We then correct the order of these `k` elements and the rest of the array through further reversals. This method efficiently achieves the 
rotation without additional memory for a secondary array, adhering to the problem's constraints and follow-up challenge.

*/
