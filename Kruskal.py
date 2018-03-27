#NEEDS IMPROVEMENT
vert=5
#spanset=[True]*5
spanset=[]
for i in range(vert):
        spanset.append(True)
weight= [
         [1000,1,3,4,1000],
         [1,1000,5,1000,7],
         [3,5,1000,6,8],
         [4,1000,6,1000,2],
         [1000,7,8,2,1000]
        ]
rows=[0]
for i in xrange(vert-1):
  row,col,min_no=-1,-1,1000
  for i in rows:
    temp=min(weight[rows[i]])
    if(min_no>temp):
      min_no=temp
      row=i
      col=weight[i].index(temp)
  print str(min_no)+"("+str(row)+","+str(col)+")"
  spanset[col]=False
  weight[col][row]=1000
  for i in xrange(vert):
    weight[i][col]=1000
  rows.append(col)

d=input()
