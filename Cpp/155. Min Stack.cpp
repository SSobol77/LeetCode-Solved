// 155. Min Stack.


// Topic: Stack, Design.


/*
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

Example 1:
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
 
Constraints:
-2^31 <= val <= 2^31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

Hint 1:
Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan)

### Testcase:
---
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

### Code:
---
class MinStack {
public:
    MinStack() {
        
    }
    
    void push(int val) {
        
    }
    
    void pop() {
        
    }
    
    int top() {
        
    }
    
    int getMin() {
        
    }
};

// * Your MinStack object will be instantiated and called as such:
// * MinStack* obj = new MinStack();
// * obj->push(val);
// * obj->pop();
// * int param_3 = obj->top();
// * int param_4 = obj->getMin();
// 

*/
// Solution: --------------------------------------


class MinStack {
    stack<int> stackMain; // Main stack to store all the elements
    stack<int> stackMin;  // Auxiliary stack to store the minimum elements

public:
    // Constructor initializes the MinStack object
    MinStack() { }

    // Pushes a new element onto the stack
    void push(int val) {
        // Always push the new value onto the main stack
        stackMain.push(val);

        // If the min stack is empty or the new value is less than or equal to the current minimum,
        // push the new value onto the min stack. Otherwise, push the current minimum again to maintain
        // the size consistency with the main stack and ensure the top of the min stack always represents
        // the current minimum.
        if (stackMin.empty() || val <= stackMin.top()) {
            stackMin.push(val);
        } else {
            stackMin.push(stackMin.top());
        }
    }
    
    // Removes the element on top of the stack
    void pop() {
        // Pop the top elements from both the main and min stacks to maintain consistency.
        // This ensures the min stack accurately reflects the minimum of the current stack state.
        stackMain.pop();
        stackMin.pop();
    }
    
    // Gets the top element of the stack
    int top() {
        // Return the top element of the main stack
        return stackMain.top();
    }
    
    // Retrieves the minimum element in the stack
    int getMin() {
        // Return the top element of the min stack, which represents the current minimum element in the stack
        return stackMin.top();
    }
};


// Description: ===================================
/*
To design a MinStack class that supports push, pop, top, and retrieving the minimum element in constant time, we need to ensure that 
each operation has a time complexity of O(1). A conventional stack data structure would allow us to achieve O(1) time complexity for 
push, pop, and top operations. However, retrieving the minimum element in O(1) time requires additional considerations.

The key to solving this problem lies in maintaining an auxiliary stack (let's call it minStack) that keeps track of the minimum element 
at every state of the main stack. Whenever a new element is pushed onto the main stack, we compare it with the current minimum (the top 
element of minStack) and push the smaller one onto minStack. When an element is popped from the main stack, we also pop from minStack, 
ensuring that minStack always contains the minimum element of the main stack at its top.

Here is a step-by-step guide to implementing the MinStack class:

1. **Constructor `MinStack()`:** Initialize the main stack and the auxiliary minStack to store the elements and the minimum elements, 
respectively.

2. **Method `void push(int val)`:** Push the value `val` onto the main stack. Compare `val` with the top of minStack (if minStack is 
not empty). If `val` is smaller or minStack is empty, push `val` onto minStack. Otherwise, push the current top of minStack again (to 
maintain the size consistency with the main stack).

3. **Method `void pop()`:** Pop the top element from the main stack and the top element from minStack to ensure that minStack continues 
to reflect the minimum element of the current state of the main stack.

4. **Method `int top()`:** Return the top element of the main stack.

5. **Method `int getMin()`:** Return the top element of minStack, which represents the minimum element in the main stack.


### Description:

This implementation defines two stacks: `stackMain` for storing all the elements and `stackMin` for keeping track of the minimum elements. 
The `push` method adds a new element to `stackMain` and decides whether to push the new element or the current minimum onto `stackMin`. 
The `pop` method removes the top elements from both `stackMain` and `stackMin` to keep them synchronized. The `top` method simply returns 
the top element of `stackMain`, and the `getMin` method returns the top element of `stackMin`, which is the current minimum element of the 
stack.

By maintaining an auxiliary stack (`stackMin`), we ensure that the `getMin` operation can be performed in O(1) time, fulfilling the 
requirement of constant-time retrieval of the minimum element.

*/
