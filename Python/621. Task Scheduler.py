# 621. Task Scheduler

# Topics: Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting.

"""
# Task:
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.
​Return the minimum number of intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

Constraints:
1 <= tasks.length <= 10^4
tasks[i] is an uppercase English letter.
0 <= n <= 100


# Testcase:
["A","A","A","B","B","B"]
2
["A","C","A","B","D","B"]
1
["A","A","A", "B","B","B"]
3

# Code:
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
"""

## Solution:

import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        task_counts = Counter(tasks)  # Count frequency of each task
        max_heap = [-cnt for cnt in task_counts.values()]  # Max heap of task frequencies
        heapq.heapify(max_heap)  # Convert list to heap

        intervals = 0
        while max_heap:
            temp = []  # Store frequencies of tasks executed in this round
            for _ in range(n + 1):  # Up to n+1 tasks in a round
                if max_heap:
                    cnt = heapq.heappop(max_heap) + 1  # Execute the task with the highest frequency
                    if cnt < 0:  # If there are still tasks left, add to temp
                        temp.append(cnt)
                intervals += 1  # Count this interval
                if not max_heap and not temp:  # No more tasks left
                    break

            for item in temp:  # Re-add the updated frequencies to the heap
                heapq.heappush(max_heap, item)

        return intervals

# Test
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
solution = Solution()
result = solution.leastInterval(tasks, n)
print(result)  # This should print the minimum number of intervals needed


## Description:
'''
To solve the "Task Scheduler" problem, we'll use a greedy approach. The core idea is that the tasks with the highest frequency determine the minimum time required. We'll count the frequency of each task and use a max heap (priority queue) to keep these frequencies sorted, with the most frequent tasks at the top.

### Approach:
1. **Count Task Frequencies**: Determine how often each task occurs.
2. **Use a Max Heap**: Store the task frequencies in a max heap so the task with the highest frequency is always accessible at the top.
3. **Process Tasks in Intervals**: For each interval (up to `n+1` intervals, since we can run `n+1` tasks before a task can repeat), select the most frequent tasks to execute.
4. **Decrease Frequencies and Cool Down**: After executing a task, decrease its frequency (since one instance of the task is done) and temporarily store this updated frequency. This task is now in its "cooling" period.
5. **Handle Idle Times**: If no tasks are eligible for execution (i.e., all remaining tasks are in their cooling period), the CPU remains idle for that interval.
6. **Repeat Until Done**: Continue this process until all tasks are executed.

The total time taken is the sum of all intervals, including the idle times.

### My pseudocode:

import heapq  # For the priority queue

def leastInterval(tasks, n):
    # Step 1: Count task frequencies
    task_counts = collections.Counter(tasks)
    # Step 2: Create a max heap with negative frequencies for max heap behavior
    max_heap = [-cnt for cnt in task_counts.values()]
    heapq.heapify(max_heap)  # Turn the list into a heap

    intervals = 0
    while max_heap:
        # Temporary storage for tasks executed in the current round
        temp = []
        for _ in range(n + 1):  # Process up to n+1 tasks in a round
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1  # Execute the most frequent task
                if cnt:  # If there are tasks left, add to temporary storage
                    temp.append(cnt)
            intervals += 1  # Count this interval
            if not max_heap and not temp:  # No more tasks left
                break

        # Re-add the updated frequencies to the heap after the cooling period
        for item in temp:
            heapq.heappush(max_heap, item)

    return intervals

This pseudocode outlines a high-level solution to the task scheduler problem. It provides a solid foundation for writing a detailed implementation, handling the core logic of scheduling tasks with cooling periods.

'''
