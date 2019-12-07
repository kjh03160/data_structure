'''
방문하지 않은 이웃 노드부터 탐색
한 레벨 모두를 방문 후 아래 레벨

큐를 이용하여
같은 레벨에 있는 노드들 enqueue 하고 빼면서 방문
BFS(v):
    Q.enqueue(v)
    while Q is not empty:
        v = Q.dequeue()
        visited[v] = True
        for each edge (v, w):   # w는 v에 인접한 노드
            if visited[w] == False:
                Q.enqueue(w)
                parent[w] = v
                distance[w] = distance[v] + 1   # 출발한 노드에서부터 w까지 몇 번의 엣지를 거쳐서 왔는가

'''