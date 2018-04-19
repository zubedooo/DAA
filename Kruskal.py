graph = {
        1 : { 2:10, 5:100 },
        2 : { 1:10, 3:50 },
        3 : { 2:50, 4:20, 5:10 },
        4 : { 3:20, 5:60 },
        5 : { 1:100, 3:10, 4:60 }
}
def Kruskals():
	Trees,visited,count,cost,weights=[],[0]*len(graph),1,0,[]
	for i in graph.keys():
		for j in graph[i]:
			e=[graph[i][j],min(i,j),max(i,j)]
			if e not in weights:
				weights.append(e)
	while count<len(graph):
		e=min(weights)
		weights.remove(e)
		if visited[e[1]-1]==1 and visited[e[2]-1]==1:
			continue
		Trees.append([e[1],e[2]])
		cost+=e[0]
		count+=1
		visited[e[1]-1],visited[e[2]-1]=1,1
	return cost,Trees
cost,tree=Kruskals()
print "Cost:",cost
print "Tree:"
for i in tree:
	print i
