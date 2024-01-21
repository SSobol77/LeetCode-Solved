# 2385. Amount of Time for Binary Tree to Be Infected.

# Topic: Tree, Depth-First Search, Breadth-First Search.

"""
### Task:
---------
You are given the root of a binary tree with unique values, and an integer start. At minute 0, 
an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

#Example 1:
Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.

#Example 2:
Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.

#Constraints:
The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 10^5
Each node has a unique value.
A node with a value of start exists in the tree.

Hint 1:
Convert the tree to an undirected graph to make it easier to handle.
Hint 2:
Use BFS starting at the start node to find the distance between each node and the start node. 
The answer is the maximum distance.


### Testcase:
-------------
[1,5,3,null,4,10,6,9,2]
3
[1]
1


### Code:
---------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

"""
# Solution:

from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Convert the binary tree to an undirected graph
        graph = defaultdict(list)
        
        def build_graph(node, parent):
            if not node:
                return
            if parent:
                # Add an edge between the current node and its parent in the undirected graph
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            
            # Recursively build the graph for the left and right subtrees
            build_graph(node.left, node)
            build_graph(node.right, node)
        
        # Start building the graph from the root with no parent (None)
        build_graph(root, None)
        
        # Perform BFS starting at the "start" node
        queue = deque([(start, 0)])  # Initialize the queue with the start node and distance 0
        visited = set([start])      # Create a set to keep track of visited nodes
        max_distance = 0            # Initialize the maximum distance
        
        while queue:
            node, distance = queue.popleft()  # Dequeue a node and its distance from the queue
            max_distance = max(max_distance, distance)  # Update the maximum distance
            
            # Iterate through neighbors (adjacent nodes) of the current node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)  # Mark the neighbor as visited
                    queue.append((neighbor, distance + 1))  # Enqueue the neighbor with an increased distance
        
        # Return the maximum distance, which represents the number of minutes needed for the entire tree to be infected
        return max_distance


### Description:
'''
To solve this problem, you can follow these steps:
    1. Convert the binary tree to an undirected graph to make it easier to handle.
    2. Use Breadth-First Search (BFS) starting at the "start" node to find the distance between each node and the "start" node.
    3. The answer is the maximum distance found during the BFS traversal.

    This code first converts the binary tree into an undirected graph, and then it uses BFS to find the maximum 
    distance from the "start" node to any other node in the tree, which represents the number of minutes needed 
    for the entire tree to be infected.

'''
