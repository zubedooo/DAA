import time
graph = {
    1:{ 2:10, 5:100},
    2:{ 1:10, 3:50},
    3:{ 2:50, 4:20, 5:10},
    4:{ 3:20, 5:60},
    5:{ 1:100, 3:10, 4:600}
}
def Dijkstra(s):
  d,visited=[999]*len(graph),[0]*len(graph)
  d[s-1]=0
  visited[s-1]=s-1
  vertices=[s]
  while len(vertices)!=len(graph.keys()):
    edges={}
    for u in vertices:
      for v in graph[u].keys():
        if visited[v-1]==0:
          t=d[u-1]+graph[u][v]
          edges.update({t:[u,v]})
    min_d=min(edges.keys())
    node=edges[min_d][1]
    d[node-1]=min_d
    vertices.append(node)
    visited[node-1]=node-1
  return d
start=time.clock()
print (Dijkstra(1))
end=time.clock()
print ("The Program Ran for: ",end-start,"seconds")
