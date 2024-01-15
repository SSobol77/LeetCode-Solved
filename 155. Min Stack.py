# 155. Min Stack.         Medium

# Topic:

'''
### Task:
---
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

#Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

#Constraints:
-2^31 <= val <= 2^31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 10^4 calls will be made to push, pop, top, and getMin.

Hint 1:
Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan).

### Testcase:
---
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]


### Code:
---
class MinStack(object):

    def __init__(self):
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        """
        :rtype: None
        """
        

    def top(self):
        """
        :rtype: int
        """
        

    def getMin(self):
        """
        :rtype: int
        """     

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

'''
### Solution: ---------------------------------------------------------------

class MinStack(object):

    def __init__(self):
        # Initialize the stack
        self.stack = []

    def push(self, val):
        # If the stack is empty, the min value is the value itself
        # Otherwise, the min value is the min between val and the current min
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self):
        # Pop the top element from the stack
        self.stack.pop()

    def top(self):
        # Return the value of the top element
        return self.stack[-1][0]

    def getMin(self):
        # Return the min value of the top element
        return self.stack[-1][1]


###  Description: ----------------------------------------------
'''
To design a `MinStack` that supports push, pop, top, and retrieving the minimum element in constant time, 
we need to keep track of the minimum element at each state of the stack. We can achieve this by using a 
stack where each element is a pair: the value and the minimum value when this element was added to the stack.

Here's how we can implement each method:

1. **__init__()**: Initialize the stack.

2. **push(val)**: Insert a pair into the stack. The pair consists of the value `val` and the current minimum. 
   The current minimum is the smaller one between `val` and the minimum of the previous top element of the stack.

3. **pop()**: Remove the top element from the stack.

4. **top()**: Return the value of the top element of the stack (the first element of the pair).

5. **getMin()**: Return the minimum element of the top element of the stack (the second element of the pair).



### Explanation:
- Each element in the stack is a tuple of the form `(value, min_value)`.
- When pushing a new value, we calculate the current minimum and store it with the value.
- The `pop`, `top`, and `getMin` methods work in constant time \(O(1)\) as required.

This design ensures that each operation (`push`, `pop`, `top`, `getMin`) has a time complexity of O(1), meeting 
the problem's constraint. The space complexity is O(n), where n is the number of elements in the stack, to store 
the minimum value with each element.

'''
