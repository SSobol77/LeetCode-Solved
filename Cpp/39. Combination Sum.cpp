// 39. Combination Sum.

// Topic: Array, Backtracking.


/*
### Task:
-----------------
Given an array of distinct integers candidates and a target integer target, return a list of all 
unique combinations of candidates where the chosen numbers sum to target. You may return the combinations 
in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if 
the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less 
than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40


# Testcase:
--------------
[2,3,6,7]
7
[2,3,5]
8
[2]
1


# Code:
-------------
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        
    }
};

*/

// Solution: ------------------------------------------------------------------------------------------------

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    // Function to initiate the process of finding combinations
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result; // Stores all the valid combinations
        vector<int> combination; // Current combination being explored
        sort(candidates.begin(), candidates.end()); // Sort the candidates to optimize the process

        // Start the backtracking process from the first index
        backtrack(result, combination, candidates, target, 0);
        return result;
    }

private:
    // Backtracking function to find all combinations that sum up to the target
    void backtrack(vector<vector<int>>& result, vector<int>& combination, vector<int>& candidates, int target, int begin) {
        // Check if the current combination sums up to the target
        if (target == 0) {
            // If yes, add the current combination to the result
            result.push_back(combination);
            return;
        }

        // Iterate through the candidates starting from 'begin' index
        for (int i = begin; i != candidates.size() && target >= candidates[i]; ++i) {
            // Include the current candidate in the combination
            combination.push_back(candidates[i]);

            // Recursively call the function with the updated target (reduced by the value of the current candidate)
            // Note: 'i' is passed instead of 'i+1' because we can use the same element multiple times
            backtrack(result, combination, candidates, target - candidates[i], i);

            // Backtrack: Remove the last element added and try the next candidate
            combination.pop_back();
        }
    }
};


// Description: =======================================================================================================

/*
To solve the "Combination Sum" problem, we need to use backtracking. The essence of backtracking is to explore all possible solutions 
for a problem and to backtrack as soon as we know that a potential solution cannot possibly be a correct one. 

In this case, we explore all combinations of numbers in the `candidates` array that sum up to the `target`. We can pick the same number 
multiple times, and we need to find all unique combinations.


### Explanation:

1. **Sorting Candidates**: Initially, we sort the `candidates` array. This step isn't strictly necessary but can improve efficiency 
   by allowing early termination in some cases.

2. **Backtracking Function**: The `backtrack` function is where the main logic resides. It attempts to build a combination that sums 
   up to the `target`. If the sum of the current combination equals the target, we add it to the `result`.

3. **Recursive Calls**: For each element in the candidates array, we include it in the current combination and recursively call 
   `backtrack` with the updated target (`target - candidates[i]`). After exploring with the current element included, we remove it 
   (backtrack) and try with the next element.

4. **Efficiency Considerations**: The condition `target >= candidates[i]` ensures that we only consider elements that do not exceed 
   the remaining target. This is where sorting helps, as once we reach an element larger than the remaining target, we can stop 
   considering further elements.

5. **Handling Duplicates**: As all elements in the candidates array are distinct, and we are allowed to use the same element multiple 
   times, we do not need to handle duplicates explicitly.

6. **Returning the Result**: Finally, the `combinationSum` function returns the `result`, which contains all unique combinations.

This solution effectively explores all possible combinations using backtracking, ensuring that the sum of elements in each combination 
equals the target, and it handles the possibility of using the same number multiple times.

*/