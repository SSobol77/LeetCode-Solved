// 160. Intersection of Two Linked Lists.


// Topic: Hash Table, Linked List, Two Pointers.


/*
### Task:
---
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:
The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

   - intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
   - listA - The first linked list.
   - listB - The second linked list.
   - skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
   - skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.

The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. 
If you correctly return the intersected node, then your solution will be accepted.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Constraints:
The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 10^4
1 <= Node.val <= 10^5
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
 
Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?

### Testcase:
---
8
[4,1,8,4,5]
[5,6,1,8,4,5]
2
3
2
[1,9,1,2,4]
[3,2,4]
3
1
0
[2,6,4]
[1,5]
3
2


### Code:
---
//*
//* Definition for singly-linked list.
//* struct ListNode {
//*     int val;
//*     ListNode *next;
//*     ListNode(int x) : val(x), next(NULL) {}
//* };
// 
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // Initialize two pointers for both lists
        ListNode *pA = headA, *pB = headB;

        // Continue traversing until both pointers meet or reach the end of lists
        while (pA != pB) {
            // If pointer A reaches the end, switch to headB; otherwise, move to the next node
            pA = pA == nullptr ? headB : pA->next;
            // If pointer B reaches the end, switch to headA; otherwise, move to the next node
            pB = pB == nullptr ? headA : pB->next;
        }

        // Return either the intersection node or null
        return pA;
    }
};

// Description: ===================================
/*
To find the intersection node of two singly linked lists with optimal time and space complexity, we can use the two pointers technique. 
This approach does not require additional data structures like a hash table and thus uses O(1) memory, aligning with the follow-up 
requirement.

### Algorithm:
1. **Initialize Two Pointers**: Start two pointers `pA` and `pB` at the heads of the two lists, `headA` and `headB`, respectively.
2. **Traverse the Lists**: Move `pA` and `pB` forward through the lists.
3. **Switch Lists**: When `pA` reaches the end of list A, continue from the head of list B. Similarly, when `pB` reaches the end of 
     list B, continue from the head of list A.
4. **Intersection or End**: The pointers `pA` and `pB` will either meet at the intersection node or reach the end of both lists 
     simultaneously (null), indicating there is no intersection.

### Why This Works:
The idea is to offset the difference in lengths between the two lists. By switching lists, both pointers traverse the same total 
length (length of A + length of B). If the lists intersect, the pointers will meet at the intersection node. Otherwise, they will 
both reach the end (null).

### Comments:

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // Initialize pointers to traverse both lists
        ListNode *pA = headA, *pB = headB;

        // Loop until both pointers meet or both reach the end (null)
        while (pA != pB) {
            // Switch list A pointer to headB upon reaching the end, and vice versa
            pA = pA == nullptr ? headB : pA->next;
            pB = pB == nullptr ? headA : pB->next;
        }

        // If there is an intersection, pA (or pB) will point to the intersection node;
        // otherwise, it will be null, indicating no intersection.
        return pA;
    }
};


This solution efficiently identifies the intersection node (if one exists) with a time complexity of O(m + n) and a space complexity 
of O(1), where m and n are the lengths of the two linked lists.

*/
