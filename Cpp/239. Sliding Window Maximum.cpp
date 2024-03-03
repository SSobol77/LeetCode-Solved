// 239. Sliding Window Maximum.        - HARD -


// Topic: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue.


/*
### Task:
---
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

Hint 1:
How about using a data structure such as deque (double-ended queue)?
Hint 2:
The queue size need not be the same as the window’s size.
Hint 3:
Remove redundant elements and the queue should store only elements that need to be considered.

### Testcase:
---
[1,3,-1,-3,5,3,6,7]
3
[1]
1


### Code:
---
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq; // Deque to store indices of nums
        vector<int> result;

        for (int i = 0; i < nums.size(); ++i) {
            // Remove indices that are out of the current window
            if (!dq.empty() && dq.front() == i - k) {
                dq.pop_front();
            }

            // Remove indices of all elements smaller than the current element
            while (!dq.empty() && nums[i] > nums[dq.back()]) {
                dq.pop_back();
            }

            // Add the current element's index
            dq.push_back(i);

            // If the window size is reached, add the maximum to the result
            if (i >= k - 1) {
                result.push_back(nums[dq.front()]);
            }
        }

        return result;
    }
};

// Description: ===================================
/*
To solve the "Sliding Window Maximum" problem, we can use a Deque (double-ended queue) to efficiently track the maximum value within 
each window of size `k`. The key is to maintain the Deque in such a way that it always contains potential candidates for the maximum 
of the current window, with the largest value at the front.

Here's a step-by-step approach:

1. **Initialize**: Create a Deque to store indices of elements in `nums`. This will allow easy access to the elements while also being 
able to efficiently remove elements from both ends of the Deque.

2. **Process the first `k` elements**: Iterate through the first `k` elements of `nums` and for each element, remove from the Deque all 
elements that are smaller than the current element (since they cannot be the maximum), then add the index of the current element to the 
Deque. This ensures that the Deque's front always represents the maximum of the current window.

3. **Process the rest of the array**: Iterate through the remaining elements in `nums`. For each new element, remove indices from the 
front of the Deque if they are out of the current window's bounds (i.e., if `Deque.front() <= i - k`). Then, as before, remove all elements 
from the Deque that are smaller than the current element and add the index of the current element. After this, the front of the Deque will 
represent the maximum of the current window, which can be added to the result array.

4. **Return Result**: After processing all elements in `nums`, return the result array containing the maximum of each window.

### Description:

This solution leverages a Deque to efficiently find the maximum element in each sliding window of size `k` across the array `nums`. 
The Deque stores indices of `nums` and is maintained in a decreasing order, ensuring the front of the Deque always contains the index 
of the maximum element in the current window. By carefully adding new elements and removing those that are either out of the window's 
bounds or smaller than the current element, the Deque remains an effective tool for tracking the maximum value as the window slides 
through the array. This approach guarantees linear time complexity, O(n), where n is the number of elements in `nums`, as each element 
is added and removed from the Deque at most once.

*/
