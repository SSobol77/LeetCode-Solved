// 295. Find Median from Data Stream.       - HARD -


// Topic: Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream.


/*
### Task:
---
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 
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

### Testcase:
---
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]


### Code:
---
class MedianFinder {
public:
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        
    }
    
    double findMedian() {
        
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */

/**/

// Solution: ----------------------------------------------------------------------------------------------------------------

#include <queue>
#include <vector>

class MedianFinder {
    std::priority_queue<int> maxHeap; // Max heap for the smaller half
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap; // Min heap for the larger half

public:
    MedianFinder() {
        // Constructor doesn't need to do anything
    }
    
    void addNum(int num) {
        // Add to max heap if number is smaller than or equal to top of max heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            // Otherwise, add to min heap
            minHeap.push(num);
        }

        // Rebalance heaps to ensure the size difference is not more than 1
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }
    
    double findMedian() {
        // If the total number of elements is odd, the median is the top of the max heap
        if (maxHeap.size() > minHeap.size()) {
            return maxHeap.top();
        } else {
            // If it's even, the median is the average of the tops of both heaps
            return (maxHeap.top() + minHeap.top()) / 2.0;
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */




// Description: ===================================================================================================================
/*
To implement the MedianFinder class that efficiently finds the median of a data stream, we can use two heaps: a max heap to store 
the smaller half of the numbers and a min heap to store the larger half. This approach ensures that the heaps are balanced or that 
the max heap has at most one more element than the min heap, allowing us to efficiently compute the median.

# Key Operations:
addNum(int num): Adds a number to the data structure. If the number is less than or equal to the top of the max heap, 
                 it goes into the max heap; otherwise, it goes into the min heap. After adding, if the size difference 
                 between the heaps is more than one, we rebalance them by moving an element from the larger heap to the smaller heap.

findMedian(): Returns the median of all elements. If the total number of elements is odd, the median is the top of the max heap. 
              If it's even, the median is the average of the tops of both heaps.


It defines a MedianFinder class that uses two heaps to efficiently track the median of a dynamically changing data stream. The addNum 
method ensures that numbers are added to the appropriate heap and that the heaps are rebalanced if necessary, while the findMedian method 
computes the median based on the sizes and top values of the heaps.

*/