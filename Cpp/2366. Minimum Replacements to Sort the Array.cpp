// 2366. Minimum Replacements to Sort the Array

// Topic: Array, Math, Greedy.


/*
### Task:
---
You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.

For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
Return the minimum number of operations to make an array that is sorted in non-decreasing order.

Example 1:
Input: nums = [3,9,3]
Output: 2
Explanation: Here are the steps to sort the array in non-decreasing order:
- From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
- From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 0
Explanation: The array is already in non-decreasing order. Therefore, we return 0. 

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9

Hint 1:
It is optimal to never make an operation to the last element of the array.
Hint 2:
You can iterate from the second last element to the first. If the current value is greater than the previous bound, we want to break 
it into pieces so that the smaller one is as large as possible but not larger than the previous one.


### Testcase:
---
[3,9,3]
[1,2,3,4,5]


### Code:
---
class Solution {
public:
    long long minimumReplacement(vector<int>& nums) {
        
    }
};

*/
// Solution: --------------------------------------


class Solution {
public:
    long long minimumReplacement(vector<int>& nums) {
        int n = nums.size();
        long long replacements = 0;

        // Start from the second last element
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] > nums[i + 1]) {
                // Calculate the number of pieces to split the current element into
                int pieces = (nums[i] + nums[i + 1] - 1) / nums[i + 1];
                replacements += pieces - 1; // Add the number of extra pieces required as replacements

                // Update the current element to the largest possible value that maintains the order
                nums[i] = nums[i] / pieces;
            }
        }

        return replacements;
    }
};


// Sample Tests:

int main() {
    Solution solution;

    vector<int> nums1 = {3, 9, 3};
    cout << solution.minimumReplacement(nums1) << endl; // Expected output: 2

    vector<int> nums2 = {1, 2, 3, 4, 5};
    cout << solution.minimumReplacement(nums2) << endl; // Expected output: 0

    return 0;
}


// Description: ===================================
/*
To solve the "Minimum Replacements to Sort the Array" problem, we'll use a greedy approach as suggested by the hints. The key idea is to iterate from the second-last element to the first and make replacements such that each new value is as large as possible but not larger than its next element (to maintain non-decreasing order).

Here's a step-by-step algorithm:
1. Start iterating from the second last element to the first element of the array.
2. For each element, if it is greater than its next element, we need to replace it.
3. To minimize the number of replacements, we should split the current element into parts that are as large as possible, with each part being less than or equal to the next element.
4. Calculate the number of replacements needed for each element and sum them up.



### Description
---
In this solution, we iterate backward through the array and check if the current element is greater than its next element. If it is, we calculate the optimal number of pieces to split the element into. This number is determined by dividing the current element by the next element and rounding up. The number of replacements is incremented by the number of additional pieces minus one. Finally, we update the current element to the largest value that maintains the order. The sum of all such replacements gives us the minimum number of operations required to sort the array.

*/
