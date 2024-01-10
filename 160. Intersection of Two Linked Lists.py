# 160. Intersection of Two Linked Lists

# Topic: Hash Table, Linked List, Two Pointers

'''
# Task:
-------
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

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



# Testcase:
-----------
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


# Code:
-------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
   


'''
# Solution:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Initialize two pointers for each list
        pointerA, pointerB = headA, headB

        # Traverse both lists
        while pointerA != pointerB:
            # Move to the next node or switch to the other list's head when the end is reached
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        # If the lists intersect, pointerA and pointerB will meet at the intersection node
        # Otherwise, they will both be null
        return pointerA

# Example usage
# Note: The creation of linked lists and nodes is just for demonstration and testing.
# In a real scenario, the lists would be provided by the problem's context.
node_common = ListNode(8)
node_common.next = ListNode(4)
node_common.next.next = ListNode(5)

listA = ListNode(4)
listA.next = ListNode(1)
listA.next.next = node_common

listB = ListNode(5)
listB.next = ListNode(6)
listB.next.next = ListNode(1)
listB.next.next.next = node_common

sol = Solution()
print(sol.getIntersectionNode(listA, listB).val)  # Output: 8


# Description
'''
The solution is designed to find the intersection point of two singly linked lists. The key idea is to use a 
two-pointer technique, which is both efficient and straightforward. Here's how the code works:

ListNode Class:
The ListNode class defines the structure of a node in a singly linked list. Each node contains a value (val) 
and a reference to the next node (next).

Solution Class with getIntersectionNode Method:
The Solution class contains the method getIntersectionNode, which takes the heads of two singly linked 
lists (headA and headB) as input.

Two-Pointer Technique:
Two pointers, pointerA and pointerB, are initialized at the heads of the two lists.
The method iterates through both lists simultaneously. If a pointer reaches the end of a list, it is 
redirected to the head of the other list.
This process equalizes the path lengths by effectively appending the length of the other list to each list.

Intersection Detection:
The loop continues until the two pointers either meet at the intersection point or both reach the end of 
their respective lists (indicated by both pointers being None).
If the lists intersect, the pointers will meet at the intersection node. Otherwise, they will both reach 
the end without meeting.

Return Value:
The method returns the intersecting node or None if no intersection exists.

Example Usage:
The code includes an example to demonstrate its usage:
- Two linked lists are created with a common intersection node (node_common).
- The getIntersectionNode method is called with the heads of these two lists.
- The value of the intersecting node is printed (8 in this case).

Efficiency:
Time Complexity: The algorithm runs in O(m + n) time, where m and n are the lengths of the two linked lists. Each list is traversed at most twice.
Space Complexity: The space complexity is O(1), as no additional space is used proportional to the input size. Only two pointers are utilized for traversal.
This solution is efficient and conforms to the constraints of the problem, particularly the requirement to use only O(1) memory. The two-pointer technique is a clever way to handle the potential difference in lengths of the two linked lists and find the intersection point in a linear time complexity.

'''
