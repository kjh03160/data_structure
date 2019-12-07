'''
RecursiveDFS(v): # 현재 v노드 방문 중
    visited[v] = True   # mark m as 'visited' -> 다음에 돌아왔을 때 방문 했다는 것을 알기 위해
    for each edge v -> w:   # w 는 인접한 노드
        if w is unmarked:
            RecursiveDFS(w)

current_time = 1    # 전역변수
DFS(v):
    visited[v] = True
    prev[v] = current_time  # v의 첫 방문 시간 기록
    current_time += 1
    for each edge(v, w):    # v에 인접한 w
        if visited[w] ==False:      # 여기서 else로 True일때 추가하면 사이클이 존재하는지 안하는지 알 수 있다!
            parent[w] = v   # v로부터 방문, v가 w의 parent
            DFS(w)
        else:
            cycle 발견
    post[v] = current_time  # v 마지막 방문 시간 (모든 노드 방문 한 시간)
    current_time += 1

'''