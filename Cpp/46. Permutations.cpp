// 46. Permutations/

// Topic: Array, Backtracking.

/*
### Task:
---------
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


### Testcase:
-------------
[1,2,3]
[0,1]
[1]


### Code:
----------
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        
    }
};    

*/
// Solution: --------------------------------------------------------------------------------

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    // Function to initiate the process of finding permutations
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> permutations; // This will store all the permutations
        backtrack(nums, permutations, 0); // Start the backtracking process from index 0
        return permutations;
    }

private:
    // Backtracking function to generate permutations
    void backtrack(vector<int>& nums, vector<vector<int>>& permutations, int start) {
        // Check if we have reached the end of the array
        if (start == nums.size()) {
            permutations.push_back(nums); // Add the current permutation to the list
            return;
        }

        // Iterate through the array elements
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]); // Swap the current element with the element at 'start'
            backtrack(nums, permutations, start + 1); // Recurse for the next element in the array
            swap(nums[start], nums[i]); // Swap back to restore the original state of 'nums' for the next iteration
        }
    }
};




// Description: =====================================================================
/*

To solve the problem of generating all possible permutations of a given array `nums` of distinct integers, we can use backtracking. 
The key to backtracking is to explore each possibility and backtrack to try a different path when a dead end is reached. In this case,
we need to explore every possible arrangement of the elements in `nums`.

Given the constraint that the number of elements in `nums` is relatively small (up to 6), this approach is feasible. However, as you 
specifically mentioned memory cleaning, we should ensure that our solution does not use unnecessary memory and that any used memory 
is properly managed.

### Explanation:

1. **Backtracking Function**: The `backtrack` function generates permutations by recursively swapping elements in the array. 
   It takes `nums`, the current permutation, `permutations`, the collection of all permutations, and `start`, the current index to process.

2. **Base Case**: When `start` equals the size of `nums`, a new permutation has been formed, which is then added to `permutations`.

3. **Generating Permutations**: For each recursive call, the function iterates through the array, swapping the current `start` element 
   with each subsequent element (`i`). This swapping generates different permutations.

4. **Restoring State**: After each recursive call, the array is restored to its original state by swapping the elements back. This 
   step is crucial to ensure that each recursive call works on the correct array configuration.

5. **Efficient Memory Usage**: The solution avoids using extra memory for each permutation. Instead, it modifies the original array 
   in place and adds a copy of the array to the result only when a full permutation is formed. After backtracking, it restores the array 
   to its original state, ensuring efficient memory usage.

This solution efficiently generates all permutations of the array `nums` using backtracking, while being mindful of memory usage by 
avoiding unnecessary allocations and restoring the array's state after each recursive call.

*/
