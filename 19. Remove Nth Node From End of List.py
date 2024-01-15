# 19. Remove Nth Node From End of List.

# Topic: Linked List,Two Pointers.

"""
### Task:
---
Given the head of a linked list, remove the nth node from the end of the list and return i^ts head.

#Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

#Example 2:
Input: head = [1], n = 1
Output: []

#Example 3:
Input: head = [1,2], n = 1
Output: [1]

#Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Hint 1:
Maintain two pointers and update one with a delay of n steps.


### Testcase:
---
[1,2,3,4,5]
2
[1]
1
[1,2]
1

### Code:
---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

"""
### Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0)  # Create a dummy head node to handle edge cases
        dummy_head.next = head    # Connect the dummy head to the original head
        slow = dummy_head         # Initialize the slow pointer
        fast = dummy_head         # Initialize the fast pointer
        
        # Move the fast pointer n nodes ahead
        for i in range(n + 1):
            fast = fast.next
        
        # Move both pointers until the fast pointer reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node from the end by updating the slow pointer's next
        slow.next = slow.next.next
        
        return dummy_head.next  # Return the updated head of the linked list


### Description:
'''
To remove the nth node from the end of a linked list, you can use the two-pointer technique.

This code uses two pointers, slow and fast, initially pointing to the dummy head. First, it moves
the fast pointer n nodes ahead. Then, both pointers are moved together until the fast pointer 
reaches the end of the linked list. At this point, the slow pointer will be pointing to the node 
just before the nth node from the end.

To remove the nth node, the slow pointer's next is updated to skip the nth node. Finally, the 
updated head of the linked list is returned.

This algorithm works in a single pass through the linked list and has a time complexity of O(N), 
where N is the number of nodes in the linked list.

'''
