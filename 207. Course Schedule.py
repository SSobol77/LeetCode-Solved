# 207. Course Schedule

# Topic

'''
# Task:
-------
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

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
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is
impossible.
 
Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.


# Testcase:
-----------
2
[[1,0]]
2
[[1,0],[0,1]]


# Code:
-------
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
'''
# Solution:
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Creating a graph where each node represents a course
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)  # Adding prerequisites for each course

        # Set to keep track of visited courses
        visited = set()

        # Function to check for a cycle using DFS
        def dfs(course, path):
            if course in path:
                return False  # Cycle detected
            if course in visited:
                return True  # Course already checked and no cycle found

            path.add(course)  # Mark the course as being visited in the current path
            for prereq in graph[course]:
                if not dfs(prereq, path):  # Recursively visit prerequisites
                    return False
            path.remove(course)  # Remove the course from the current path
            visited.add(course)  # Mark the course as fully visited
            return True

        # Checking each course for a cycle
        for course in range(numCourses):
            if not dfs(course, set()):  # If a cycle is found, return False
                return False

        return True  # If no cycles are found, all courses can be finished

# Testing the solution
sol = Solution()
print(sol.canFinish(2, [[1,0]]))  # Expected output: True
print(sol.canFinish(2, [[1,0],[0,1]]))  # Expected output: False


# Description:
'''
To solve the "Course Schedule" problem, we can use the concept of topological sorting in a graph. This task boils
down to determining whether there is a cycle in a directed graph representing courses and their prerequisites. If
the cycle exists, it means that it is impossible to complete all the courses. We can use Kahn's algorithm or 
depth-first search (DFS) to detect the loop.
This code uses Depth-First Search (DFS) to detect cycles in the graph representing courses and their prerequisites.
If a cycle is detected, it's impossible to complete all courses, and the function returns False. Otherwise, it returns 
True, indicating that all courses can be completed.

Description of the Solution for "Course Schedule" Problem:

The given Python solution addresses the "Course Schedule" problem, which is a classic problem in computer science related 
to course scheduling and dependency resolution. The main objective is to determine whether all courses can be completed 
given a set of prerequisite relationships.

Key Concepts:

* Graph Representation: The problem is modeled as a directed graph where each node represents a course, and edges represent 
prerequisite relationships. An edge from node A to node B implies that course A is a prerequisite for course B.

* Cycle Detection: The core challenge is to detect if there's a cycle in the graph. If a cycle exists, it's impossible to 
complete all courses (as it would require completing a course before its prerequisite).

* Solution Approach:
Graph Construction: The solution begins by constructing a graph from the given prerequisites list. Each course is a node,
and a directed edge is created from each prerequisite to the corresponding course.

* Depth-First Search (DFS): The solution employs DFS to traverse the graph. DFS is a suitable choice for cycle detection in 
directed graphs.

* Cycle Detection: During the DFS traversal, the algorithm keeps track of the courses currently in the traversal path. If a 
course is encountered that is already in the current path, a cycle is detected, indicating that it's impossible to complete 
all courses.

* Visited Set: A set of visited nodes is maintained to avoid reprocessing a node. Once a node is fully processed (all its 
descendants are visited), it's added to the visited set.

* Checking Each Course: The algorithm iterates through each course and performs DFS to check for cycles. If any cycle is 
detected, the function returns False.

* Result: If no cycles are detected in the graph, the function returns True, indicating that it's possible to complete all 
courses.

'''
