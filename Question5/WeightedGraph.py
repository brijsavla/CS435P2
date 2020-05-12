class GraphNode:
  def __init__(self, val):
    self.val = val
    #neighbors is now a list containing list of the neighbors and the weights to get to them
    self.neighbors = list()
    self.visited = False

class Graph:
  def __init__(self):
    self.vertices = list()

  def addNode(self, nodeValue):
    nodeToAdd = GraphNode(nodeValue)
    self.vertices.append(nodeToAdd)

  def addWeightedEdge(self, first, second, weight):
    if first not in second.neighbors:
      first.neighbors.append([second, weight])

  def removeWeightedEdge(self, first, second):
    for neighbor in first.neighbors:
      if second in neighbor:
        first.neighbors.remove(second)

  def getAllNodes(self):
    return self.vertices
