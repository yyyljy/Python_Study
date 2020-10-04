def bfs(i,j,MAP,answer):
    MAP[i][j] = answer
    if j < len(MAP[i])-1:
        if MAP[i][j+1] > answer or MAP[i][j+1] == 1:
            #MAP[i][j+1] = tmp+1
            bfs(i,j+1,MAP,answer+1)
    if j > 1:
        if MAP[i][j-1] > answer or MAP[i][j-1] == 1:
            #MAP[i][j-1] = tmp+1
            bfs(i,j-1,MAP,answer+1)
    if i < len(MAP)-1:
        if MAP[i+1][j] > answer or MAP[i+1][j] == 1:
            #MAP[i+1][j] = tmp+1
            bfs(i+1,j,MAP,answer+1)
    if i > 1:
        if MAP[i-1][j] > answer or MAP[i-1][j] == 1:
            #MAP[i-1][j] = tmp+1
            bfs(i-1,j,MAP,answer+1)
    
def solution(N,M,MAP):
    answer = 1
    i = 0
    j = 0
    bfs(i,j,MAP,answer)
    answer = MAP[N-1][M-1]
    print(MAP)
    return answer

N = 5
M = 6
MAP = [ [1,0,1,0,1,0],
        [1,1,1,1,1,1],
        [0,0,0,0,0,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1]
        ]
print(solution(N,M,MAP))

N = 3
M = 3
MAP = [[1,1,1],[1,1,1],[1,1,1]]
print(solution(N,M,MAP))
