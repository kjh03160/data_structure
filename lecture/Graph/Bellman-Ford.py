"""

def relax(u, v):
	if d[v] > d[u] + cost(u, v):
		d[v] = d[u] + cost(u, v)
		p[v] = u

# Bellman-Ford Algorithm
# Graph G = (V, E) with edges of (possibly negative) costs
def Bellamn-Ford(G = (V, E)):
	# n = number of nodes, m = number of edges
	d = [inf, ..., inf], d[s] = 0
	for i in range(1, n):  # total (n-1) rounds
		for each edge e = (u, v):
			relax(u, v)

	return d

수행시간 : O(노드 수 * 엣지 수) = O(n^3)
"""