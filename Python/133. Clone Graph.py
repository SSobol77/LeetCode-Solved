# 133. Clone Graph

# Topic: Hash Table, Depth-First Search, Breadth-First Search, Graph.

'''
# Task:
-------
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first 
node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case 
using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes
the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as 
a reference to the cloned graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
 
Constraints:
*  The number of nodes in the graph is in the range [0, 100].
*  1 <= Node.val <= 100
*  Node.val is unique for each node.
*  There are no repeated edges and no self-loops in the graph.
*  The Graph is connected and all nodes can be visited starting from the given node.

'''
# Solution:
from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # Create a dictionary to map original nodes to their clones
        node_clone_mapping = {}
        
        # Initialize a queue for BFS
        queue = deque()
        
        # Start from the given node and create a clone node
        clone_node = Node(node.val, [])
        
        # Map the original node to its clone
        node_clone_mapping[node] = clone_node
        
        # Add the original node to the queue to start BFS
        queue.append(node)
        
        while queue:
            current_node = queue.popleft()
            
            # Traverse the neighbors of the current node
            for neighbor in current_node.neighbors:
                if neighbor not in node_clone_mapping:
                    # If the neighbor is not cloned yet, create a clone node
                    neighbor_clone = Node(neighbor.val, [])
                    # Map the original neighbor to its clone
                    node_clone_mapping[neighbor] = neighbor_clone
                    # Add the original neighbor to the queue for BFS
                    queue.append(neighbor)
                # Add the clone of the neighbor to the clone node's neighbors list
                node_clone_mapping[current_node].neighbors.append(node_clone_mapping[neighbor])
        
        return clone_node

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    cloned_node = solution.cloneGraph(node1)
    
    # Check if the cloned graph is correctly created
    assert cloned_node.val == 1
    assert cloned_node.neighbors[0].val == 2
    assert cloned_node.neighbors[1].val == 4
    assert cloned_node.neighbors[0].neighbors[0].val == 1
    assert cloned_node.neighbors[0].neighbors[1].val == 3
    assert cloned_node.neighbors[1].neighbors[0].val == 2
    assert cloned_node.neighbors[1].neighbors[1].val == 4
    
    print("Test case 1 passed.")
    
# Description:
'''
In the "Clone Graph" problem, you are given a reference to a node in a connected undirected graph.
The goal is to create a deep copy (clone) of the graph, where each node in the cloned graph contains 
a value and a list of its neighbors.

To solve this problem, we use a breadth-first search (BFS) algorithm to traverse the original graph 
and create clone nodes along with their neighbors. We maintain a mapping between the original nodes 
and their corresponding clones to ensure that we don't create duplicate nodes in the cloned graph. 
Finally, we return the reference to the cloned graph.

The code provided above implements this algorithm and includes test cases to verify its correctness.

'''
