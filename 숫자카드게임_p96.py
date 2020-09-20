def solution(N, M, Arr):
    answer = 1
    minlist = []
    for i in range(0,N):
        minlist.append(min(Arr[i]))
    #print(minlist)
    answer = max(minlist)
    return answer

# N = 3
# M = 3
# Arr = [[3,1,2],[4,1,4],[2,2,2]]

N = 2
M = 4
Arr = [[7,3,1,8], [3,3,3,4]]

print(solution(N, M, Arr))