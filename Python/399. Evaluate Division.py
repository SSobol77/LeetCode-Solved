# 399. Evaluate Division.

# Topic:

'''
# Task:
-------
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer
for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and 
that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 
Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.


# Testcase:
-----------
[["a","b"],["b","c"]]
[2.0,3.0]
[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
[["a","b"],["b","c"],["bc","cd"]]
[1.5,2.5,5.0]
[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
[["a","b"]]
[0.5]
[["a","b"],["b","a"],["a","c"],["x","y"]]


# Code:
-------
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
   

'''
# Solution:
from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        # Creating a graph where each node is a variable and each edge represents an equation
        graph = defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val  # Edge from x to y with weight val
            graph[y][x] = 1.0 / val  # Edge from y to x with weight 1/val

        # DFS function to find the value of the division from x to y
        def dfs(x, y, visited):
            if x not in graph or y not in graph:  # If x or y is not in the graph, return -1.0
                return -1.0
            if y in graph[x]:  # Direct edge from x to y
                return graph[x][y]
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i, y, visited)  # DFS to the next node
                    if temp == -1.0:
                        continue
                    else:
                        return graph[x][i] * temp  # Multiply the edge values along the path
            return -1.0

        # Calculating results for each query
        results = []
        for query in queries:
            results.append(dfs(query[0], query[1], set()))  # Perform DFS for each query
        return results

# Testing the solution
sol = Solution()
print(sol.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
print(sol.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
print(sol.calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]))

# Description:
'''
This Python code solves the "Evaluate Division" problem using a graph-based approach. It constructs a graph where 
each variable is a node and each equation is an edge with a weight representing the division result. The solution 
uses Depth-First Search (DFS) to find the division result between two variables for each query. If a query involves 
undefined variables or a path does not exist between them, it returns -1.0. This approach efficiently handles 
multiple queries by reusing the graph structure without recalculating known relationships.

'''
