# 207. Course Schedule.

# Topic:

"""
## Task:
---------
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an 
array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want 
to take course ai.

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
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. 
So it is impossible.

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

## Testcase:
-------------
2
[[1,0]]
2
[[1,0],[0,1]]


## Code:
----------
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
"""
# Solution

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a graph to represent the courses and their prerequisites
        graph = defaultdict(list)
        
        # Populate the graph based on the prerequisites
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # Initialize a list to keep track of visited courses during DFS
        visited = [0] * numCourses
        
        def is_cyclic(course):
            if visited[course] == -1:
                return True  # Found a cycle
            if visited[course] == 1:
                return False  # Already visited, no cycle
            
            visited[course] = -1  # Mark as currently visiting
            
            # Check prerequisites for the current course
            for prereq in graph[course]:
                if is_cyclic(prereq):
                    return True
            
            visited[course] = 1  # Mark as visited without cycles
            return False
        
        # Check for cycles in the graph using DFS
        for course in range(numCourses):
            if is_cyclic(course):
                return False  # If a cycle is found, it's impossible to finish all courses
        
        return True  # If no cycle is found, it's possible to finish all courses



### Description
'''
To solve this problem, you can use a topological sorting algorithm, such as Depth-First Search (DFS), to check if 
there exists a valid order in which you can finish all the courses.

Here's a breakdown of the code with comments:
---------------------------------------------

1. Create a `defaultdict` called `graph` to represent the courses and their prerequisites. Each course is a key, and 
   its prerequisites are stored as values in a list.

2. Populate the `graph` based on the given prerequisites.

3. Initialize a list called `visited` to keep track of visited courses during DFS. `visited[i]` can have three values:
   - `0`: Not visited.
   - `-1`: Currently visiting (used to detect cycles).
   - `1`: Visited without cycles.

4. Define a recursive `is_cyclic` function that checks if there is a cycle starting from the `course`. If a cycle is found, 
   it returns `True`; otherwise, it returns `False`.

5. In the `is_cyclic` function:
   - If a course is currently being visited (`visited[course] == -1`), it means a cycle is found, so return `True`.
   - If a course has already been visited (`visited[course] == 1`), there is no cycle, so return `False`.
   - Mark the current course as currently visiting by setting `visited[course] = -1`.
   - Check the prerequisites for the current course using DFS and the `is_cyclic` function.
   - If a cycle is found during DFS, return `True`.
   - Mark the current course as visited without cycles by setting `visited[course] = 1`.

6. Finally, check for cycles in the graph by iterating through all courses and calling the `is_cyclic` function. If any course 
   results in a cycle, return `False`. If no cycle is found, return `True`.

This code checks whether it's possible to finish all courses based on the given prerequisites and graph topology. If there are 
no cycles in the graph, it's possible to finish all courses; otherwise, it's impossible.

'''
