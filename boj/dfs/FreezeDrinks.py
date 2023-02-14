n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0


def dfs(x,y):
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
    
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                if nx == n-1 and ny ==m-1:
                    return
                dfs(nx,ny)
    return

dfs(0,0)
print(visited[n-1][m-1])