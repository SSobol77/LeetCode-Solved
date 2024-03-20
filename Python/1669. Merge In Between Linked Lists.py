# 1669. Merge In Between Linked Lists.

# Topic: Linked List.

"""
# Task:
--------
You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
The blue edges and nodes in the following figure indicate the result:
Build the result list and return its head.

Example 1:
Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

Example 2:
Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.

Constraints:
3 <= list1.length <= 10^4
1 <= a <= b < list1.length - 1
1 <= list2.length <= 10^4

# Testcase:
-----------
[10,1,13,6,9,5]
3
4
[1000000,1000001,1000002]
[0,1,2,3,4,5,6]
2
5
[1000000,1000001,1000002,1000003,1000004]

## Code:
-------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    
"""

## Solution:

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Step 1: Traverse to the (a-1)th node of list1
        prev = list1
        for _ in range(a - 1):
            prev = prev.next
        
        # Step 3: Traverse to the bth node of list1
        temp = prev.next
        for _ in range(b - a + 1):
            temp = temp.next
        
        # Step 4: Connect the (a-1)th node of list1 to the head of list2
        prev.next = list2
        
        # Step 5: Traverse to the end of list2
        while list2.next:
            list2 = list2.next
        
        # Step 6: Connect the end of list2 to the node after the bth node of list1
        list2.next = temp
        
        # Step 7: Return the modified list1
        return list1



## Description:
'''
To solve the problem of merging two linked lists, where list1's nodes from the ath node to the bth node are removed and list2 is inserted in their place, we can follow these steps:

### Steps:
1. **Traverse list1**: Start from the head of list1 and traverse it until you reach the (a-1)th node. This node will be the point where we'll start inserting list2.
2. **Store the Connection Point**: Keep a reference to the (a-1)th node since this is where we'll connect the head of list2.
3. **Reach the bth Node**: Continue traversing list1 until you reach the bth node. This node and everything between it and the (a-1)th node will be removed. Keep a reference to the node right after the bth node, as this will be the point where we'll reconnect list1 after inserting list2.
4. **Insert list2**: Connect the (a-1)th node of list1 to the head of list2.
5. **Traverse to the End of list2**: Traverse list2 until you reach its end.
6. **Reconnect list1**: Connect the last node of list2 to the node right after the bth node of list1.
7. **Return the Modified list1**: The head of list1 remains the head of the modified list, so return it.

### my pseudocode:

def mergeInBetween(list1, a, b, list2):
    # Step 1: Traverse to the (a-1)th node of list1
    prev = list1
    for _ in range(a - 1):
        prev = prev.next
    
    # Step 3: Traverse to the bth node of list1
    temp = prev.next
    for _ in range(b - a + 1):
        temp = temp.next
    
    # Step 4: Connect the (a-1)th node of list1 to the head of list2
    prev.next = list2
    
    # Step 5: Traverse to the end of list2
    while list2.next:
        list2 = list2.next
    
    # Step 6: Connect the end of list2 to the node after the bth node of list1
    list2.next = temp
    
    # Step 7: Return the modified list1
    return list1

### Description:
This solution effectively 'cuts' the section from the ath to the bth node in list1 and 'pastes' list2 in its place. The connections are carefully updated to ensure the integrity of the resulting linked list. This approach maintains the original structure of list1 except for the replaced section, seamlessly integrating list2.

'''
