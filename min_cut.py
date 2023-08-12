import networkx as nx
import random

### NAVODILA ZA POGANJANJE ###
# v direktoriju, kjer imamo to datoteko mora obstajati mapa tests, v kateri so grafi
# grafi morajo biti imenovani g01.graph, g02.graph, ..., g13.graph (enako kot so bili podani testi)
# poženemo z ukazom python3 min_cut.py
# rezultati se izpišejo na standardni izhod

def read_graph(path):
    G = nx.read_edgelist(path, nodetype=int)
    return G

# Python3 program to implement Disjoint Set Data
# Structure.

class DisjointSet:
    def __init__(self, n):
		# Constructor to create and
		# initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        self.sizes = [1] * n
        self.no_of_sets = n


	# Finds set of given item x
    def find(self, x):
		
		# Finds the representative of the set
		# that x is an element of
        while (self.parent[x] != x):
			
			# if x is not the parent of itself
			# Then x is not the representative of
			# its set,
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
			# so we recursively call Find on its parent
			# and move i's node directly under the
			# representative of this set

        return x
	
	# Do union of two sets represented
	# by x and y.
    def Union(self, x, y):
		
		# Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)

		# If they are already in same set
        if xset == yset:
            return

		# Put smaller ranked item under
		# bigger ranked item if ranks are
		# different
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
            self.sizes[xset] += self.sizes[yset]
            
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
            self.sizes[yset] += self.sizes[xset] 
		# If ranks are same, then move y under
		# x (doesn't matter which one goes where)
		# and increment rank of x's tree
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1
            self.sizes[yset] += self.sizes[xset]
        self.no_of_sets -= 1
			
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
# function that makes a random permutation of the edges
def random_permutation(G):
    edges = list(G.edges())
    random.shuffle(edges)
    return edges


def min_cut(edges, n, m):
    # create a disjoint set
    ds = DisjointSet(n)
    
    min_cut_value = 0
    for i in range(len(edges)):
        e = edges[i]
        if ds.no_of_sets == 2 and not ds.connected(e[0], e[1]):
            min_cut_value += 1
        elif not ds.connected(e[0], e[1]):
            ds.Union(e[0], e[1])
    #print('after'+str(min_cut_value))
    return min_cut_value
            
def main():
    for i in range(1, 14):
        name = './tests/g' + str(i).zfill(2) + '.graph'
        # read the graph
        G = read_graph(name)
        # compute the min cut
        min_cuts = []
        e = list(G.edges())
        # compute the number of edges
        m = len(G.edges())
        # compute the number of nodes
        n = len(G.nodes())
        for i in range(50):
            #print(i)
            min_cut_value = min_cut(e,n,m)
            random.shuffle(e)
            min_cuts.append(min_cut_value)

        minimal_value = min(min_cuts)

        counters = []

        for i in range(20):
            counter = 1
            random.shuffle(e)
            while min_cut(e, n, m) > minimal_value:
                counter += 1
                random.shuffle(e)
            counters.append(counter)
        
        print(name + ' | (' + str(len(G.nodes())) + ', ' + str(len(G.edges())) + ') | ' + str(minimal_value) + ' | ' + str(sum(counters)/len(counters)))

main()