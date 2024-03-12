# 1171. Remove Zero Sum Consecutive Nodes from Linked List.


# Topic: Hash Table, Linked List.

"""
### Task:
---
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

Example 2:
Input: head = [1,2,3,-3,4]
Output: [1,2,4]

Example 3:
Input: head = [1,2,3,-3,-2]
Output: [1]

Constraints:
The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.

Hint 1:
Convert the linked list into an array.
Hint 2:
While you can find a non-empty subarray with sum = 0, erase it.
Hint 3:
Convert the array into a linked list.

### Testcase:
---
[1,2,-3,3,1]
[1,2,3,-3,4]
[1,2,3,-3,-2]


### Code:
---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
  
    

"""
### Solution: --------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node that precedes the head of the list for simplicity.
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize a cumulative sum to track the sum of node values from the start to the current node.
        cumulative_sum = 0
        # Start from the dummy node to handle edge cases where the head needs to be removed.
        node = dummy
        # Use a hash table to map cumulative sums to their corresponding nodes.
        hash_table = {}

        # First pass: Calculate cumulative sums and populate the hash table.
        while node:
            cumulative_sum += node.val
            # Update the hash table with the current cumulative sum.
            # If the same sum is encountered again, it will overwrite the previous entry, effectively marking the start of a new subsequence.
            hash_table[cumulative_sum] = node
            node = node.next

        # Reset variables for the second pass through the list.
        node = dummy
        cumulative_sum = 0

        # Second pass: Use the hash table to skip over nodes that are part of zero-sum sequences.
        while node:
            cumulative_sum += node.val
            # Link the current node to the last node that had the same cumulative sum.
            # This effectively removes the zero-sum sequence from the list by skipping it.
            node.next = hash_table[cumulative_sum].next
            node = node.next

        # Return the modified list, starting from the node next to dummy, as dummy was a placeholder.
        return dummy.next

### Description: ===================================
'''
### Explanation of the Comments:

- The comments guide through the creation of a dummy node to simplify edge case handling, especially when nodes at the beginning of the 
  list are part of a zero-sum sequence and need to be removed.

- They explain the use of a cumulative sum to track the sum of values from the start to the current node, and the use of a hash table 
  to map these sums to their corresponding nodes. This is crucial for identifying zero-sum sequences.

- The first pass through the list involves computing cumulative sums and updating the hash table. The key insight is that if a cumulative 
  sum is encountered again, it indicates the end of a zero-sum sequence.

- The second pass revisits each node and uses the hash table to skip over the nodes that are part of zero-sum sequences, effectively 
  removing those sequences from the list.

- Finally, the comments clarify the return statement, emphasizing that the dummy node was a placeholder and the modified list starts 
  from `dummy.next`.

  
To solve the task of removing zero sum consecutive nodes from a linked list using a hash table and linked list, we will follow a two-step 
process:

1. Traverse the linked list and compute the cumulative sum at each node. Store these cumulative sums in a hash table with the cumulative 
sum as the key and the node with that cumulative sum as the value. If the same cumulative sum is encountered again, it means the nodes 
between these two instances sum up to zero and should be removed.

2. Re-traverse the list, using the hash table to skip over the nodes that are part of a zero-sum sequence.


### Description:

This solution starts with a dummy node linked to the head of the list to simplify edge cases handling. As we traverse the linked list 
for the first time, we calculate the cumulative sum of node values up to the current node and use a hash table to keep track of the 
most recent node for each cumulative sum encountered. If the same cumulative sum is encountered again, it means the nodes between these 
two instances (inclusive of the start, exclusive of the end) sum up to zero and should be removed.

In the second pass, we traverse the list again, updating the `next` pointers of the nodes to skip over the nodes that are part of any 
zero-sum sequence found in the first pass. This effectively removes the zero-sum sequences from the list.

Finally, we return `dummy.next`, which is the head of the modified list, after potentially removing some nodes at the beginning.

'''
