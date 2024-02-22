// 997. Find the Town Judge.


// Topic: Array, Hash Table, Graph.


/*
### Task:
---
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Constraints:
1 <= n <= 1000
0 <= trust.length <= 10^4
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n

### Testcase:
---
2
[[1,2]]
3
[[1,3],[2,3]]
3
[[1,3],[2,3],[3,1]]


### Code:
---
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        
    }
};

*/


// Solution: --------------------------------------

class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        // Arrays to keep track of in-degrees and out-degrees
        vector<int> inDegrees(n + 1, 0);
        vector<int> outDegrees(n + 1, 0);

        // Process the trust relationships
        for (const auto& relation : trust) {
            int a = relation[0]; // Person who trusts
            int b = relation[1]; // Person being trusted

            // Increment the in-degree of the person being trusted
            // and the out-degree of the person who trusts
            inDegrees[b]++;
            outDegrees[a]++;
        }

        // Find the town judge
        for (int i = 1; i <= n; ++i) {
            if (inDegrees[i] == n - 1 && outDegrees[i] == 0) {
                // If a person's in-degree is n-1 and out-degree is 0,
                // they are the town judge
                return i;
            }
        }

        // If no town judge is found
        return -1;
    }
};


// Description: ===================================
/*
To find the town judge, we can use a graph theory approach. Each person in the town can be seen as a vertex in the graph, and 
each trust relationship can be seen as a directed edge from one person to another. The town judge, if exists, would be the vertex 
with in-degree of `n-1` (everybody trusts the judge) and out-degree of `0` (the judge trusts nobody).

We can use two arrays to keep track of the in-degrees and out-degrees of each vertex. The in-degree of a vertex is the number of 
edges coming into it, and the out-degree of a vertex is the number of edges going out from it. Initially, all values in these arrays 
are 0. For each trust relationship `[a, b]` in the `trust` array, we increment the in-degree of `b` and the out-degree of `a`. After 
processing all trust relationships, the town judge will be the person whose in-degree is `n-1` and out-degree is `0`.


### Description:

In this solution, we initialize two arrays, `inDegrees` and `outDegrees`, to keep track of the in-degrees and out-degrees of each person 
in the town. We then iterate over each trust relationship, updating the in-degree for the person being trusted and the out-degree for the 
person who trusts. Finally, we iterate through each person, checking if their in-degree is `n-1` and out-degree is `0`, which would identify
them as the town judge. If no such person exists, we return `-1`.

*/
