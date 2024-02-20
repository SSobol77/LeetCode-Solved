// 268. Missing Number.


// Topic: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting.


/*
### Task:
---
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

Constraints:
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.
 
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?


### Testcase:
---
[3,0,1]
[0,1]
[9,6,4,2,3,5,7,0,1]


### Code:
---
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        // Calculate the sum of the first n natural numbers
        int totalSum = n * (n + 1) / 2;
        
        // Calculate the sum of numbers in the array
        int arraySum = 0;
        for (int num : nums) {
            arraySum += num;
        }
        
        // The missing number is the difference between the total sum and the array sum
        return totalSum - arraySum;
    }
};


// Description: ===================================
/*
To solve the task of finding the missing number in an array containing n distinct numbers in the range [0, n], we can 
use a mathematical approach that leverages the property of arithmetic series. Specifically, we know that the sum of 
the first n natural numbers is given by the formula \( \frac{n(n + 1)}{2} \). By finding the sum of all numbers in the 
given array and subtracting it from the sum of the first n natural numbers, we can find the missing number. This approach 
has a time complexity of O(n) and a space complexity of O(1), meeting the follow-up constraint.


### Description:

1. **Calculate the total sum**: First, we calculate the sum of the first n natural numbers using the formula \( \frac{n(n + 1)}{2} \), 
     where `n` is the length of the array `nums`. This gives us the sum of all numbers in the range [0, n].

2. **Calculate the array sum**: We then iterate through the array `nums` and calculate the sum of all its elements.

3. **Find the missing number**: The missing number is the difference between the total sum (sum of numbers from 0 to n) and the sum 
     of numbers in the array. This is because the total sum includes the missing number, and subtracting the sum of the array from it 
     leaves us with the missing number.

This solution is efficient and meets the constraints of using only O(1) extra space and having O(n) runtime complexity.

*/
