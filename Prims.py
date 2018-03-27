import time
def popmin(pqueue):
    lowest = 1000
    keylowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keylowest = key
    del pqueue[keylowest]
    return keylowest
 
def prim(graph, root):
    pred = {}
    key = {}
    pqueue = {}
 
    for v in graph:
        pred[v] = -1
        key[v] = 1000
    key[root] = 0
    for v in graph:
        pqueue[v] = key[v]
     
    while pqueue:
        u = popmin(pqueue)
        for v in graph[u]:
            if v in pqueue and graph[u][v] < key[v]:
                pred[v] = u
                key[v] = graph[u][v]
                pqueue[v] = graph[u][v]
    return pred
 
graph = {0 : {1:6, 2:8},
1 : {4:11},
2 : {3: 9},
3 : {},
4 : {5:3},
5 : {2: 7, 3:4}}

start=time.clock()
pred = prim(graph, 0)
for v in pred: print "%s: %s" % (v, pred[v])
end=time.clock()
print "The program ran for: ",end-start,"seconds"
