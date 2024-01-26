// 78. Subsets.


// Topic: Array, Backtracking, Bit Manipulation.


/*
### Task:
---
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.


### Testcase:
---
[1,2,3]
[0]


### Code:
---
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        
    }
};
 
*/
// Solution: --------------------------------------

class Solution {
public:
    // A helper function for the backtracking approach.
    // It recursively builds subsets starting from the 'start' index.
    void backtrack(vector<int>& nums, int start, vector<int>& subset, vector<vector<int>>& subsets) {
        // Add the current subset to the list of all subsets.
        subsets.push_back(subset);

        // Iterate through the array starting from 'start'.
        for (int i = start; i < nums.size(); i++) {
            // Include the current element in the subset.
            subset.push_back(nums[i]);

            // Recurse to add further elements to the subset.
            // 'i + 1' ensures we move forward in the array and avoid duplicates.
            backtrack(nums, i + 1, subset, subsets);

            // Exclude the current element from the subset (backtrack).
            // This is crucial for exploring other combinations without this element.
            subset.pop_back();
        }
    }

    // The main function to generate all subsets.
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result; // To store all possible subsets.
        vector<int> currentSubset;  // A temporary vector to store the current subset.

        // Start backtracking with an empty subset.
        backtrack(nums, 0, currentSubset, result);

        return result; // Return the collection of all subsets.
    }
};



// Description: ===================================
/*

The task here involves generating all possible subsets of a given set of unique integers. This problem can be approached using 
backtracking or bit manipulation. Below is a C++ solution using the backtracking approach, which is more intuitive for understanding 
the concept of generating subsets.


### Backtracking Approach:

1. **Idea**: Use a recursive function to explore all possible combinations of elements in the input array. At each step, choose 
   whether to include the current element in the subset.

2. **Base Case**: When the end of the input array is reached, add the current subset to the result.

3. **Recursive Case**: For each element, make a decision to either include it in the current subset or not, and then recurse for 
   the next element.

4. **Optimization**: Since the problem doesn't require the subsets to be in any specific order, we don't need to sort the input or output.


### Explanation:

- `backtrack` is a recursive function that takes the current starting index (`start`), the current subset (`subset`), and the 
   collection of all subsets (`subsets`).
- It starts by adding the current subset to the list of all subsets.
- Then, it iterates over the array, starting from the current index. For each element, it includes the element in the current 
  subset, calls itself recursively to handle the rest of the elements, and then excludes the element (backtracking) to explore 
  other combinations.
- The `subsets` function initializes the required variables and starts the backtracking process.


### Complexity Analysis:

- **Time Complexity**: O(2^n), where n is the number of elements in the input array. Each element has two choices (either to be 
    included or not), leading to 2^n possible subsets.
- **Space Complexity**: O(n), used by the recursion stack. In the worst case, the recursion can go up to n levels deep.

*/
