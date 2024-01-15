# 739. Daily Temperatures.       Medium

# Topic: Array, Stack, Monotonic Stack.

"""
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
class Solution(object):
    def dailyTemperatures(self, temperatures):
        '''
        :type temperatures: List[int]
        :rtype: List[int]
        '''
"""
### Solution: ----------------------------------------------------------

class Solution(object):
    def dailyTemperatures(self, temperatures):
        '''
        :type temperatures: List[int]
        :rtype: List[int]
        '''
        # Initialize the stack and the answer array
        stack = []
        answer = [0] * len(temperatures)

        # Iterate over the temperatures
        for i, temp in enumerate(temperatures):
            # Pop indices from the stack as long as the current temp is higher than the temp at those indices
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            # Push the current index onto the stack
            stack.append(i)

        return answer


### Description:  -------------------------------------------------------
'''
To solve the "Daily Temperatures" problem, we can use a monotonic stack. The idea is to maintain a stack of indices 
of the days. We iterate through the array, and for each day, we check if the current day's temperature is higher 
than the temperature of the days indexed in the stack. If it is, we pop those days from the stack and calculate the 
difference in days, updating our result array. 

Here's a step-by-step approach:

1. **Initialize a Stack and an Answer Array**: Create an empty stack to keep track of indices of days. Also, 
     initialize an array `answer` with the same length as `temperatures`, filled with zeros.

2. **Iterate Over Temperatures**: Go through each day's temperature in `temperatures`:
   - While the stack is not empty and the current day's temperature is greater than the temperature at the index 
     at the top of the stack, pop the top index from the stack. Calculate the difference in days between the current 
     day and the popped index, and update the corresponding position in the `answer` array.
   - Push the current index onto the stack.

3. **Return the Answer Array**: After processing all days, return the `answer` array.

### Explanation:
- **Stack**: This is used to store indices of days with temperatures that haven't yet found a warmer day.
- **While Loop inside the For Loop**: This checks if the current temperature is higher than the temperature on the 
    days in the stack. If it is, those days are popped from the stack, and their corresponding positions in the 
    `answer` array are updated with the number of days until a warmer temperature.
- **Pushing to Stack**: If the current temperature isn't higher than the last temperature on the stack, the current
    day's index is added to the stack.

The time complexity of this algorithm is O(n), where n is the number of days, because each day is pushed and popped 
from the stack exactly once. The space complexity is also O(n) due to the stack and the answer array. 
This solution effectively handles the requirement of finding the next warmer temperature for each day.

'''
