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

  def addDirectedEdge(self, first, second):
    if first not in second.neighbors:
      first.neighbors.append(second)

  def removeDirectedEdge(self, first, second):
    if first in second.neighbors:
      first.neighbors.remove(second)

  def getAllNodes(self):
    return self.vertices
