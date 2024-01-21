# 2225. Find Players With Zero or One Losses            - Medium -

       

# Topic: Array, Hash Table, Sorting, Counting.

"""
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
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
"""
### Solution: ----------------------------------------------------------------


class Solution:
    def findWinners(self, matches):
        loss_count = {}
        has_won = {}

        # Count losses and track winners
        for winner, loser in matches:
            loss_count[loser] = loss_count.get(loser, 0) + 1
            has_won[winner] = True

        # Categorize players
        no_loss = [player for player in has_won if loss_count.get(player, 0) == 0]
        one_loss = [player for player, losses in loss_count.items() if losses == 1]

        # Sort and return result
        return [sorted(no_loss), sorted(one_loss)]

# Test cases
sol = Solution()
print(sol.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))  # [[1,2,10],[4,5,7,8]]
print(sol.findWinners([[2,3],[1,3],[5,4],[6,4]]))  # [[1,2,5,6],[]]


### Description: -------------------------------------------------------------
'''
To solve this problem, we can use a hash table (or a dictionary in Python) to keep track of the number of losses for each player. We'll iterate through the `matches` list and update the count of losses for the losers of each match. Then, we can categorize the players into two groups: those who have not lost any matches and those who have lost exactly one match.

Here's a step-by-step approach:

1. **Initialize two dictionaries**: One for counting losses (`loss_count`) and another for checking if a player has ever won a match (`has_won`).

2. **Iterate over the matches**: For each match, increment the loss count for the loser and mark the winner as having won at least one match.

3. **Categorize players**: Based on the loss count and whether they've won at least one match, categorize players into two groups: 
   - Players with zero losses (who have won at least once).
   - Players with exactly one loss.

4. **Sort and return the result**: Sort the players in each category in increasing order and return the lists as the final result.


This code creates a `Solution` class with a `findWinners` method that takes a list of matches and returns the desired output. 
It effectively counts the losses and categorizes the players based on the criteria given in the problem statement.

'''
