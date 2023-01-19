V = int(input("Enter the number of vertices:"))
E = int(input("Enter the number of edges:"))
X = int(input("Enter element to be searched"))
graph = [[0]*V for i in range(V)]
print("Enter edges:")
for i in range(E):
    a,b = [int(_i) for _i in input().split()]
    graph[a][b] = graph[b][a] = 1
q1 = [0]
d1 = {0:0}
while(len(q1)):
    curre = q1[0]
    q1 = q1[1:]
    for j in range(V):
        if graph[curre][j]:
            q1.append(j)
            graph[curre][j],graph[j][curre] = 0,0
            d1[j] = d1[curre]+1
print(f"The vertex is at {d1[X]} level")
