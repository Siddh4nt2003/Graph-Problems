V = int(input("Enter the number of vertices:"))
E = int(input("Enter the number of edges:"))
X = int(input("Enter element to be started"))
graph = [[0]*V for i in range(V)]
print("Enter edges:")
for i in range(E):
    a,b = [int(_i) for _i in input().split()]
    graph[a][b] = graph[b][a] = 1
q1 = [X]
visited = {X}
while(len(q1)):
    curre = q1[0]
    q1 = q1[1:]
    for j in range(V):
        if graph[curre][j]:
            q1.append(j)
            graph[curre][j],graph[j][curre] = 0,0
            visited.add(j)
print("Visited nodes are:\n",visited)
if len(visited)==V:
    print("All nodes are reachable")
else:
    print("All nodes are not reachable")
