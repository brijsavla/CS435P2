import random
from graph import Graph
from graph import GraphNode

#3B in progress
def createRandomUnweightedGraphIter(n):
  graph = Graph()
  for i in range(0,n):
    graph.addNode(i)
  
  for node in graph.vertices:
    idx = graph.vertices.idx(node)
    randomNode = random.randint(0, idx)
    
#3C
def createLinkedList(n):
  graph = Graph()
  for i in range(n):
    graph.addNode(i)
  
  for i in range(n-1):
    graph.addUndirectedEdge(i, i+1)
  
  return graph

def BFTRecLinkedList(graph):
  graphSearch = GraphSearch()
  bftRec = graphSearch.BFTRec(graph)
  return bftRec

def BFTIterLinkedList(graph):
  graphSearch = GraphSearch()
  bftIter = graphSearch.BFTIter(graph)
  return bftIter
