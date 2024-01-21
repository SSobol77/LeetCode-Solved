# 210. Course Schedule II

# Topic: Depth-First Search, Breadth-First Search, Graph, Topological Sort

'''
# Task:
-------
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.

Hint 1
This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Hint 2
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Hint 3
Topological sort could also be done via BFS.


# Testcase:
-----------
2
[[1,0]]
4
[[1,0],[2,0],[3,1],[3,2]]
1
[]


# Code:
-------
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

'''
# Solution:
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Creating a graph where each node represents a course
        graph = {i: [] for i in range(numCourses)}
        for dest, src in prerequisites:
            graph[src].append(dest)  # Adding course dependencies

        # States: 0 = unvisited, 1 = visiting, -1 = visited
        state = [0] * numCourses
        order = []

        # DFS function for topological sorting
        def dfs(course):
            if state[course] == -1:
                return True  # Course already processed
            if state[course] == 1:
                return False  # Cycle detected

            state[course] = 1  # Marking course as visiting
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            state[course] = -1  # Marking course as visited
            order.append(course)  # Adding course to the order
            return True

        # Checking each course for cycles and processing for order
        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return []  # Cycle detected, return empty array

        return order[::-1]  # Reversing the order for correct topological sorting

# Testing the solution
sol = Solution()
print(sol.findOrder(2, [[1,0]]))  # [0, 1]
print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))  # [0, 1, 2, 3] or [0, 2, 1, 3]
print(sol.findOrder(1, []))  # [0]


# Description:
'''
Description of the Solution for "Course Schedule II" Problem:

The "Course Schedule II" problem is a classic example of applying topological sorting in a directed graph to solve 
course scheduling with prerequisites. The goal is to find an order in which all courses can be completed, given the 
prerequisites for each course.

Key Concepts:
Directed Graph Representation: The courses and their prerequisites are represented as a directed graph, where each 
course is a node, and a directed edge from course A to B implies A is a prerequisite for B.

Topological Sorting: The problem is solved using topological sorting, which orders the nodes (courses) in a linear 
sequence such that for every directed edge from A to B, A comes before B in the ordering.

Cycle Detection: A critical aspect of this problem is detecting cycles. If a cycle exists, it's impossible to complete 
all courses, and the function should return an empty array.

Solution Approach:
Graph Construction: The solution starts by constructing a graph from the prerequisites. Each course points to the courses 
that require it as a prerequisite.

DFS for Topological Sort: Depth-First Search (DFS) is used for topological sorting. The algorithm explores each node 
and its neighbors recursively.

State Tracking: Each course is marked with its state: unvisited (0), visiting (1), or visited (-1). This helps in both 
cycle detection and ensuring each node is processed only once.

Order Determination: The courses are added to the order list in their finishing order (when their DFS recursion finishes).
This order is then reversed at the end to get the correct topological order.

Cycle Detection: If a cycle is detected (a course in the current path is revisited), the function returns an empty array.

Result: The function returns the topological order of courses if possible, otherwise an empty array.

Efficiency:
Time Complexity: O(N + P), where N is the number of courses and P is the number of prerequisites. Each node and edge is 
visited once.
Space Complexity: O(N + P) for storing the graph and O(N) for the recursion stack in DFS.
This solution efficiently determines the order of courses using topological sorting with DFS, handling cycles and 
dependencies effectively.


'''
