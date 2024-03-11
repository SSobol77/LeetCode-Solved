# 237. Delete Node in a Linked List.


# Topic: Linked List.

"""
### Task:
---
There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

- The value of the given node should not exist in the linked list.
- The number of nodes in the linked list should decrease by one.
- All the values before node should be in the same order.
- All the values after node should be in the same order.

Custom testing:

- For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
- We will build the linked list and pass the node to your function.
- The output will be the entire list after calling your function.
 
Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

Constraints:
The number of the nodes in the given list is in the range [2, 1000].
-1000 <= Node.val <= 1000
The value of each node in the list is unique.
The node to be deleted is in the list and is not a tail node.


### Testcase:
---
[4,5,1,9]
5
[4,5,1,9]
1


### Code:
---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        '''
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        '''
        

"""
### Solution: --------------------------------------


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        '''
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        
        Given a node in a singly linked list, this function will delete the node
        from the list. It does so not by literally removing the node, but by copying
        the value from the next node into this one and then removing the next node.
        
        This approach is used because we do not have access to the node before the one
        we want to delete, so we cannot change the previous node's next pointer.
        '''
        # Copy the value from the next node into the current node. This effectively
        # "overwrites" the current node with the next node's data.
        node.val = node.next.val
        
        # Set the current node's next pointer to point to the next next node,
        # effectively removing the next node from the list.
        node.next = node.next.next


### Description: ===================================
'''
To delete a node in a singly linked list without access to the head, you can copy the data from the next node into the current 
node and then delete the next node. This effectively removes the current node from the list by overwriting it with the next 
node's data and then removing the next node.

This code defines a `Solution` class with a `deleteNode` method that takes a `node` as its input and modifies the list in place 
to "delete" that node. The method works by copying the data from the next node into the `node` and then skipping over the next 
node in the list by adjusting the `next` pointer. This approach works because it's guaranteed that the node to be deleted is not 
the tail node of the list .

'''
