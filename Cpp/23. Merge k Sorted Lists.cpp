// 23. Merge k Sorted Lists.         - HARD -


// Topic: Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort.


/*
### Task:
---
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 
Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.


### Testcase:
---
[[1,4,5],[1,3,4],[2,6]]
[]
[[]]


### Code:
---
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 *//*
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
    }
};
*/


// Solution: ------------------------------------------------------------------------

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // Custom comparator for the priority queue that compares the value of two nodes
        auto compare = [](ListNode* a, ListNode* b) { return a->val > b->val; };
        
        // Initialize a priority queue with the custom comparator. The queue will store ListNode* and sort them by their values in ascending order.
        priority_queue<ListNode*, vector<ListNode*>, decltype(compare)> pq(compare);

        // Populate the priority queue with the head of each non-empty list
        for (ListNode* list : lists) {
            if (list) pq.push(list); // Only add non-null head nodes to the queue
        }

        // Create a dummy head node for the merged list. This simplifies list construction and avoids special cases for the head.
        ListNode dummy(0);
        ListNode* current = &dummy; // This pointer will traverse and build the merged list

        // While the priority queue is not empty, continue removing the smallest element and adding it to the merged list
        while (!pq.empty()) {
            ListNode* smallest = pq.top(); // Get the smallest node from the queue
            pq.pop(); // Remove this node from the queue

            current->next = smallest; // Add the smallest node to the merged list
            current = current->next; // Move the pointer forward

            // If the smallest node has a next node, add that node to the queue for future consideration
            if (smallest->next) pq.push(smallest->next);
        }

        // The dummy node's next pointer points to the head of the merged list. Return this node.
        return dummy.next;
    }
};



// Description: ===================================
/*
Merging k sorted linked lists into one sorted linked list can be efficiently achieved using a priority queue (min heap) 
to keep track of the smallest elements across all lists at any given time. This approach has a better time complexity compared 
to naively merging lists one by one.


Here's a step-by-step guide to implementing this solution:

1. **Initialize a priority queue**: The priority queue will store pairs consisting of a node's value and the node itself. The queue will automatically order these pairs by their values, ensuring the smallest element is always at the front.

2. **Populate the priority queue**: Iterate through the initial list of linked lists, and for each non-empty list, add its head node to the priority queue.

3. **Merge process**: Create a new dummy head for the merged list and maintain a current pointer to build the merged list. While the priority queue is not empty, repeatedly remove the smallest element from the queue, add it to the merged list, and if the removed element has a next node, add that node to the queue. This ensures that at each step, the smallest available node across all lists is added to the merged list.

4. **Return the merged list**: Once the priority queue is empty, all nodes have been merged into the new list. Return the node following the dummy head, which is the actual start of the merged list.

### Description:

- **Priority Queue**: The priority queue ensures that we always have access to the smallest node across all lists. By using a custom comparator, we maintain the queue in ascending order based on node values.

- **Merging**: By always choosing the smallest node (the top of the priority queue) and moving it to the merged list, we maintain the sorted order. After adding a node to the merged list, we insert its next node into the priority queue, ensuring that all nodes from all lists are considered.

- **Efficiency**: This approach is efficient because it minimizes comparisons and takes advantage of the heap's properties to quickly find the smallest element. The time complexity is O(N log k), where N is the total number of nodes across all lists, and k is the number of lists. This is because each insertion and removal operation in the priority queue has a time complexity of O(log k), and we perform these operations for each of the N nodes.

*/
