// 287. Find the Duplicate Number.

// Topic: Array, Two Pointers, Binary Search, Bit Manipulation.


/*
### Task:
---
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3

Constraints:
1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 
Follow up:
-How can we prove that at least one duplicate number must exist in nums?
-Can you solve the problem in linear runtime complexity?


### Testcase:
---
[1,3,4,2,2]
[3,1,3,4,2]
[3,3,3,3,3]


### Code:
---
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>

class Solution {
public:
    int findDuplicate(std::vector<int>& nums) {
        // Initialize two pointers for the "tortoise and hare" step.
        int tortoise = nums[0];
        int hare = nums[0];

        // Phase 1: Start the tortoise and hare race to find a point in the cycle.
        // The hare moves twice as fast as the tortoise.
        do {
            tortoise = nums[tortoise]; // Moves one step.
            hare = nums[nums[hare]];   // Moves two steps.
        } while (tortoise != hare); // Continue until they meet inside the loop.

        // At this point, we have detected a cycle, which confirms a duplicate exists.

        // Phase 2: Find the entrance to the cycle, which is the duplicate element.
        // Move tortoise back to the start.
        tortoise = nums[0];

        // Move tortoise and hare at the same pace to find the entrance of the cycle.
        while (tortoise != hare) {
            tortoise = nums[tortoise]; // Tortoise moves one step.
            hare = nums[hare];         // Hare also moves one step.
        }

        // The point where they meet is the start of the cycle, which is the duplicate number.
        return hare; // You can return either hare or tortoise as they are equal at this point.
    }
};


// Description: ===================================
/*
To solve the problem of finding the duplicate number in an array where each integer is between 1 and n (inclusive) and the array size 
is n+1, we can use the "Floyd's Tortoise and Hare" cycle detection algorithm. This approach is particularly useful because it meets 
the constraints of not modifying the original array and using only constant extra space.

The core idea behind this algorithm is to treat the array as if it were a linked list where each element's value is a pointer to the 
next node. In this context, the presence of a duplicate number creates a cycle. By using two pointers that move at different speeds 
(tortoise and hare), a cycle can be detected, and the duplicate number can be found.

Here's how the algorithm works:

1. **Phase 1 (Detecting the cycle):** Use two pointers, one moving one step at a time (tortoise) and the other moving two steps at a 
     time (hare). Move these pointers until they meet within the cycle, which indicates that a cycle exists.

2. **Phase 2 (Finding the entrance to the cycle):** Once a cycle is detected, keep one pointer where the two pointers met and move 
     the other pointer back to the start of the array. Then, move both pointers one step at a time until they meet again. The meeting 
     point is the duplicate number.

### Description:
---
This solution uses Floyd's Tortoise and Hare algorithm for cycle detection. In the context of this problem, the cycle occurs because 
of the duplicate number acting as an entrance to a cycle within the virtual linked list created by the array indices and values. The 
first phase is to detect the cycle using two pointers moving at different speeds. Once the cycle is detected, the second phase locates 
the entrance to the cycle, which corresponds to the duplicate number. This approach is efficient, with a linear time complexity (O(n)) 
and constant space complexity (O(1)), fulfilling the problem's constraints and follow-up challenges.

*/