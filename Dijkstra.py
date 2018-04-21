import time

str_nodes=input("Enter the nodes\n").upper() 
nodes=str_nodes.split(" ")
print (nodes)

distances=dict()
dummy_dict=dict()

for i in nodes:
    dummy_dict={}
    noOfAttachments=int(input("How many nodes are attached to %c "%(i)))
    for j in range(noOfAttachments):
        a=input("Enter one node %c is attached to "%(i)).upper()
        b=int(input("Enter the weight"))
        dummy_dict[a]=b
    distances[i]=dummy_dict
print (distances)

unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = 'B'
currentDistance = 0
unvisited[current] = currentDistance

start=time.clock()
while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

end=time.clock()
print(visited)
print ("The program ran for: ",end-start,"seconds")
