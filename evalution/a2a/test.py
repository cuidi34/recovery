from igraph import *



g=Graph.Bipartite([0,1,0,1],[(0,1),(2,3),(0,3)])

# print g.is_bipartite()

# print g

g1=Graph()

g1.add_vertices(4)
g1.add_edges([(0,1),(2,3),(0,3)])

print g1


matching=g1.maximum_bipartite_matching([0,1,0,1],(3,4,5))

print matching.matching

attentation=[1,2,3,4]
