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

// Description:
/*
To solve the "Daily Temperatures" problem, we can use a Monotonic Stack approach. A Monotonic Stack is particularly useful in this scenario because it helps us keep track of elements (temperatures in this case) in a way that allows us to efficiently find the next greater element for each item in the array. The stack will store indices of the temperatures array, and we will maintain it in a decreasing order of temperatures (from bottom to top of the stack).

Here's a step-by-step approach to implement the solution:
1. Initialize an empty stack that will store indices of the `temperatures` array.
2. Initialize the `answer` array of the same length as `temperatures` with all elements set to 0. This array will hold the number of days to wait for a warmer temperature.
3. Iterate through the `temperatures` array. For each temperature, perform the following steps:
   - While the stack is not empty and the current temperature is greater than the temperature at the index on the top of the stack, it means we have found a warmer temperature for the day at the top of the stack. Pop the top index from the stack, and calculate the difference between the current index and the popped index to find the number of days to wait. Update the `answer` array at the popped index with this difference.
   - Push the current index onto the stack.
4. After iterating through all temperatures, the `answer` array will have the required number of days to wait for a warmer temperature for each day.


This solution efficiently computes the required number of days to wait for a warmer temperature for each day, leveraging the Monotonic Stack data structure to maintain relevant indices and facilitate the comparison process.
*/