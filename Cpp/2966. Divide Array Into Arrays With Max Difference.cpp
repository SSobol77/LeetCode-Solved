// 2966. Divide Array Into Arrays With Max Difference.

// Topic: Array, Greedy, Sorting


/*
### Task:
---
You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following conditions:

Each element of nums should be in exactly one array.
The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. 
And if there are multiple answers, return any of them.

Example 1:
Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
Output: [[1,1,3],[3,4,5],[7,8,9]]
Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
The difference between any two elements in each array is less than or equal to 2.
Note that the order of elements is not important.

Example 2:
Input: nums = [1,3,3,2,7,3], k = 3
Output: []
Explanation: It is not possible to divide the array satisfying all the conditions.
 
Constraints:
n == nums.length
1 <= n <= 10^5
n is a multiple of 3.
1 <= nums[i] <= 10^5
1 <= k <= 10^5

Hint 1:
Try to use a greedy approach.
Hint 2:
Sort the array and try to group each 3 consecutive elements.


### Testcase:
---
[1,3,4,8,7,9,3,5,1]
2
[1,3,3,2,7,3]
3


### Code:
---
class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        
    }
};

*/
//  Solution: -------------------------------------------------------------

#include <vector>
#include <algorithm> // Include for the sort function

using namespace std;

class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        // First, sort the nums array to ensure that we can easily group elements with minimal differences.
        sort(nums.begin(), nums.end());

        vector<vector<int>> result; // This will store the final groups of arrays.
        
        // Iterate through the sorted array in steps of 3 since we need to divide the array into subarrays of size 3.
        for (int i = 0; i < nums.size(); i += 3) {
            // Check if the difference between the max and min element in the current group of 3 elements is within the limit k.
            // In a sorted subarray of size 3, nums[i + 2] is the max and nums[i] is the min.
            if (nums[i + 2] - nums[i] > k) {
                // If the difference is more than k, it's impossible to satisfy the condition for all groups.
                // Therefore, return an empty array as per the problem's requirement.
                return {};
            }
            // If the difference is within the limit, add the current group to the result.
            // This group now forms one of the subarrays in our solution.
            result.push_back({nums[i], nums[i + 1], nums[i + 2]});
        }

        // Return the 2D array containing all the subarrays formed.
        // This 2D array satisfies the problem's conditions where each subarray of size 3 has differences less than or equal to k.
        return result;
    }
};


// Description:  ===========================================================
/*
To solve the problem using a greedy approach, we will first sort the array to ensure that we can easily group elements 
with minimum differences. After sorting, we will iterate through the array, grouping every three consecutive elements 
into a subarray. We will then check if the difference between the maximum and minimum elements in each subarray is less 
than or equal to `k`. If it is, we add the subarray to our result. If at any point we find a subarray that does not 
satisfy the condition, we return an empty array since it's impossible to divide the array as per the requirements.


### Explanation:
1. **Sorting the Array**: The array is sorted to ensure that the elements with the smallest differences are adjacent, 
     facilitating the grouping into subarrays where the difference between the maximum and minimum elements is minimized.

2. **Iterating in Groups of Three**: The loop iterates through the sorted array in steps of three, considering each 
     group of three consecutive elements as a potential subarray.

3. **Checking the Difference**: For each group of three elements, the difference between the maximum and minimum elements 
     (which are the first and the third elements in the sorted group, respectively) is compared to `k`. If this difference 
     exceeds `k`, the function immediately returns an empty array, indicating it's impossible to divide the original array 
     under the given constraints.

4. **Building the Result**: If the group satisfies the condition (the difference is less than or equal to `k`), it is added 
     to the result as a subarray. This process is repeated until all elements are grouped, ensuring each element of `nums` 
     is included exactly once in the resulting 2D array.

5. **Returning the Result**: The function returns the 2D array containing all subarrays if all groups satisfy the condition. 
     Otherwise, it returns an empty array, indicating no valid division could be found.

*/

