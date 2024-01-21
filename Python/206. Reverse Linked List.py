# 206. Reverse Linked List.

# Topic: Linked List, Recursion.

"""
### Task:
---
Given the head of a singly linked list, reverse the list, and return the reversed list.

#Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

#Example 2:
Input: head = [1,2]
Output: [2,1]

#Example 3:
Input: head = []
Output: []

#Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

### Testcase:
---
[1,2,3,4,5]
[1,2]
[]


### Code:
---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

"""
### Solution: --------------------------------------------------------------------------------------------

# Sol. 1. Iterative Approach:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # Initialize a pointer to keep track of the previous node
        current = head  # Start at the head of the linked list
        
        while current:
            next_node = current.next  # Store the next node temporarily
            current.next = prev  # Reverse the next pointer
            prev = current  # Move the previous pointer forward
            current = next_node  # Move the current pointer forward
        
        return prev  # Return the new head of the reversed list


# Sol. 2. Recursive Approach:
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node, return the head
        if not head or not head.next:
            return head
        
        # Recursive case: reverse the sublist starting from head's next
        reversed_head = self.reverseList(head.next)
        
        # Update the next pointer of the current head to point to None
        head.next.next = head
        head.next = None
        
        return reversed_head  # Return the new head of the reversed list


# Description: --------------------------------------------------------------------------------------------
'''
Descriptions for both the iterative and recursive solutions to the "Reverse Linked List" problem:

**Iterative Approach:**

In the iterative approach, the goal is to reverse a singly linked list by iteratively changing the direction of the `next` 
pointers of each node. We start with two pointers, `prev` and `current`, initially set to `None` and the `head` of the 
linked list, respectively. 

We traverse the linked list, and at each step, we update the `next` pointer of the `current` node to point to the `prev` node,
effectively reversing the direction of the edge. Then, we move both the `prev` and `current` pointers one step forward in the list.

This process continues until we reach the end of the original list, at which point the `prev` pointer points to the new head of 
the reversed list. Finally, we return this new head.

The time complexity of this iterative approach is O(n), where n is the number of nodes in the linked list, as we visit each node 
once, making it an efficient solution for reversing the list.


**Recursive Approach:**

In the recursive approach, we reverse a singly linked list by recursively reversing a sublist starting from the second node (i.e., 
the `head.next`) and connecting it to the current head node. We use a base case to handle empty lists or lists with only one node.

The recursive function takes the current `head` as input and, in the base case, returns the `head` itself. For non-base cases, the 
function recursively reverses the sublist starting from `head.next` and returns the new head of the reversed sublist.

After reversing the sublist, we update the `next` pointer of the current `head` (originally the first node) to point to `None`. This 
step effectively reverses the direction of the edge for the current `head` node.

The recursion continues until we reach the end of the original list, at which point the new head of the reversed list is returned.

The time complexity of this recursive approach is also O(n), where n is the number of nodes in the linked list, as we process each 
node once during the recursive calls. Although this approach is less intuitive than the iterative one, it is a valid and efficient way to reverse a linked list.

'''
