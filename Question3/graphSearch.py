from graph import Graph
from graph import GraphNode

class GraphSearch:
  def __init__(self):
    pass
  
  def DFSRec(self, start, end):
    visitedPath = list()
    if start != end:
      DFSHelper(self, start, end, visitedPath)
    return visitedPath
  #Helper function for DFS
  def DFSHelper(self, start, end, visitedPath): 
    #Check if current node is the node we need
    if start == end:
      visitedPath.append(start)
    #Add start to list of visited nodes, then check if neighbors are visited
    if start not in visitedPath:
      visitedPath.append(start)
      for neighbor in start.neighbors:
        self.DFSHelper(neighbor, end)
  

  def DFSIter(self, start, end):
    s = list()
    visitedPath = list()
    s.append(start)
    visitedPath.append(start)
    endOfPath = False
    while len(s) > 0:
      curr = s.pop()
      #Check if the current node is the node we need
      if curr == end:
        visitedPath.append(curr)
        endOfPath = True
        return visitedPath
      #Check if neighbors are visited
      for neighbor in current.neighbors:
        if neighbor not in visitedPath:
          s.append(neighbor)
          visitedPath.append(neighbor)
    if endOfPath:
      return visitedPath
    else:
      return None
  
  #Similar to DFS but instead of stack we use a queue
  def BFTRec(self, graph):
    q = list()
    visitedPath = list()
    for node in graph.vertices:
      if node not in visitedPath:
        visitedPath.append(node)
        queue.append(node)
        self.BFTHelper(graph, q, visitedPath)
    return visitedPath
  #Helper function for BFT
  def BFTHelper(self, graph, q, visitedPath):
    if len(q) == 0:
      return
    curr = q.pop(0)
    for neighbor in curr.neighbors:
      if neighbor not in visitedPath:
        q.append(neighbor)
        visitedPath.append(neighbor)
    self.BFTHelper(graph, q, visitedPath)
  
  def BFTIter(self, graph):
    q = list()
    visitedPath = list()
    for node in graph.vertices:
      if node not in visitedPath:
        visitedPath.append(node)
        q.append(node)
        while len(q) > 0:
          curr = q.pop(0)
          for neighbor in curr.neighbors:
            if neighbor not in visitedPath:
              visitedPath.append(neighbor)
              q.append(neighbor)
  
  return visitedPath
  
