#Problem 3A
#Brij Savla

class GraphNode:
  def __init__(self, val):
    self.val = val
    self.neighbors = list()
    self.visited = False

class Graph:
  def __init__(self):
    self.vertices = list()
  
  def addNode(self, nodeValue):
    nodeToAdd = GraphNode(nodeValue)
    self.vertices.append(nodeToAdd)
  
  def addUndirectedEdge(self, first, second):
    if first not in self.vertices or second not in self.vertices:
      return
    else:
      if first not in second.neighbors:
        second.neighbors.append(first)
      if second not in first.neighbors:
        first.neighbors.append(second)

  def removeUndirectedEdge(self, first, second):
    if first in second.neighbors:
      second.neighbors.remove(first)
    if second in first.neighbors:
      first.neighbors.remove(second)
  
  def getAllNodes(self):
    return self.vertices
