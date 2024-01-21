# 295. Find Median from Data Stream

# Topic: Two Pointers, Design, Sorting, Heap(Priority Queue), Data Stream.

'''
# Task:
--------
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, 
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.
 

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


# Testscase:
-------------
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]


'''

# Solution:
import heapq

class MedianFinder:
    def __init__(self):
        # Max heap for the lower half
        self.lower_half = []
        # Min heap for the upper half
        self.upper_half = []

    def addNum(self, num: int) -> None:
        # Add to lower half (max heap), then move the largest element to upper half
        heapq.heappush(self.lower_half, -num)
        heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))

        # Balance the heaps: if upper half has more elements, move one back to lower half
        if len(self.upper_half) > len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))

    def findMedian(self) -> float:
        # If heaps are of equal size, median is the average of the roots
        # Otherwise, median is the root of the heap with more elements
        if len(self.lower_half) > len(self.upper_half):
            return -self.lower_half[0]
        return (-self.lower_half[0] + self.upper_half[0]) / 2.0

# Test cases
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())  # Output: 1.5
medianFinder.addNum(3)
print(medianFinder.findMedian())  # Output: 2.0

'''
In this implementation:

Two heaps are used: self.lower_half is a max heap (using negation to simulate a max heap with Python's 
in heap implementation), and self.upper_half is a min heap.
Each new number is first added to self.lower_half. The largest number from self.lower_half is then moved
 to self.upper_half to maintain the order.
If self.upper_half becomes larger than self.lower_half, the smallest element from self.upper_half is moved
 back to self.lower_half to maintain the balance.
findMedian calculates the median based on the sizes of the heaps. If they are equal, the median is the
average of the two roots. Otherwise, it is the root of the larger heap.
This approach ensures that the median is always accessible in constant time, while additions to the data 
structure have a logarithmic time complexity.

'''