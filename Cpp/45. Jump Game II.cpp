// 45. Jump Game II.


// Topic: Array, Dynamic Programming, Greedy.


/*
### Task:
---
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

### Testcase:
---
[2,3,1,1,4]
[2,3,0,1,4]


### Code:
---
class Solution {
public:
    int jump(vector<int>& nums) {
        
    }
};


*/
// Solution: --------------------------------------

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int maxReach = 0; // Tracks the farthest we can reach
        int lastJumpMax = 0; // Tracks the farthest we can reach with the current number of jumps
        int jumps = 0; // Counts the number of jumps

        // Loop through the array, but not including the last element
        // because we jump from the current position to a future position
        for (int i = 0; i < n - 1; ++i) {
            // Update the farthest we can reach from the current position
            maxReach = max(maxReach, i + nums[i]);

            // If we've reached the end of the current jump's reach,
            // it's time to increase the jump count
            if (i == lastJumpMax) {
                jumps++; // Increment the jump count
                lastJumpMax = maxReach; // Update the last jump's max reach
            }
        }

        return jumps;
    }
};


// Description: ===================================
/*
The Jump Game II problem is a classic example of a greedy algorithm applied to an array. The task is to find the minimum number of jumps required to reach the last index of a non-negative integer array, starting from the first index. Each element in the array represents the maximum jump length at that position.

### Approach:
The solution involves iterating through the array while keeping track of the current maximum reach, the maximum reach for the next jump, and the number of jumps made so far. The key idea is to extend the reach as far as possible with each jump, thereby minimizing the total number of jumps.

1. **Initialize Variables**: 
   - `maxReach` to keep track of the furthest index that can be reached at any point.
   - `lastJumpMax` to store the furthest index that can be reached with the current number of jumps.
   - `jumps` to count the number of jumps needed to reach the end.

2. **Iterate Through the Array**:
   - For each position, update `maxReach` to be the maximum of the current `maxReach` and the index plus the value at that index (`i + nums[i]`), which represents the furthest we can reach from the current position.
   - When the current index `i` reaches `lastJumpMax`, it indicates that to go further, a jump is necessary. Therefore, increment `jumps` and update `lastJumpMax` to `maxReach`, extending the reach for the next jump.

3. **End Condition**: 
   - The loop iterates until the second-to-last element, as the goal is to reach (not necessarily jump from) the last index. When `i` equals `lastJumpMax`, it means a jump is made to the furthest reachable index so far, indicating the need for another jump if the last index hasn't been reached yet.

4. **Return the Number of Jumps**: 
   - The `jumps` variable, which has been incremented each time a new jump is made to extend the reach, will hold the minimum number of jumps required to reach the last index.

### Complexity Analysis:
- **Time Complexity**: O(n), where n is the length of the array. The algorithm makes a single pass through the array, with each element being visited exactly once.
- **Space Complexity**: O(1), as the solution uses a constant amount of space regardless of the input size.

### Conclusion:
This greedy approach efficiently solves the problem by always making the optimal choice at each step, aiming to reach as far as possible with each jump, thereby minimizing the total number of jumps required to reach the end of the array.



*/