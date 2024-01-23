# 225. Implement Stack using Queues.

# Topic: Stack, Design, Queue.

"""
### Task:
---
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

Example 1:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.

Follow-up: Can you implement the stack using only one queue?

### Testcase:
---
["MyStack","push","push","top","pop","empty"]
[[],[1],[2],[],[],[]]


### Code:
---
class MyStack:

    def __init__(self):


    def push(self, x: int) -> None:


    def pop(self) -> int:


    def top(self) -> int:


    def empty(self) -> bool:



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


"""
### Solution: --------------------------------------

from collections import deque

class MyStack:

    def __init__(self):
        # Initialize two queues
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        # Push element x onto stack by enqueuing it to the primary queue
        self.queue1.append(x)

    def pop(self) -> int:
        # Move all elements except the last from queue1 to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        # The last element of queue1 is the top element of the stack
        top_element = self.queue1.popleft()

        # Swap the roles of the two queues
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def top(self) -> int:
        # Similar to pop, but re-enqueue the last element back to queue1
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        top_element = self.queue1.popleft()
        self.queue2.append(top_element)
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def empty(self) -> bool:
        # Return whether the stack is empty
        return not self.queue1

# Example usage
myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())  # Output: 2
print(myStack.pop())  # Output: 2
print(myStack.empty())  # Output: False



### Description: ===================================
'''
Implementing a stack using two queues is an interesting problem that demonstrates the flexibility of data structures.
The stack operations we need to support are push, pop, top, and empty. The key challenge is to maintain the
Last-In-First-Out (LIFO) nature of a stack using queues, which inherently operate in a First-In-First-Out (FIFO) manner.

### Solution Overview:
To simulate a stack using two queues, we can use one queue for the main operations and the other for assisting in the
`pop` and `push` operations. Here's a brief idea of how each operation can be implemented:

1. **Push**: Enqueue the new element into the primary queue.
2. **Pop**: Dequeue all elements except the last from the primary queue and enqueue them into the secondary queue.
     The last element dequeued is the top element of the stack, which we'll return. Then, swap the roles of the primary
     and secondary queues.
3. **Top**: Similar to pop, but we'll re-enqueue the last element back to the primary queue.
4. **Empty**: Check if the primary queue is empty.

### Follow-up (Using One Queue):
Implementing the stack using only one queue requires a slightly different approach. When pushing a new element, we can
re-enqueue the previously stored elements in a way that the new element ends up at the front of the queue, thereby
maintaining the LIFO order. However, this approach is less efficient in terms of time complexity for the `push` operation.


'''
