class GridGraphNode:
  def __init__(self, x, y, nodeVal):
    self.x = x
    self.y = y
    self.nodeVal = nodeVal
    self.neighbors = list()

class GridGraph:
  def __init__(self):
    self.gridGraph = list()
  
  def addGridNode(self, x, y, nodeVal):
    gridNode = GridGraphNode(x, y, nodeVal)
    self.gridGraph.append(gridNode)
  
  def addUndirectedEdge(self, first, second):
    #check if the distance between x or y is 0 and y and x coordinates are equal to each other to prove that they're neighbors 
    if (abs(first.x - second.x) <= 1 and first.y == second.y) or (abs(first.y - second.y) <= 1 and first.x == second.x):
      first.neighbors.append(second)
      second.neighbors.append(first)

  def removeUndirectedEdge(self, first, second):
    if first in second.neighbors and second in first.neighbors:
      first.neighbors.remove(second)
      second.neighbors.remove(first) 
  
  def getAllNodes(self):
    return self.gridGraph


