import abc
import numpy as np

### Base class representing a graph with all of the instance methods
### We use the ABC library of python because it:
###		- provides decorators
### 	- provides testability of conformance to a protocol for an object
### 	(for inspection, rather than invocation). See: PEP 3119
class Graph(abc.ABC):
	
	def __init__(self, numVertices, directed=False):
		self.numVertices = numVertices
		self.directed = directed
		
	@abc.abstractmethod
	def add_edge(self, v1, v2, weight):
		pass
	
	@abc.abstractmethod
	def get_indegree(self, v):
		pass
	
	@abc.abstractmethod
	def get_edge_weight(self, v1, v2):
		pass
	
	@abc.abstractmethod
	def display(self):
		pass
	
	
class AdjacencyMatrix(Graph):
	
	def __init__(self, numVertices, directed=False):
		super(AdjacencyMatrix, self).__init__(numVertices, directed)
		self.matrix = np.zeros((numVertices, numVertices))
		
	def add_edge(self, v1, v2, weight=1):
		if v1 >= self.numVertices \
		or v2 >= self.numVertices \
		or v1 < 0 or v2 < 0:
			raise ValueError("Vertices have to be between 0 and %d" % self.numVertices)
