# 2225. Find Players With Zero or One Losses.        MEDIUM

# Topic: Array, Hash Table, Sorting, Counting.

"""
### Task:
---
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

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

### Testcase:
---
[[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
[[2,3],[1,3],[5,4],[6,4]]


### Code:
---
class Solution(object):
    def findWinners(self, matches):
        '''
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        '''
        
"""
### Solution: ---------------------------------------------------------

class Solution(object):
    def findWinners(self, matches):
        no_losses = set()
        one_loss = set()
        loss_count = {}

        # Add all players to no_losses initially
        for winner, loser in matches:
            no_losses.add(winner)
            no_losses.add(loser)

        for winner, loser in matches:
            # Update loss count for the loser
            if loser in loss_count:
                loss_count[loser] += 1
            else:
                loss_count[loser] = 1

            # Update sets based on loss count
            if loss_count[loser] == 1:
                one_loss.add(loser)
            elif loss_count[loser] > 1:
                one_loss.discard(loser)

            # Remove the loser from no_losses
            no_losses.discard(loser)

        return [sorted(list(no_losses)), sorted(list(one_loss))]

# Testing the corrected solution
sol = Solution()
print(sol.findWinners(test1))  # Expected Output: [[1,2,10],[4,5,7,8]]
print(sol.findWinners(test2))  # Expected Output: [[1,2,5,6],[]]



### Desription: ---------------------------------------------------------
'''
Sure, here's a description of the solution to the problem of finding players with zero or one losses 
in a series of matches:

### Problem Description
Given an array of match outcomes, where each element is a pair `[winner, loser]` indicating the winner 
and loser of a match, the task is to find all players who have not lost any matches and all players who 
have lost exactly one match.

### Solution Overview
The solution involves tracking the number of losses for each player and whether they have played at least
one match. This is achieved using data structures like sets and a dictionary.

### Implementation Details
1. **Initialization**: 
   - `no_losses`: A set to store players with no losses.
   - `one_loss`: A set to store players with exactly one loss.
   - `loss_count`: A dictionary to count the number of losses for each player.

2. **Populating `no_losses`**:
   - Initially, add every player (both winners and losers) to the `no_losses` set.

3. **Processing Matches**:
   - Iterate through each match in `matches`.
   - Update `loss_count` for the loser of each match. If it's their first loss, add them to `one_loss` and 
     remove them from `no_losses`. If they lose more than once, remove them from `one_loss`.

4. **Updating `no_losses`**:
   - Remove a player from `no_losses` if they lose a match.

5. **Result**:
   - Convert the `no_losses` and `one_loss` sets to sorted lists and return them as the final result.

### Test Cases
- **Test Case 1**: For matches like `[[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]`, the 
                   solution correctly identifies `[[1,2,10],[4,5,7,8]]` as the output.
- **Test Case 2**: For matches like `[[2,3],[1,3],[5,4],[6,4]]`, the solution correctly returns `[[1,2,5,6],[]]`.

### Conclusion
This solution efficiently tracks players' performance across matches, accurately identifying those with zero or 
one losses. It handles various scenarios and test cases effectively, ensuring correctness and performance.

'''
