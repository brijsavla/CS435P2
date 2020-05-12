import math
import WeightedGraph

def createLinkedList(n):
  graph = WeightedGraph()
  for i in range(n):
    graph.addNode(i)
  if i > 0:
    graph.addWeightedEdge(graph.vertices[i-1], graph.vertices[i], 1)
  return graph

#Helper function returns minimum distance
#Referred off of Lesson 18 repl.it  
def minDist(distances, visited):
  ans = None
  m = math.inf
  for current in distances.keys():
    if current not in visited and distances[current] <= m:
      m = distances[curr]
      ans = curr
  return ans

def dijkstras(start):
  # Create an empty map of nodes to distances.
  distances = dict()
  # Set the distance for the origin to 0. Let curr be the origin.
  distances[start] = 0
  visited = list()
  current = start
  # While curr is not null and its distance is not infinity.
  while current is not None:
    # “Finalize” curr.
    visited.append(current)
    # Iterate over its neighbors, “relax” each neighbor:
    for neighbor in current.neighbors:
      # For each neighbor that is not finalized, update its distance (if less than its current distance) to the sum of curr’s distance and the weight of the edge between curr and this neighbor.
      if neighbor[0] not in distances or distances[neighbor[0]] > distance[current] + neighbor[1]:
        distances[neighbor[0]] = distances[current] + neighbor[1]
    # Set curr to the next min distance node – the node with the smallest distance that is not yet finalized.
    current = minDist(distances, visited)
  
  return distances
