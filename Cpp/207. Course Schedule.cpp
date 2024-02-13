// 207. Course Schedule.


// Topic: Depth-First Search, Breadth-First Search, Graph, Topological Sort


/*
### Task:
---
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 
Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

Hint 1:
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Hint 2:
Topological Sort via DFS - A great tutorial explaining the basic concepts of Topological Sort.
Hint 3:
Topological sort could also be done via BFS.

### Testcase:
---
2
[[1,0]]
2
[[1,0],[0,1]]


### Code:
---
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
    }
};


*/
// Solution: --------------------------------------

#include <vector>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses); // Adjacency list representation of graph
        vector<int> visited(numCourses, 0); // Track visited courses: 0 = unvisited, 1 = visiting, 2 = visited

        // Build the graph
        for (const auto& pre : prerequisites) {
            graph[pre[1]].push_back(pre[0]);
        }

        // Check for cycles in the graph
        for (int i = 0; i < numCourses; ++i) {
            if (visited[i] == 0) { // If the course hasn't been visited
                if (isCyclic(graph, visited, i)) {
                    return false; // Cycle detected, impossible to finish all courses
                }
            }
        }

        return true; // No cycles detected, possible to finish all courses
    }

private:
    bool isCyclic(const vector<vector<int>>& graph, vector<int>& visited, int course) {
        if (visited[course] == 1) return true; // Cycle detected
        if (visited[course] == 2) return false; // Already visited, no cycle here

        visited[course] = 1; // Mark the course as being visited

        // Recursively visit all the prerequisites of the current course
        for (int prereq : graph[course]) {
            if (isCyclic(graph, visited, prereq)) {
                return true; // Cycle detected in the prerequisites
            }
        }

        visited[course] = 2; // Mark the course as fully visited
        return false; // No cycle detected
    }
};


// Description: ===================================
/*
To solve the "Course Schedule" problem, we can model the courses and their prerequisites as a directed graph, where each course 
is a node and a directed edge from node `a` to node `b` indicates that course `b` is a prerequisite for course `a`. The problem 
then reduces to detecting if there's a cycle in this directed graph. If there's a cycle, it's impossible to complete all courses, 
so we should return `false`. Otherwise, we can return `true`.

We can use Depth-First Search (DFS) to detect cycles. During the DFS, we mark each node with one of three states: unvisited, 
visiting, and visited. A cycle is detected if we encounter a node that is currently being visited.

### Comments Explanation:

- **Graph Representation**: The graph is represented as an adjacency list, where `graph[i]` contains a list of courses that require course `i` as a prerequisite.
- **Visited States**: Each course has three states represented by the `visited` vector: `0` for unvisited, `1` for visiting (currently in the DFS stack), and `2` for visited (fully explored).
- **Building the Graph**: The graph is built based on the prerequisites. For each pair `[a, b]` in `prerequisites`, an edge from `b` to `a` is added to the graph, indicating that course `a` requires course `b`.
- **Cycle Detection**: The `isCyclic` function performs a DFS from the given course and checks for cycles. If a course being visited (`visited[course] == 1`) is encountered again, a cycle is detected, indicating it's impossible to complete all courses.
- **DFS Traversal**: The main function iterates over all courses and performs a DFS for courses that haven't been visited. If a cycle is detected in any DFS call, the function returns `false`.
- **Completion Check**: If no cycles are detected after exploring all courses, it's possible to complete all courses, and the function returns `true`.

*/
