// 55. Jump Game.


// Topic: Array, Dynamic Programming, Greedy.


/*
### Task:
---
You are given an integer array nums. You are initially positioned at the array's first index, and each element 
in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5

### Testcase:
---
[2,3,1,1,4]
[3,2,1,0,4]

### Code:
---
class Solution {
public:
    bool canJump(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0; // Initialize the maximum reachable index to 0
        int target = nums.size() - 1; // The target index we want to reach, which is the last index of the array

        // Iterate through the array
        for (int i = 0; i <= maxReach; ++i) {
            // Update the maximum reachable index if the current position allows us to reach further
            maxReach = max(maxReach, i + nums[i]);

            // If the maximum reachable index is greater than or equal to the target index, return true
            if (maxReach >= target) {
                return true;
            }
        }

        // If we exit the loop and haven't reached the target, return false
        return false;
    }
};


// Description: ===================================
/*
This solution uses a greedy approach to solve the Jump Game problem. The key idea is to keep track of the maximum 
reachable index (`maxReach`) as we iterate through the array. At each step, we update `maxReach` based on the current 
index and the jump length from that index (`nums[i]`). If at any point `maxReach` is greater than or equal to the target 
index (the last index of the array), we can reach the end, and the function returns `true`. If we reach a point where the 
current index is greater than `maxReach`, it means we are stuck and cannot move forward, so the function returns `false`.

### Complexity Analysis:
- **Time Complexity**: O(n), where n is the length of the array. We make a single pass through the array, with each element being 
    visited at most once.
- **Space Complexity**: O(1), as the solution uses a constant amount of space regardless of the input size.

*/
