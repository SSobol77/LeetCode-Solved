// 948. Bag of Tokens.


// Topic: Array, Two Pointers, Greedy, Sorting.


/*
### Task:
---
You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] donates the value of tokeni.

Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):

    - Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
    - Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.

Return the maximum possible score you can achieve after playing any number of tokens.

Example 1:
Input: tokens = [100], power = 50
Output: 0
Explanation: Since your score is 0 initially, you cannot play the token face-down. You also cannot play it face-up since your power (50) is less than tokens[0] (100).

Example 2:
Input: tokens = [200,100], power = 150
Output: 1
Explanation: Play token1 (100) face-up, reducing your power to 50 and increasing your score to 1.
There is no need to play token0, since you cannot play it face-up to add to your score. The maximum score achievable is 1.

Example 3:
Input: tokens = [100,200,300,400], power = 200
Output: 2
Explanation: Play the tokens in this order to get a score of 2:

Play token0 (100) face-up, reducing power to 100 and increasing score to 1.
Play token3 (400) face-down, increasing power to 500 and reducing score to 0.
Play token1 (200) face-up, reducing power to 300 and increasing score to 1.
Play token2 (300) face-up, reducing power to 0 and increasing score to 2.
The maximum score achievable is 2.

Constraints:
0 <= tokens.length <= 1000
0 <= tokens[i], power < 10^4

### Testcase:
---
[100]
50
[200,100]
150
[100,200,300,400]
200


### Code:
---
class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        
    }
};


*/
// Solution: --------------------------------------


class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        // Step 1: Sort the tokens in non-decreasing order.
        sort(tokens.begin(), tokens.end());

        // Initialize two pointers for the two ends of the array.
        int left = 0, right = tokens.size() - 1;

        // Initialize variables to keep track of the current and maximum scores.
        int maxScore = 0, currentScore = 0;

        // Step 3: Iterate through the tokens array as long as left is less than or equal to right.
        while (left <= right) {
            if (power >= tokens[left]) { 
                // Play Face-Up: If we have enough power to play the leftmost token face-up,
                // we do so to gain a score. We then increase the left pointer to move to the next token.
                power -= tokens[left++];
                currentScore++;
                // Update the maximum score achieved so far.
                maxScore = max(maxScore, currentScore);
            } else if (currentScore > 0) {
                // Play Face-Down: If we don't have enough power to play any token face-up,
                // but we have at least 1 score, we can play the rightmost token face-down
                // to regain some power. We then decrease the right pointer to move to the next token from the end.
                power += tokens[right--];
                currentScore--;
            } else {
                // If we cannot play a token face-up (due to lack of power) or face-down (due to lack of score),
                // we break out of the loop as no more tokens can be played.
                break;
            }
        }

        // Step 5: Return the maximum score that can be achieved.
        return maxScore;
    }
};


// Description: ===================================
/*
To solve the "Bag of Tokens" problem, we can follow a greedy approach using two pointers. The main idea is to play tokens 
face-up to gain scores when we have enough power, and play tokens face-down to regain power when we don't have enough power 
to play any more tokens face-up but still have scores to spend. The process involves sorting the tokens first to ensure we 
always play the smallest token face-up and the largest token face-down.

Here's a step-by-step guide to the algorithm:

1. **Sort the Tokens**: Sort the array of tokens to ensure that we always play the least power-consuming token face-up and 
the highest power-giving token face-down.

2. **Initialize Variables**: Set up two pointers, `left` at the start of the array and `right` at the end. Also, initialize 
`maxScore` and `currentScore` to 0.

3. **Iterate through Tokens**: While the `left` pointer is less than or equal to `right`:

   - **Play Face-Up**: If the current power is greater than or equal to `tokens[left]`, play this token face-up. Decrease the 
     power by `tokens[left]` and increase `currentScore` by 1. Move the `left` pointer to the right (i.e., `left++`).

   - **Play Face-Down**: If the current power is not enough to play the `left` token face-up, and `currentScore` is greater 
     than 0, play the `right` token face-down. Increase the power by `tokens[right]` and decrease `currentScore` by 1. Move 
     the `right` pointer to the left (i.e., `right--`).

   - If neither condition is met, break the loop as no more tokens can be played.

4. **Update Max Score**: After each move, update `maxScore` with the maximum of `maxScore` and `currentScore`.

5. **Return Max Score**: After the loop ends, return `maxScore` as the maximum possible score achievable.


This implementation first sorts the tokens and then iteratively plays the tokens face-up or face-down based on the current power 
and score, always updating the maximum score achieved. It ensures the greedy strategy of minimizing power loss and maximizing score 
gain at each step.

*/
