// 1642. Furthest Building You Can Reach.


// Topic: Array, Greedy, Heap (Priority Queue).


/*
### Task:
---
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),
    - If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
    - If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

Example 1:
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

Example 2:
Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7

Example 3:
Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3
 
Constraints:
1 <= heights.length <= 10^5
1 <= heights[i] <= 10^6
0 <= bricks <= 10^9
0 <= ladders <= heights.length

Hint 1:
Assume the problem is to check whether you can reach the last building or not.
Hint 2:
You'll have to do a set of jumps, and choose for each one whether to do it using a ladder or bricks. It's always optimal to use ladders in the largest jumps.
Hint 3:
Iterate on the buildings, maintaining the largest r jumps and the sum of the remaining ones so far, and stop whenever this sum exceeds b.

### Testcase:
---
[4,2,7,6,9,14,12]
5
1
[4,12,2,7,3,18,20,3,19]
10
2
[14,3,19,3]
17
0


### Code:
---
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        
    }
};

*/
// Solution: ---------------------------------------------------------------------------------------------

#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        // Min-heap to store the heights of jumps where ladders are used
        priority_queue<int, vector<int>, greater<int>> minHeap;

        // Iterate through each building
        for (int i = 0; i < heights.size() - 1; ++i) {
            // Calculate the height difference to the next building
            int diff = heights[i + 1] - heights[i];

            // If the next building is higher
            if (diff > 0) {
                // If we have a ladder, use it for this jump
                if (ladders > 0) {
                    minHeap.push(diff); // Add the jump height to the min-heap
                    --ladders; // Decrement the ladder count
                } 
                // If no ladders left but the smallest ladder jump is smaller than the current jump
                else if (!minHeap.empty() && minHeap.top() < diff) {
                    // Use bricks for the smallest ladder jump
                    bricks -= minHeap.top();
                    minHeap.pop(); // Remove the smallest ladder jump from the heap
                    minHeap.push(diff); // Use a ladder for the current jump instead
                } 
                // If no ladders or not beneficial to replace, use bricks
                else {
                    bricks -= diff;
                }
                // If we run out of bricks, we can't proceed further
                if (bricks < 0) {
                    return i; // Return the furthest building we can reach
                }
            }
        }
        // If we can reach the last building, return its index
        return heights.size() - 1;
    }
};




// Description: ========================================================================================================
/*
To solve the "Furthest Building You Can Reach" problem, we can use a min-heap to keep track of the largest jumps we 
have made so far, and use ladders for those jumps. For other jumps that are smaller, we can use bricks. If at any point 
we run out of bricks, we cannot proceed further. This approach ensures that we use ladders for the largest jumps, which is optimal.

Here's a step-by-step breakdown of the solution:
1. Iterate through the array of building heights.
2. For each jump (where the next building is higher than the current one), calculate the height difference.
3. If we have a ladder, use it for the jump and add the height difference to the min-heap. This is because we want to keep 
   track of the largest jumps we have used ladders for, in case we need to replace one of them with bricks later.
4. If we don't have a ladder, check if the min-heap is not empty and the smallest jump we used a ladder for 
   (top of the min-heap) is smaller than the current jump. If so, replace that jump with bricks (remove it from the heap 
   and add its height difference to the bricks used), and use a ladder for the current jump.
5. If we can't use a ladder, use bricks for the jump. If we don't have enough bricks, return the current index as the f
   urthest we can reach.
6. If we reach the end of the array, return the last index.

This solution iterates through the buildings once, making it O(N log N) due to the heap operations, where N is the number of buildings. 
The space complexity is O(L), where L is the number of ladders, due to the min-heap storing at most L elements.

*/
