import DirectedGraph
import collections
class TopSort:
  def Kahns(self, graph):
    inDegree = dict()
    for node in graph.vertices:
      inDegree[node] = 0
    
    for node in graph.vertices:
      for neighbor in node.neighbors:
        inDegree[neighbor] = inDegree[neighbor] + 1
    
    topSort = list()
    queue = collections.deque()
    #add all elements of M whose values are 0 to Q
    for curr in list(inDegree.keys())[::-1]:
      if inDegree[curr] == 0:
        queue.append(curr)
        inDegree[curr] = inDegree[curr] - 1
    
    #while Q is not empty
    while queue:
      #N←first element in Q
      current = queue.popleft()
      #add N to A
      topSort.append(curr)
      for neighbor in curr.neighbors:
        #decrement the in-degrees of all dependents of N
        inDegree[neighbor] = inDegree[neighbor] -1
      
      for curr in list(inDegree.keys())[::-1]:
        if inDegree[curr] == 0:
          queue.append(curr)
          inDegree[curr] = inDegree[curr] - 1
    
    return topSort

  def mDFS(self, graph):
    stack = list()
    for vertex in graph.vertices:
      if not vertex.visited:
        self.mDFSHelper(vertex, stack)
    
    inOrderStack = stack[::-1]

    return inOrderStack
  
  def mDFSHelper(self, vertex, stack):
    vertex.visited = True
    for neighbor in vertex.neighbors:
      if not neighbor.visited:
        self.mDFSHelper(vertex, stack)
    
    stack.append(vertex)
  
        
