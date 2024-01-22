# 403. Frog Jump.           - HARD -

# Topic: Array, Dynamic Programming.

"""
### Task:
---
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.



Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.


Constraints:

2 <= stones.length <= 2000
0 <= stones[i] <= 2^31 - 1
stones[0] == 0
stones is sorted in a strictly increasing order.


### Testcase:
---
[0,1,3,5,6,8,12,17]
[0,1,2,3,4,8,9,11]

### Code:
---
class Solution:
    def canCross(self, stones: List[int]) -> bool:

"""
### Solution:   ---------------------------------------------------------------------

class Solution:
    def canCross(self, stones):
        # First, check if the frog can make the initial jump
        if stones[1] != 1:
            return False

        # Dictionary to hold the positions of stones and corresponding jump sizes that can reach each stone
        jump_sizes = {stone: set() for stone in stones}
        # The first jump is always 1 unit, so we add 1 to the set for the second stone
        jump_sizes[1].add(1)

        # Iterate over each stone in the array
        for stone in stones:
            # Iterate over each jump size that can reach the current stone
            for jump in jump_sizes[stone]:
                # For each jump size, calculate the next possible jump sizes
                for next_jump in (jump - 1, jump, jump + 1):
                    # Check if the next jump is positive and can reach a stone in the array
                    if next_jump > 0 and stone + next_jump in jump_sizes:
                        # Add the next jump size to the set of jump sizes for the stone that can be reached
                        jump_sizes[stone + next_jump].add(next_jump)

        # Check if the last stone has any jump sizes that can reach it
        # If yes, it means the frog can reach the last stone
        return bool(jump_sizes[stones[-1]])

# Test cases
sol = Solution()
print(sol.canCross([0,1,3,5,6,8,12,17]))  # Output: True
print(sol.canCross([0,1,2,3,4,8,9,11]))   # Output: False


### Description: ====================================================================
'''
This problem can be solved using dynamic programming. The main idea is to keep track of the positions
where the frog can reach and the last jump size at each position. Since the frog can make a jump of
size k-1, k, or k+1 from its current position, we need to check if any of these jumps can reach the
next stone.

### Additional Comments:
- **Initialization**: We initialize a dictionary `jump_sizes` where keys are the stone positions and values are sets of jump sizes that can reach that stone.
- **Initial Jump Check**: We check if the second stone (`stones[1]`) is one unit away from the first stone. If not, it's impossible for the frog to start, and we return `False`.
- **Main Loop**: We iterate over each stone. For each stone, we consider all jump sizes that can reach it and then calculate the next possible jumps.
- **Next Jump Calculation**: For each jump size, we calculate three possible next jumps (k-1, k, k+1) and check if they can reach another stone in the river.
- **Final Check**: We check if the last stone in `stones` has any possible jump sizes that reach it. If so, the frog can reach the last stone, and we return `True`. If the set is empty, it means there's no way to reach the last stone, and we return `False`.


Here's how we can implement this:

1. **Initialize a dictionary** that maps each stone to a set of jump sizes that can reach that stone.
2. **Iterate over each stone**, and for each stone, iterate over the jump sizes that can reach it.
3. **For each jump size**, calculate the next jump sizes (k-1, k, k+1) and check if these jumps can
     reach the next stone.
4. If we can reach the last stone, return `True`.


### Explanation:
- The dictionary `jump_sizes` maps each stone to a set of jump sizes that can reach that stone.
- We start from the second stone (index 1) and assume the first jump is always 1 unit.
- For each stone, we look at the possible jumps that can reach it and calculate the next possible jumps.
- If the set of jump sizes for the last stone is not empty, it means the frog can reach the last stone.

The time complexity of this solution is O(n^2) in the worst case, as for each stone, we might have to check
all previous stones. The space complexity is also O(n^2) due to the storage of jump sizes for each stone.

'''
