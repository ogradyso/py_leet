from collections import deque

# A class to represent a graph object
class Graph:
#constructor
	def __init__(self, edges, n):
		# a list of lists to represent an adjaceny list:
		self.adjList = [[] for _ in range(n)]
		# add edges to the undirected graph
		for (src, dest) in edges:
			self.adjList[src].append(dest)
			self.adjList[dest].append(src)

# function to perform iterative DFS on graph starting from vertex `v`
def iterativeDFS(graph, v, discovered):
	# create a stack used to do iterative DFS:
	stack = deque()
	# push the source node into the stack
	stack.append(v)
	# loop till stack is empty
	while stack:
		v = stack.pop()
		#if the vertex is already discovered, ignore it
		if discovered[v]:
			continue
		# we will reach here if the popped verex `v` is not discovered yet
		# print `v` and process its undiscovered adjacent nodes into the stack
		discovered[v] = True
		print(v, end=' ')
		#for every edge:
		adjList = graph.adjList[v]
		for i in reversed(range(len(adjList))):
			u = adjList[i]
			if not discovered[u]:
				stack.append(u)

#Function to perform DFS Traversal on the graph on a graph
def recursiveDFS(graph, v, discovered):
	discovered[v] = True      # mark the current node as discovered
	print(v, end=' ')               # print the current node
	# do for every edge (v, u)
	for u in graph.adjList[v]:
		if not discovered[u]:
			recursiveDFS(graph, u, discovered)

if __name__ == '__main__':
    # list of graph edges as per the above diagram
    edges = [
        # notice that node 0 is unconnected
        (1,2), (1,7), (1,8), (2,3), (2,6), (3,4),
        (3,5), (8,9), (8,12), (9,10), (9,11)
]
	# total number of nodes in the graph (labelled from 0 to 12)
    n =13
	# build a graph from the given edges
    graph = Graph(edges, n)
	# to keep track of whether a vertex is discovered or not 
    discovered = [False] * n
	# perform DFS traversal from all undiscovered nodes to 
	# cover all connected components of a graph
    print("Recursive DFS: \n")
    for i in range(n):
        if not discovered[i]:
            recursiveDFS(graph, i, discovered) 
    print("\nIterative DFS: \n") 
    graph = Graph(edges, n) 
    discovered = [False] * n
	# do iterative DFS traversal from all undiscovered nodes to
	# cover all connected components of a graph
    for i in range(n):
        if not discovered[i]: 
            iterativeDFS(graph, i, discovered)
