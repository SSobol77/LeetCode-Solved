// 2483. Minimum Penalty for a Shop

// Topic:


/*
### Task:
---
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

  *  if the i^th character is 'Y', it means that customers come at the i^th hour
  *  whereas 'N' indicates that no customers come at the i^th hour.

If the shop closes at the j^th hour (0 <= j <= n), the penalty is calculated as follows:

  * For every hour when the shop is open and no customers come, the penalty increases by 1.
  * For every hour when the shop is closed and customers come, the penalty increases by 1.

Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the j^th hour, it means the shop is closed at the hour j.

Example 1:
Input: customers = "YYNY"
Output: 2
Explanation: 
- Closing the shop at the 0^th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1^st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2^nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3^rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4^th hour incurs in 0+0+1+0 = 1 penalty.

Closing the shop at 2^nd or 4^th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.

Example 2:
Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0^th hour as no customers arrive.

Example 3:
Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4^th hour as customers arrive at each hour.

Constraints:
1 <= customers.length <= 10^5
customers consists only of characters 'Y' and 'N'.

Hint 1
At any index, the penalty is the sum of prefix count of ‘N’ and suffix count of ‘Y’.
Hint 2
Enumerate all indices and find the minimum such value.


### Testcase:
---
"YYNY"
"NNNNN"
"YYYY"


### Code:
---
class Solution {
public:
    int bestClosingTime(string customers) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    int bestClosingTime(string customers) {
        int n = customers.size();
        int noCustomerCount = 0; // Count of 'N's (no customers when shop is open)
        int minPenalty = INT_MAX;
        int bestHour = 0;

        // Calculate the initial count of 'Y's (customers arrive when shop is closed)
        int customerCountWhenClosed = count(customers.begin(), customers.end(), 'Y');

        for (int i = 0; i <= n; ++i) {
            // Calculate penalty at hour i
            // Penalty = Count of 'N's up to i + Count of 'Y's after i
            int penalty = noCustomerCount + customerCountWhenClosed;

            // Update minimum penalty and the corresponding hour
            if (penalty < minPenalty) {
                minPenalty = penalty;
                bestHour = i;
            }

            // Update counts for next iteration
            if (i < n && customers[i] == 'N') {
                // If shop is open and no customer, increment noCustomerCount
                noCustomerCount++;
            } else if (i < n && customers[i] == 'Y') {
                // If shop is closed and a customer arrives, decrement customerCountWhenClosed
                customerCountWhenClosed--;
            }
        }

        return bestHour; // Return the earliest hour for minimum penalty
    }
};

// Sample Tests:
int main() {
    Solution solution;

    cout << solution.bestClosingTime("YYNY") << endl; // Expected output: 2
    cout << solution.bestClosingTime("NNNNN") << endl; // Expected output: 0
    cout << solution.bestClosingTime("YYYY") << endl; // Expected output: 4

    return 0;
}


// Description: ===================================
/*
### Comments Explanation
---
- `noCustomerCount` keeps track of the number of hours the shop is open without customers ('N's in the string).
- `minPenalty` is initialized to the maximum possible value to find the minimum penalty.
- `customerCountWhenClosed` counts the number of 'Y's in the string, representing hours the shop is closed but customers arrive.
- Within the loop, we calculate the penalty for closing the shop at each hour (i.e., the sum of `noCustomerCount` and `customerCountWhenClosed`).
- The `if` condition inside the loop checks if the current penalty is lower than the minimum recorded penalty. If it is, the minimum penalty and 
  the best closing hour are updated.
- The counters (`noCustomerCount` and `customerCountWhenClosed`) are updated based on whether the shop is open or closed at the current hour.
- Finally, the function returns the best hour to close the shop, which corresponds to the minimum penalty.


To solve the "Minimum Penalty for a Shop" problem, we can follow the hints provided. The key idea is to calculate the penalty at each hour by 
considering the prefix count of 'N' (indicating hours the shop is open but no customers arrive) and the suffix count of 'Y' (indicating hours 
the shop is closed but customers arrive). We'll iterate over each possible closing hour and calculate the penalty, aiming to find the minimum penalty.

Here's a step-by-step approach:
1. Iterate through each character in the `customers` string.
2. Calculate the cumulative count of 'N's (no customers when the shop is open) up to the current hour.
3. Calculate the count of 'Y's (customers when the shop is closed) after the current hour.
4. The penalty for closing the shop at the current hour is the sum of the two counts.
5. Keep track of the minimum penalty and the earliest hour at which this penalty occurs.
6. Return the earliest hour with the minimum penalty.

### Description
---
In this solution, we iterate through the `customers` string and calculate the penalty for closing the shop at each hour. We maintain the count of 'N's 
and decrement the count of 'Y's as we move through the string. The penalty at each hour is the sum of the 'N' count and the remaining 'Y' count. 
We track the minimum penalty and return the earliest hour at which this minimum penalty occurs.


*/
