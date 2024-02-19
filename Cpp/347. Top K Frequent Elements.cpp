// 347. Top K Frequent Elements.


// Topic: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect.


/*
### Task:
---
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

### Testcase:
---
[1,1,1,2,2,3]
2
[1]
1

### Code:
---
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>
#include <unordered_map>
#include <queue>
#include <utility> // For std::pair

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Step 1: Count the frequency of each element
        unordered_map<int, int> frequencyMap;
        for (int num : nums) {
            frequencyMap[num]++;
        }

        // Step 2: Use a min-heap to keep the top k frequent elements
        // The heap will store pairs of (-frequency, element)
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;

        for (auto& [num, freq] : frequencyMap) {
            minHeap.push({freq, num});
            // If the heap size exceeds k, remove the least frequent element
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }

        // Step 3: Build the result vector from the heap
        vector<int> topKElements;
        while (!minHeap.empty()) {
            topKElements.push_back(minHeap.top().second); // Get the element value
            minHeap.pop();
        }

        return topKElements;
    }
};

// Description: ===================================
/*
To solve the "Top K Frequent Elements" problem, we can use a combination of a hash table to count the frequency of each element and a heap (priority queue) to find the top k frequent elements. This approach ensures that we meet the constraint of having a time complexity better than O(n log n).

### Steps:
1. **Count Frequencies**: Use a hash table (e.g., `unordered_map` in C++) to count the frequency of each element in the array.
2. **Use a Min-Heap**: Create a min-heap (priority queue in C++) to keep track of the top k frequent elements. The heap will store pairs of the frequency and the element value. The reason for using a min-heap instead of a max-heap is to efficiently remove the least frequent elements until we retain only the top k frequent elements.
3. **Build the Result**: Extract the elements from the heap to build the result vector.


### Explanation:
- The `frequencyMap` counts the occurrences of each element in `nums`.
- The `minHeap` is used to maintain the top k frequent elements. By using a min-heap, we ensure that when the heap size exceeds k, we can efficiently remove the element with the lowest frequency, thus always keeping the top k frequent elements.
- Finally, we extract elements from the heap to form the result. Since we're using a min-heap and we want the top k frequent elements, the order of elements in the result vector is not necessarily sorted by frequency.

### Complexity:
- **Time Complexity**: O(N log k) where N is the number of elements in the array. Inserting an element into a heap of size k takes O(log k) time, and we do this for each of the N elements.
- **Space Complexity**: O(N) for storing the frequency map and the heap, where N is the number of unique elements in `nums`.



*/