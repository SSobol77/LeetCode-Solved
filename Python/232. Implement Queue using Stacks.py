# 232. Implement Queue using Stacks.


# Topic: Stack, Design, Queue.

"""
### Task:
---
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
- You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 
Example 1:
    Input
    ["MyQueue", "push", "push", "peek", "pop", "empty"]
    [[], [1], [2], [], [], []]
    Output
    [null, null, null, 1, 1, false]

    Explanation
    MyQueue myQueue = new MyQueue();
    myQueue.push(1); // queue is: [1]
    myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
    myQueue.peek(); // return 1
    myQueue.pop(); // return 1, queue is [2]
    myQueue.empty(); // return false
    
Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

### Testcase:
---
["MyQueue","push","push","peek","pop","empty"]
[[],[1],[2],[],[],[]]


### Code:
---
class MyQueue:

    def __init__(self):
        

    def push(self, x: int) -> None:
        

    def pop(self) -> int:
        

    def peek(self) -> int:
        

    def empty(self) -> bool:
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""
# Solution: --------------------------------------

class MyQueue:
    def __init__(self):
        # Initialize two stacks: inStack for push operations, outStack for pop and peek operations
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        # Push element x to the back of the queue (top of inStack)
        self.inStack.append(x)

    def pop(self) -> int:
        # If outStack is empty, transfer all elements from inStack to outStack
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        # Pop the top element from outStack, which is the front element of the queue
        return self.outStack.pop()

    def peek(self) -> int:
        # If outStack is empty, transfer all elements from inStack to outStack
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        # Peek at the top element of outStack, which is the front element of the queue
        return self.outStack[-1]

    def empty(self) -> bool:
        # The queue is empty if both inStack and outStack are empty
        return not self.inStack and not self.outStack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# Description: ===================================
'''
To implement a queue using two stacks, we'll maintain two stack instances. The first stack, `inStack`, will be used to 
handle incoming `push` operations, while the second stack, `outStack`, will be used for `pop` and `peek` operations. 
When `pop` or `peek` is called and `outStack` is empty, we'll transfer all elements from `inStack` to `outStack`, 
reversing the order so that the first element pushed into `inStack` is now on top of `outStack`. This ensures FIFO order. 

### Explanation:
- `__init__`: Initializes two stacks, `inStack` for incoming elements and `outStack` for outgoing elements.
- `push`: Adds an element to `inStack`, effectively pushing it to the back of the queue.
- `pop`: If `outStack` is empty, all elements from `inStack` are moved to `outStack`, reversing their order. Then, the top
   element of `outStack` is popped, simulating a queue's front element being removed.
- `peek`: Similar to `pop`, but returns the top element of `outStack` without removing it, representing the front element 
   of the queue.
- `empty`: Returns `True` if both stacks are empty, indicating the queue is empty; otherwise, returns `False`.

This implementation ensures that each operation has an amortized time complexity of O(1), meeting the follow-up requirement. 
The worst-case time complexity for a single operation might be O(n) (when transferring elements from `inStack` to `outStack`), 
but this cost is spread out over all subsequent `pop` and `peek` operations, making each operation's average time complexity O(1).

'''
