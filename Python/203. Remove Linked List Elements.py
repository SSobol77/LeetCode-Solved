# 203. Remove Linked List Elements.

# Topic: Linked List, Recursion.

"""
### Task:
---
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and 
return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:
The number of nodes in the list is in the range [0, 10^4].
1 <= Node.val <= 50
0 <= val <= 50

### Testcases:
---
[1,2,6,3,4,5,6]
6
[]
1
[7,7,7,7]
7


### Code:
---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        

"""
### Solution: 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Handle the case where the list is empty
        # If the list is empty, there's nothing to remove, so just return the head (which is None)
        if not head:
            return head
        
        # Remove matching nodes from the beginning of the list
        # This loop continues as long as the head itself has a value equal to `val`
        # It updates the head to the next node each time, effectively removing the matching head nodes
        while head and head.val == val:
            head = head.next
        
        # If after removing head nodes, the list becomes empty, return None
        if not head:
            return None

        # Iterate over the list to remove matching nodes
        # `current` points to the current node being examined
        current = head
        while current and current.next:
            # If the next node's value matches `val`, it needs to be removed
            # We do this by updating the `next` pointer of the `current` node to skip the next node
            if current.next.val == val:
                current.next = current.next.next
            else:
                # If the next node's value doesn't match, simply move to the next node
                current = current.next
        
        # Return the new head of the list (which might be different if we removed head nodes earlier)
        return head


### Description:
'''
To solve the "Remove Linked List Elements" problem, you need to implement a function that iterates through the linked list, removing all nodes whose value equals the specified `val`. This can be done iteratively or recursively. Here, I'll provide an iterative solution for clarity.

#### Iterative Approach:
1. **Handle Edge Cases**: If the list is empty, return `None`.
2. **Remove Matching Head Nodes**: Since the head of the list might match `val`, you need to update the head until it doesn't match.
3. **Iterate Over the List**: Go through each node of the list and check if the next node needs to be removed.
4. **Update Links**: If a node needs to be removed, update the next pointer of the current node to skip it.

In this solution:
- We first deal with the case where the head itself needs to be removed. This is done in a loop because there could be several nodes at the start of the list with the matching value.
- Then, we iterate through the rest of the list, checking each node's next value. If it matches `val`, we remove it by skipping over it in the linked list.
- Finally, we return the potentially new head of the list.

'''