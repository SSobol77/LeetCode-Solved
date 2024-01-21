"""
# 239. Sliding Window Maximum

# Topic: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue.


# Task:
---------
You are given an array of integers nums, there is a sliding window of size k which is moving from 
the very left of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

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



# Testcase:
-------------
[1,3,-1,-3,5,3,6,7]
3
[1]
1


# Code:
-------------
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        


"""
# Solution:
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        if k == 1:
            return nums

        # Initialize deque for indices and result list for max values of each window
        deq = deque()
        result = []

        for i in range(len(nums)):
            # Remove indices from the front of the deque that are not in the current window
            while deq and deq[0] < i - k + 1:
                deq.popleft()

            # Remove elements from the back of the deque if they are smaller than the current element
            # This maintains the decreasing order of elements in the deque
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

            # Add the current element's index to the deque
            deq.append(i)

            # If we have processed at least k elements, add the front element of deque to the result
            # The front element of the deque is the max of the current window
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result


# Description:
'''
To solve this problem, we can use a data structure like a deque (double-ended queue) to keep track of the elements
that could potentially be the maximum in the current and future windows. The key idea is to maintain a decreasing 
sequence in the deque so that the front of the deque always holds the maximum element of the current window.

Here's how to implement the solution:
----------------------------------------
1. Initialize a Deque: Use a deque to store indices of elements in nums.

2. Process First k Elements: For the first k elements, remove elements from the back of the deque if they are less than 
   the current element. This ensures the deque is decreasing. Then, add the current element's index to the deque.

3. Process Remaining Elements: For the rest of the elements in nums, the front of the deque is the maximum of the previous 
   window. Add it to the output list. Before processing the current element, remove indices from the front of the deque if 
   they are out of the current window's range (i.e., index <= current index - k). Then, similar to the first step, remove 
   elements from the back of the deque if they are less than the current element and add the current element's index to 
   the deque.

4. Add Maximum for Last Window: After processing all elements, add the front of the deque to the output list as it is the 
   maximum of the last window.

In this code:
------------------
* We start by handling edge cases: if nums is empty or k is 0, we return an empty list. If k is 1, we return the original 
  list as every element forms a window.
* The deque deq is used to store indices of nums. The deque is maintained in such a way that its elements (indices) are 
  in decreasing order of their corresponding values in nums.
* In each iteration, we first remove indices that are not in the current window (i.e., they are older than the current 
  window's starting index).
* Then, we remove elements from the back of the deque if they are smaller than the current element, as they cannot be 
  the maximum in the current or future windows.
* We add the index of the current element to the deque and, if the window size is at least k, we add the value 
  corresponding to the front index of the deque to result. This value is the maximum for the current window.
* This way, the algorithm efficiently keeps track of the maximum in each window as the window slides through nums.

'''
