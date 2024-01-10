// 23. Merge k Sorted Lists

/*
### Task:
----------
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

#Example 2:
Input: lists = []
Output: []

#Example 3:
Input: lists = [[]]
Output: []

Constraints:
#k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.

### Code: 
--------
 
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 *
 
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
    }
};
*/

// Solution:
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // Define a custom comparison function for the priority queue
        auto cmp = [](ListNode* a, ListNode* b) {
            return a->val > b->val; // We want a min-heap, so the smaller value comes to the top
        };
        
        // Create a priority queue (min-heap) using the custom comparison function
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> pq(cmp);
        
        // Push the head of each list into the priority queue
        for (ListNode* list : lists) {
            if (list) {
                pq.push(list);
            }
        }
        
        // Create a dummy node to simplify the list merging
        ListNode dummy(0);
        ListNode* current = &dummy; // Pointer to the current node in the merged list
        
        // While the priority queue is not empty
        while (!pq.empty()) {
            // Pop the smallest element from the priority queue
            ListNode* node = pq.top();
            pq.pop();
            
            // Append the node to the merged list
            current->next = node;
            current = current->next;
            
            // If the current node has a next element in its original list
            if (node->next) {
                // Push the next element from the same list into the priority queue
                pq.push(node->next);
            }
        }
        
        return dummy.next; // Return the merged sorted linked list starting from the next of the dummy node
    }
};


// Description:
/*
This code uses a priority queue (min-heap) to keep track of the smallest elements from all lists. It starts 
by pushing the heads of all lists into the priority queue. Then, it repeatedly pops the smallest element 
from the priority queue, appends it to the result list, and pushes the next element from the same list into 
the priority queue. This process continues until the priority queue is empty.

The result is a merged sorted linked list, and the time complexity of this solution is O(N log k), where N is 
the total number of nodes in all linked lists, and k is the number of linked lists.

*/
