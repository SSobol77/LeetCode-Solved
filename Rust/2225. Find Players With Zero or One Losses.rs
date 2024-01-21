// 2225. Find Players With Zero or One Losses.         - Medium -

// Topic: Array, Hash Table, Sorting, Counting.

/*
### Task:
---
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri 
defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:
You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.

#Example 1:
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

#Example 2:
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].

#Constraints:
1 <= matches.length <= 10^5
matches[i].length == 2
1 <= winneri, loseri <= 10^5
winneri != loseri
All matches[i] are unique.

Hint 1:
Count the number of times a player loses while iterating through the matches.

### Testcase:
---
[[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
[[2,3],[1,3],[5,4],[6,4]]


### Code:
---
impl Solution {
    pub fn find_winners(matches: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
*/
// Solution: ----------------------------------------------------------

use std::collections::HashMap;

impl Solution {
    pub fn find_winners(matches: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        // Create a HashMap to store the loss count of each player.
        let mut loss_count = HashMap::new();

        // Iterate over each match.
        for match_result in &matches {
            // Increment the loss count for the losing player.
            // If the player is not already in the map, it's initialized to 0 and then incremented.
            *loss_count.entry(match_result[1]).or_insert(0) += 1;

            // Add the winning player to the map with 0 losses if they are not already present.
            // This is to account for players who have won but never lost.
            loss_count.entry(match_result[0]).or_insert(0);
        }

        // Vectors to store players with no losses and exactly one loss.
        let mut no_loss = Vec::new();
        let mut one_loss = Vec::new();

        // Iterate through the loss count map.
        for (&player, &losses) in &loss_count {
            match losses {
                0 => no_loss.push(player), // Add player to no_loss list if they have 0 losses.
                1 => one_loss.push(player), // Add player to one_loss list if they have 1 loss.
                _ =>

{}, // Ignore players with more than one loss.
            }
        }

        // Sort the lists of players with no losses and one loss in increasing order.
        // Unstable sort is used for efficiency as we don't need to maintain order between equal elements.
        no_loss.sort_unstable();
        one_loss.sort_unstable();

        // Return the vector containing the two lists.
        // The first list contains players with no losses, and the second list contains players with exactly one loss.
        vec![no_loss, one_loss]
    }
}



// Description: -------------------------------------------------------
/*
To solve the problem "Find Players With Zero or One Losses", we will approach it step by step.

### Algorithm:
1. Use hash tables (like `HashMap` in Rust) to keep track of the number of losses for each player. 
2. Iterate through the `matches` vector, updating the loss count for each player.
3. Iterate through the hash table to categorize players into two groups: those with zero losses and those with exactly one loss.
4. Sort both lists in increasing order.
5. Return the final result as a vector containing these two lists.

### Description of the Implementation:
- We utilize a `HashMap` to store the loss count for each player. The key is the player's ID, and the value is the number of losses.
- We iterate over each match in `matches`, updating the loss count for the loser. If a player is not already in the map (indicating no prior losses), we add them with a loss count of 0.
- After processing all matches, we separate the players into two groups based on their loss count: those with zero losses and those with exactly one loss.
- We then sort these lists in increasing order to meet the problem's requirement.
- Finally, we return a vector containing these two sorted lists. 

This implementation should efficiently solve the problem while maintaining the constraints provided.

*/