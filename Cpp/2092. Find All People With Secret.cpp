// 2092. Find All People With Secret.            - HARD -


// Topic: Depth-First Search, Breadth-First Search, Union Find, Graph, Sorting.


/**
### Task:
---
You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.

Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.

The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.

Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.

Example 1:
Input: n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
Output: [0,1,2,3,5]
Explanation:
At time 0, person 0 shares the secret with person 1.
At time 5, person 1 shares the secret with person 2.
At time 8, person 2 shares the secret with person 3.
At time 10, person 1 shares the secret with person 5.​​​​
Thus, people 0, 1, 2, 3, and 5 know the secret after all the meetings.

Example 2:
Input: n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3
Output: [0,1,3]
Explanation:
At time 0, person 0 shares the secret with person 3.
At time 2, neither person 1 nor person 2 know the secret.
At time 3, person 3 shares the secret with person 0 and person 1.
Thus, people 0, 1, and 3 know the secret after all the meetings.

Example 3:
Input: n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1
Output: [0,1,2,3,4]
Explanation:
At time 0, person 0 shares the secret with person 1.
At time 1, person 1 shares the secret with person 2, and person 2 shares the secret with person 3.
Note that person 2 can share the secret at the same time as receiving it.
At time 2, person 3 shares the secret with person 4.
Thus, people 0, 1, 2, 3, and 4 know the secret after all the meetings.
 
Constraints:
2 <= n <= 10^5
1 <= meetings.length <= 10^5
meetings[i].length == 3
0 <= xi, yi <= n - 1
xi != yi
1 <= timei <= 10^5
1 <= firstPerson <= n - 1

Hint 1:
Could you model all the meetings happening at the same time as a graph?
Hint 2:
What data structure can you use to efficiently share the secret?
Hint 3:
You can use the union-find data structure to quickly determine who knows the secret and share the secret.

### Testcase:
---
6
[[1,2,5],[2,3,8],[1,5,10]]
1
4
[[3,1,3],[1,2,2],[0,3,3]]
3
5
[[3,4,2],[1,2,1],[2,3,1]]
1


### Code:
---
class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        
    }
};

*/

// Solution: --------------------------------------

class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        // Initialize Union-Find structure.
        vector<int> parent(n), rank(n, 0);
        iota(parent.begin(), parent.end(), 0); // Set each person as their own parent initially.

        // Define the find function with path compression for Union-Find.
        function<int(int)> find = [&](int x) -> int {
            return x == parent[x] ? x : parent[x] = find(parent[x]);
        };

        // Define the union function for Union-Find, which unions sets by rank.
        auto unionSets = [&](int x, int y) {
            x = find(x), y = find(y);
            if (x != y) {
                if (rank[x] < rank[y]) {
                    parent[x] = y; // Attach smaller rank tree under root of higher rank tree.
                } else if (rank[x] > rank[y]) {
                    parent[y] = x; // Attach smaller rank tree under root of higher rank tree.
                } else {
                    parent[y] = x; // If ranks are the same, make one root and increment its rank.
                    rank[x]++;
                }
            }
        };

        // Initially, person 0 shares the secret with firstPerson.
        unionSets(0, firstPerson);

        // Sort the meetings based on their time to process them chronologically.
        sort(meetings.begin(), meetings.end(), [](const auto& a, const auto& b) {
            return a[2] < b[2];
        });

        // Temporary storage to keep track of meetings and involved people for each unique time.
        vector<pair<int, int>> tempMeetings;
        unordered_set<int> involved;
        int lastTime = -1; // Track the last processed time.

        // Function to process and clear temporary meetings and involved people.
        auto processMeetings = [&]() {
            for (auto& m : tempMeetings) {
                unionSets(m.first, m.second); // Union the participants of each meeting.
            }

            for (int person : involved) {
                // If a person is not connected to person 0, reset their parent and rank.
                if (find(person) != find(0)) {
                    parent[person] = person;
                    rank[person] = 0;
                }
            }

            // Clear the temporary storage after processing.
            tempMeetings.clear();
            involved.clear();
        };

        // Iterate through all meetings to group them by time and process each group.
        for (auto& meeting : meetings) {
            if (meeting[2] != lastTime && !tempMeetings.empty()) {
                processMeetings(); // Process the previous group of meetings.
            }

            lastTime = meeting[2]; // Update the last processed time.
            tempMeetings.emplace_back(meeting[0], meeting[1]); // Add the meeting to the temporary list.
            involved.insert(meeting[0]); // Mark the participants as involved.
            involved.insert(meeting[1]);
        }

        // Process the last group of meetings if any remain.
        if (!tempMeetings.empty()) {
            processMeetings();
        }

        // Collect the result: all people connected to person 0 know the secret.
        vector<int> result;
        for (int i = 0; i < n; ++i) {
            if (find(i) == find(0)) {
                result.push_back(i);
            }
        }

        return result; // Return the list of people who know the secret.
    }
};


// Description: ===================================
/*
This solution tackles a problem related to secret sharing among individuals attending various meetings at different times. 
The goal is to determine which individuals will know a secret after all meetings have concluded, given that the secret is initially 
known by person 0 and a specified `firstPerson`.

### Key Concepts and Data Structures:

- **Union-Find Data Structure**: Used for efficiently managing and merging sets, representing individuals who know the secret. It consists 
    of two main operations:

        - `find`: Determines the representative (or root) of a set containing a given element, applying path compression for efficiency.
        - `unionSets`: Merges two sets into one, based on the rank (depth of the tree), ensuring the tree remains balanced.

- **Sorting Meetings by Time**: Meetings are sorted chronologically to process them in order, simulating the real-time flow and sharing of 
    the secret.

- **Batch Processing of Meetings**: Meetings occurring at the same time are processed together. This approach simulates the instantaneous 
    sharing of the secret among participants of these meetings.

- **Temporary Storage for Batch Processing**: Uses a temporary list to store meetings and a set to track involved individuals for each 
    unique meeting time. This allows for efficient management of meetings and participants within the same time frame.

### Algorithm Overview:

1. **Initialization**: Set up the Union-Find structure with each person initially in their own set. Union person 0 and `firstPerson` 
     since they share the secret at the start.

2. **Sort and Process Meetings**: Sort all meetings by time to ensure chronological processing. Iterate through the sorted meetings, 
     grouping them by their meeting times.

3. **Union and Reset Operations**:
   - For each time group, perform union operations for all meeting participants, temporarily connecting them.
   - After processing a time group, check each involved individual. If they are not connected to person 0 (do not know the secret), reset 
     their Union-Find structure to reflect their isolated state.

4. **Collect Results**: After all meetings are processed, iterate through all individuals. Those connected to person 0 in the Union-Find 
     structure are considered to know the secret.

5. **Return the Final List**: Compile and return a list of all individuals who know the secret after all meetings.

### Efficiency Considerations:

- The Union-Find structure, with path compression and union by rank, ensures efficient management of sets, keeping the trees balanced 
  and minimizing the time complexity of find and union operations.
- Processing meetings in batches by their times reduces the number of redundant operations, enhancing the overall efficiency.
- The algorithm ensures that only necessary union operations are performed, and individuals are only reset if they do not remain 
  connected to person 0, minimizing unnecessary computations.

This solution effectively models the problem as a series of dynamic connections among individuals, leveraging efficient data 
structures and algorithms to determine the spread of the secret through the network of meetings.

*/
