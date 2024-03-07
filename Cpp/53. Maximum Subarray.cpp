// 53. Maximum Subarray.


// Topic: Array, Divide and Conquer, Dynamic Programming.


/*
### Task:
---
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
 
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


### Testcase:
---
[-2,1,-3,4,-1,2,1,-5,4]
[1]
[5,4,-1,7,8]


### Code:
---
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxCurrent = nums[0];
        int maxGlobal = nums[0];
        
        // Start iterating from the second element
        for(int i = 1; i < nums.size(); i++) {
            // Decide whether to add the current element to the existing subarray
            // or start a new subarray with the current element
            maxCurrent = max(nums[i], maxCurrent + nums[i]);
            
            // Update maxGlobal if maxCurrent is greater
            if(maxCurrent > maxGlobal) {
                maxGlobal = maxCurrent;
            }
        }
        
        return maxGlobal;
    }
};


// Description: ===================================
/*
For the problem of finding the Maximum Subarray, a popular and efficient approach is to use Kadane's algorithm, which is a dynamic 
programming technique. The essence of Kadane's algorithm is to iterate through the array and at each position, decide whether to 
add the current element to the existing subarray or start a new subarray from that element. This decision is based on whether adding 
the current element increases the maximum sum found so far. The algorithm maintains a running sum of the maximum subarray found as it 
iterates through the array and updates the maximum sum when a larger sum is found.

Here's a step-by-step explanation of the algorithm:

1. Initialize two variables, `maxCurrent` and `maxGlobal`, with the value of the first element of the array. `maxCurrent` will track 
   the maximum subarray sum ending at the current position, and `maxGlobal` will track the overall maximum subarray sum found so far.
2. Iterate through the array starting from the second element.
3. For each element, update `maxCurrent` to be the maximum of the current element itself and the sum of `maxCurrent` and the current 
   element. This step effectively decides whether to start a new subarray at the current element (if the current element is greater) 
   or to continue the existing subarray (if the sum is greater).
4. Update `maxGlobal` if `maxCurrent` is greater than `maxGlobal`.
5. After iterating through the entire array, `maxGlobal` will hold the maximum subarray sum.

### Description:
This code defines a function `maxSubArray` that takes an integer array `nums` and returns the sum of the subarray with the largest sum 
using Kadane's algorithm. It initializes `maxCurrent` and `maxGlobal` with the first element's value, then iterates through the array 
starting from the second element. For each element, it updates `maxCurrent` to either the element itself or the sum of `maxCurrent` and 
the element, whichever is larger. This update step decides whether to extend the current subarray or start a new one. `maxGlobal` is 
updated whenever a new maximum is found. After the iteration, `maxGlobal` contains the maximum subarray sum.

*/
