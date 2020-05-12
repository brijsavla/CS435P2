import GridGraph
import random

def createRandomGridGraph(n):
  graph = GridGraph()
  iterator = 0
  for x in range(n):
    for y in range(n):
      graph.addGridNode(x, y, iterator)
      iterator += 1
  for x in graph.gridGraph:
    for y in graph.gridGraph:
      if random.randint(1,100) % 2 == 0:
        graph.addUndirectedEdge(x, y)

def minDist(distances, visited):
  ans = None
  m = math.inf
  for current in distances.keys():
    if current not in visited and distances[current] <= m:
      m = distances[current]
      ans = current
  return ans

#Similar to dijkstras but now there is a heuristic.
def astar(self, sourceNode, destNode):
  # Create an empty map of nodes to pairs of distances (g, h). g is the distance so far, and his the estimated distance to the goal using the heuristic. Initialize every node to map to infinity g.
  distances = dict()
  distances[sourceNode] = 0
  visited = list()
  # We're returning this list 
  path = list()
  current = sourceNode
  # While curr is not the destination node:
  while current is not None:
    # “Finalize” curr.
    visited.append(current)
    #Iterate over its neighbors, “relax” each neighbor
    for neighbor in current.neighbors:
      # For each neighbor that is not finalized, update its distance (if less than the current g value) to the sum of curr’s distance and the weight of the edge between curr and this neighbor.  Calculate the heuristic value for this neighbor and assign it to h.
      if neighbor not in path:
        distances[neighbor] = distances[current] + calcHeuristic(neighbor, destNode)
    current = minDist(distances, visited)
  if current == destNode:
    path.append(current)
  
  return path

# This will calculate the heuristic to find the best path
def calcHeuristic(current, destNode):
  return abs(current.x - destNode.x) + abs(current.y - destNode.y)
