// 787. Cheapest Flights Within K Stops.


// Topic: Dynamic Programming, Depth-First Search, Breadth-First Search, Graph, Heap (Priority Queue), Shortest Path.


/*
### Task:
---
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

Constraints:
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst


### Testcase:
---
4
[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
0
3
1
3
[[0,1,100],[1,2,100],[0,2,500]]
0
2
1
3
[[0,1,100],[1,2,100],[0,2,500]]
0
2
0


### Code:
---
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        
    }
};

*/

// Solution: --------------------------------------

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // Initialize the DP table with INT_MAX
        vector<vector<long>> dp(k + 2, vector<long>(n, INT_MAX));
        
        // The cost to reach src from src with 0 stops is 0
        dp[0][src] = 0;

        // Relaxing edges up to k + 1 times (k stops)
        for (int stops = 1; stops <= k + 1; ++stops) {
            dp[stops][src] = 0;  // Cost to reach src remains 0
            for (const auto& flight : flights) {
                int from = flight[0], to = flight[1], price = flight[2];
                
                // If there is no way to reach 'from' city with stops - 1, continue
                if (dp[stops - 1][from] == INT_MAX) continue;
                
                // Relaxation step
                dp[stops][to] = min(dp[stops][to], dp[stops - 1][from] + price);
            }
        }
        
        // The answer is the minimum cost to reach dst with at most k stops
        long answer = dp[k + 1][dst];
        return answer == INT_MAX ? -1 : answer;
    }
};


// Description: ===================================
/*
To solve the "Cheapest Flights Within K Stops" problem, we can use a Dynamic Programming approach, which is particularly efficient for this type of shortest path problem with constraints (like the maximum number of stops). The Bellman-Ford algorithm is a suitable choice here, as it is designed to find the shortest paths from a single source to all other vertices in a weighted graph, handling graphs with negative weight edges as well.

### Approach:

1. **Initialization:** Create a 2D array `dp` with dimensions `(k + 2) x n` to store the minimum costs. `dp[i][j]` represents the minimum cost to reach city `j` from the source city `src` with at most `i - 1` stops. Initialize the first row (i.e., when 0 stops are used) with `INT_MAX` (infinity) except for `dp[0][src]`, which should be 0, as it costs nothing to stay at the source.
   
2. **Dynamic Programming Update:** For each level of stops from 1 to `k + 1` (inclusive), iterate through each flight `[from, to, price]` and update the DP table: `dp[stops][to] = min(dp[stops][to], dp[stops - 1][from] + price)`. This step essentially relaxes the edges, considering an additional stop and updating the minimum cost if a cheaper path is found.

3. **Answer Extraction:** After filling the DP table, the answer will be in `dp[k + 1][dst]`, which represents the minimum cost to reach `dst` from `src` with at most `k` stops. If this value is `INT_MAX`, it means no such path exists, and we return -1.

### Explanation:

- The DP table `dp` is used to keep track of the minimum costs while incrementally increasing the number of stops.
- By iterating up to `k + 1` stops, we ensure that the path can have at most `k` intermediate stops between the source and the destination.
- The relaxation step updates the DP table based on the current knowledge of the cheapest paths with one less stop.
- If the final cost to reach the destination is still `INT_MAX`, it indicates that no such path adhering to the constraints exists, hence `-1` is returned.

*/
