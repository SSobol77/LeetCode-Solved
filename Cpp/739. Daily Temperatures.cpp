// 739. Daily Temperatures.         Medium

// Topic: Array, Stack, Monotonic Stack.

/*
###Task:
---
Given an array of integers temperatures represents the daily temperatures, return an array answer 
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100

Hint 1:
If the temperature is say, 70 today, then in the future a warmer temperature must be 
either 71, 72, 73, ..., 99, or 100. We could remember when all of them occur next.

### Testcase:
---
[73,74,75,71,69,72,76,73]
[30,40,50,60]
[30,60,90]


### Code:
---
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        
    }
};
*/
// Solution: ----------------------------------------------------------

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        // Initialize result vector with 0s, same length as temperatures array
        vector<int> result(temperatures.size(), 0);  
        // Stack to store indices of the temperatures array, for temperatures that are waiting to find a warmer day
        stack<int> tempIndices;  

        // Iterate through each day in the temperatures array
        for (int i = 0; i < temperatures.size(); ++i) {
            // While the stack is not empty and the current temperature is warmer than the temperature at the index on the top of the stack
            while (!tempIndices.empty() && temperatures[i] > temperatures[tempIndices.top()]) {
                int idx = tempIndices.top();  // Get the index from the top of the stack
                tempIndices.pop();  // Remove the top element from the stack
                result[idx] = i - idx;  // Update the result for this index with the number of days to wait for a warmer temperature
            }
            // Push the current index onto the stack. This index represents a temperature that is waiting to find a warmer future day.
            tempIndices.push(i);  
        }

        // Return the result vector, which now contains the number of days to wait for a warmer temperature for each day
        return result;  
    }
};


// Description:
/*
To solve the "Daily Temperatures" problem, we can use a monotonic stack, which is a stack where the elements are always in 
decreasing order from top to bottom. The stack will store the indices of the temperatures array. As we iterate through the 
temperatures array, we'll compare the current temperature with the temperature at the index on top of the stack. If the 
current temperature is warmer, it means we have found a warmer day for the day at the stack's top index, and we can calculate 
the difference in days.

Here's a step-by-step guide to the algorithm:

1. Initialize an empty stack to store indices of the temperatures array.
2. Create a result vector initialized with 0s, with the same size as the temperatures array. This vector will store the number 
   of days to wait for a warmer temperature.
3. Iterate through each day in the temperatures array.
4. While the stack is not empty and the current temperature is warmer than the temperature at the index on top of the stack, pop 
   from the stack. For each popped index, update the result at that index with the current day index minus the popped index, 
   indicating the number of days to wait for a warmer temperature.
5. Push the current index onto the stack.
6. After iterating through all temperatures, return the result vector.

In this solution, the stack is used to keep track of temperatures that have not yet found a warmer day. By maintaining the 
stack in a decreasing order, we ensure that once we encounter a warmer temperature, we can efficiently update the result for 
all cooler temperatures stored in the stack before it. This approach ensures that each temperature is pushed and popped from 
the stack exactly once, leading to a time complexity of O(n), where n is the length of the temperatures array.

*/
