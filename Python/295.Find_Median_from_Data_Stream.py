"""
# 295. Find Median from Data Stream.

# Topic: Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream.

# Task:
------------
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, 
and the median is the mean of the two middle values.

- For example, for arr = [2,3,4], the median is 3.
- For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.
 

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
-10^5 <= num <= 10^5
There will be at least one element in the data structure before calling findMedian.
At most 5 * 10^4 calls will be made to addNum and findMedian.
 

Follow up:
If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?


# Testcase:
--------------
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]


# Code:
----------
class MedianFinder:

    def __init__(self):
        

    def addNum(self, num: int) -> None:
        

    def findMedian(self) -> float:
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


"""
# Solution:
import heapq

class MedianFinder:
    def __init__(self):
        # Initialize two heaps: 
        # 'left' is a max heap for the smaller half of the numbers.
        # 'right' is a min heap for the larger half of the numbers.
        self.left = []  # max heap (using negation to simulate max heap behavior)
        self.right = [] # min heap

    def addNum(self, num: int) -> None:
        # Add number to the appropriate heap
        # If 'left' is empty or 'num' is smaller than the largest in 'left', add to 'left'
        if not self.left or num < -self.left[0]:
            heapq.heappush(self.left, -num)  # Negate to maintain max heap property
        else:
            # Otherwise, add to 'right'
            heapq.heappush(self.right, num)

        # Balance the heaps to make sure their sizes differ at most by 1
        # If 'left' has more than one extra element, move the top element to 'right'
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            # If 'right' has more elements, move the top element to 'left'
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        # Find the median
        # If both heaps are of equal size, median is the average of the tops of both heaps
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            # If heaps are of unequal size, median is the top of the larger heap
            return -self.left[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



# Description:
'''
To implement the MedianFinder class, we can use two heaps (priority queues): a max heap to store the smaller 
half of the numbers and a min heap to store the larger half. This approach ensures that the median can always
be found or calculated efficiently.

Here's a detailed explanation of the implementation:
------------------------------------------------------
1. Two Heaps Structure:
    - A max heap (left) to store the smaller half of the numbers.
    - A min heap (right) to store the larger half of the numbers.

2. Adding a Number (addNum):
    - Add the new number to one of the heaps.
    - If it's smaller than the current median, add it to the max heap (left). Otherwise, add it to the min heap (right).
    - Balance the heaps: if one heap contains more than one additional element than the other, move the top element from 
      the bigger heap to the smaller one.

3. Finding the Median (findMedian):
    - If the heaps have an equal number of elements, the median is the average of the tops of the two heaps.
    - If one heap has more elements, the median is the top of the larger heap.


This code efficiently maintains the order of elements to quickly retrieve the median. Note that Python's heapq is a min heap,
so we store negative values in left to simulate a max heap.

Follow-up Optimization:
---------------------------
* Range [0, 100]: If all numbers are in the range [0, 100], we could use an array of size 101 to count the occurrences 
  of each number. Finding the median would then involve iterating over this array to find the middle value.

* 99% in Range [0, 100]: In this case, we could combine the array approach for numbers in [0, 100] with a min and max 
  heap for numbers outside this range. This would optimize for the common case while still handling outliers effectively.

'''
